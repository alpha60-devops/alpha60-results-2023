---
layout: default
title: "foundation-201 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# foundation-201 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Foundation |
| Collection key | `foundation-201` |
| imdb_id | [tt0804484](https://www.imdb.com/title/tt0804484/) |
| wikipedia_url | [Foundation (TV series)](https://en.wikipedia.org/wiki/Foundation_(TV_series)) |
| Sample dates | 2023-07-14-to-2023-10-26 |
| Sample days | 105 |
| BTIH count | 137 |
| Unique BTIH count | 118 |
| Downloaders total | 4,213,091 |
| Uploaders total | 900,370 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/foundation-201.xz`
- Hour directories: 2503
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 0 (0 missing hours)
- Missing days: 0

### Sample archive discontinuities

None detected.

## 3. Media objects file size histogram

![Foundation collection size histogram](figures/foundation-201-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/foundation-201-downloads-by-week-foundation-201-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![foundation-201 downloads by day](figures/foundation-201-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 4.00 | 22.47 | 16.42 | 49.22 | 2.26 | 0.58 |

### Cumulative network infrastructure

[![Foundation cumulative map](figures/foundation-201-carto.png)](figures/foundation-201-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/foundation-201-data-ge-1080p.webp)](figures/foundation-201-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/foundation-201-data-lt-1080p.webp)](figures/foundation-201-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
