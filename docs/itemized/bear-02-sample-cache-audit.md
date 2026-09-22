---
layout: default
title: "bear-02 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# bear-02 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | The Bear |
| Collection key | `bear-02` |
| imdb_id | [tt14452776](https://www.imdb.com/title/tt14452776/) |
| wikipedia_url | [The Bear (TV series)](https://en.wikipedia.org/wiki/The_Bear_(TV_series)) |
| Sample dates | 2023-06-22-to-2023-12-20 |
| Sample days | 182 |
| BTIH count | 448 |
| Unique BTIH count | 410 |
| Downloaders total | 23,270,247 |
| Uploaders total | 3,043,763 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/bear-02.xz`
- Hour directories: 4331
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 2 (27 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-08-29 09:06`, resumed `2023-08-29 14:06` — missing 4 hour(s)
- hourly gap: last `2023-12-01 22:06`, resumed `2023-12-02 22:30` — missing 23 hour(s)

## 3. File sizes histogram *median[lowest, highest]*

![The Bear collection size histogram](figures/bear-02-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/bear-02-downloads-by-week-bear-02-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![bear-02 downloads by day](figures/bear-02-downloads-by-day-day.svg)

## 5. Cumulative Maps

<script defer type="text/javascript" crossorigin="anonymous" id="geojson-map"
        src="../../resources/izzi-map-leaflet-geojson-v7.8.js"></script>

<!-- https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/ -->

### <a href="https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/geojson.cumulative/bear-02-cumulative-aggregate.geojson.gz" data-map-title="The Bear — bear-02" onclick="leaflet_map_open_window(this.href, this.dataset.mapTitle); return false;" class="table-link" aria-label="Open The Bear (bear-02) cumulative data map in new window" title="Opens interactive map for The Bear (bear-02) data">Swarm Detail</a>

### Geographic Regions

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 2.46 | 23.70 | 17.95 | 50.25 | 1.85 | 0.51 |

### Network infrastructure

[![The Bear cumulative map](figures/bear-02-carto.png)](figures/bear-02-carto-4k.webp){:target="_blank" rel="noopener"}

### Resolution >= 1080p

[![Cumulative >= 1080p](figures/bear-02-data-ge-1080p.webp)](figures/bear-02-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

### Resolution < 1080p

[![Cumulative < 1080p](figures/bear-02-data-lt-1080p.webp)](figures/bear-02-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
