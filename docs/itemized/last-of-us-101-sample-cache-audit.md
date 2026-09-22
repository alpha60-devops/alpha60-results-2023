---
layout: default
title: "last-of-us-101 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# last-of-us-101 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Last of Us |
| Collection key | `last-of-us-101` |
| imdb_id | [tt3581920](https://www.imdb.com/title/tt3581920/) |
| wikipedia_url | [The Last of Us (TV series)](https://en.wikipedia.org/wiki/The_Last_of_Us_(TV_series)) |
| Sample dates | 2023-01-16-to-2023-07-16 |
| Sample days | 182 |
| BTIH count | 228 |
| Unique BTIH count | 206 |
| Downloaders total | 14,927,147 |
| Uploaders total | 4,504,122 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/last-of-us-101.xz`
- Hour directories: 4335
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 4 (29 missing hours)
- Missing days: 1

### Sample archive discontinuities

- hourly gap: last `2023-03-26 01:00`, resumed `2023-03-26 03:00` — missing 1 hour(s)
- hourly gap: last `2023-04-29 23:00`, resumed `2023-05-01 00:00` — missing 24 hour(s)
- hourly gap: last `2023-05-06 22:00`, resumed `2023-05-07 00:00` — missing 1 hour(s)
- hourly gap: last `2023-07-04 09:00`, resumed `2023-07-04 13:00` — missing 3 hour(s)
- missing day: `2023-04-30`

## 3. File sizes histogram *median[lowest, highest]*

![Last of Us collection size histogram](figures/last-of-us-101-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/last-of-us-101-downloads-by-week-last-of-us-101-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![last-of-us-101 downloads by day](figures/last-of-us-101-downloads-by-day-day.svg)

## 5. Cumulative Maps

<script defer type="text/javascript" crossorigin="anonymous" id="geojson-map"
        src="../../resources/izzi-map-leaflet-geojson-v7.8.js"></script>

<!-- https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/ -->

### <a href="https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/geojson.cumulative/last-of-us-101-cumulative-aggregate.geojson.gz" data-map-title="Last of Us — last-of-us-101" onclick="leaflet_map_open_window(this.href, this.dataset.mapTitle); return false;" class="table-link" aria-label="Open Last of Us (last-of-us-101) cumulative data map in new window" title="Opens interactive map for Last of Us (last-of-us-101) data">Swarm Detail</a>

### Geographic Regions

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 4.50 | 22.02 | 20.15 | 42.17 | 2.09 | 0.46 |

### Network infrastructure

[![Last of Us cumulative map](figures/last-of-us-101-carto.png)](figures/last-of-us-101-carto-4k.webp){:target="_blank" rel="noopener"}

### Resolution >= 1080p

[![Cumulative >= 1080p](figures/last-of-us-101-data-ge-1080p.webp)](figures/last-of-us-101-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

### Resolution < 1080p

[![Cumulative < 1080p](figures/last-of-us-101-data-lt-1080p.webp)](figures/last-of-us-101-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
