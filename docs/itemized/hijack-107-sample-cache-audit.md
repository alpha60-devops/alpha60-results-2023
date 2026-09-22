---
layout: default
title: "hijack-107 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# hijack-107 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Hijack |
| Collection key | `hijack-107` |
| imdb_id | [tt19854762](https://www.imdb.com/title/tt19854762/) |
| wikipedia_url | [Hijack (TV series)](https://en.wikipedia.org/wiki/Hijack_(TV_series)) |
| Sample dates | 2023-08-02-to-2023-11-15 |
| Sample days | 106 |
| BTIH count | 177 |
| Unique BTIH count | 156 |
| Downloaders total | 6,415,091 |
| Uploaders total | 1,362,597 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/hijack-107.xz`
- Hour directories: 2431
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 2 (86 missing hours)
- Missing days: 1

### Sample archive discontinuities

- hourly gap: last `2023-09-15 01:00`, resumed `2023-09-16 20:00` — missing 42 hour(s)
- hourly gap: last `2023-10-06 22:00`, resumed `2023-10-08 19:00` — missing 44 hour(s)
- missing day: `2023-10-07`

## 3. File sizes histogram *median[lowest, highest]*

![Hijack collection size histogram](figures/hijack-107-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/hijack-107-downloads-by-week-hijack-107-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![hijack-107 downloads by day](figures/hijack-107-downloads-by-day-day.svg)

## 5. Cumulative Maps

<script defer type="text/javascript" crossorigin="anonymous" id="geojson-map"
        src="../../resources/izzi-map-leaflet-geojson-v7.8.js"></script>

<!-- https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/ -->

### <a href="https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/geojson.cumulative/hijack-107-cumulative-aggregate.geojson.gz" data-map-title="Hijack — hijack-107" onclick="leaflet_map_open_window(this.href, this.dataset.mapTitle); return false;" class="table-link" aria-label="Open Hijack (hijack-107) cumulative data map in new window" title="Opens interactive map for Hijack (hijack-107) data">Swarm Detail</a>

### Geographic Regions

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 7.41 | 17.11 | 17.34 | 52.44 | 1.70 | 0.55 |

### Network infrastructure

[![Hijack cumulative map](figures/hijack-107-carto.png)](figures/hijack-107-carto-4k.webp){:target="_blank" rel="noopener"}

### Resolution >= 1080p

[![Cumulative >= 1080p](figures/hijack-107-data-ge-1080p.webp)](figures/hijack-107-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

### Resolution < 1080p

[![Cumulative < 1080p](figures/hijack-107-data-lt-1080p.webp)](figures/hijack-107-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
