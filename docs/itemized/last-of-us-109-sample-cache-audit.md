---
layout: default
title: "last-of-us-109 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# last-of-us-109 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Last of Us |
| Collection key | `last-of-us-109` |
| imdb_id | [tt3581920](https://www.imdb.com/title/tt3581920/) |
| wikipedia_url | [The Last of Us (TV series)](https://en.wikipedia.org/wiki/The_Last_of_Us_(TV_series)) |
| Sample dates | 2023-03-13-to-2023-07-02 |
| Sample days | 112 |
| BTIH count | 316 |
| Unique BTIH count | 283 |
| Downloaders total | 11,509,026 |
| Uploaders total | 3,732,601 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/last-of-us-109.xz`
- Hour directories: 2680
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 2 (5 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-03-26 01:06`, resumed `2023-03-26 03:06` — missing 1 hour(s)
- hourly gap: last `2023-05-11 09:06`, resumed `2023-05-11 14:06` — missing 4 hour(s)

## 3. Media objects file size histogram

![Last of Us collection size histogram](figures/last-of-us-109-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/last-of-us-109-downloads-by-week-last-of-us-109-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![last-of-us-109 downloads by day](figures/last-of-us-109-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 5.22 | 19.49 | 18.70 | 48.15 | 2.45 | 0.55 |

### Cumulative network infrastructure

[![Last of Us cumulative map](figures/last-of-us-109-carto.png)](figures/last-of-us-109-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/last-of-us-109-data-ge-1080p.webp)](figures/last-of-us-109-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/last-of-us-109-data-lt-1080p.webp)](figures/last-of-us-109-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
