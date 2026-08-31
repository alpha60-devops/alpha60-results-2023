---
layout: default
title: "power-105 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# power-105 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | The Power |
| Collection key | `power-105` |
| imdb_id | [tt10369484](https://www.imdb.com/title/tt10369484/) |
| wikipedia_url | [The Power (TV series)](https://en.wikipedia.org/wiki/The_Power_(TV_series)) |
| Sample dates | 2023-04-14-to-2023-06-23 |
| Sample days | 71 |
| BTIH count | 52 |
| Unique BTIH count | 42 |
| Downloaders total | 406,340 |
| Uploaders total | 43,811 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:24Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/power-105.xz`
- Hour directories: 1682
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (4 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-05-23 09:06`, resumed `2023-05-23 14:06` — missing 4 hour(s)

## 3. Media objects file size histogram

![The Power collection size histogram](figures/power-105-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/power-105-downloads-by-week-power-105-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![power-105 downloads by day](figures/power-105-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 4.90 | 21.37 | 17.31 | 47.32 | 1.95 | 0.59 |

### Cumulative network infrastructure

[![The Power cumulative map](figures/power-105-carto.png)](figures/power-105-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/power-105-data-ge-1080p.webp)](figures/power-105-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/power-105-data-lt-1080p.webp)](figures/power-105-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
