---
layout: default
title: "barry-401 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# barry-401 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Barry |
| Collection key | `barry-401` |
| imdb_id | [tt5348176](https://www.imdb.com/title/tt5348176/) |
| wikipedia_url | [Barry (TV series)](https://en.wikipedia.org/wiki/Barry_(TV_series)) |
| Sample dates | 2023-04-17-to-2023-06-25 |
| Sample days | 70 |
| BTIH count | 94 |
| Unique BTIH count | 88 |
| Downloaders total | 1,070,964 |
| Uploaders total | 218,176 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/barry-401.xz`
- Hour directories: 1662
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 0 (0 missing hours)
- Missing days: 0

### Sample archive discontinuities

None detected.

## 3. Media objects file size histogram

![Barry collection size histogram](figures/barry-401-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/barry-401-downloads-by-week-barry-401-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![barry-401 downloads by day](figures/barry-401-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 3.05 | 28.06 | 15.84 | 43.12 | 3.90 | 0.43 |

### Cumulative network infrastructure

[![Barry cumulative map](figures/barry-401-carto.png)](figures/barry-401-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/barry-401-data-ge-1080p.webp)](figures/barry-401-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/barry-401-data-lt-1080p.webp)](figures/barry-401-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
