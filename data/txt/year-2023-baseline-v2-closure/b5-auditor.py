#!/usr/bin/env python3
"""Build the independent year-2023 baseline-v2 B5 campaign audit receipt."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import re
import subprocess
import sys
from typing import Any


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def file_identity(path: pathlib.Path) -> dict[str, Any]:
    return {
        "path": str(path),
        "size": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def load_json(path: pathlib.Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON document is not an object: {path}")
    return value


def read_inventory(path: pathlib.Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def git_output(repo: pathlib.Path, *arguments: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *arguments], check=True,
        capture_output=True, text=True).stdout.strip()


def git_identity(repo: pathlib.Path) -> dict[str, Any]:
    tracked_status = git_output(
        repo, "status", "--porcelain", "--untracked-files=no")
    untracked_output = git_output(
        repo, "ls-files", "--others", "--exclude-standard")
    untracked = untracked_output.splitlines() if untracked_output else []
    return {
        "path": str(repo),
        "revision": git_output(repo, "rev-parse", "HEAD"),
        "tracked_clean": not bool(tracked_status),
        "worktree_clean": not bool(tracked_status) and not untracked,
        "untracked_files": untracked,
    }


def normalized_counts(records: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "records": len(records),
        "passed": sum(
            record.get("status") in {"pass", "pass-existing"}
            for record in records),
        "errors": sum(record.get("status") == "error" for record in records),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--year", required=True)
    parser.add_argument("--alpha60-dir", type=pathlib.Path, required=True)
    parser.add_argument("--results-dir", type=pathlib.Path, required=True)
    parser.add_argument("--metadata-dir", type=pathlib.Path, required=True)
    parser.add_argument("--izzi-dir", type=pathlib.Path, required=True)
    parser.add_argument("--archive-map", type=pathlib.Path, required=True)
    parser.add_argument("--site-audit", type=pathlib.Path, required=True)
    parser.add_argument("--metadata-audit", type=pathlib.Path, required=True)
    parser.add_argument("--scope-receipt", type=pathlib.Path, required=True)
    parser.add_argument("--scope-revision", required=True)
    parser.add_argument(
        "--worker-receipt", type=pathlib.Path, action="append", required=True)
    parser.add_argument("--repair-receipt", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    for name in (
            "alpha60_dir", "results_dir", "metadata_dir", "izzi_dir",
            "archive_map", "site_audit", "metadata_audit", "scope_receipt",
            "repair_receipt", "output"):
        setattr(args, name, getattr(args, name).resolve())
    args.worker_receipt = [path.resolve() for path in args.worker_receipt]

    sys.path.insert(0, str(args.alpha60_dir / "scripts"))
    from day_product_contract import DayProductError, validate_day_products
    from year_day_contract import (
        YearDayContractError,
        validate_day_cache_stream_contract,
        validate_day_contract_for_indices,
    )

    issues: list[str] = []
    year = str(args.year)
    inventory_path = (
        args.results_dir / "data/txt" / f"year-{year}-0-media-objects.txt")
    inventory = read_inventory(inventory_path)
    if not inventory or len(inventory) != len(set(inventory)):
        issues.append("inventory is empty or contains duplicates")

    archive_document = load_json(args.archive_map)
    archive_records = {
        record.get("collection_key"): record
        for record in archive_document.get("records", [])
        if isinstance(record, dict) and isinstance(
            record.get("collection_key"), str)
    }
    if archive_document.get("schema") != "alpha60-year-cache-archive-map/1" \
            or archive_document.get("status") != "pass" \
            or str(archive_document.get("year")) != year:
        issues.append("archive map schema, status, or year mismatch")
    if set(archive_records) != set(inventory) \
            or len(archive_records) != len(inventory):
        issues.append("archive map does not exactly match inventory")

    site_audit = load_json(args.site_audit)
    site_counts = site_audit.get("counts", {})
    if site_audit.get("status") != "pass" \
            or site_counts.get("passed") != len(inventory) \
            or any(site_counts.get(field) != 0
                   for field in ("absent", "old", "failed")):
        issues.append("whole-site baseline-v2 audit did not pass exactly")

    metadata_audit = load_json(args.metadata_audit)
    metadata_counts = metadata_audit.get("counts", {})
    if metadata_audit.get("status") != "pass" \
            or metadata_counts.get("ready_records") != len(inventory) \
            or metadata_counts.get("error_records") != 0:
        issues.append("fresh canonical metadata audit did not pass exactly")

    original_records: dict[str, dict[str, Any]] = {}
    original_receipts = []
    for path in args.worker_receipt:
        receipt = load_json(path)
        records = receipt.get("records", [])
        if receipt.get("schema") != "alpha60-year-baseline-v2-worker-run/1" \
                or str(receipt.get("year")) != year \
                or not isinstance(records, list):
            issues.append(f"invalid original worker receipt: {path}")
            continue
        counts = normalized_counts(records)
        if receipt.get("counts") != counts:
            issues.append(f"worker counts mismatch: {path}")
        expected_status = "pass" if counts["errors"] == 0 else "error"
        if receipt.get("status") != expected_status:
            issues.append(f"worker terminal status mismatch: {path}")
        for record in records:
            key = record.get("collection_key") \
                if isinstance(record, dict) else None
            if not isinstance(key, str) or not key or key in original_records:
                issues.append(f"duplicate or invalid original worker key: {key}")
                continue
            original_records[key] = record
        original_receipts.append({
            "identity": file_identity(path),
            "owner": receipt.get("owner"),
            "executor": receipt.get("executor"),
            "status": receipt.get("status"),
            "counts": counts,
        })
    if set(original_records) != set(inventory):
        issues.append("original worker receipts do not exactly cover inventory")

    repair = load_json(args.repair_receipt)
    repair_records_value = repair.get("records", [])
    repair_records: dict[str, dict[str, Any]] = {}
    if repair.get("schema") != "alpha60-year-baseline-v2-worker-run/1" \
            or str(repair.get("year")) != year \
            or repair.get("status") != "pass" \
            or not isinstance(repair_records_value, list):
        issues.append("repair receipt schema, year, or terminal status mismatch")
    else:
        for record in repair_records_value:
            key = record.get("collection_key") \
                if isinstance(record, dict) else None
            if not isinstance(key, str) or not key or key in repair_records:
                issues.append(f"duplicate or invalid repair key: {key}")
                continue
            repair_records[key] = record
        repair_counts = normalized_counts(repair_records_value)
        if repair.get("counts") != repair_counts \
                or repair_counts["passed"] != len(repair_records_value) \
                or repair_counts["errors"] != 0:
            issues.append("repair receipt counts are not all-pass")

    original_errors = {
        key for key, record in original_records.items()
        if record.get("status") == "error"
    }
    if set(repair_records) != original_errors:
        issues.append("repair key set does not exactly equal original errors")

    terminal_records = []
    for key in inventory:
        original = original_records.get(key, {})
        repaired = repair_records.get(key)
        original_status = original.get("status")
        repair_status = repaired.get("status") if repaired else None
        final_pass = original_status in {"pass", "pass-existing"} \
            or repair_status in {"pass", "pass-existing"}
        terminal_records.append({
            "collection_key": key,
            "owner": original.get("owner"),
            "executor": (repaired or original).get("executor"),
            "original_status": original_status,
            "repair_status": repair_status,
            "final_status": "pass" if final_pass else "fail",
            "results_revision": (repaired or original).get(
                "results_revision"),
        })
    terminal_passed = sum(
        record["final_status"] == "pass" for record in terminal_records)
    if terminal_passed != len(inventory):
        issues.append("not all terminal worker dispositions pass")

    day_records = []
    day_pairs = 0
    for key in inventory:
        try:
            record = archive_records[key]
            validation = record["day_cache_validation"]
            stream_path = (
                args.results_dir / "data/txt"
                / f"year-{year}-day-cache-stream-receipts" / f"{key}.json")
            product_path = (
                args.results_dir / "data/txt"
                / f"year-{year}-day-product-receipts" / f"{key}.json")
            stream = load_json(stream_path)
            product = load_json(product_path)
            indices = validate_day_cache_stream_contract(
                stream, key,
                expected_count=int(validation.get(
                    "required_day_products",
                    validation["required_sample_days"])),
                expected_span=int(validation["required_sample_days"]))
            expected_dates = {
                "first_date": validation.get("required_sample_start"),
                "last_date": validation.get("required_sample_end"),
            }
            for field, expected in expected_dates.items():
                if expected and stream.get(field) != expected:
                    raise ValueError(
                        f"stream {field} expected {expected}, "
                        f"found {stream.get(field)}")
            validate_day_contract_for_indices(
                product, key, indices,
                validation.get("required_sample_start"),
                validation.get("required_sample_end"))
            regenerated = validate_day_products(
                key, args.results_dir / "data/json",
                args.results_dir / "data/geojson.day",
                len(indices), indices)
            if regenerated != product:
                raise ValueError("published day contract changed")
            coverage_path = (
                args.results_dir / "data/txt"
                / f"year-{year}-coverage-evidence" / f"{key}.md")
            if not coverage_path.is_file() or coverage_path.stat().st_size == 0:
                raise ValueError("coverage evidence is missing or empty")
            day_pairs += len(indices)
            day_records.append({
                "collection_key": key,
                "status": "pass",
                "day_products": len(indices),
                "first_index": indices[0],
                "last_index": indices[-1],
                "sparse": product.get("sparse"),
                "day_stream_sha256": sha256_file(stream_path),
                "day_product_sha256": sha256_file(product_path),
                "coverage_sha256": sha256_file(coverage_path),
            })
        except (DayProductError, YearDayContractError,
                KeyError, OSError, TypeError, ValueError) as error:
            issues.append(f"day audit failed for {key}: {error}")
            day_records.append({
                "collection_key": key,
                "status": "fail",
                "issue": str(error),
            })
    day_passed = sum(record["status"] == "pass" for record in day_records)

    include_path = args.results_dir / "_includes" / f"year-{year}-0-media-objects.txt"
    include = include_path.read_text(encoding="utf-8")
    links = re.findall(
        r"^\s*- \[([^]]+)\]\((docs/itemized/[^)]+)\)\s*$",
        include, flags=re.MULTILINE)
    link_labels = [label for label, _ in links]
    link_targets_exist = all(
        (args.results_dir / target).is_file() for _, target in links)
    expected_targets = [
        f"docs/itemized/{key}-sample-cache-audit.md" for key in inventory]
    if link_labels != inventory \
            or [target for _, target in links] != expected_targets \
            or not link_targets_exist:
        issues.append("index include does not exactly link the inventory")

    scope = load_json(args.scope_receipt)
    excluded = scope.get("excluded_collection_keys", [])
    expected_excluded = [
        "3d-guns",
        "distributed-denial-of-secrets-corporate",
        "distributed-denial-of-secrets-cyberwar-rus-ukr",
        "hacks-leaks-yandex",
    ]
    if scope.get("schema") != "alpha60-year-media-object-campaign-scope/1" \
            or str(scope.get("year")) != year \
            or excluded != expected_excluded:
        issues.append("scope receipt does not contain the exact exclusions")
    if any(key in inventory for key in excluded) \
            or any(key.startswith("distributed-denial-of-secrets")
                   for key in inventory):
        issues.append("excluded key is present in the effective inventory")

    metadata_repo = args.metadata_dir.parent
    excluded_records = []
    all_result_files = [
        path.relative_to(args.results_dir).as_posix()
        for path in args.results_dir.rglob("*") if path.is_file()
    ]
    for key in excluded:
        current_path = args.metadata_dir / f"{key}.json"
        current = current_path.read_bytes()
        baseline = subprocess.run(
            ["git", "-C", str(metadata_repo), "show",
             f"{args.scope_revision}:metadata/{key}.json"],
            check=True, capture_output=True).stdout
        current_sha = sha256_bytes(current)
        baseline_sha = sha256_bytes(baseline)
        if current_sha != baseline_sha:
            issues.append(f"excluded canonical metadata changed: {key}")
        forbidden = [
            relative for relative in all_result_files
            if pathlib.PurePosixPath(relative).name.startswith(key)
        ]
        if forbidden:
            issues.append(f"excluded output published for {key}: {forbidden}")
        excluded_records.append({
            "collection_key": key,
            "scope_revision": args.scope_revision,
            "scope_sha256": baseline_sha,
            "current_sha256": current_sha,
            "unchanged": current_sha == baseline_sha,
            "published_outputs": forbidden,
        })

    publication_sources: dict[str, set[str]] = {}
    for key in inventory:
        receipt_path = (
            args.results_dir / "data/txt"
            / f"year-{year}-baseline-v2-receipts" / f"{key}.json")
        try:
            receipt = load_json(receipt_path)
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
            issues.append(f"baseline-v2 receipt unavailable for {key}: {error}")
            continue
        for component, revision in receipt.get("source_revisions", {}).items():
            if isinstance(component, str) and isinstance(revision, str):
                publication_sources.setdefault(component, set()).add(revision)
    source_revisions = {
        component: sorted(revisions)
        for component, revisions in sorted(publication_sources.items())
    }

    results_repository = git_identity(args.results_dir)
    metadata_repository = git_identity(metadata_repo)
    if not results_repository["worktree_clean"]:
        issues.append("results repository is not clean")
    if not metadata_repository["tracked_clean"]:
        issues.append("canonical metadata tracked tree is not clean")

    gates = {
        "inventory": len(inventory) == len(set(inventory))
        and set(inventory) == set(archive_records),
        "worker_terminal_dispositions": terminal_passed == len(inventory),
        "baseline_v2_pages": site_audit.get("status") == "pass",
        "day_products": day_passed == len(inventory),
        "index_links": link_labels == inventory and link_targets_exist,
        "canonical_metadata": metadata_audit.get("status") == "pass",
        "exclusions_unchanged": all(
            record["unchanged"] and not record["published_outputs"]
            for record in excluded_records),
        "repositories_clean": results_repository["worktree_clean"]
        and metadata_repository["tracked_clean"],
    }
    report = {
        "schema": "alpha60-year-baseline-v2-campaign-audit/1",
        "year": year,
        "status": "pass" if not issues and all(gates.values()) else "fail",
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "gates": gates,
        "counts": {
            "inventory": len(inventory),
            "unique": len(set(inventory)),
            "archive_records": len(archive_records),
            "worker_passed": terminal_passed,
            "worker_failed": len(inventory) - terminal_passed,
            "worker_repairs": len(repair_records),
            "baseline_v2_pages": site_counts.get("passed"),
            "day_complete": day_passed,
            "day_product_pairs": day_pairs,
            "index_links": len(links),
            "excluded_records": len(excluded_records),
        },
        "issues": issues,
        "inputs": {
            "inventory": file_identity(inventory_path),
            "archive_map": file_identity(args.archive_map),
            "site_audit": file_identity(args.site_audit),
            "metadata_audit": file_identity(args.metadata_audit),
            "scope_receipt": file_identity(args.scope_receipt),
            "original_worker_receipts": original_receipts,
            "repair_worker_receipt": file_identity(args.repair_receipt),
            "index_include": file_identity(include_path),
        },
        "publication_source_revisions": source_revisions,
        "results_repository": results_repository,
        "metadata_repository": metadata_repository,
        "terminal_records": terminal_records,
        "day_records": day_records,
        "excluded_records": excluded_records,
        "site_counts": site_counts,
        "metadata_counts": metadata_counts,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "counts": report["counts"],
        "issues": issues,
    }, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
