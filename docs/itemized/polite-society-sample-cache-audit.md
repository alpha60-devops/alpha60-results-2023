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

## 2. Sample coverage report

- Generated: 2026-08-31T06:28:24Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/polite-society.xz`
- Hour directories: 1656
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 1 (4 missing hours)
- Missing days: 0

### Sample archive discontinuities

- hourly gap: last `2023-07-04 08:06`, resumed `2023-07-04 13:06` — missing 4 hour(s)

## 3. Media objects file size histogram

![Polite Society collection size histogram](figures/polite-society-cumulative-detail-btiha-itemized-by-bytes.svg)

## 4. Visualization pass — graphs

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

## 5. Visualization pass — maps

### Cumulative geographic slices

| Africa | Americas | Asia | Europe | Oceania | Unknown |
| --- | --- | --- | --- | --- | --- |
| 12.24 | 21.27 | 21.03 | 34.98 | 1.95 | 0.45 |

### Cumulative network infrastructure

[![Polite Society cumulative map](figures/polite-society-carto.png)](figures/polite-society-carto-4k.webp){:target="_blank" rel="noopener"}

### Cumulative data maps

**Cumulative >= 1080p**

[![Cumulative >= 1080p](figures/polite-society-data-ge-1080p.webp)](figures/polite-society-data-ge-1080p-4k.webp){:target="_blank" rel="noopener"}

**Cumulative < 1080p**

[![Cumulative < 1080p](figures/polite-society-data-lt-1080p.webp)](figures/polite-society-data-lt-1080p-4k.webp){:target="_blank" rel="noopener"}
