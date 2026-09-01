---
layout: default
title: "Alpha60 Swarm Results 2023"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Analysis of peer-to-peer distribution"
---

{::nomarkdown}
<img src="resources/a60-logo-block-gray.simple.svg?sanitize=true" height="50" width="100">

<div style="height: 50px;"></div>
{:/}

## About

These are results from sampling peer swarms associated with *media objects*
being *shared* on the internet. Here, *media objects* are specific films,
television series or episodes, recorded events, and other media distributed as
files or archives. *Sharing* refers to peer-to-peer distribution over
BitTorrent. This is part of the long-term [Alpha60](https://alpha60.co/)
project.

<div style="height: 50px;"></div>

## Results, Commentary

- Media Objects
{% capture media_objects %}{% include year-2023-0-media-objects.txt %}{% endcapture %}{{ media_objects | replace: '.md)', '.html)' }}

<div style="height: 50px;"></div>

## Data

### Forms

- Cumulative (`title-cumulative.json`)
- Cumulative BTIHA metadata (`title-cumulative-btiha-media-objects.json`)
- Cumulative IP swarm (`title-cumulative-ip-swarm.json`)
- Weekly (`title-week.json`)
- Day (`title-swarm-day-NNNNN-YYYY-MM-DD.json`)
- Cumulative GeoJSON (`title-cumulative-*.geojson.gz`)
- Weekly GeoJSON (`title-week-NNNNN.geojson.gz`)
- Day GeoJSON (`title-day-NNNNN.geojson.gz`)

### Source

- [Year-2023 data](https://github.com/alpha60-devops/alpha60-results-2023/tree/main/data)
- [Canonical media-object metadata](https://github.com/alpha60-devops/alpha60-swarm-metadata/tree/main/metadata)

{::nomarkdown}
<svg width="100" height="100">
  <circle cx="20" cy="50" r="10" fill="black"/>
</svg>
{:/}
