# Defects

Signed texts are not amended in this lane. When something is found to be
wrong or badly posed, it is recorded here and corrected forward. This file is
append only in practice: entries are added, and an entry that turns out to be
mistaken gets a later entry saying so rather than an edit.

Every entry states what the defect is, how it was found, what was done, and
what it cost. An entry that cannot say how it was found is a weaker entry and
should say that too.

Opened in the inaugural session with four entries.

---

## Defect one: the signature of the preregistration contradicts its own section (b)

**What.** The closing section of `PREREGISTRATION.md` opens with "No quantity
of `N0` or `N1` has been computed at the time of this commit." Sections (b.3)
and (b.4) of the same document compute two quantities of exactly those
families: the exact mean of the focal statistic under `N0`, and the exact
mean of the order 6 energy under `N1`. Both are derived by hand, both are
printed, and both are quantities of a null family. The sentence is false as
written.

**How found.** By re-reading the signed document against its own contents
while writing this register, in the same session, after the root commit
existed.

**What the document should have said.** The third sentence of the same
paragraph already says it: the arithmetic performed "concerns no sample, and
is checkable by hand from this text alone". That is the restriction that was
meant and it is the one that governs. The correct claim is that nothing was
measured: no draw was taken from either family, no sampler existed, and the
received sequence had not been read. The claim that no quantity of either
family had been derived is wrong and was never true of a document whose whole
section (b) is such derivations.

**Done.** Nothing to the signed text, which stands as it is. Corrected
forward here. Any reader of the signature should read its first sentence as
governed by its third.

**Cost.** A reader of the signature alone would take the document to claim
more purity than it has. The claim it actually needs, and which is true, is
the narrower one. The cost is real, it is not recovered by this entry, and it
is a good argument for writing the narrow claim first and the sweeping one
never.

**What it does not affect.** The declared analytic facts are predictions
under test in `VALIDATION-PLAN.md`, they are registered in `FIGURES.jsonl` as
unusable until an artefact here produces them, and none of them is a focal
quantity. Nothing about the design changes.

---

## Defect two: the untouchable gate refused its own test suite

**What.** The pattern tests added in this lane wrote an untouchable
repository name as a literal fixture in `tools/test_gates.py`. The gate scans
every tracked text file, that file is not in the short allowance of files
permitted to name those repositories, and so the suite that tests the rule
was itself an offender against it.

**How found.** By the gate, on the first commit that tried to carry it. The
commit was refused before it existed.

**Done.** Every fixture in that test is now built from the tool's own list at
run time, so no untouchable name is written anywhere in the file. The
alternative, adding the suite to the allowance, was rejected: an exemption
for the enforcer is the first hole a reader should look for, and granting one
would make every later clean sweep worth less.

**Cost.** None beyond the fix. The defect never entered the history, because
the pre-commit hook ran before the commit was created.

---

## Defect three: the figure registry has no status for a derivation made here and not executed

**What.** `PREREGISTRATION.md` derives two constants by hand. They are not
citations: they came from nowhere outside this repository. They are also not
verified here: no artefact in this repository has produced them. The registry
carries three statuses, `cited-unverified`, `verified-here` and `superseded`,
and none of them is the right name for that state. Both constants are filed
as `cited-unverified`.

**How found.** While registering them, by noticing that the status being
applied said something untrue about where they came from.

**Done.** The status is accurate about the only thing the gate acts on, which
is usability: both are blocked from every commit message until an artefact
here produces them, which is exactly right. The `object` field of both
records says in words that they are hand derivations of this lane and
unexecuted, so the record as a whole is not misleading even though its status
label is.

The status set was not extended. The gate and its tests came from a closed
lane at a named commit, and changing its vocabulary in the same session that
adopted it would leave the inherited tests covering a tool that no longer
exists. A fourth status is a reasonable correction for a later session and is
recorded here as an option, not taken.

**Cost.** A reader scanning statuses rather than objects would take two hand
derivations for external citations. That is a real misreading and this entry
is the only thing standing against it until the status set is fixed.

---

## Defect four: the effort log binds to its commits more weakly than it looks

**What.** Two things, both about binding rather than integrity.

First, entries are appended when the work is done, which is before the commit
that carries the work exists. Only the entry for the root commit carries a
commit hash; the rest bind to their work by timestamp and by the list of
artefacts they name. That is a weaker binding than a hash.

Second, `EFFORT-LOG.jsonl` was staged with the apparatus commit and then not
staged again until the validation commit, so between those two commits the
tracked copy of the log was one commit behind the working copy. A reader
checking out the registers commit would find a log that does not mention the
registers.

**How found.** By reading `git status` after a commit and seeing the log
listed as modified rather than clean.

**Done.** From the validation commit onward the log is staged with every
commit. The earlier gap stands in the history and is not rewritten.

**Cost.** Small and bounded. The hash chain is intact throughout and no entry
is altered; what is weaker than it appears is the link from an entry to the
commit that carried its work, not the integrity of the entry itself. The
practice that follows: append the entry, make the commit, and stage the log
with it, accepting that the entry names the work rather than the commit.

**Not done, deliberately.** No history rewrite. A repository whose whole
claim is that its record is exact cannot buy neatness with a rewrite.

---

## Defect five: the validation plan fixed a tolerance and forgot the draw counts

**What.** `VALIDATION-PLAN.md` fixes the tolerance of V3 and V4, four
standard errors of the sample mean with the standard error taken from the
sample's own dispersion, and it never says how many draws those checks are
computed over. It says "the declared draws" and points at a declaration that
does not exist: the signed preregistration fixes the sample size of the
analysis run, not of the validation, and the validation runs on its own
stream.

**How found.** While writing the sampler, by trying to read the count out of
the plan and not finding one.

**Done.** The three counts are declared in the module docstring of
`analysis/validate.py`, in writing, before the run rather than after it, with
the reason for each. The moment checks use the same count as the analysis run
so that the acceptance test has the precision of the run it gates. Nothing in
`VALIDATION-PLAN.md` is edited, because filling the gap silently in the
document that has the gap is the failure mode this register exists against.

**Cost.** A reader of the plan alone cannot tell how strong V3 and V4 are.
They have to open the code. That is a real cost of a plan that governs a run
and does not fully determine it.

---

## Defect six: an acceptance test was briefly written so that it was easier to pass

**What.** The first version of the free null check on the focal share
compared the sample mean against its analytic value using a bound on the
standard error rather than the standard error: the sum of the two per order
standard errors, which is at least the standard error of their sum. A
tolerance of four standard errors applied to an over-estimated standard error
is a wider window than the one the plan declares. The check was therefore
easier to pass than written, and the direction of the error is the wrong one
for an acceptance test.

**How found.** By reading the code while writing this register, before the
result had been committed.

**Done.** The focal share is now accumulated as its own quantity, so the
check uses the standard error of the thing it is testing. The validation was
run twice. The two runs draw the same numbers, because the seed, the stream
and the order of the calls that consume randomness are unchanged and the fix
consumes none, and the reported means are identical between them. What
changed is only the width of the window: the deviation is reported against
the true standard error and is larger than it was against the bound, and it
passes either way.

**Cost.** None to the record, since the loose version never reached a commit.
The general point it illustrates is worth keeping: a conservative bound is
conservative for a confidence statement and anti-conservative for an
acceptance test, and the two are easy to confuse.

---

## Defect seven: the validation was a claim about code that named no code

**What.** `results/validation.json` recorded that both routes passed and did
not record what they passed on. Nothing tied the run to the source of the
sampler, the transform or the harness, so any later edit to
`analysis/core.py` would have left a result file asserting a validation of
code that no longer existed, with nothing in the repository noticing.

**How found.** By this lane, about itself, in `SESSION-REPORT-002.md`, in the
section on the test suite, and reported there as a weakness rather than
discovered later by a reader. What that report did not do was fix it.

**Done.** Closed by mechanism, in session three, not by an intention to
remember. `analysis/validate.py` now records the digest of every module the
validation is a statement about, computed at the end of the run so that the
digests describe the files as they stood for it. `tools/validation_gate.py`
recomputes them and fails, naming the file and printing both digests, when
any has moved. It runs with the standing gates, so a commit made on a stale
validation is refused before it exists.

It was tested by breaking it: a comment appended to `analysis/core.py` made
the gate fail naming that file, made the standing gates refuse, and the
failure went away when the file was restored. Four further checks attack the
comparison directly with a wrong digest and an absent path.

**What it deliberately does not do.** It does not fail on a validation that
did not pass, because a record of a failed validation has to be committable
or the repository cannot report its own bad news. The refusal to measure on a
failed validation lives in `analysis/measure.py`. And it does not cover a
module the validation never imported, because a new consumer of the sampler
cannot invalidate a run that already happened.

**Cost.** The window in which the hole existed ran from the validation commit
of session two to this one, and inside that window no module changed, which
is checkable from the history rather than asserted here.
