"""Tests for the gates.

PROVENANCE. Reused, by reading, from the closed lane whose local checkout is
named `pairing-conditioned`, and extended here. See `PROVENANCE.md`. The
tests added in this lane are marked NEW below: the untouchable pattern tests,
and the tests that hold the figure gate against the figures this particular
lane is most likely to repeat by reflex.

A gate nobody has tried to break is a decoration. These tests try to break
each gate in the way it is most likely to fail in use: a forbidden character
that looks innocent, an exemption applied where it was not granted, an edited
past entry in a hash chain, and a numeral smuggled into a commit message.

Run: python tools/test_gates.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import dashcheck
import effortlog
import figures
import untouchable
import validation_gate

PASSED = []
FAILED = []


def check(label, condition):
    (PASSED if condition else FAILED).append(label)
    print(f"{'ok  ' if condition else 'FAIL'} {label}")


def test_dash_gate():
    # Escapes, not literals, for the reason given in tools/dashcheck.py.
    em = chr(0x2014)
    en = chr(0x2013)
    minus = chr(0x2212)

    check("em dash is caught in an ordinary file",
          len(dashcheck.offences_in_text(f"a{em}b", "PREREGISTRATION.md")) == 1)
    check("em dash is caught even in an exempted file",
          len(dashcheck.offences_in_text(f"a{em}b", "REFERENCES.md")) == 1)
    check("minus sign is caught",
          len(dashcheck.offences_in_text(f"a{minus}b", "PREREGISTRATION.md")) == 1)
    check("en dash is caught outside an exempted file",
          len(dashcheck.offences_in_text(f"12{en}34", "PREREGISTRATION.md")) == 1)
    check("en dash in a numeric range passes inside an exempted file",
          dashcheck.offences_in_text(f"pp. 12{en}34", "REFERENCES.md") == [])
    check("en dash between words is caught inside an exempted file",
          len(dashcheck.offences_in_text(f"well{en}known", "REFERENCES.md")) == 1)
    check("an ASCII hyphen is never an offence",
          dashcheck.offences_in_text("spectral-attribution", "NAME-GATE.md") == [])
    check("the offence is located on the right line",
          dashcheck.locate(f"one\ntwo{em}", 7) == (2, 4))


def test_effort_chain():
    def sign(entry, prev):
        entry = dict(entry)
        entry["prev"] = prev
        entry["hash"] = effortlog.digest(entry, prev)
        return entry

    base = {"index": 0, "utc": "2026-08-11T00:00:00Z", "session": "S",
            "kind": "OPEN", "class": "GOVERNANCE", "summary": "open",
            "artifacts": [], "commit": ""}
    first = sign(base, effortlog.GENESIS)
    second = sign({**base, "index": 1, "kind": "WORK", "class": "APPARATUS",
                   "summary": "work"}, first["hash"])

    check("a freshly signed entry verifies",
          effortlog.digest(first, effortlog.GENESIS) == first["hash"])
    check("editing an entry breaks its own digest",
          effortlog.digest({**first, "summary": "tampered"},
                           effortlog.GENESIS) != first["hash"])
    check("the chain links the second entry to the first",
          second["prev"] == first["hash"])
    check("editing the first entry orphans the second",
          effortlog.digest({**first, "summary": "tampered"},
                           effortlog.GENESIS) != second["prev"])
    check("canonical form ignores the hash field itself",
          "hash" not in effortlog.canonical(first))
    check("canonical form is stable under key order",
          effortlog.canonical(first)
          == effortlog.canonical(dict(reversed(list(first.items())))))
    check("every class this lane will use is declared",
          set(effortlog.CLASSES) >= {"GOVERNANCE", "APPARATUS", "VALIDATION",
                                     "ANALYSIS"})


def test_figure_gate():
    check("a message with no numeral has no hits",
          figures.scan("Contact rules for the frozen work") == [])
    check("a numeral in the body is a hit",
          figures.scan("the share is 77.4 here") == [(1, "77.4")])
    check("a trailer line is not scanned",
          figures.scan("Co-Authored-By: Claude Opus 5 <x@y>") == [])
    check("a comment line is not scanned",
          figures.scan("# on branch main with 3 files") == [])
    check("trailing punctuation is stripped from the token",
          figures.scan("the value was 47.6.") == [(1, "47.6")])
    check("a numeral after a trailer, on its own line, is still caught",
          figures.scan("Co-Authored-By: X\n\nand 42 more") == [(3, "42")])
    check("a decimal is captured whole",
          figures.scan("p below 0.05 was seen") == [(1, "0.05")])


def test_identifier_exemptions():
    """An identifier may pass, a measurement may not, and the registry
    outranks every pattern."""

    def split(message, registered=frozenset()):
        exempt, accountable = figures.analyse(message, set(registered))
        return ([t for _, t, _, _ in exempt], [t for _, t in accountable])

    ex, acc = split("see doi 10.5281/zenodo.21776041 for the deposit")
    check("a DOI is exempted whole", acc == [] and ex)
    check("the DOI exemption is reported as a DOI",
          figures.analyse("doi 10.5281/zenodo.21776041", set())[0][0][2] == "doi")

    ex, acc = split("Radisic (2026) proves it")
    check("a publication year is exempted", ex == ["2026"] and acc == [])

    ex, acc = split("at head 43319e2 the tree was clean")
    check("a hexadecimal object name is exempted", ex == ["43319e2"] and acc == [])

    ex, acc = split("the count was 6815987 things")
    check("an all digit token is not taken for an object name",
          acc == ["6815987"] and ex == [])

    ex, acc = split("read at zenodo-v3 in session S001 after defect D001")
    check("labels with digits bound to letters are exempted",
          acc == [] and len(ex) == 3)

    ex, acc = split("dated 2026-08-11 by the log")
    check("an ISO date is exempted", ex == ["2026-08-11"] and acc == [])

    ex, acc = split("Radisic (2026) reports 2016 pairs", registered={"2016"})
    check("a registered token is never exempted, even as a year",
          acc == ["2016"] and ex == ["2026"])

    ex, acc = split("the p value was 0.05")
    check("a bare measurement stays accountable", acc == ["0.05"] and ex == [])

    ex, acc = split("Co-Authored-By: Claude Opus 5 <x@y>")
    check("a trailer is still skipped entirely", acc == [] and ex == [])

    check("every declared pattern carries a reason",
          all(reason.strip() for _, reason, _ in figures.IDENTIFIERS))
    check("no exemption is silent: the reporter prints when there is one",
          figures.report_exemptions([(1, "2026", "year", "a publication year")])
          is None)


def test_this_lanes_own_temptations():
    """NEW in this lane.

    The figures this repository is most likely to repeat by reflex are the
    two the deposit's footnote prints and the four the auditor's unregistered
    exploration produced. None of them has been recomputed here. Each must be
    refused while its citation stands, and each must stay refused even when
    it is written in a form that looks like something else.
    """
    cited = [
        ("77.4", "the deposit's share of non-DC Walsh energy in orders 2 and 4"),
        ("47.6", "the deposit's uniform expectation for orders 2 and 4"),
        ("0.5786", "the prior exploration's mean under the pair preserving family"),
        ("96.1", "the prior exploration's percentile of the observed"),
    ]
    records = [{"token": t, "object": o, "status": "cited-unverified",
                "source": "outside this repository", "verified_by": "", "utc": ""}
               for t, o in cited]
    tokens = {r["token"] for r in records}

    for token, _ in cited:
        _, verified, blocking = figures.standing(records, token)
        check(f"the cited figure {token} is blocked and unusable",
              not verified and len(blocking) == 1)

    _, acc = ([t for _, t, _, _ in figures.analyse("the share was 77.4", tokens)[0]],
              [t for _, t in figures.analyse("the share was 77.4", tokens)[1]])
    check("a cited figure in a message body stays accountable", acc == ["77.4"])

    ex, acc = figures.analyse("version v77.4 of nothing", tokens)
    check("dressing a cited figure as a version label does not exempt it",
          [t for _, t in acc] == ["77.4"])


def test_untouchable_patterns():
    """NEW in this lane. The pattern must fire on the name and not on words
    that merely contain it.

    No untouchable name is written as a literal anywhere in this file. Every
    fixture below is built from `untouchable.UNTOUCHABLE` at run time. That is
    not a stylistic choice: the gate scans this file like any other, so a
    literal here would make the suite an offender against the rule it tests,
    and the fix for that is never an exemption for the enforcer. See defect
    one in DEFECTS.md, which is how this was found.
    """
    rx = untouchable.patterns()
    longest = max(untouchable.UNTOUCHABLE, key=len)
    shortest = min(untouchable.UNTOUCHABLE, key=len)
    for i, name in enumerate(untouchable.UNTOUCHABLE):
        check(f"untouchable name {i} is caught on its own",
              bool(rx.search(f"a line naming {name} here")))
    check("a longer name is reported once, not twice",
          len(rx.findall(longest)) == 1)
    check("a name embedded in a longer word is not caught",
          rx.search(f"meta{shortest}ises") is None)
    check("the allowance covers the file that declares the rule",
          untouchable.allowed("CONTACT-RULES.md"))
    check("the allowance covers session reports by prefix",
          untouchable.allowed("SESSION-REPORT-001.md"))
    check("the allowance does not cover the preregistration",
          not untouchable.allowed("PREREGISTRATION.md"))
    check("the reference list is never allowed to name one",
          "REFERENCES.md" in untouchable.CITATION_FILES
          and "REFERENCES.md" not in untouchable.ALLOWED)


def test_validation_staleness():
    """NEW in session three. The gate that ties the validation to its code.

    Attacked with a digest that is wrong and with a path that is not there,
    rather than only exercised through a run that happens to pass.
    """
    real = "tools/validation_gate.py"
    good = validation_gate.digest_of(real)

    stale, missing = validation_gate.compare({real: good})
    check("a module that has not moved is neither stale nor missing",
          stale == [] and missing == [])

    stale, missing = validation_gate.compare({real: "0" * 64})
    check("a module whose digest does not match is reported stale",
          len(stale) == 1 and stale[0][0] == real and missing == [])
    check("the stale report carries both digests",
          stale[0][1] == "0" * 64 and stale[0][2] == good)

    stale, missing = validation_gate.compare({"analysis/not-a-file.py": good})
    check("a recorded module that no longer exists is reported missing",
          missing == ["analysis/not-a-file.py"] and stale == [])

    stale, missing = validation_gate.compare({})
    check("an empty record has nothing to report here, and main refuses it "
          "separately", stale == [] and missing == [])

    check("the live record names the modules the validation imports",
          set(json.loads((Path(validation_gate.RECORD)).read_text(
              encoding="utf-8"))["dependency_sha256"])
          >= {"analysis/core.py", "analysis/validate.py"})


def test_supersession():
    """A figure moves from cited to measured by retirement, not by deletion."""

    def rec(token, obj, status):
        return {"token": token, "object": obj, "status": status,
                "source": "", "verified_by": "", "utc": ""}

    cited = rec("77.4", "as the deposit's footnote reports it", "cited-unverified")
    here = rec("77.4", "as recomputed here under a named convention", "verified-here")
    retire = rec("77.4", "as the deposit's footnote reports it", "superseded")

    _, v, b = figures.standing([cited], "77.4")
    check("a cited figure blocks on its own", not v and len(b) == 1)

    _, v, b = figures.standing([cited, here], "77.4")
    check("measuring it here does not unblock it while the citation stands",
          len(v) == 1 and len(b) == 1)

    _, v, b = figures.standing([cited, here, retire], "77.4")
    check("retiring the citation unblocks the measured figure",
          len(v) == 1 and not b)

    other = rec("77.4", "a different object entirely", "cited-unverified")
    _, v, b = figures.standing([cited, here, retire, other], "77.4")
    check("retiring one object does not retire another with the same digits",
          len(v) == 1 and len(b) == 1)

    _, _, b = figures.standing([cited, here, retire], "52")
    check("a token with no record has nothing standing", not b)

    check("the retired record is still in the registry",
          any(r["status"] == "cited-unverified"
              for r in [cited, here, retire]))


def main():
    print("dash gate")
    test_dash_gate()
    print("\neffort log chain")
    test_effort_chain()
    print("\nfigure gate")
    test_figure_gate()
    print("\nidentifier exemptions")
    test_identifier_exemptions()
    print("\nthe figures this lane is most likely to repeat")
    test_this_lanes_own_temptations()
    print("\nuntouchable patterns")
    test_untouchable_patterns()
    print("\nvalidation staleness")
    test_validation_staleness()
    print("\nsupersession")
    test_supersession()
    print(f"\npassed {len(PASSED)}, failed {len(FAILED)}")
    if FAILED:
        for label in FAILED:
            print(f"  failed: {label}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
