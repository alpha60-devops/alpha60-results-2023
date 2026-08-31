---
layout: default
title: "barbie Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# barbie sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Barbie |
| Collection key | `barbie` |
| imdb_id | [tt1517268](https://www.imdb.com/title/tt1517268/) |
| wikipedia_url | [Barbie (film)](https://en.wikipedia.org/wiki/Barbie_(film)) |
| Sample dates | 2023-09-03-to-2024-03-02 |
| Sample days | 182 |
| BTIH count | 446 |
| Unique BTIH count | 371 |
| Downloaders total | 51,700,810 |
| Uploaders total | 12,817,797 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/barbie.xz`
- Hour directories: 4364
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 0 (0 missing hours)
- Missing days: 0

### Sample archive discontinuities

None detected.

## 3. Media objects file size histogram

![Barbie collection size histogram](figures/barbie-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/barbie-downloads-by-week-barbie-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![barbie downloads by day](figures/barbie-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 3.57 | 20.04 | 20.30 | 50.67 | 1.41 | 0.57 |

### Cumulative network infrastructure

[![Barbie cumulative map](figures/barbie-carto.png)](figures/barbie-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/barbie-data-ge-1080p.webp)](figures/barbie-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/barbie-data-lt-1080p.webp)](figures/barbie-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
