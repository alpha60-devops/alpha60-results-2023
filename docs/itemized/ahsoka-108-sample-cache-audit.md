---
layout: default
title: "ahsoka-108 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# ahsoka-108 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Ahsoka |
| Collection key | `ahsoka-108` |
| imdb_id | [tt13622776](https://www.imdb.com/title/tt13622776/) |
| wikipedia_url | [Star Wars: Ahsoka](https://en.wikipedia.org/wiki/Star_Wars:_Ahsoka) |
| Sample dates | 2023-10-04-to-2024-04-02 |
| Sample days | 182 |
| BTIH count | 285 |
| Unique BTIH count | 252 |
| Downloaders total | 26,450,502 |
| Uploaders total | 1,935,807 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/ahsoka-108.xz`
- Hour directories: 4352
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 2 (12 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2024-02-16 19:03`, resumed `2024-02-17 07:03` — missing 11 hour(s)
- hourly gap: last `2024-03-31 01:03`, resumed `2024-03-31 03:03` — missing 1 hour(s)

## 3. Media objects file size histogram

![Ahsoka collection size histogram](figures/ahsoka-108-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/ahsoka-108-downloads-by-week-ahsoka-108-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![ahsoka-108 downloads by day](figures/ahsoka-108-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 1.63 | 20.77 | 20.25 | 53.61 | 1.04 | 0.53 |

### Cumulative network infrastructure

[![Ahsoka cumulative map](figures/ahsoka-108-carto.png)](figures/ahsoka-108-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/ahsoka-108-data-ge-1080p.webp)](figures/ahsoka-108-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/ahsoka-108-data-lt-1080p.webp)](figures/ahsoka-108-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
