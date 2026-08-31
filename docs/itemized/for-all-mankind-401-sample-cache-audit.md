---
layout: default
title: "for-all-mankind-401 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# for-all-mankind-401 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | For All Mankind |
| Collection key | `for-all-mankind-401` |
| imdb_id | [tt7772588](https://www.imdb.com/title/tt7772588/) |
| wikipedia_url | [For All Mankind (TV series)](https://en.wikipedia.org/wiki/For_All_Mankind_(TV_series)) |
| Sample dates | 2023-11-10-to-2024-05-09 |
| Sample days | 182 |
| BTIH count | 170 |
| Unique BTIH count | 164 |
| Downloaders total | 15,535,315 |
| Uploaders total | 648,563 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/for-all-mankind-401.xz`
- Hour directories: 4349
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (1 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2024-03-31 01:03`, resumed `2024-03-31 03:03` — missing 1 hour(s)

## 3. Media objects file size histogram

![For All Mankind collection size histogram](figures/for-all-mankind-401-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/for-all-mankind-401-downloads-by-week-for-all-mankind-401-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![for-all-mankind-401 downloads by day](figures/for-all-mankind-401-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 1.01 | 22.30 | 21.02 | 51.63 | 1.03 | 0.54 |

### Cumulative network infrastructure

[![For All Mankind cumulative map](figures/for-all-mankind-401-carto.png)](figures/for-all-mankind-401-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/for-all-mankind-401-data-ge-1080p.webp)](figures/for-all-mankind-401-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/for-all-mankind-401-data-lt-1080p.webp)](figures/for-all-mankind-401-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
