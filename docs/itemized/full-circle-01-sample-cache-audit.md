---
layout: default
title: "full-circle-01 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# full-circle-01 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Full Circle |
| Collection key | `full-circle-01` |
| imdb_id | [tt15303234](https://www.imdb.com/title/tt15303234/) |
| wikipedia_url | [Full Circle (miniseries)](https://en.wikipedia.org/wiki/Full_Circle_(miniseries)) |
| Sample dates | 2023-07-14-to-2023-11-03 |
| Sample days | 113 |
| BTIH count | 400 |
| Unique BTIH count | 376 |
| Downloaders total | 3,973,585 |
| Uploaders total | 270,362 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/full-circle-01.xz`
- Hour directories: 2706
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 0 (0 missing hours)
- Missing days: 0

### Sample archive discontinuities

None detected.

## 3. Media objects file size histogram

![Full Circle collection size histogram](figures/full-circle-01-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/full-circle-01-downloads-by-week-full-circle-01-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![full-circle-01 downloads by day](figures/full-circle-01-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 4.22 | 22.60 | 17.42 | 52.51 | 1.56 | 0.57 |

### Cumulative network infrastructure

[![Full Circle cumulative map](figures/full-circle-01-carto.png)](figures/full-circle-01-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/full-circle-01-data-ge-1080p.webp)](figures/full-circle-01-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/full-circle-01-data-lt-1080p.webp)](figures/full-circle-01-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
