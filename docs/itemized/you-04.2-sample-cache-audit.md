---
layout: default
title: "you-04.2 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# you-04.2 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | You |
| Collection key | `you-04.2` |
| imdb_id | [tt7335184](https://www.imdb.com/title/tt7335184/) |
| wikipedia_url | [You (TV series)](https://en.wikipedia.org/wiki/You_(TV_series)) |
| Sample dates | 2023-03-09-to-2023-05-17 |
| Sample days | 70 |
| BTIH count | 133 |
| Unique BTIH count | 126 |
| Downloaders total | 1,630,447 |
| Uploaders total | 355,683 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:24Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/you-04.2.xz`
- Hour directories: 1655
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 2 (5 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-03-26 01:03`, resumed `2023-03-26 03:03` — missing 1 hour(s)
- hourly gap: last `2023-05-11 09:03`, resumed `2023-05-11 14:03` — missing 4 hour(s)

## 3. Media objects file size histogram

![You collection size histogram](figures/you-04.2-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/you-04-2-downloads-by-week-you-04.2-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![you-04.2 downloads by day](figures/you-04-2-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 12.65 | 20.22 | 15.99 | 40.60 | 1.65 | 0.43 |

### Cumulative network infrastructure

[![You cumulative map](figures/you-04.2-carto.png)](figures/you-04.2-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/you-04.2-data-ge-1080p.webp)](figures/you-04.2-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/you-04.2-data-lt-1080p.webp)](figures/you-04.2-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
