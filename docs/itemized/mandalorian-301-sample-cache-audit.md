---
layout: default
title: "mandalorian-301 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# mandalorian-301 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | The Mandalorian |
| Collection key | `mandalorian-301` |
| imdb_id | [tt8111088](https://www.imdb.com/title/tt8111088/) |
| wikipedia_url | [The Mandalorian](https://en.wikipedia.org/wiki/The_Mandalorian) |
| Sample dates | 2023-03-01-to-2023-08-29 |
| Sample days | 182 |
| BTIH count | 252 |
| Unique BTIH count | 230 |
| Downloaders total | 9,852,929 |
| Uploaders total | 2,329,478 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/mandalorian-301.xz`
- Hour directories: 4350
- Zero-length sample files: 1
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (1 missing hours)
- Missing days: 0

Zero-length files are sampler-failure evidence: a sampler killed
before writing the file, or a sampling host whose disk filled
before the write completed. Caching proceeded past every file
listed here.

### Zero-length sample files

- `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/mandalorian-301.xz/2023-04-18-at-13-00.tar.xz`

### Sample archive discontinuities

- hourly gap: last `2023-03-26 01:00`, resumed `2023-03-26 03:00` — missing 1 hour(s)

## 3. Media objects file size histogram

![The Mandalorian collection size histogram](figures/mandalorian-301-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/mandalorian-301-downloads-by-week-mandalorian-301-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![mandalorian-301 downloads by day](figures/mandalorian-301-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 3.10 | 21.59 | 17.77 | 49.88 | 1.93 | 0.51 |

### Cumulative network infrastructure

[![The Mandalorian cumulative map](figures/mandalorian-301-carto.png)](figures/mandalorian-301-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/mandalorian-301-data-ge-1080p.webp)](figures/mandalorian-301-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/mandalorian-301-data-lt-1080p.webp)](figures/mandalorian-301-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
