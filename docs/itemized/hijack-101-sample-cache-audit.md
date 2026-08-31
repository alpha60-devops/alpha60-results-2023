---
layout: default
title: "hijack-101 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# hijack-101 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Hijack |
| Collection key | `hijack-101` |
| imdb_id | [tt19854762](https://www.imdb.com/title/tt19854762/) |
| wikipedia_url | [Hijack (TV series)](https://en.wikipedia.org/wiki/Hijack_(TV_series)) |
| Sample dates | 2023-06-29-to-2023-10-18 |
| Sample days | 112 |
| BTIH count | 193 |
| Unique BTIH count | 171 |
| Downloaders total | 5,620,287 |
| Uploaders total | 1,258,951 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/hijack-101.xz`
- Hour directories: 2591
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 3 (92 missing hours)
- Missing days: 1

### Sample archive discontinuities

- hourly gap: last `2023-07-30 12:03`, resumed `2023-07-30 19:03` — missing 6 hour(s)
- hourly gap: last `2023-09-15 01:03`, resumed `2023-09-16 20:03` — missing 42 hour(s)
- hourly gap: last `2023-10-06 22:03`, resumed `2023-10-08 19:03` — missing 44 hour(s)
- missing day: `2023-10-07`

## 3. Media objects file size histogram

![Hijack collection size histogram](figures/hijack-101-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/hijack-101-downloads-by-week-hijack-101-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![hijack-101 downloads by day](figures/hijack-101-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 11.16 | 20.83 | 17.16 | 42.24 | 2.71 | 0.46 |

### Cumulative network infrastructure

[![Hijack cumulative map](figures/hijack-101-carto.png)](figures/hijack-101-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/hijack-101-data-ge-1080p.webp)](figures/hijack-101-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/hijack-101-data-lt-1080p.webp)](figures/hijack-101-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
