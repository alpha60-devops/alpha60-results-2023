---
layout: default
title: "warrior-310 Sample Cache Audit"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Cache coverage and visualization audit for one media object."
---

# warrior-310 sample cache audit

## 1. Media object

| Field | Value |
| --- | --- |
| Media object | Warrior |
| Collection key | `warrior-310` |
| imdb_id | [tt5743796](https://www.imdb.com/title/tt5743796/) |
| wikipedia_url | [Warrior (TV series)](https://en.wikipedia.org/wiki/Warrior_(TV_series)) |
| Sample dates | 2023-08-18-to-2023-10-26 |
| Sample days | 70 |
| BTIH count | 131 |
| Unique BTIH count | 119 |
| Downloaders total | 2,098,320 |
| Uploaders total | 288,719 |
| Data version | `2026-08-05` |
| IP geolocation version | `6:1777968300` |

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:24Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/warrior-310.xz`
- Hour directories: 1589
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 2 (86 missing hours)
- Missing days: 1

### Sample archive discontinuities

- hourly gap: last `2023-09-15 01:03`, resumed `2023-09-16 20:03` — missing 42 hour(s)
- hourly gap: last `2023-10-06 22:03`, resumed `2023-10-08 19:03` — missing 44 hour(s)
- missing day: `2023-10-07`

## 3. Media objects file size histogram

![Warrior collection size histogram](figures/warrior-310-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

### Downloads by week cumulative (normalized start)

<script type="text/javascript" crossorigin="anonymous" id="graph-hover"
	src="../../resources/izzi-graph-hover-txt-polyline-red.js">
</script>

<div class="media-object-audit-week-graph" style="max-width: 100%;">
{% include_relative figures/warrior-310-downloads-by-week-warrior-310-week.svg %}
</div>
<style>
.media-object-audit-week-graph svg {
  display: block;
  width: 100%;
  height: auto;
}
</style>

### Downloads by day, Saturday and Sunday in gray

![warrior-310 downloads by day](figures/warrior-310-downloads-by-day-day.svg)

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 7.15 | 19.29 | 17.80 | 50.21 | 1.40 | 0.58 |

### Cumulative network infrastructure

[![Warrior cumulative map](figures/warrior-310-carto.png)](figures/warrior-310-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/warrior-310-data-ge-1080p.webp)](figures/warrior-310-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/warrior-310-data-lt-1080p.webp)](figures/warrior-310-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
