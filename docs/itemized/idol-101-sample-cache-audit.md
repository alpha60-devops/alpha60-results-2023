---
layout: default
title: "idol-101 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# idol-101 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | The Idol |
| Collection key | `idol-101` |
| imdb_id | [tt14954666](https://www.imdb.com/title/tt14954666/) |
| wikipedia_url | [The Idol (TV series)](https://en.wikipedia.org/wiki/The_Idol_(TV_series)) |
| Sample dates | 2023-06-05-to-2023-08-20 |
| Sample days | 77 |
| BTIH count | 102 |
| Unique BTIH count | 88 |
| Downloaders total | 1,619,116 |
| Uploaders total | 337,007 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/idol-101.xz`
- Hour directories: 1796
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (48 missing hours)
- Missing days: 2

### Sample archive discontinuities

- hourly gap: last `2023-06-30 23:03`, resumed `2023-07-03 00:03` — missing 48 hour(s)
- missing day: `2023-07-01`
- missing day: `2023-07-02`

## 3. Media objects file size histogram

![The Idol collection size histogram](figures/idol-101-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/idol-101-downloads-by-week-idol-101-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![idol-101 downloads by day](figures/idol-101-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 7.01 | 20.66 | 18.90 | 41.11 | 1.76 | 0.44 |

### Cumulative network infrastructure

[![The Idol cumulative map](figures/idol-101-carto.png)](figures/idol-101-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/idol-101-data-ge-1080p.webp)](figures/idol-101-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/idol-101-data-lt-1080p.webp)](figures/idol-101-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
