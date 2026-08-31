# Cache coverage report — hijack-107

- Generated: 2026-08-31T06:28:23Z
- Sample archive directory: `/run/media/bkoz/gold/src/alpha60-samples-raw.gold/hijack-107.xz`
- Hour directories: 2431
- Zero-length sample files: 0
- Other unparsable sample files: 0
- Hourly discontinuities: 2 (86 missing hours)
- Missing days: 1

## Sample archive discontinuities

- hourly gap: last `2023-09-15 01:00`, resumed `2023-09-16 20:00` — missing 42 hour(s)
- hourly gap: last `2023-10-06 22:00`, resumed `2023-10-08 19:00` — missing 44 hour(s)
- missing day: `2023-10-07`

## Review

Confirm the sampler state and disk capacity on the sampling
hosts for every zero-length file and discontinuity above
before treating the aggregate outputs as complete.
