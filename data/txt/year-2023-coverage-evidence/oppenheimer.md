# Cache coverage report — oppenheimer

- Generated: 2026-08-31T06:28:24Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/oppenheimer.xz`
- Hour directories: 4308
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 5 (61 missing hours)
- Missing days: 0

## Sample archive discontinuities

- hourly gap: last `2023-12-22 05:00`, resumed `2023-12-23 00:00` — missing 18 hour(s)
- hourly gap: last `2024-01-04 23:00`, resumed `2024-01-05 20:00` — missing 20 hour(s)
- hourly gap: last `2024-02-16 03:00`, resumed `2024-02-16 05:00` — missing 1 hour(s)
- hourly gap: last `2024-02-16 19:00`, resumed `2024-02-17 17:56` — missing 21 hour(s)
- hourly gap: last `2024-03-31 01:03`, resumed `2024-03-31 03:03` — missing 1 hour(s)

## Review

Confirm the sampler state and disk capacity on the sampling
hosts for every zero-length file and discontinuity above
before treating the aggregate outputs as complete.
