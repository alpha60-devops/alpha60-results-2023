---
layout: default
title: "loki-206 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# loki-206 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Loki |
| Collection key | `loki-206` |
| imdb_id | [tt9140554](https://www.imdb.com/title/tt9140554/) |
| wikipedia_url | [Loki (TV series)](https://en.wikipedia.org/wiki/Loki_(TV_series)) |
| Sample dates | 2023-11-10-to-2024-05-09 |
| Sample days | 182 |
| BTIH count | 257 |
| Unique BTIH count | 241 |
| Downloaders total | 28,271,366 |
| Uploaders total | 2,266,335 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/loki-206.xz`
- Hour directories: 4363
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (1 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2024-03-31 01:06`, resumed `2024-03-31 03:06` — missing 1 hour(s)

## 3. File sizes histogram *median[lowest, highest]*

![Loki collection size histogram](figures/loki-206-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/loki-206-downloads-by-week-loki-206-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![loki-206 downloads by day](figures/loki-206-downloads-by-day-day.svg)

## 5. Cumulative Maps

<script defer type="text/javascript" crossorigin="anonymous" id="geojson-map"
        src="../../resources/izzi-map-leaflet-geojson-v7.8.js"></script>

<!-- https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/ -->

### <a href="https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/geojson.cumulative/loki-206-cumulative-aggregate.geojson.gz" data-map-title="Loki — loki-206" onclick="leaflet_map_open_window(this.href, this.dataset.mapTitle); return false;" class="table-link" aria-label="Open Loki (loki-206) cumulative data map in new window" title="Opens interactive map for Loki (loki-206) data">Swarm Detail</a>

### Geographic Regions

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 2.40 | 20.14 | 24.05 | 49.78 | 0.87 | 0.57 |

### Network infrastructure

[![Loki cumulative map](figures/loki-206-carto.png)](figures/loki-206-carto-4k.webp){:target="_blank" rel="noopener"}

### Resolution >= 1080p

[![Cumulative >= 1080p](figures/loki-206-data-ge-1080p.webp)](figures/loki-206-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

### Resolution < 1080p

[![Cumulative < 1080p](figures/loki-206-data-lt-1080p.webp)](figures/loki-206-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
