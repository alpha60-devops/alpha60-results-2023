---
layout: default
title: "polite-society Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# polite-society sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Polite Society |
| Collection key | `polite-society` |
| imdb_id | [tt18257464](https://www.imdb.com/title/tt18257464/) |
| wikipedia_url | [Polite Society (film)](https://en.wikipedia.org/wiki/Polite_Society_(film)) |
| Sample dates | 2023-05-16-to-2023-07-24 |
| Sample days | 70 |
| BTIH count | 123 |
| Unique BTIH count | 100 |
| Downloaders total | 1,475,455 |
| Uploaders total | 286,867 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Coverage report

- Generated: 2026-08-31T06:28:24Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/polite-society.xz`
- Hour directories: 1656
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (4 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-07-04 08:06`, resumed `2023-07-04 13:06` — missing 4 hour(s)

## 3. File sizes histogram *median[lowest, highest]*

![Polite Society collection size histogram](figures/polite-society-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/polite-society-downloads-by-week-polite-society-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![polite-society downloads by day](figures/polite-society-downloads-by-day-day.svg)

## 5. Cumulative Maps

<script defer type="text/javascript" crossorigin="anonymous" id="geojson-map"
        src="../../resources/izzi-map-leaflet-geojson-v7.8.js"></script>

<!-- https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/ -->

### <a href="https://raw.githubusercontent.com/alpha60-devops/alpha60-results-2023/refs/heads/main/data/geojson.cumulative/polite-society-cumulative-aggregate.geojson.gz" data-map-title="Polite Society — polite-society" onclick="leaflet_map_open_window(this.href, this.dataset.mapTitle); return false;" class="table-link" aria-label="Open Polite Society (polite-society) cumulative data map in new window" title="Opens interactive map for Polite Society (polite-society) data">Swarm Detail</a>

### Geographic Regions

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 12.24 | 21.27 | 21.03 | 34.98 | 1.95 | 0.45 |

### Network infrastructure

[![Polite Society cumulative map](figures/polite-society-carto.png)](figures/polite-society-carto-4k.webp){:target="_blank" rel="noopener"}

### Resolution >= 1080p

[![Cumulative >= 1080p](figures/polite-society-data-ge-1080p.webp)](figures/polite-society-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

### Resolution < 1080p

[![Cumulative < 1080p](figures/polite-society-data-lt-1080p.webp)](figures/polite-society-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
