---
layout: default
title: "curse-01 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# curse-01 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | The Curse |
| Collection key | `curse-01` |
| imdb_id | [tt13623608](https://www.imdb.com/title/tt13623608/) |
| wikipedia_url | [The Curse (American TV series)](https://en.wikipedia.org/wiki/The_Curse_(American_TV_series)) |
| Sample dates | 2023-11-10-to-2024-02-22 |
| Sample days | 105 |
| BTIH count | 357 |
| Unique BTIH count | 335 |
| Downloaders total | 11,412,792 |
| Uploaders total | 927,254 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/curse-01.xz`
- Hour directories: 2511
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 0 (0 missing hours)
- Missing days: 0

### Sample archive discontinuities

None detected.

## 3. File sizes histogram *median[lowest, highest]*

![The Curse collection size histogram](figures/curse-01-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/curse-01-downloads-by-week-curse-01-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![curse-01 downloads by day](figures/curse-01-downloads-by-day-day.svg)

## 5. Cumulative Maps

<script defer type="text/javascript" crossorigin="anonymous" id="geojson-map"
        src="../../resources/izzi-map-leaflet-geojson-v7.8.js"></script>

<!-- https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/ -->

### <a href="https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/geojson.cumulative/curse-01-cumulative-aggregate.geojson.gz" data-map-title="The Curse — curse-01" onclick="leaflet_map_open_window(this.href, this.dataset.mapTitle); return false;" class="table-link" aria-label="Open The Curse (curse-01) cumulative data map in new window" title="Opens interactive map for The Curse (curse-01) data">Swarm Detail</a>

### Geographic Regions

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 1.34 | 26.75 | 18.97 | 49.23 | 1.61 | 0.50 |

### Network infrastructure

[![The Curse cumulative map](figures/curse-01-carto.png)](figures/curse-01-carto-4k.webp){:target="_blank" rel="noopener"}

### Resolution >= 1080p

[![Cumulative >= 1080p](figures/curse-01-data-ge-1080p.webp)](figures/curse-01-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

### Resolution < 1080p

[![Cumulative < 1080p](figures/curse-01-data-lt-1080p.webp)](figures/curse-01-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
