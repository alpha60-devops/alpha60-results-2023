---
layout: default
title: "loki-201 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# loki-201 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Loki |
| Collection key | `loki-201` |
| imdb_id | [tt9140554](https://www.imdb.com/title/tt9140554/) |
| wikipedia_url | [Loki (TV series)](https://en.wikipedia.org/wiki/Loki_(TV_series)) |
| Sample dates | 2023-10-06-to-2024-04-04 |
| Sample days | 182 |
| BTIH count | 263 |
| Unique BTIH count | 234 |
| Downloaders total | 25,645,455 |
| Uploaders total | 2,304,262 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/loki-201.xz`
- Hour directories: 4327
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 3 (35 missing hours)
- Missing days: 1

### Sample archive discontinuities

- hourly gap: last `2023-12-21 23:06`, resumed `2023-12-23 00:06` — missing 24 hour(s)
- hourly gap: last `2024-02-16 19:06`, resumed `2024-02-17 07:03` — missing 10 hour(s)
- hourly gap: last `2024-03-31 01:03`, resumed `2024-03-31 03:03` — missing 1 hour(s)
- missing day: `2023-12-22`

## 3. Media objects file size histogram

![Loki collection size histogram](figures/loki-201-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/loki-201-downloads-by-week-loki-201-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![loki-201 downloads by day](figures/loki-201-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 2.51 | 21.35 | 23.34 | 48.35 | 0.94 | 0.51 |

### Cumulative network infrastructure

[![Loki cumulative map](figures/loki-201-carto.png)](figures/loki-201-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/loki-201-data-ge-1080p.webp)](figures/loki-201-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/loki-201-data-lt-1080p.webp)](figures/loki-201-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
