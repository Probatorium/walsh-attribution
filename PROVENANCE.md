# Provenance of what this lane did not invent

Contact rule two permits reading the closed lane at its final head and reusing
its sampler of the pair preserving family, with the provenance declared. This
file is that declaration. It is written at the moment of reuse, not
afterwards.

It is not a citation and it is not a credit line in a paper. Rule two forbids
citing that lane, because it carries no deposit and a reader cannot obtain a
fixed version of it. This file exists for a different purpose: so that nobody
reading this repository can believe that its apparatus was built here from
nothing.

## What was read, and from where

- **Repository**: the closed lane whose local checkout is named
  `pairing-conditioned`, on the forge as
  `github.com/Probatorium/pairing-conditioned`.
- **Commit read**: `2fb7127269b5afd26eee91cbf98648c63d8b9fc4`, its final head.
  Addressed by that commit and not by a branch name, so that what was read
  cannot change under this record.
- **How**: `git -C <checkout> show <commit>:<path>`. Nothing in that
  repository was moved. Its working tree was on its own branch before the
  read and was still on it afterwards, which was checked.
- **Date**: 2026-08-11.
- **Rights**: same lane, same author.

## The files read, with digests

Digests are SHA-256 of the blob contents at that commit, as read.

| file read | SHA-256 |
| --- | --- |
| `tools/dashcheck.py` | `9bdf2e5283d97f33ef202e9a22e3e48b0274f2d400d9efade79cce0cccb3274b` |
| `tools/effortlog.py` | `e216d2712830a507bb651cfd80a985c355b05e4476609065541c3f3aae80de51` |
| `tools/figures.py` | `630839c1d41643aa3f03ea4e7951443a073c700f6d7fd46e033a2e57a3cf7010` |
| `tools/gates.py` | `c1ae074a508a6abe50438c3b2f7ecb02ba4b6110086166898022c7d506dfe309` |
| `tools/install-hooks.py` | `2cd9cb2f6f708977218b1479b3c7f826b76aed94455f7a49d416272940575fb1` |
| `tools/untouchable.py` | `73ed6ca529323aa2016796958b0a7d842c27d76779ac17e0f7f3553c48e0d350` |
| `tools/test_gates.py` | `c03e4be7e573811aca2901fd24a2d6bdf2ef3dbc0aba06d0623bfbac522f71e6` |
| `hooks/pre-commit` | `83ebe92c521e9af4212c84ddb9df428fcb9934f49fee3cfdfd2371251cb8edf9` |
| `hooks/commit-msg` | `6578bf07321981586e96cbaa41bb4356a31b4d5bbc23a48545ab8d16a34721a4` |
| `analysis/core.py` | `64a1d6e1b8f6c957079643b46c2dd3c61fdbe7ebe1ac5ad2d112a76e1fd77ca8` |
| `analysis/neighbour.py` | `02c3b02e3c0f026e27a8c7ad1a5969d3d0fff4cfe9a64b8900a362949add8881` |
| `analysis/validate.py` | `28cddaa5aa42affbb1d6fe3ce48df2d708469bc22ee633ebc36cc8e8c63b767d` |

## What this lane took, file by file

### The gates and the hooks: taken substantially as they stand

`tools/dashcheck.py`, `tools/effortlog.py`, `tools/figures.py`,
`tools/gates.py`, `tools/install-hooks.py`, `tools/untouchable.py`,
`hooks/pre-commit` and `hooks/commit-msg` are reused. Each carries a
provenance note in its own header, so a reader who opens the file rather than
this one still learns where it came from.

What changed here, and why:

- `tools/untouchable.py`: the rule it enforces is rule five in this lane and
  was rule four in that one, so the messages and the docstring name the right
  rule. The list of untouchable repositories is unchanged.
- `tools/effortlog.py`: one class added, `VALIDATION`, because this lane runs
  a validation stage that must be loggable as itself rather than folded into
  analysis.
- `tools/gates.py`, `tools/dashcheck.py`, `tools/figures.py`,
  `tools/install-hooks.py` and both hooks: unchanged in substance.

### The test suite: taken and extended

`tools/test_gates.py` is reused and extended. The tests carried over are the
ones that attack the dash gate, the hash chain, the message scanner, the
identifier exemptions and the supersession rule. Two groups are new here and
are marked NEW in the file:

- tests that hold the figure gate against the specific figures this lane is
  most likely to repeat by reflex, which are the two the audited footnote
  prints and the four the unregistered exploration produced;
- tests of the untouchable gate's pattern boundaries, which that lane's suite
  did not have.

### The sampler: read, not copied, and reimplemented from the signed definition

`analysis/core.py` of that lane contains a sampler of the same family this
lane calls `N1`. It was read. It has not been copied into this repository and
no file of it is present here.

The reason is not squeamishness about reuse. It is that the two lanes need
different things from the same family. That lane sampled the family to
compute a rank statistic and represented a draw as an arrangement of
positions. This lane needs, for each draw, the inverse map: the position of
each hexagram, indexed by the hexagram, because that is the domain of the
Walsh characters. Copying a representation built for the other direction and
inverting it at every draw would be slower and, more to the point, would put
the burden of correctness on a translation step that no test in either lane
covers.

So this lane will write its own sampler from the definition in
`PREREGISTRATION.md` section (d), and will validate it against the published
predicate of a deposited neighbour, not against the code read here. What was
taken from `analysis/core.py` is knowledge, not text: that the two free
choices are a permutation of thirty-two blocks and thirty-two independent
fair bits, that both can be drawn exactly with no rejection step, and that a
draw can be handed to a published membership predicate without translation if
the arrangement representation is chosen to match it.

`analysis/neighbour.py` was read for the same reason: it shows how to read a
neighbour at its tag and execute a module of it from a scratch file outside
the repository without anything entering this history. This lane will write
its own version of that helper. `analysis/validate.py` was read for the shape
of a two route validation. What this lane inherits from it, and what it
explicitly does not, is set out in `VALIDATION-PLAN.md` rather than here,
because that accounting belongs with the validation it governs.

## What is not claimed here

That the apparatus of this lane is original. It is not, and this file exists
to say so.
