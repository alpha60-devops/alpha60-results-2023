# Cache coverage report — loki-201

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/loki-201.xz`
- Hour directories: 4327
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 3 (35 missing hours)
- Missing days: 1

## Sample archive discontinuities

- hourly gap: last `2023-12-21 23:06`, resumed `2023-12-23 00:06` — missing 24 hour(s)
- hourly gap: last `2024-02-16 19:06`, resumed `2024-02-17 07:03` — missing 10 hour(s)
- hourly gap: last `2024-03-31 01:03`, resumed `2024-03-31 03:03` — missing 1 hour(s)
- missing day: `2023-12-22`

## Review

Confirm the sampler state and disk capacity on the sampling
hosts for every zero-length file and discontinuity above
before treating the aggregate outputs as complete.
