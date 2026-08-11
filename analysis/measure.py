"""The declared analysis, run once, exactly as `PREREGISTRATION.md` fixes it.

Order of operations, from `VALIDATION-PLAN.md`: the validation has already
passed and is still current, and only then is the received sequence read, the
preconditions run, the observed value read and the declared tests run. This
file refuses to start if the first of those is not true.

Everything below is fixed by the signed document and nothing here chooses
anything. The statistic, the focal orders, the two nulls, the seven tests,
their tails, the correction, the sample size and the seed are all quoted from
it in the code that uses them.

Usage:
    python analysis/measure.py
"""

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

import core

ROOT = Path(__file__).resolve().parent.parent
VALIDATION = ROOT / "results" / "validation.json"
RECEIVED = ROOT / "data" / "king-wen-received.json"

SEED = 21776041          # PREREGISTRATION.md section (f)
N_DRAWS = 200_000        # section (f), fixed there, not raised, not lowered
CHUNK = 25_000
FAMILY_WISE = 0.05       # section (e), Holm at this level
FOOTNOTE_PERCENT = 77.4  # the figure the audited footnote prints, for P2

OUT = {"seed": SEED, "draws_per_null": N_DRAWS}


def refuse_unless_validated():
    """No p-value is read from an unvalidated or a stale sampler."""
    if not VALIDATION.exists():
        raise SystemExit("no validation on record; measurement refused")
    record = json.loads(VALIDATION.read_text(encoding="utf-8"))
    if not record.get("passed"):
        raise SystemExit("the validation on record did not pass; "
                         "measurement refused")
    for relpath, was in record["dependency_sha256"].items():
        now = hashlib.sha256((ROOT / relpath).read_bytes()).hexdigest()
        if now != was:
            raise SystemExit(f"{relpath} has changed since the validation; "
                             f"re-run analysis/validate.py; measurement refused")
    OUT["validation_record_sha256"] = hashlib.sha256(
        VALIDATION.read_bytes()).hexdigest()
    print("validation on record: passed, and every module it names is byte "
          "identical to the tree")
    print(f"  record digest {OUT['validation_record_sha256']}")


def received():
    payload = json.loads(RECEIVED.read_text(encoding="utf-8"))
    values = payload["values"]
    assert len(values) == 64 and len(set(values)) == 64
    OUT["received_source"] = {
        "repository": payload["origin_repository"],
        "deposit": payload["origin_deposit"],
        "ref": payload["origin_ref"],
        "file": payload["origin_file"],
        "symbol": payload["origin_symbol"],
        "file_sha256": payload["origin_file_sha256"],
        "transcription_sha256": hashlib.sha256(
            RECEIVED.read_bytes()).hexdigest(),
    }
    return values


# --- the preconditions of PREREGISTRATION.md section (d) --------------------

def precondition_one(rec):
    """P1: is the received adjacency pairing the rotation and complementation
    matching. Reported either way. It does not stop the lane."""
    adjacency = {frozenset((rec[2 * j], rec[2 * j + 1])) for j in range(32)}
    matching = {frozenset((a, b)) for a, b in core.BLOCKS}
    same = adjacency == matching
    OUT["P1"] = {"received_adjacency_is_the_matching": bool(same),
                 "blocks_in_common": len(adjacency & matching)}
    print(f"\nP1  the received adjacency pairing against the rotation and "
          f"complementation matching")
    print(f"    {'they are the same set partition' if same else 'THEY DIFFER'}"
          f", {len(adjacency & matching)} of 32 blocks in common")
    return same


def precondition_two(observed_focal):
    """P2: does the focal statistic recomputed here agree with the printed
    figure. If it disagrees the recomputed value is what is carried forward."""
    here = round(100 * observed_focal, 1)
    agrees = here == FOOTNOTE_PERCENT
    OUT["P2"] = {"recomputed_percent": here,
                 "printed_percent": FOOTNOTE_PERCENT,
                 "agrees_to_one_decimal": bool(agrees)}
    print(f"\nP2  the focal share recomputed here against the printed figure")
    print(f"    recomputed {here}, printed {FOOTNOTE_PERCENT}: "
          f"{'agree' if agrees else 'DISAGREE'}")
    if not agrees:
        print("    the recomputed value is the one carried forward, and the "
              "disagreement is reported as a finding about the deposit")
    return agrees


# --- sampling ---------------------------------------------------------------

def sample_shares(rng, kind):
    """All six per order shares for N_DRAWS draws of one null."""
    out = np.empty((N_DRAWS, core.N_ORDERS), dtype=np.float64)
    done = 0
    while done < N_DRAWS:
        m = min(CHUNK, N_DRAWS - done)
        if kind == "pair":
            perms, flips = core.draw_pair(rng, m)
            sig = core.signals_pair(perms, flips)
        else:
            sig = core.draw_free(rng, m)
        rows = core.energies(sig)
        assert (core.non_dc(rows) == core.NON_DC_ENERGY).all()
        out[done:done + m] = core.shares(rows)
        done += m
    return out


# --- the seven declared tests of section (e) --------------------------------

def mc_p(count):
    """PREREGISTRATION.md section (f): p = (1 + at least as extreme) / (1 + n).
    Never zero, conservative, and a floor is reported as a floor."""
    return (1.0 + count) / (1.0 + N_DRAWS)


def holm(raw):
    """Holm's step down at the declared family wise level, over the set of
    tests actually run. Section (f). Holm needs no independence, and these
    tests are not independent: the focal statistic is the sum of two of the
    six per order shares, and by (b.1) the six sum to one exactly."""
    m = len(raw)
    order = sorted(range(m), key=lambda i: raw[i])
    adjusted = [0.0] * m
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, min(1.0, (m - rank) * raw[i]))
        adjusted[i] = running
    return adjusted


def percentile(draws, observed):
    """Declared convention: the fraction of draws strictly below the observed
    value, as a percentage."""
    return 100.0 * float((draws < observed).sum()) / len(draws)


def main():
    print("=" * 72)
    print("THE DECLARED ANALYSIS")
    print("=" * 72)
    refuse_unless_validated()

    rec = received()
    print(f"\nreceived sequence read from "
          f"{OUT['received_source']['repository']} at "
          f"{OUT['received_source']['ref']}, never recomputed here")

    observed_rows = core.energies(core.signal_of_ordering(rec))
    observed = core.shares(observed_rows)[0]
    focal_idx = [k - 1 for k in core.FOCAL_ORDERS]
    observed_focal = float(observed[focal_idx].sum())
    OUT["observed_non_dc_energy"] = int(core.non_dc(observed_rows)[0])
    OUT["observed_shares"] = [float(x) for x in observed]
    OUT["observed_focal"] = observed_focal

    p1 = precondition_one(rec)
    if not p1:
        raise SystemExit(
            "P1 failed. The family this lane's validated sampler draws from "
            "is the matching's family, which is then not the family of the "
            "received pairing. Reported, and the run stops here rather than "
            "reporting a null it did not validate.")
    p2 = precondition_two(observed_focal)

    print(f"\nobserved non-DC energy {OUT['observed_non_dc_energy']}, which "
          f"the constant of (b.1) requires")

    streams = core.streams(SEED, 3)
    pair = sample_shares(streams[0], "pair")     # stream 0, declared
    free = sample_shares(streams[1], "free")     # stream 1, declared

    pair_focal = pair[:, focal_idx].sum(axis=1)
    free_focal = free[:, focal_idx].sum(axis=1)

    # --- the primary report: the whole profile, order by order -------------
    print("\nTHE PROFILE, orders 1 to 6, the primary report of section (c)")
    print(f"{'order':>5} {'observed':>10} {'pair mean':>10} {'pair sd':>9} "
          f"{'pctile N1':>10} {'free mean':>10} {'pctile N0':>10}")
    profile = []
    for k in range(1, core.N_ORDERS + 1):
        col = pair[:, k - 1]
        row = {"order": k,
               "observed": float(observed[k - 1]),
               "pair_mean": float(col.mean()), "pair_sd": float(col.std(ddof=1)),
               "pair_percentile": percentile(col, observed[k - 1]),
               "free_mean": float(free[:, k - 1].mean()),
               "free_percentile": percentile(free[:, k - 1], observed[k - 1])}
        profile.append(row)
        print(f"{k:>5} {row['observed']:>10.6f} {row['pair_mean']:>10.6f} "
              f"{row['pair_sd']:>9.6f} {row['pair_percentile']:>10.3f} "
              f"{row['free_mean']:>10.6f} {row['free_percentile']:>10.3f}")
    OUT["profile"] = profile

    m1 = float(pair_focal.mean())
    sd1 = float(pair_focal.std(ddof=1))
    se1 = sd1 / np.sqrt(N_DRAWS)
    m0 = float(Fraction(sum(core.CHARACTERS_BY_ORDER[k - 1]
                            for k in core.FOCAL_ORDERS), core.N_NON_DC))
    OUT["focal"] = {
        "observed": observed_focal,
        "pair_mean": m1, "pair_sd": sd1, "pair_se_of_mean": se1,
        "pair_percentile": percentile(pair_focal, observed_focal),
        "free_mean_exact": m0,
        "free_mean_sampled": float(free_focal.mean()),
        "free_percentile": percentile(free_focal, observed_focal),
    }
    print(f"\nTHE FOCAL STATISTIC, the share at orders 2 and 4")
    print(f"  observed                        {observed_focal:.6f}")
    print(f"  pair preserving mean            {m1:.6f}  sd {sd1:.6f}")
    print(f"  percentile in the pair family   "
          f"{OUT['focal']['pair_percentile']:.3f}")
    print(f"  free null mean, exact by (b.3)  {m0:.6f}")
    print(f"  percentile in the free null     "
          f"{OUT['focal']['free_percentile']:.3f}   (descriptive, untested)")

    # --- the attribution, the primary quantity of section (d) --------------
    excess = observed_focal - m0
    explained = m1 - m0
    residual = observed_focal - m1
    admissible = abs(excess) >= 4 * se1
    attribution = {"excess": excess, "explained": explained,
                   "residual": residual, "ratio_admissible": bool(admissible)}
    if admissible:
        attribution["A_attributable"] = explained / excess
        attribution["R_residual"] = residual / excess
        lo, hi = m1 - 1.96 * se1, m1 + 1.96 * se1
        attribution["A_interval"] = sorted([(lo - m0) / excess,
                                            (hi - m0) / excess])
        attribution["R_interval"] = sorted([(observed_focal - hi) / excess,
                                            (observed_focal - lo) / excess])
    OUT["attribution"] = attribution

    print("\nTHE ATTRIBUTION, the primary quantity of section (d)")
    print(f"  excess    observed minus the free null mean   {excess:.6f}")
    print(f"  explained pair mean minus the free null mean  {explained:.6f}")
    print(f"  residual  observed minus the pair mean        {residual:.6f}")
    if admissible:
        print(f"  A  attributable to the pair rule  "
              f"{attribution['A_attributable']:.4f}  "
              f"[{attribution['A_interval'][0]:.4f}, "
              f"{attribution['A_interval'][1]:.4f}]")
        print(f"  R  not attributable               "
              f"{attribution['R_residual']:.4f}  "
              f"[{attribution['R_interval'][0]:.4f}, "
              f"{attribution['R_interval'][1]:.4f}]")
        print("  the interval is Monte Carlo error on the family mean and "
              "nothing else")
    else:
        print("  the ratios are not reported: the excess is not four Monte "
              "Carlo standard errors from zero, and section (d) fixes that "
              "rule in advance")

    # --- the seven declared tests ------------------------------------------
    tests = []
    count = int((pair_focal >= observed_focal).sum())
    tests.append({"test": "T0", "what": "share at orders 2 and 4",
                  "tail": "one sided, upper", "raw_p": mc_p(count),
                  "at_least_as_extreme": count})
    for k in range(1, core.N_ORDERS + 1):
        col = pair[:, k - 1]
        centre = float(col.mean())
        count = int((np.abs(col - centre) >= abs(observed[k - 1] - centre)).sum())
        tests.append({"test": f"T{k}", "what": f"share at order {k}",
                      "tail": "two sided", "raw_p": mc_p(count),
                      "at_least_as_extreme": count})

    adjusted = holm([t["raw_p"] for t in tests])
    for t, adj in zip(tests, adjusted):
        t["adjusted_p"] = adj
        t["below_threshold"] = bool(adj < FAMILY_WISE)
    OUT["tests"] = tests
    OUT["family_wise_level"] = FAMILY_WISE
    floor = 1.0 / (1.0 + N_DRAWS)

    print(f"\nTHE SEVEN DECLARED TESTS, all under the pair preserving null, "
          f"Holm at {FAMILY_WISE}")
    print(f"{'test':>5} {'statistic':<24} {'tail':<18} {'raw p':>10} "
          f"{'adjusted p':>11}")
    for t in tests:
        flag = " at the floor" if t["raw_p"] <= floor else ""
        print(f"{t['test']:>5} {t['what']:<24} {t['tail']:<18} "
              f"{t['raw_p']:>10.6f} {t['adjusted_p']:>11.6f}{flag}")

    survivors = [t for t in tests if t["below_threshold"]]
    refuted = not survivors
    OUT["H_resid_refuted"] = bool(refuted)
    OUT["smallest_adjusted_p"] = min(adjusted)

    print("\nTHE SIGNED CRITERION, PREREGISTRATION.md section (e)")
    print('  "H_resid is refuted if every one of the seven declared tests, '
          'after the')
    print('   Holm correction of section (f), yields an adjusted p of at '
          'least 0.05."')
    if refuted:
        print(f"\n  REFUTED. Every adjusted p is at least {FAMILY_WISE}. "
              f"The smallest is {min(adjusted):.6f}.")
    else:
        names = ", ".join(f"{t['test']} ({t['what']}, {t['tail']})"
                          for t in survivors)
        print(f"\n  NOT REFUTED. Below the threshold: {names}.")

    (ROOT / "results").mkdir(exist_ok=True)
    (ROOT / "results" / "measurement.json").write_text(
        json.dumps(OUT, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    print("\nwritten results/measurement.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
