"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "Celo Commons Payroll",
  "track": "Celo Best Agent on Celo",
  "pitch": "A Celo-focused operator loop that routes stablecoin-native payments and grants after identity and policy checks, ready for live cUSD execution.",
  "overlap_targets": [
    "PayWithLocus",
    "Octant",
    "ERC-8004 Receipts",
    "ENS",
    "Lido stETH Treasury",
    "Slice"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
