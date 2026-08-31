---
layout: default
title: "gen-v-101 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# gen-v-101 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Gen V |
| Collection key | `gen-v-101` |
| imdb_id | [tt13159924](https://www.imdb.com/title/tt13159924/) |
| wikipedia_url | [Gen V](https://en.wikipedia.org/wiki/Gen_V) |
| Sample dates | 2023-09-29-to-2024-03-28 |
| Sample days | 182 |
| BTIH count | 317 |
| Unique BTIH count | 282 |
| Downloaders total | 28,495,254 |
| Uploaders total | 2,966,275 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/gen-v-101.xz`
- Hour directories: 4353
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (10 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2024-02-16 19:00`, resumed `2024-02-17 06:00` — missing 10 hour(s)

## 3. Media objects file size histogram

![Gen V collection size histogram](figures/gen-v-101-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/gen-v-101-downloads-by-week-gen-v-101-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![gen-v-101 downloads by day](figures/gen-v-101-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 3.90 | 21.27 | 22.22 | 48.34 | 1.28 | 0.51 |

### Cumulative network infrastructure

[![Gen V cumulative map](figures/gen-v-101-carto.png)](figures/gen-v-101-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/gen-v-101-data-ge-1080p.webp)](figures/gen-v-101-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/gen-v-101-data-lt-1080p.webp)](figures/gen-v-101-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
