---
layout: default
title: "power-109 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# power-109 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | The Power |
| Collection key | `power-109` |
| imdb_id | [tt10369484](https://www.imdb.com/title/tt10369484/) |
| wikipedia_url | [The Power (TV series)](https://en.wikipedia.org/wiki/The_Power_(TV_series)) |
| Sample dates | 2023-05-12-to-2023-07-20 |
| Sample days | 70 |
| BTIH count | 93 |
| Unique BTIH count | 75 |
| Downloaders total | 757,561 |
| Uploaders total | 77,050 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Coverage report

- Generated: 2026-08-31T06:28:24Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/power-109.xz`
- Hour directories: 1672
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (4 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-05-23 09:06`, resumed `2023-05-23 14:06` — missing 4 hour(s)

## 3. File sizes histogram *median[lowest, highest]*

![The Power collection size histogram](figures/power-109-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/power-109-downloads-by-week-power-109-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![power-109 downloads by day](figures/power-109-downloads-by-day-day.svg)

## 5. Cumulative Maps

<script defer type="text/javascript" crossorigin="anonymous" id="geojson-map"
        src="../../resources/izzi-map-leaflet-geojson-v7.8.js"></script>

<!-- https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/ -->

### <a href="https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/geojson.cumulative/power-109-cumulative-aggregate.geojson.gz" data-map-title="The Power — power-109" onclick="leaflet_map_open_window(this.href, this.dataset.mapTitle); return false;" class="table-link" aria-label="Open The Power (power-109) cumulative data map in new window" title="Opens interactive map for The Power (power-109) data">Swarm Detail</a>

### Geographic Regions

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 3.22 | 20.56 | 18.23 | 48.91 | 1.57 | 0.61 |

### Network infrastructure

[![The Power cumulative map](figures/power-109-carto.png)](figures/power-109-carto-4k.webp){:target="_blank" rel="noopener"}

### Resolution >= 1080p

[![Cumulative >= 1080p](figures/power-109-data-ge-1080p.webp)](figures/power-109-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

### Resolution < 1080p

[![Cumulative < 1080p](figures/power-109-data-lt-1080p.webp)](figures/power-109-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
