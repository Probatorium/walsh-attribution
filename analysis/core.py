"""The objects `PREREGISTRATION.md` defines, and nothing else.

Every definition here is fixed by that signed document. Where this file makes
a choice the document did not force, it says so in a comment. Nothing here
reads a result.

WHAT THIS MODULE DELIBERATELY DOES NOT CONTAIN. It does not read the received
King Wen sequence. It cannot: no path in this repository points at one, and
the file does not exist. Everything below is built from the six dimensional
Boolean cube and from the matching that the deposit under audit describes, so
the whole validation of `VALIDATION-PLAN.md` runs before any received datum
enters, which is what the declared order of operations in that plan requires.

REPRESENTATION, two of them, and the map between them.

  Cube space. A hexagram is an element of the cube, an integer 0 to 63 under
  the bit convention quoted in `PREREGISTRATION.md` section (b): line 1 is the
  bottom line and the most significant bit, and a solid line is one. The
  signal is a function on this space: `f(v)` is the King Wen number of the
  hexagram `v`, that is one plus its position in the ordering.

  Slot space. The published membership predicate of the family, which route
  one of the validation runs against, works on arrangements of the sixty-four
  received positions, grouped into thirty-two consecutive pair slots. A draw
  of this sampler is expressed in that space by labelling the thirty-two
  blocks of the matching 0 to 31 in the canonical order fixed below.

  That labelling is a labelling. It makes the combinatorial law of this
  sampler comparable with the published predicate, which is what route one is
  for. It does not assert that block j of the matching is pair slot j of the
  received sequence. That assertion is precondition P1 of
  `PREREGISTRATION.md` section (d), it is checked at step four of
  `VALIDATION-PLAN.md`, and nothing here anticipates it.
"""

import numpy as np

N_POS = 64
N_BLOCKS = 32
N_ORDERS = 6

# Declared in PREREGISTRATION.md (b.1) and (b.4), by hand, before signing.
# They are predictions under test in VALIDATION-PLAN.md, not results.
NON_DC_ENERGY = 1397760
MEAN_ENERGY_ORDER6_PAIR = 45056

# Declared in PREREGISTRATION.md (b.3): C(6,k) characters at order k, out of
# the sixty-three characters other than the constant one.
CHARACTERS_BY_ORDER = (6, 15, 20, 15, 6, 1)
N_NON_DC = 63
FOCAL_ORDERS = (2, 4)          # PREREGISTRATION.md section (b), fixed there


# --- the figure, and the operations that are properties of the figure ------
# Reversal is turning the figure upside down. Complement is changing every
# line. Neither depends on how the figure is read as a number.

def reverse6(v):
    return int(format(v, "06b")[::-1], 2)


def complement6(v):
    return v ^ 63


def partner(v):
    """The matching the deposit under audit describes in its introduction:
    'each pair is related by 180-degree rotation, or by complementation when
    the figure is rotation-symmetric'."""
    r = reverse6(v)
    return complement6(v) if r == v else r


def blocks():
    """The thirty-two blocks, in a canonical order fixed here.

    The signed document does not fix an order of the blocks and does not need
    one: the family permutes them uniformly, so any labelling gives the same
    law. The order is fixed here only so that a run is reproducible from the
    seed. Blocks are sorted by their smaller member, and each block is
    (smaller, larger).
    """
    seen, out = set(), []
    for v in range(N_POS):
        if v in seen:
            continue
        w = partner(v)
        seen.add(v)
        seen.add(w)
        out.append((min(v, w), max(v, w)))
    out.sort()
    assert len(out) == N_BLOCKS
    assert sorted(x for pair in out for x in pair) == list(range(N_POS))
    return out


BLOCKS = blocks()
BLOCK_LOW = np.array([a for a, _ in BLOCKS], dtype=np.int64)
BLOCK_HIGH = np.array([b for _, b in BLOCKS], dtype=np.int64)


# --- the four bit conventions, as relabellings of the cube ------------------
# A convention is fixed by two choices: which end of the figure carries the
# most significant bit, and which line type is one. Changing either is a
# relabelling of the cube, and PREREGISTRATION.md (b.2) predicts that the
# energy profile by interaction order is invariant under all four. The
# reference convention, index 0, is the one quoted from the deposit.

CONVENTIONS = [
    ("bottom-significant, solid as one", lambda v: v),
    ("bottom-significant, solid as zero", lambda v: complement6(v)),
    ("top-significant, solid as one", lambda v: reverse6(v)),
    ("top-significant, solid as zero", lambda v: complement6(reverse6(v))),
]


def relabelling(convention_index):
    """`idx` such that `signal_under_convention = signal_reference[idx]`.

    The convention map `t` sends the figure `v` to its cube index under that
    convention, so the signal under the convention satisfies
    `g(t(v)) = f(v)`, that is `g[u] = f[t_inverse(u)]`.
    """
    _, t = CONVENTIONS[convention_index]
    forward = np.array([t(v) for v in range(N_POS)], dtype=np.int64)
    assert sorted(forward.tolist()) == list(range(N_POS))
    inverse = np.empty(N_POS, dtype=np.int64)
    inverse[forward] = np.arange(N_POS, dtype=np.int64)
    return inverse


# --- the transform, in exact integer arithmetic ----------------------------
# The Walsh character at w takes the value (-1)^popcount(w AND v) at v. The
# matrix is sixty-four by sixty-four, its entries are plus and minus one, and
# every signal this lane transforms is integer valued, so the coefficients and
# their squares are exact integers. Nothing here is floating point, which is
# what allows VALIDATION-PLAN.md to demand exact equality rather than a
# tolerance in V0, V1 and V2.

def _hadamard():
    idx = np.arange(N_POS, dtype=np.int64)
    parity = np.array([bin(x).count("1") & 1
                       for x in (idx[:, None] & idx[None, :]).ravel()],
                      dtype=np.int64).reshape(N_POS, N_POS)
    return 1 - 2 * parity


HADAMARD = _hadamard()
ORDER_OF = np.array([bin(w).count("1") for w in range(N_POS)], dtype=np.int64)


def energies(signals):
    """Unnormalised Walsh energy by interaction order 0 to 6, per signal.

    `signals` is an array of shape (n, 64) of integers. The result has shape
    (n, 7): column k is the sum of the squared coefficients over the
    characters of interaction order k, and column 0 is the DC term.
    """
    signals = np.asarray(signals, dtype=np.int64)
    if signals.ndim == 1:
        signals = signals[None, :]
    coeffs = signals @ HADAMARD
    squares = coeffs * coeffs
    out = np.zeros((signals.shape[0], N_ORDERS + 1), dtype=np.int64)
    for k in range(N_ORDERS + 1):
        out[:, k] = squares[:, ORDER_OF == k].sum(axis=1)
    return out


def non_dc(energy_rows):
    """Total energy excluding the constant character."""
    return energy_rows[:, 1:].sum(axis=1)


def shares(energy_rows):
    """Energy at orders 1 to 6 as a fraction of the non-DC total."""
    return energy_rows[:, 1:] / non_dc(energy_rows)[:, None]


# --- the signals ------------------------------------------------------------

def signal_of_ordering(ordering):
    """The single order signal of an ordering, indexed by the hexagram.

    `ordering[p]` is the hexagram at position p. The signal is
    `f(v) = 1 + position of v`, which is the King Wen number of v when the
    ordering is the King Wen sequence. PREREGISTRATION.md section (b).
    """
    sig = np.empty(N_POS, dtype=np.int64)
    sig[np.asarray(ordering, dtype=np.int64)] = np.arange(1, N_POS + 1,
                                                          dtype=np.int64)
    return sig


BINARY_ORDERING = list(range(N_POS))


# --- the sampler of N1, the pair preserving family --------------------------
# PREREGISTRATION.md section (d): a member is generated by exactly two free
# choices, a permutation of the thirty-two blocks into the thirty-two slots
# and an orientation for each. Both are sampled exactly: a uniform permutation
# of thirty-two objects, and thirty-two independent fair bits. No rejection,
# no approximation, no burn-in.

def draw_pair(rng, n):
    perms = np.tile(np.arange(N_BLOCKS, dtype=np.int8), (n, 1))
    perms = rng.permuted(perms, axis=1)
    flips = rng.integers(0, 2, size=(n, N_BLOCKS), dtype=np.int8)
    return perms, flips


def signals_pair(perms, flips):
    """Signals in cube space for a batch of draws from N1.

    Block `perms[i, s]` occupies slot s, that is positions 2s and 2s+1, and
    `flips[i, s]` says which of its two hexagrams takes the earlier position.
    The signal is one plus the position, as `signal_of_ordering` defines it.
    """
    n = perms.shape[0]
    slots = np.arange(N_BLOCKS, dtype=np.int64)[None, :]
    perm64 = perms.astype(np.int64)
    flip64 = flips.astype(np.int64)
    low_pos = 2 * slots + flip64
    high_pos = 2 * slots + 1 - flip64
    sig = np.empty((n, N_POS), dtype=np.int64)
    rows = np.arange(n, dtype=np.int64)[:, None]
    sig[rows, BLOCK_LOW[perm64]] = low_pos + 1
    sig[rows, BLOCK_HIGH[perm64]] = high_pos + 1
    return sig


# --- the sampler of N0, the free null ---------------------------------------

def draw_free(rng, n):
    """n uniform orderings of the sixty-four hexagrams, as signals.

    A uniform permutation assigns the sixty-four positions to the sixty-four
    hexagrams, and the signal is one plus the position. Drawing the inverse
    permutation directly is the same law and saves an inversion.
    """
    base = np.tile(np.arange(1, N_POS + 1, dtype=np.int64), (n, 1))
    return rng.permuted(base, axis=1)


# --- membership, this lane's own predicate ----------------------------------

def assemble(perm, flips):
    """A slot space arrangement from a block permutation and orientations.

    Written from the definition in PREREGISTRATION.md section (d), in the
    representation the published predicate uses, so that a draw can be handed
    to that predicate without translation.
    """
    out = []
    for s in range(N_BLOCKS):
        a, b = 2 * int(perm[s]), 2 * int(perm[s]) + 1
        out += [b, a] if flips[s] else [a, b]
    return tuple(out)


def in_family(arr):
    """True if arr preserves the pairing, by this lane's own definition.

    Written from PREREGISTRATION.md section (d) alone, independently of any
    other implementation, so that agreement with the published predicate is
    evidence rather than tautology. It is deliberately stricter than the
    published one in one respect, recorded here rather than discovered later:
    it also requires arr to be a permutation of the sixty-four positions.
    """
    if sorted(arr) != list(range(N_POS)):
        return False
    for s in range(N_BLOCKS):
        a, b = arr[2 * s], arr[2 * s + 1]
        if a == b or a // 2 != b // 2:
            return False
    return True


# --- streams ----------------------------------------------------------------

def streams(seed, count):
    """One independent stream per declared consumer, in the declared order.

    PREREGISTRATION.md section (f): "with independent streams spawned in this
    declared order: stream 0 for N1, stream 1 for N0, stream 2 for the
    validation of the sampler."
    """
    children = np.random.SeedSequence(seed).spawn(count)
    return [np.random.Generator(np.random.PCG64(c)) for c in children]
