# Rigour report, session three

Session identifier: S003. Date: 2026-08-11. The analysis session.

State at open, reported before anything was done: head
`6b6a3bddd0a50b00f3c4b75b973ec01981b79129`, the session two close, as
expected; working tree clean; thirty-one tracked paths; no remote; the root
tree holding one path; and the preregistration blob identical at the root and
at the head.

**This session measured the thing the lane exists to measure, and it did so
after publishing the document that governs it.** The two events are in the
effort log with their clock and are set out below in order.

---

## Commits

Four.

- **The fifth gate**, `da4b5d1`. The staleness gate, the digests it reads,
  its tests, and defect seven.
- **Publication**, `59836ed`. The two contracts updated to record the push.
- **The measurement**, `989afd2`. `analysis/measure.py`,
  `tools/receive_kingwen.py`, `data/`, `results/measurement.json`,
  `RESULTS.md`, the manifest and the registry.
- **This report**, which is the fourth and is counted.

Thirty-eight tracked paths at the close.

---

## The ordering, which is the point of this session

| clock, UTC | event |
| --- | --- |
| 22:32:19 | session opened, head reported, nothing observed read |
| 22:34:51 | house procedure begun over the history as it then stood |
| 22:35:04 | push begun |
| 22:35:06 | push returned |
| 22:41:14 | received sequence transcribed, and the analysis run |

The observed value of the statistic was not computed, read, printed or stored
before 22:35:06. There is no code path by which it could have been: no file
in this repository held the received sequence before 22:41, `data/` did not
exist, and `tools/receive_kingwen.py` had not been written.

A preregistration is worth what its timestamp is worth, and a timestamp that
exists only on the machine that wrote it is worth nothing to a reader. The
root commit that carries the signed document is now on a public remote, and
it got there before the measurement it governs.

## The push, reported as rule six requires

- **Address**: `https://github.com/Probatorium/walsh-attribution`.
- **Visibility**: PUBLIC.
- **House procedure, step one**: one line log of all fourteen commits then in
  the history, all authored under the git identity `alexcat84`.
- **House procedure, step two**: fifty-one distinct text blobs swept for
  secrets, tokens and personal paths. One file allowed by name with its
  reason printed, which is the sweep tool itself since the patterns live
  there. **Zero findings.**
- **House procedure, step three**: `git ls-remote` against the address
  returned no refs before the remote was attached. Empty, confirmed, and
  confirmed before attaching rather than after.
- **Local head after the push**: `da4b5d1725604841a88f280079f631bb59f70316`.
- **Remote head after the push**: the same.
- **Local tree**: `5a1fa2b1e9d5aa68f75d69cb13fdbc7115187152`. **Remote
  tree**: the same. `git diff` between the two heads is empty.
- The root commit is present on the remote.

**What is still local.** The three commits made after the push, this one
included. `CONTACT-RULES.md` rule six and decision two both say the
authorisation covered the history it published and does not make later pushes
automatic, so they wait for that to be asked for, and the house procedure
will run again over what is new.

## The fifth gate, which closes a hole this lane reported about itself

Session two wrote in its own rigour report that nothing forced the validation
to be re-run when its code changed. This session closed that by mechanism.

`results/validation.json` now records the digest of every module the
validation is a statement about, computed at the end of the run so the
digests describe the files as they stood for it.
`tools/validation_gate.py` recomputes them and fails, naming the file and
printing both digests, when any has moved. It runs with the standing gates.

**It was tested by breaking it.** A comment appended to `analysis/core.py`
made the gate fail naming that file and made the standing gates refuse a
commit; restoring the file made both pass. Six further checks in the suite
attack the comparison directly, with a digest that is wrong and with a path
that is not there. Sixty-two checks in the suite now, all passing.

Two limits are written into the gate's own docstring rather than left to be
found. It does not fail on a validation that did not pass, because a
repository that cannot commit its own bad news is worse than one with no
gate; the refusal to measure on a failed validation lives in
`analysis/measure.py` and fired nowhere, because the validation passed. And
it does not cover a module the validation never imported, because a new
consumer of the sampler cannot invalidate a run that already happened. That
second limit is why `analysis/measure.py` is outside its list.

## The received sequence

Transcribed mechanically from the deposit at its tag by
`tools/receive_kingwen.py`, not typed. Checked on entry for sixty-four
distinct six bit values and for nothing else, because recomputing the
sequence is what receiving it forbids. Recorded in
`THIRD-PARTY-MANIFEST.md` at the moment of entry with the digest of the
source file at the tag and the digest of the file written here. The
neighbour's working tree did not move and was on its own branch before and
after.

## The measurement

`RESULTS.md` carries the result and `results/measurement.json` the machine
record. In brief, and without repeating the tables:

- **Both preconditions pass.** The received adjacency pairing is the rotation
  and complementation matching, thirty-two blocks of thirty-two. The focal
  share recomputed here is the figure the audited footnote prints, to one
  decimal.
- **The primary report is the whole profile**, orders one to six, under both
  nulls, as section (c) fixed in advance.
- **The attribution is the primary quantity**, computed under the definition
  the signed document fixed before anything was measured: 0.3504 of the
  excess over uniformity is attributable to the pair rule and 0.6496 is not.
- **The signed criterion is met in its refutation branch.** All seven
  declared tests, Holm corrected over the whole set, yield adjusted p of at
  least the declared level, the smallest being 0.312583.
- **The constant of (b.1) was re-verified inside the measurement itself**, on
  the received sequence and on every one of the four hundred thousand draws,
  by an assertion in the sampling loop rather than by trust in the earlier
  validation.

## What the primary report showed that the focal statistic conceals

Reported here because it is the reason section (c) demanded the full profile,
and it is a description of a table rather than a test. The concentration sits
at order two, which is far up its family. Order four is slightly below its own
family mean and sits at an ordinary place in the family. A statistic that adds
the two carries one of each.

Nothing in the signed design tests that observation, and this lane does not
test it now. It is recorded so that a reader has it, and any lane that wants
to pursue it starts by preregistering it.

## Figure gate

Thirty records. Thirteen figures usable, and **one still blocked**: the draw
count of the auditor's unregistered prior exploration. That one can never
move, because it is a fact about a run that happened elsewhere and no
artefact here can produce it. Everything else that was blocked has been
retired by a record naming exactly what it retired, and every retired record
is still in the file.

Both figures of the audited footnote are now measured here rather than cited.
So are the four figures of the prior exploration, in the sense that the
objects they named have been measured: the values this lane carries forward
are its own and differ from the exploration's in the third and fourth places,
which is what a hundredfold larger draw count buys.

The gate was exercised in both directions. The measurement commit carries
seven accountable numerals and passed, each resolving to an object verified
here. Every other commit message of the session carries none.

## Dash sweep

- Working tree, every tracked text file: clean.
- Every blob of every commit: clean.
- The single registered exemption is unchanged and still unused.

## Untouchable gate

Tree, remotes, config and every blob of every commit: clean. The remote check
is no longer trivial, since a remote now exists, and it passes.

## Defects

One added and closed in the same session: defect seven, that the validation
was a claim about code that named no code. It was raised by this lane about
itself in the previous session's report and is now closed by mechanism rather
than by an intention to remember.

Defects one, two, four, five and six stand as recorded. Defect three is closed
as of session two.

## What is pending

1. **Publishing the commits made after the push**, including the measurement.
   That is an ask, not a decision this lane takes for itself.
2. **The background review**, still unstarted, which is why no claim of
   novelty is made about anything, including the four exact facts derived in
   section (b).
3. **The two errata candidates**, prepared in session two and applied
   nowhere. They are for the deposit's own errata process and belong to
   Alexis in that capacity. The measurement strengthens the case for the
   second one and does not change either candidate: both figures the footnote
   prints are confirmed, and what both candidates are about is the prose.

## What is not claimed

Nothing about design, intention, purpose or awareness. Nothing about the
makers of the sequence or their knowledge. Nothing about the meaning,
authenticity, antiquity or authority of any text. Nothing about any person,
including the writer of the audited footnote, who is the author of this lane.

That the sampler is uniform on the family. What is claimed is what
`VALIDATION-PLAN.md` said in advance a pass would establish: every draw is in
the family by three independently written predicates, and six exactly known
quantities came out right.

No claim of novelty about anything.
