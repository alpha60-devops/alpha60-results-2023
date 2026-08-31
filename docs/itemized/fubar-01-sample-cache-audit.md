---
layout: default
title: "fubar-01 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# fubar-01 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | FUBAR |
| Collection key | `fubar-01` |
| imdb_id | [tt13064902](https://www.imdb.com/title/tt13064902/) |
| wikipedia_url | [FUBAR (TV series)](https://en.wikipedia.org/wiki/FUBAR_(TV_series)) |
| Sample dates | 2023-05-25-to-2023-09-16 |
| Sample days | 115 |
| BTIH count | 399 |
| Unique BTIH count | 371 |
| Downloaders total | 7,038,903 |
| Uploaders total | 1,095,302 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/fubar-01.xz`
- Hour directories: 2733
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (4 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-08-29 09:00`, resumed `2023-08-29 14:00` — missing 4 hour(s)

## 3. Media objects file size histogram

![FUBAR collection size histogram](figures/fubar-01-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/fubar-01-downloads-by-week-fubar-01-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![fubar-01 downloads by day](figures/fubar-01-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 3.11 | 22.82 | 17.10 | 51.03 | 1.50 | 0.59 |

### Cumulative network infrastructure

[![FUBAR cumulative map](figures/fubar-01-carto.png)](figures/fubar-01-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/fubar-01-data-ge-1080p.webp)](figures/fubar-01-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/fubar-01-data-lt-1080p.webp)](figures/fubar-01-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
