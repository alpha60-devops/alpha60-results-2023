---
layout: default
title: "spider-man-across-the-spider-verse Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# spider-man-across-the-spider-verse sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Spider Man Across The Spider Verse |
| Collection key | `spider-man-across-the-spider-verse` |
| imdb_id | [tt9362722](https://www.imdb.com/title/tt9362722/) |
| wikipedia_url | [Spider-Man: Across the Spider-Verse](https://en.wikipedia.org/wiki/Spider-Man:_Across_the_Spider-Verse) |
| Sample dates | 2023-08-07-to-2024-02-05 |
| Sample days | 183 |
| BTIH count | 421 |
| Unique BTIH count | 366 |
| Downloaders total | 37,574,408 |
| Uploaders total | 7,126,774 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Coverage report

- Generated: 2026-08-31T06:28:24Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/spider-man-across-the-spider-verse.xz`
- Hour directories: 4331
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 3 (42 missing hours)
- Missing days: 1

### Sample archive discontinuities

- hourly gap: last `2023-09-07 09:00`, resumed `2023-09-07 13:00` — missing 3 hour(s)
- hourly gap: last `2023-10-22 11:00`, resumed `2023-10-24 01:23` — missing 37 hour(s)
- hourly gap: last `2023-11-27 23:00`, resumed `2023-11-28 02:00` — missing 2 hour(s)
- missing day: `2023-10-23`

## 3. File sizes histogram *median[lowest, highest]*

![Spider Man Across The Spider Verse collection size histogram](figures/spider-man-across-the-spider-verse-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/spider-man-across-the-spider-verse-downloads-by-week-spider-man-across-the-spider-verse-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![spider-man-across-the-spider-verse downloads by day](figures/spider-man-across-the-spider-verse-downloads-by-day-day.svg)

## 5. Cumulative Maps

<script defer type="text/javascript" crossorigin="anonymous" id="geojson-map"
        src="../../resources/izzi-map-leaflet-geojson-v7.8.js"></script>

<!-- https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/ -->

### <a href="https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/geojson.cumulative/spider-man-across-the-spider-verse-cumulative-aggregate.geojson.gz" data-map-title="Spider Man Across The Spider Verse — spider-man-across-the-spider-verse" onclick="leaflet_map_open_window(this.href, this.dataset.mapTitle); return false;" class="table-link" aria-label="Open Spider Man Across The Spider Verse (spider-man-across-the-spider-verse) cumulative data map in new window" title="Opens interactive map for Spider Man Across The Spider Verse (spider-man-across-the-spider-verse) data">Swarm Detail</a>

### Geographic Regions

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 5.57 | 19.52 | 25.40 | 44.19 | 1.16 | 0.49 |

### Network infrastructure

[![Spider Man Across The Spider Verse cumulative map](figures/spider-man-across-the-spider-verse-carto.png)](figures/spider-man-across-the-spider-verse-carto-4k.webp){:target="_blank" rel="noopener"}

### Resolution >= 1080p

[![Cumulative >= 1080p](figures/spider-man-across-the-spider-verse-data-ge-1080p.webp)](figures/spider-man-across-the-spider-verse-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

### Resolution < 1080p

[![Cumulative < 1080p](figures/spider-man-across-the-spider-verse-data-lt-1080p.webp)](figures/spider-man-across-the-spider-verse-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
