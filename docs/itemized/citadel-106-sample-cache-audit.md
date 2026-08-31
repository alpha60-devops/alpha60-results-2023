---
layout: default
title: "citadel-106 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# citadel-106 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Citadel |
| Collection key | `citadel-106` |
| imdb_id | [tt9794044](https://www.imdb.com/title/tt9794044/) |
| wikipedia_url | [Citadel (TV series)](https://en.wikipedia.org/wiki/Citadel_(TV_series)) |
| Sample dates | 2023-05-26-to-2023-08-11 |
| Sample days | 78 |
| BTIH count | 254 |
| Unique BTIH count | 225 |
| Downloaders total | 3,375,112 |
| Uploaders total | 579,415 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/citadel-106.xz`
- Hour directories: 1855
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 0 (0 missing hours)
- Missing days: 0

### Sample archive discontinuities

None detected.

## 3. Media objects file size histogram

![Citadel collection size histogram](figures/citadel-106-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/citadel-106-downloads-by-week-citadel-106-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![citadel-106 downloads by day](figures/citadel-106-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 6.87 | 19.90 | 19.05 | 45.74 | 1.47 | 0.48 |

### Cumulative network infrastructure

[![Citadel cumulative map](figures/citadel-106-carto.png)](figures/citadel-106-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/citadel-106-data-ge-1080p.webp)](figures/citadel-106-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/citadel-106-data-lt-1080p.webp)](figures/citadel-106-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
