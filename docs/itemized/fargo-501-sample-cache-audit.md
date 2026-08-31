---
layout: default
title: "fargo-501 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# fargo-501 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Fargo |
| Collection key | `fargo-501` |
| imdb_id | [tt2802850](https://www.imdb.com/title/tt2802850/) |
| wikipedia_url | [Fargo (TV series)](https://en.wikipedia.org/wiki/Fargo_(TV_series)) |
| Sample dates | 2023-11-22-to-2024-03-05 |
| Sample days | 105 |
| BTIH count | 197 |
| Unique BTIH count | 174 |
| Downloaders total | 11,148,227 |
| Uploaders total | 1,060,645 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/fargo-501.xz`
- Hour directories: 2494
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (10 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2024-02-16 19:00`, resumed `2024-02-17 06:40` — missing 10 hour(s)

## 3. Media objects file size histogram

![Fargo collection size histogram](figures/fargo-501-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/fargo-501-downloads-by-week-fargo-501-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![fargo-501 downloads by day](figures/fargo-501-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 1.80 | 23.14 | 19.89 | 50.40 | 1.43 | 0.47 |

### Cumulative network infrastructure

[![Fargo cumulative map](figures/fargo-501-carto.png)](figures/fargo-501-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/fargo-501-data-ge-1080p.webp)](figures/fargo-501-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/fargo-501-data-lt-1080p.webp)](figures/fargo-501-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
