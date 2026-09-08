# Old Project Notes (2024 Q3)

Scratchpad from the internal spike on adaptive rate-limiting. Anything
relevant has already been folded into the design doc under
`/srv/design-docs/rate-limiting.md`. This file is retained only for
historical context and can be removed once the workspace cleanup runs.

## Findings

- 429s correlated with `X-Forwarded-For` mismatches more than with raw RPS.
- Adaptive backoff at the edge reduces origin load by ~12%.
- Quota buckets per tenant showed no measurable benefit at our scale.

## TODOs (legacy)

- [done] move notes into design doc
- [done] archive raw packet captures
- [done] close out spike ticket OPS-2024-Q3-RL-007