# Alpha60 results: year 2023 campaign

This directory holds the in-progress year-2023 Alpha60 results dataset. The
fixed campaign inventory contains 69 media objects at SHA-256
`3f3c8e97f74b789432e21206cceea8011c8e78f37302c9a84eb9d02075ca15be`.

## Campaign inputs

- `txt/year-2023-0-media-objects.txt`: canonical ordered 69-object inventory.
- `txt/year-2023-cache-aliases.tsv`: empty alias map; every canonical key maps
  directly to its same-named gold cache directory.
- `txt/year-2023-cache-archive-overrides.json`: the two explicitly approved
  later-archive selections whose canonical release windows end earlier than
  their immutable archives.
- `txt/year-2023-cache-archive-map.json`: exact archive paths, sizes, SHA-256
  identities, canonical sample contracts, sparse intervals, and byte-balanced
  ord/eureka ownership.

Cache archives and raw samples are immutable external campaign inputs and are
never committed to this repository. Generated data, figures, audit pages, and
the final checksum/release manifests will be added by the verified campaign
pipeline.
