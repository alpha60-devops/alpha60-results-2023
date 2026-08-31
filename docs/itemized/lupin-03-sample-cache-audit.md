---
layout: default
title: "lupin-03 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# lupin-03 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Lupin |
| Collection key | `lupin-03` |
| imdb_id | [tt2531336](https://www.imdb.com/title/tt2531336/) |
| wikipedia_url | [Lupin (French TV series)](https://en.wikipedia.org/wiki/Lupin_(French_TV_series)) |
| Sample dates | 2023-10-05-to-2024-01-17 |
| Sample days | 105 |
| BTIH count | 271 |
| Unique BTIH count | 238 |
| Downloaders total | 12,338,731 |
| Uploaders total | 873,041 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/lupin-03.xz`
- Hour directories: 2481
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (23 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-12-01 22:03`, resumed `2023-12-02 22:30` — missing 23 hour(s)

## 3. Media objects file size histogram

![Lupin collection size histogram](figures/lupin-03-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/lupin-03-downloads-by-week-lupin-03-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![lupin-03 downloads by day](figures/lupin-03-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 3.30 | 21.29 | 18.25 | 54.47 | 0.67 | 0.47 |

### Cumulative network infrastructure

[![Lupin cumulative map](figures/lupin-03-carto.png)](figures/lupin-03-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/lupin-03-data-ge-1080p.webp)](figures/lupin-03-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/lupin-03-data-lt-1080p.webp)](figures/lupin-03-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
