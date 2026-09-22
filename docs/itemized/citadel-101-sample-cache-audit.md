---
layout: default
title: "citadel-101 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# citadel-101 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Citadel |
| Collection key | `citadel-101` |
| imdb_id | [tt9794044](https://www.imdb.com/title/tt9794044/) |
| wikipedia_url | [Citadel (TV series)](https://en.wikipedia.org/wiki/Citadel_(TV_series)) |
| Sample dates | 2023-04-28-to-2023-06-22 |
| Sample days | 56 |
| BTIH count | 247 |
| Unique BTIH count | 211 |
| Downloaders total | 3,611,137 |
| Uploaders total | 944,160 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/citadel-101.xz`
- Hour directories: 2507
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (2 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-05-03 23:06`, resumed `2023-05-04 03:00` — missing 2 hour(s)

## 3. File sizes histogram *median[lowest, highest]*

![Citadel collection size histogram](figures/citadel-101-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/citadel-101-downloads-by-week-citadel-101-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![citadel-101 downloads by day](figures/citadel-101-downloads-by-day-day.svg)

## 5. Cumulative Maps

<script defer type="text/javascript" crossorigin="anonymous" id="geojson-map"
        src="../../resources/izzi-map-leaflet-geojson-v7.8.js"></script>

<!-- https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/ -->

### <a href="https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/geojson.cumulative/citadel-101-cumulative-aggregate.geojson.gz" data-map-title="Citadel — citadel-101" onclick="leaflet_map_open_window(this.href, this.dataset.mapTitle); return false;" class="table-link" aria-label="Open Citadel (citadel-101) cumulative data map in new window" title="Opens interactive map for Citadel (citadel-101) data">Swarm Detail</a>

### Geographic Regions

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 12.53 | 18.76 | 21.52 | 38.69 | 2.83 | 0.60 |

### Network infrastructure

[![Citadel cumulative map](figures/citadel-101-carto.png)](figures/citadel-101-carto-4k.webp){:target="_blank" rel="noopener"}

### Resolution >= 1080p

[![Cumulative >= 1080p](figures/citadel-101-data-ge-1080p.webp)](figures/citadel-101-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

### Resolution < 1080p

[![Cumulative < 1080p](figures/citadel-101-data-lt-1080p.webp)](figures/citadel-101-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
