"""Staleness gate for the validation.

Session two reported a weakness in its own rigour report, in these words: the
validation "is also a single run rather than a suite that a later change would
re-run automatically. If `analysis/core.py` changes, the validation must be
re-run by hand, and nothing in this repository currently forces that."

This tool is what forces it. It closes that hole by mechanism rather than by
memory, which is the only way a hole of that shape ever closes.

WHAT IT CHECKS. `results/validation.json` records, under `dependency_sha256`,
the digest of every module the validation is a statement about, as those
modules stood for the run that produced the file. This gate recomputes those
digests now and fails if any of them has moved, naming the file. It also fails
if the result file is missing, if it records no dependencies, or if a recorded
file no longer exists.

WHAT IT DOES NOT CHECK, and why.

  It does not fail on a validation that did not pass. A record of a failed
  validation must be committable, or the repository could not report its own
  bad news. What a failed validation stops is the measurement, and
  `analysis/measure.py` refuses to run on one; that is the right place for
  that refusal, not here.

  It does not cover a module the validation never imported. A new consumer of
  the sampler cannot invalidate a run that already happened. What can is a
  change to the sampler, the transform, the neighbour reader or the validation
  harness, and those are what the recorded list holds. The limitation is
  declared in `analysis/validate.py` beside the list itself.

  It does not know whether the recorded run was honest. It knows whether the
  code that ran is the code that is here now. That is a narrow claim and it is
  the whole claim.

Usage:
    python tools/validation_gate.py
"""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECORD = ROOT / "results" / "validation.json"


def digest_of(relpath):
    return hashlib.sha256((ROOT / relpath).read_bytes()).hexdigest()


def compare(recorded):
    """Split a recorded digest map into what moved and what vanished.

    Separated from `main` so that the test suite can attack it directly with
    a digest that is wrong and a path that does not exist, rather than only
    exercising it through a run that happens to pass.
    """
    stale, missing = [], []
    for relpath, was in sorted(recorded.items()):
        path = ROOT / relpath
        if not path.is_file():
            missing.append(relpath)
            continue
        now = digest_of(relpath)
        if now != was:
            stale.append((relpath, was, now))
    return stale, missing


def main():
    if not RECORD.exists():
        print(f"validation gate: FAIL, {RECORD.relative_to(ROOT)} does not "
              f"exist, so no validation is on record at all")
        return 1
    try:
        record = json.loads(RECORD.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"validation gate: FAIL, the result file is not JSON: {exc}")
        return 1

    recorded = record.get("dependency_sha256")
    if not recorded:
        print("validation gate: FAIL, the result file records no dependency "
              "digests, so it is a validation of nothing nameable")
        return 1

    stale, missing = compare(recorded)

    for relpath in missing:
        print(f"{relpath}: recorded by the validation and no longer present")
    for relpath, was, now in stale:
        print(f"{relpath}: changed since the validation ran")
        print(f"  validated {was}")
        print(f"  now       {now}")

    if stale or missing:
        print(f"validation gate: FAIL, {len(stale)} module(s) changed and "
              f"{len(missing)} missing since the validation on record")
        print("Re-run analysis/validate.py. Until it passes again and rewrites "
              "results/validation.json, no measurement in this repository "
              "rests on a validated sampler.")
        return 1

    verdict = record.get("passed")
    print(f"validation gate: PASS, {len(recorded)} module(s) byte identical "
          f"to the validated run, whose recorded verdict is "
          f"{'PASS' if verdict else 'FAIL'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
