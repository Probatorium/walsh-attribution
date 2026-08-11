"""The sampler and the transform, validated by two independent routes.

`VALIDATION-PLAN.md` fixes what the two routes are, what counts as a pass and
what counts as a stop. This file executes that plan and adds nothing to it.

ROUTE ONE, against the published membership predicate of the family, read
only at its deposit tag under `CONTACT-RULES.md` rule four, executed from a
scratch file outside this repository. A second predicate, from the closed
lane read at its final head under rule two, is run alongside it. That second
predicate is the inheritance the contact rule asks for: it is re-run here
rather than taken as already passed, because a verification of another
program's output says nothing about this one's.

ROUTE TWO, against the facts derived by hand in `PREREGISTRATION.md` sections
(b.1) to (b.4) and signed before any of this existed. V0 and V5 are added by
`VALIDATION-PLAN.md` on top of those four.

THE DRAW COUNTS, DECLARED HERE BECAUSE THE PLAN DID NOT FIX THEM. The signed
preregistration fixes the sample size of the analysis run. `VALIDATION-PLAN.md`
fixes the tolerance of V3 and V4, four standard errors of the sample mean with
the standard error taken from the sample's own dispersion, and it does not fix
how many draws those two checks are computed over. That gap is declared as a
defect rather than filled quietly, and the counts below are written down before
the run rather than after it:

    N_MOMENT     200000   V1, V3, V4. The same count as the analysis run, so
                          the acceptance test has the precision of the run it
                          gates.
    N_EXACT        2000   V2. Exact integer equality, so a large count buys
                          nothing.
    N_PREDICATE    2000   route one. Each draw is handed to two predicates one
                          at a time, in Python, so the count is bounded by
                          patience rather than by precision.

WHAT THIS FILE DELIBERATELY DOES NOT COMPUTE. No aggregate over the focal
interaction orders is formed at any point for draws from the pair preserving
family. V1 and V4 take the total energy and the energy at order 6 from the
coefficients directly, without grouping any other order, and that is why
`_pair_restricted` exists instead of a call to `core.energies`. The focal
statistic of this lane under that family is a primary result and belongs to
the analysis session, not to the session that validates the instrument.

The received King Wen sequence is not read here, and no path in this
repository points at one.

Usage:
    python analysis/validate.py --ladder-checkout PATH --closed-lane-checkout PATH
"""

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

import core
import neighbour

SEED = 21776041           # PREREGISTRATION.md section (f)
N_MOMENT = 200_000
N_EXACT = 2_000
N_PREDICATE = 2_000
CHUNK = 25_000
TOLERANCE_SE = 4.0        # VALIDATION-PLAN.md, V3 and V4

RESULT = {"seed": SEED, "counts": {"moment": N_MOMENT, "exact": N_EXACT,
                                   "predicate": N_PREDICATE},
          "tolerance_standard_errors": TOLERANCE_SE, "checks": []}


def record(label, passed, detail=""):
    RESULT["checks"].append({"check": label, "passed": bool(passed),
                             "detail": detail})
    print(f"  {'PASS' if passed else 'FAIL'}  {label}"
          + (f"  [{detail}]" if detail else ""))
    return bool(passed)


def _pair_restricted(signals):
    """(non-DC total, energy at order 6) without grouping any other order.

    Deliberately not `core.energies`. See the module docstring.
    """
    coeffs = np.asarray(signals, dtype=np.int64) @ core.HADAMARD
    squares = coeffs * coeffs
    total = squares.sum(axis=1) - squares[:, 0]
    return total, squares[:, 63]


class Moments:
    """Streaming mean and unbiased variance, so a chunked run needs no
    second pass and no full array in memory."""

    def __init__(self, width):
        self.n = 0
        self.total = np.zeros(width, dtype=np.float64)
        self.total_sq = np.zeros(width, dtype=np.float64)

    def add(self, values):
        values = np.asarray(values, dtype=np.float64)
        if values.ndim == 1:
            values = values[:, None]
        self.n += values.shape[0]
        self.total += values.sum(axis=0)
        self.total_sq += (values * values).sum(axis=0)

    def mean(self):
        return self.total / self.n

    def se(self):
        var = (self.total_sq - self.n * self.mean() ** 2) / (self.n - 1)
        return np.sqrt(np.maximum(var, 0.0) / self.n)


# ---------------------------------------------------------------------------
# ROUTE TWO
# ---------------------------------------------------------------------------

def v0_transform_on_a_known_input():
    print("\nV0  the transform, on an input whose spectrum is known exactly")
    sig = core.signal_of_ordering(core.BINARY_ORDERING)
    rows = core.energies(sig)
    ok = record("the binary ordering has zero energy at orders 2 to 6",
                bool((rows[0, 2:] == 0).all()),
                f"orders 2 to 6 sum to {int(rows[0, 2:].sum())}")
    ok = record("all non-DC energy of the binary ordering sits at order 1",
                int(rows[0, 1]) == int(core.non_dc(rows)[0])) and ok
    ok = record("that non-DC total is the constant of (b.1)",
                int(core.non_dc(rows)[0]) == core.NON_DC_ENERGY,
                f"{int(core.non_dc(rows)[0])}") and ok
    return ok


def v1_v3_v4_moments(rng):
    """V1 on both nulls, V3 on the free null, V4 on the pair preserving one."""
    print("\nV1  the constant denominator, on every draw of both nulls")
    print("V3  the free null mean, against 30/63 and C(6,k)/63")
    print("V4  the pair preserving mean at order 6, against 45056")

    free_shares = Moments(core.N_ORDERS)
    free_focal = Moments(1)
    pair_e6 = Moments(1)
    bad_free = bad_pair = 0
    drawn = 0
    while drawn < N_MOMENT:
        m = min(CHUNK, N_MOMENT - drawn)

        free_sig = core.draw_free(rng, m)
        free_rows = core.energies(free_sig)
        bad_free += int((core.non_dc(free_rows) != core.NON_DC_ENERGY).sum())
        free_chunk = core.shares(free_rows)
        free_shares.add(free_chunk)
        # The focal statistic is a sum of two shares, so its standard error is
        # not the sum of theirs. It is accumulated as its own quantity, which
        # is the only way to get the standard error the tolerance is stated in.
        free_focal.add(free_chunk[:, [k - 1 for k in core.FOCAL_ORDERS]].sum(axis=1))

        perms, flips = core.draw_pair(rng, m)
        total, e6 = _pair_restricted(core.signals_pair(perms, flips))
        bad_pair += int((total != core.NON_DC_ENERGY).sum())
        pair_e6.add(e6)

        drawn += m

    ok = record("every free null draw has the exact non-DC energy of (b.1)",
                bad_free == 0, f"{N_MOMENT - bad_free} of {N_MOMENT}")
    ok = record("every pair preserving draw has the exact non-DC energy of (b.1)",
                bad_pair == 0, f"{N_MOMENT - bad_pair} of {N_MOMENT}") and ok

    means, ses = free_shares.mean(), free_shares.se()
    RESULT["free_null_share_means"] = [float(x) for x in means]
    for k in range(1, core.N_ORDERS + 1):
        expected = float(Fraction(core.CHARACTERS_BY_ORDER[k - 1], core.N_NON_DC))
        dev = abs(means[k - 1] - expected) / ses[k - 1]
        ok = record(f"free null mean share at order {k} agrees with C(6,k)/63",
                    dev <= TOLERANCE_SE,
                    f"mean {means[k - 1]:.6f} against {expected:.6f}, "
                    f"{dev:.2f} standard errors") and ok

    focal_mean, focal_se = float(free_focal.mean()[0]), float(free_focal.se()[0])
    focal_expected = float(Fraction(sum(core.CHARACTERS_BY_ORDER[k - 1]
                                        for k in core.FOCAL_ORDERS),
                                    core.N_NON_DC))
    dev = abs(focal_mean - focal_expected) / focal_se
    RESULT["free_null_focal_mean"] = focal_mean
    RESULT["free_null_focal_se"] = focal_se
    RESULT["free_null_focal_expected"] = focal_expected
    ok = record("free null mean of the focal share agrees with 30/63 exactly",
                dev <= TOLERANCE_SE,
                f"mean {focal_mean:.6f} against {focal_expected:.6f}, "
                f"{dev:.2f} standard errors") and ok

    e6_mean, e6_se = float(pair_e6.mean()[0]), float(pair_e6.se()[0])
    dev6 = abs(e6_mean - core.MEAN_ENERGY_ORDER6_PAIR) / e6_se
    share6 = e6_mean / core.NON_DC_ENERGY
    share6_expected = float(Fraction(core.MEAN_ENERGY_ORDER6_PAIR,
                                     core.NON_DC_ENERGY))
    RESULT["pair_null_order6_energy_mean"] = e6_mean
    RESULT["pair_null_order6_share_mean"] = share6
    ok = record("pair preserving mean energy at order 6 agrees with (b.4)",
                dev6 <= TOLERANCE_SE,
                f"mean {e6_mean:.1f} against {core.MEAN_ENERGY_ORDER6_PAIR}, "
                f"{dev6:.2f} standard errors") and ok
    record("for the reader, the same fact as a share",
           True, f"{share6:.6f} against 44/1365 = {share6_expected:.6f}")
    return ok


def v2_convention_invariance(rng):
    print("\nV2  the profile by interaction order, under all four conventions")
    inverses = [core.relabelling(c) for c in range(len(core.CONVENTIONS))]

    sig = core.signal_of_ordering(core.BINARY_ORDERING)
    reference = core.energies(sig)
    ok = True
    for c in range(1, len(core.CONVENTIONS)):
        other = core.energies(sig[inverses[c]])
        ok = record(f"binary ordering, {core.CONVENTIONS[c][0]}",
                    bool((other[:, 1:] == reference[:, 1:]).all())) and ok

    free_sig = core.draw_free(rng, N_EXACT)
    reference = core.energies(free_sig)
    for c in range(1, len(core.CONVENTIONS)):
        other = core.energies(free_sig[:, inverses[c]])
        ok = record(f"{N_EXACT} free draws, {core.CONVENTIONS[c][0]}",
                    bool((other[:, 1:] == reference[:, 1:]).all())) and ok

    RESULT["convention_invariance_holds"] = ok
    if not ok:
        print("  V2 is the one failure that is not a stop. "
              "PREREGISTRATION.md section (f) fixes the branch: four "
              "conventions are carried and the declared test set has "
              "twenty-eight members.")
    return ok


def v5_stream_independence():
    print("\nV5  spawning the validation stream leaves the two null streams alone")
    two = core.streams(SEED, 2)
    three = core.streams(SEED, 3)
    same = all(np.array_equal(a.integers(0, 2 ** 31, 16),
                              b.integers(0, 2 ** 31, 16))
               for a, b in zip(two, three[:2]))
    return record("the first two streams are identical whether two or three "
                  "are spawned", same)


# ---------------------------------------------------------------------------
# ROUTE ONE
# ---------------------------------------------------------------------------

def route_one(rng, ladder_checkout, closed_checkout):
    print("\nROUTE ONE  against the published predicate, and the inherited one")

    published, pub_digest, pub_scratch = neighbour.import_at_ref(
        ladder_checkout, neighbour.LADDER_TAG, "ladder_containment.py",
        "published_ladder")
    print(f"  published predicate read at {neighbour.LADDER_TAG}")
    print(f"    sha256 {pub_digest}")
    print(f"    executed from {pub_scratch}, outside this repository")

    inherited, inh_digest, inh_scratch = neighbour.import_at_ref(
        closed_checkout, neighbour.CLOSED_LANE_HEAD, "analysis/core.py",
        "closed_lane_core")
    print(f"  inherited predicate read at the closed lane's final head")
    print(f"    sha256 {inh_digest}")
    print(f"    executed from {inh_scratch}, outside this repository")

    RESULT["published_predicate_sha256"] = pub_digest
    RESULT["inherited_predicate_sha256"] = inh_digest
    RESULT["ladder_ref"] = neighbour.LADDER_TAG
    RESULT["closed_lane_ref"] = neighbour.CLOSED_LANE_HEAD

    perms, flips = core.draw_pair(rng, N_PREDICATE)
    pub = mine = inh = roundtrip = same_assembly = 0
    for i in range(N_PREDICATE):
        arr = core.assemble(perms[i], flips[i])
        pub += bool(published.in_P1(arr))
        mine += bool(core.in_family(arr))
        inh += bool(inherited.in_family(arr))
        same_assembly += (arr == published.assemble(
            tuple(int(x) for x in perms[i]), tuple(int(x) for x in flips[i])))
        got = published.decompose(arr)
        roundtrip += (got is not None
                      and list(got[0]) == [int(x) for x in perms[i]]
                      and list(got[1]) == [int(x) for x in flips[i]])

    ok = record("every draw satisfies the published predicate",
                pub == N_PREDICATE, f"{pub} of {N_PREDICATE}")
    ok = record("every draw satisfies this lane's own predicate",
                mine == N_PREDICATE, f"{mine} of {N_PREDICATE}") and ok
    ok = record("every draw satisfies the closed lane's predicate",
                inh == N_PREDICATE, f"{inh} of {N_PREDICATE}") and ok
    ok = record("this lane's assembly agrees with the published assembly",
                same_assembly == N_PREDICATE,
                f"{same_assembly} of {N_PREDICATE}") and ok
    ok = record("the published decomposition recovers the permutation and the "
                "orientations this sampler chose",
                roundtrip == N_PREDICATE, f"{roundtrip} of {N_PREDICATE}") and ok

    identity = tuple(range(core.N_POS))
    witnesses = []

    swapped = list(identity)
    swapped[0], swapped[2] = swapped[2], swapped[0]
    witnesses.append(("one hexagram exchanged across two pairs",
                      tuple(swapped), False))

    rotated = tuple(list(identity)[1:] + [identity[0]])
    witnesses.append(("the whole arrangement rotated by one position",
                      rotated, False))

    free = tuple(rng.permutation(core.N_POS).tolist())
    witnesses.append(("a free shuffle of all sixty-four positions",
                      free, False))

    within = list(identity)
    within[0], within[1] = within[1], within[0]
    witnesses.append(("a within pair flip, which IS in the family",
                      tuple(within), True))

    for label, arr, expected in witnesses:
        p, m, h = (bool(published.in_P1(arr)), bool(core.in_family(arr)),
                   bool(inherited.in_family(arr)))
        ok = record(f"witness, {label}", p == m == h == expected,
                    f"published {p}, this lane {m}, closed lane {h}, "
                    f"expected {expected}") and ok

    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ladder-checkout", required=True)
    ap.add_argument("--closed-lane-checkout", required=True)
    a = ap.parse_args()

    print(f"seed {SEED}, validation on stream 2 of 3, in the declared order")
    rng = core.streams(SEED, 3)[2]

    v5 = v5_stream_independence()
    v0 = v0_transform_on_a_known_input()
    v2 = v2_convention_invariance(rng)
    r1 = route_one(rng, a.ladder_checkout, a.closed_lane_checkout)
    moments = v1_v3_v4_moments(rng)

    stops = {"V5": v5, "V0": v0, "V1, V3 and V4": moments, "ROUTE ONE": r1}
    failed = [name for name, passed in stops.items() if not passed]
    RESULT["route_two_v2_is_a_branch_not_a_stop"] = True
    RESULT["passed"] = not failed
    RESULT["v2_passed"] = v2

    print("\n" + "=" * 70)
    if failed:
        print(f"STOP. Failed: {', '.join(failed)}.")
        print("VALIDATION-PLAN.md forbids reading any observed value or any "
              "p-value from here.")
    else:
        print("BOTH ROUTES PASS.")
        print("V2 held, so the declared test set has seven members and one "
              "bit convention is carried, per PREREGISTRATION.md section (f)."
              if v2 else
              "V2 FAILED. Not a stop: four conventions are carried and the "
              "declared test set has twenty-eight members.")
    print("=" * 70)

    out = Path(__file__).resolve().parent.parent / "results"
    out.mkdir(exist_ok=True)
    (out / "validation.json").write_text(
        json.dumps(RESULT, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
