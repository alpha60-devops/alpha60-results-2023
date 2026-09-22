---
layout: default
title: "minx-02 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# minx-02 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Minx |
| Collection key | `minx-02` |
| imdb_id | [tt11947418](https://www.imdb.com/title/tt11947418/) |
| wikipedia_url | [Minx (TV series)](https://en.wikipedia.org/wiki/Minx_(TV_series)) |
| Sample dates | 2023-07-21-to-2023-11-09 |
| Sample days | 112 |
| BTIH count | 224 |
| Unique BTIH count | 219 |
| Downloaders total | 4,146,258 |
| Uploaders total | 263,256 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Coverage report

- Generated: 2026-08-31T06:28:24Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/minx-02.xz`
- Hour directories: 2668
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (4 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-09-25 23:06`, resumed `2023-09-26 04:15` — missing 4 hour(s)

## 3. File sizes histogram *median[lowest, highest]*

![Minx collection size histogram](figures/minx-02-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/minx-02-downloads-by-week-minx-02-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![minx-02 downloads by day](figures/minx-02-downloads-by-day-day.svg)

## 5. Cumulative Maps

<script defer type="text/javascript" crossorigin="anonymous" id="geojson-map"
        src="../../resources/izzi-map-leaflet-geojson-v7.8.js"></script>

<!-- https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/ -->

### <a href="https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/geojson.cumulative/minx-02-cumulative-aggregate.geojson.gz" data-map-title="Minx — minx-02" onclick="leaflet_map_open_window(this.href, this.dataset.mapTitle); return false;" class="table-link" aria-label="Open Minx (minx-02) cumulative data map in new window" title="Opens interactive map for Minx (minx-02) data">Swarm Detail</a>

### Geographic Regions

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 1.15 | 22.93 | 19.20 | 53.26 | 1.16 | 0.61 |

### Network infrastructure

[![Minx cumulative map](figures/minx-02-carto.png)](figures/minx-02-carto-4k.webp){:target="_blank" rel="noopener"}

### Resolution >= 1080p

[![Cumulative >= 1080p](figures/minx-02-data-ge-1080p.webp)](figures/minx-02-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

### Resolution < 1080p

[![Cumulative < 1080p](figures/minx-02-data-lt-1080p.webp)](figures/minx-02-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
