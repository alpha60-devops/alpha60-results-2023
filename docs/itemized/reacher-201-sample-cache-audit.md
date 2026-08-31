---
layout: default
title: "reacher-201 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# reacher-201 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Reacher |
| Collection key | `reacher-201` |
| imdb_id | [tt9288030](https://www.imdb.com/title/tt9288030/) |
| wikipedia_url | [Reacher (TV series)](https://en.wikipedia.org/wiki/Reacher_(TV_series)) |
| Sample dates | 2023-12-15-to-2024-06-13 |
| Sample days | 182 |
| BTIH count | 282 |
| Unique BTIH count | 242 |
| Downloaders total | 31,651,948 |
| Uploaders total | 3,489,993 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:24Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/reacher-201.xz`
- Hour directories: 4361
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (1 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2024-03-31 01:06`, resumed `2024-03-31 03:06` — missing 1 hour(s)

## 3. Media objects file size histogram

![Reacher collection size histogram](figures/reacher-201-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/reacher-201-downloads-by-week-reacher-201-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![reacher-201 downloads by day](figures/reacher-201-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 4.58 | 19.68 | 22.71 | 48.82 | 1.79 | 0.58 |

### Cumulative network infrastructure

[![Reacher cumulative map](figures/reacher-201-carto.png)](figures/reacher-201-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/reacher-201-data-ge-1080p.webp)](figures/reacher-201-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/reacher-201-data-lt-1080p.webp)](figures/reacher-201-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
