---
layout: default
title: "magic-mikes-last-dance Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# magic-mikes-last-dance sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Magic Mike's Last Dance |
| Collection key | `magic-mikes-last-dance` |
| imdb_id | [tt16280138](https://www.imdb.com/title/tt16280138/) |
| wikipedia_url | [Magic Mike's Last Dance](https://en.wikipedia.org/wiki/Magic_Mike%27s_Last_Dance) |
| Sample dates | 2023-02-28-to-2023-05-08 |
| Sample days | 70 |
| BTIH count | 102 |
| Unique BTIH count | 93 |
| Downloaders total | 1,798,311 |
| Uploaders total | 487,729 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/magic-mikes-last-dance.xz`
- Hour directories: 1659
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (1 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-03-26 01:06`, resumed `2023-03-26 03:06` — missing 1 hour(s)

## 3. File sizes histogram *median[lowest, highest]*

![Magic Mike's Last Dance collection size histogram](figures/magic-mikes-last-dance-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/magic-mikes-last-dance-downloads-by-week-magic-mikes-last-dance-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![magic-mikes-last-dance downloads by day](figures/magic-mikes-last-dance-downloads-by-day-day.svg)

## 5. Cumulative Maps

<script defer type="text/javascript" crossorigin="anonymous" id="geojson-map"
        src="../../resources/izzi-map-leaflet-geojson-v7.8.js"></script>

<!-- https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/ -->

### <a href="https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/geojson.cumulative/magic-mikes-last-dance-cumulative-aggregate.geojson.gz" data-map-title="Magic Mike&#x27;s Last Dance — magic-mikes-last-dance" onclick="leaflet_map_open_window(this.href, this.dataset.mapTitle); return false;" class="table-link" aria-label="Open Magic Mike&#x27;s Last Dance (magic-mikes-last-dance) cumulative data map in new window" title="Opens interactive map for Magic Mike&#x27;s Last Dance (magic-mikes-last-dance) data">Swarm Detail</a>

### Geographic Regions

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 5.79 | 19.59 | 13.83 | 43.70 | 1.88 | 0.47 |

### Network infrastructure

[![Magic Mike's Last Dance cumulative map](figures/magic-mikes-last-dance-carto.png)](figures/magic-mikes-last-dance-carto-4k.webp){:target="_blank" rel="noopener"}

### Resolution >= 1080p

[![Cumulative >= 1080p](figures/magic-mikes-last-dance-data-ge-1080p.webp)](figures/magic-mikes-last-dance-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

### Resolution < 1080p

[![Cumulative < 1080p](figures/magic-mikes-last-dance-data-lt-1080p.webp)](figures/magic-mikes-last-dance-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
