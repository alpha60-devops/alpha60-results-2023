---
layout: default
title: "mandalorian-308 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# mandalorian-308 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | The Mandalorian |
| Collection key | `mandalorian-308` |
| imdb_id | [tt8111088](https://www.imdb.com/title/tt8111088/) |
| wikipedia_url | [The Mandalorian](https://en.wikipedia.org/wiki/The_Mandalorian) |
| Sample dates | 2023-04-19-to-2023-08-01 |
| Sample days | 105 |
| BTIH count | 312 |
| Unique BTIH count | 266 |
| Downloaders total | 7,629,635 |
| Uploaders total | 2,051,761 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/mandalorian-308.xz`
- Hour directories: 2474
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 6 (30 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-04-19 22:00`, resumed `2023-04-20 00:00` — missing 1 hour(s)
- hourly gap: last `2023-04-20 22:00`, resumed `2023-04-21 00:00` — missing 1 hour(s)
- hourly gap: last `2023-04-21 22:00`, resumed `2023-04-22 00:00` — missing 1 hour(s)
- hourly gap: last `2023-05-23 09:00`, resumed `2023-05-23 14:00` — missing 4 hour(s)
- hourly gap: last `2023-07-11 23:00`, resumed `2023-07-12 17:00` — missing 17 hour(s)
- hourly gap: last `2023-07-30 12:00`, resumed `2023-07-30 19:00` — missing 6 hour(s)

## 3. Media objects file size histogram

![The Mandalorian collection size histogram](figures/mandalorian-308-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/mandalorian-308-downloads-by-week-mandalorian-308-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![mandalorian-308 downloads by day](figures/mandalorian-308-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 3.34 | 19.86 | 16.21 | 53.42 | 2.30 | 0.51 |

### Cumulative network infrastructure

[![The Mandalorian cumulative map](figures/mandalorian-308-carto.png)](figures/mandalorian-308-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/mandalorian-308-data-ge-1080p.webp)](figures/mandalorian-308-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/mandalorian-308-data-lt-1080p.webp)](figures/mandalorian-308-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
