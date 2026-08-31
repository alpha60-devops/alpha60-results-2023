---
layout: default
title: "citadel-101 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# citadel-101 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Citadel |
| Collection key | `citadel-101` |
| imdb_id | [tt9794044](https://www.imdb.com/title/tt9794044/) |
| wikipedia_url | [Citadel (TV series)](https://en.wikipedia.org/wiki/Citadel_(TV_series)) |
| Sample dates | 2023-04-28-to-2023-06-22 |
| Sample days | 56 |
| BTIH count | 247 |
| Unique BTIH count | 211 |
| Downloaders total | 3,611,137 |
| Uploaders total | 944,160 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/citadel-101.xz`
- Hour directories: 2507
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (2 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-05-03 23:06`, resumed `2023-05-04 03:00` — missing 2 hour(s)

## 3. Media objects file size histogram

![Citadel collection size histogram](figures/citadel-101-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/citadel-101-downloads-by-week-citadel-101-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![citadel-101 downloads by day](figures/citadel-101-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 12.53 | 18.76 | 21.52 | 38.69 | 2.83 | 0.60 |

### Cumulative network infrastructure

[![Citadel cumulative map](figures/citadel-101-carto.png)](figures/citadel-101-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/citadel-101-data-ge-1080p.webp)](figures/citadel-101-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/citadel-101-data-lt-1080p.webp)](figures/citadel-101-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
