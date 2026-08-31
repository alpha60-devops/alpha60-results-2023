# Cache coverage report — beacon-23-108

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/beacon-23-108.xz`
- Hour directories: 2451
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 3 (50 missing hours)
- Missing days: 1

## Sample archive discontinuities

- hourly gap: last `2023-12-30 23:00`, resumed `2024-01-01 00:00` — missing 24 hour(s)
- hourly gap: last `2024-01-03 11:00`, resumed `2024-01-03 13:00` — missing 1 hour(s)
- hourly gap: last `2024-02-16 19:00`, resumed `2024-02-17 21:06` — missing 25 hour(s)
- missing day: `2023-12-31`

## Review

Confirm the sampler state and disk capacity on the sampling
hosts for every zero-length file and discontinuity above
before treating the aggregate outputs as complete.
