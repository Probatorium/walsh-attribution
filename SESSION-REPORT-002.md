# Rigour report, session two

Session identifier: S002. Date: 2026-08-11.

**The focal statistic has not been computed.** No observed value was read, the
received King Wen sequence has not entered this repository, and no aggregate
over the focal interaction orders exists for any draw of the pair preserving
family. What this session did was decide four open questions, prepare two
errata candidates for a package it did not touch, and validate the instrument
that the next session will use.

State at open, reported before anything was done: head
`1fd6ecf98d2344b146754e1dabc83758f9e40bde`, the inaugural close, as expected;
working tree clean; twenty-four tracked paths; no remote; the root tree
holding one path; and the preregistration blob identical at the root and at
the head.

---

## Commits

Five commits.

- **Decisions**, `f3f6e07`. `DECISIONS.md`, `NAME-GATE.md`,
  `CONTACT-RULES.md`.
- **Errata candidates**, `666008c`. `ERRATA-CANDIDATES.md`.
- **Validation**, `a6f4026`. `analysis/`, `results/validation.json`,
  `DEFECTS.md`, `FIGURES.jsonl`.
- **Pre publication sweep**, `c5234f8`. `tools/prepublish.py`,
  `PROVENANCE.md`.
- **This report**, which is the fifth and is counted.

Thirty-one tracked paths at the close. Nothing under `vendor/`, and the third
party manifest still records that nothing foreign has entered.

## The four decisions, and what each one did not touch

All four are recorded in `DECISIONS.md` with decider and date.

The name is `walsh-attribution`. Two things were left alone deliberately.
`NAME-GATE.md` keeps its measurement: the declared queries, the limits, the
finding that the old name was occupied by exact string, the verdict, and the
rejected candidate with its reason, none of it rewritten to agree with the
outcome. And `PREREGISTRATION.md` is not amended, so it still opens with the
name it was signed under. That document declared the name provisional and
defined every object extensionally, which is exactly why the rename cost
nothing, and it is why the gate was run before anything was fixed.

English stands. The deflationary expected shape of the lane is accepted as
the intended one, which matters because the signed document can only be
superseded and not edited, so accepting it before the analysis session is
cheaper than after.

The remote is authorised, and could not be attached. See the house procedure
below.

## The two errata candidates, and what they are not

`ERRATA-CANDIDATES.md` holds two entries prepared here and applied nowhere.
The package of the deposit under audit was not touched, no branch of it was
opened, and nothing was written to it. It carries its own errata process at
its deposit tag and these are candidates for it, to be carried there by
Alexis if and when he wants.

Both are about sentences and neither changes a printed number. The first is
that the signal the footnote describes is the inverse of the signal its own
verifier computes at the same tag, and that the literal reading gives a first
order spectrum which cannot produce the printed figure at all. The second is
that one clause names the even interaction orders while the share and the
baseline are both computed over two orders only. Each entry carries the
literal prose with its line, the code with its file and lines, the digests of
both blobs read, and a correction in one sentence.

Neither entry touches the attribution clause. That clause is what this lane
exists to measure and it has not been measured.

## Validation: both routes pass

`results/validation.json` holds the machine record. Seed `21776041`,
validation on stream 2 of 3 in the declared order, so the two null streams
are untouched and V5 checks that spawning the third leaves them identical.

### Route one, against two independently written predicates

The published membership predicate was read at the deposit tag of
`null-ladder` and executed from a scratch file outside this repository, digest
reported in the result file. The predicate of the closed lane was read at its
final head and run alongside it: that is the inheritance `CONTACT-RULES.md`
rule two requires, re-run rather than assumed, because a verification of
another program's output says nothing about this one's.

All two thousand draws satisfy all three predicates. This lane's assembly
agrees with the published assembly on every draw, and the published
decomposition recovers the permutation and the orientation vector this
sampler actually chose, so agreement is not two functions independently
returning true. Three witnesses outside the family are refused by all three
predicates and the positive control inside the family is accepted by all
three.

One asymmetry is recorded rather than glossed: this lane's predicate is
strictly stronger than the published one, because it also requires the
arrangement to be a permutation. On every object tested the two agreed
anyway.

### Route two, against the facts the signed document derived by hand

All four hold, together with the two checks `VALIDATION-PLAN.md` added.

- **V0.** The transform reproduces the exact spectrum of the one input whose
  spectrum is known in closed form: the binary ordering has exactly zero
  energy at orders 2 through 6.
- **V1.** Every one of the two hundred thousand draws from each null carries
  non-DC energy of exactly `1397760`, in integer arithmetic, with no
  exceptions on either side.
- **V2.** The profile by interaction order is identical under all four bit
  conventions, exactly, for the binary ordering and for two thousand free
  draws. This is the branch point of `PREREGISTRATION.md` section (f): it
  held, so the declared test set has seven members and this lane carries one
  convention where a rank based lane would carry four.
- **V3.** The free null reproduces its exact per order means and the exact
  mean of the focal share. The largest deviation at any order is under two
  standard errors and the focal share is at 2.22, inside the declared window
  of four.
- **V4.** The pair preserving family reproduces `45056` at order 6, at 0.25
  standard errors. This is the acceptance test sited deliberately at the one
  interaction order that carries no declared test and on which no conclusion
  of this lane turns, so it cannot have been chosen to flatter the result.
- **V5.** Spawning the validation stream leaves the two null streams
  identical.

### What was deliberately not computed

No aggregate over the focal orders was formed for any draw of the pair
preserving family. `analysis/validate.py` takes the total energy and the
order 6 energy from the coefficients directly, without grouping any other
order, and the function that does so exists for that reason and says so. That
number is the primary result of this lane and belongs to the analysis
session.

## Figure gate

Fifteen records. Three figures are now usable in a commit message and six
remain blocked.

What moved: the uniform expectation the audited footnote prints is
recomputed here as the exact mean under the free null, so its citation is
retired by a record that names exactly what it retired, and the retired
record stays in the file. The two constants this lane had derived by hand and
not executed are retired the same way, and defect three, which was about the
registry having no honest status for that state, is closed by the derivations
becoming measurements rather than by changing the vocabulary.

What did not move: the observed share the footnote prints, and all four
figures of the auditor's unregistered prior exploration, and its draw count.
Every one of them is still refused, because none has been recomputed here.

The gate was exercised in both directions this session. The validation commit
carries three accountable numerals and the gate passed it, naming each as
resolving to an object verified here. Every other commit message of the
session carries none.

## House procedure for the first push

Required by `CONTACT-RULES.md` rule six and by decision two. All three steps
ran and their output is above in the session, reproduced here in substance.

1. **One line log of every commit.** Twelve commits at the time of the run,
   all authored under the git identity `alexcat84`, all on 2026-08-11.
2. **Sweep of every blob of every commit for secrets, tokens and personal
   paths.** Forty-two distinct text blobs scanned. One file allowed by name
   and the reason printed, which is `tools/prepublish.py` itself, since the
   patterns live there. **Zero findings.**
3. **Confirm the remote is empty.** It is not merely empty. It does not
   exist. Neither `github.com/Probatorium/walsh-attribution` nor
   `github.com/theoriginaliching/walsh-attribution` resolves, while other
   repositories under both accounts resolve with the same credentials in the
   same session, so this is the repository being absent and not a
   credentials failure.

**No remote was attached and nothing was pushed.** Decision two says Alexis
creates the repository, so this lane did not create one, and creating one
would have been the opposite of the rule the decision was recorded under. The
push is pending on that single act. The first two steps of the procedure have
passed and would be re-run before the push, since blobs will have been added
by then.

## Dash sweep

- Working tree, every tracked text file: clean.
- Every blob of every commit: clean.
- The single registered exemption is unchanged and unused.

## Untouchable gate

Tree, remotes, config and every blob of every commit: clean. The remote check
is trivially satisfied, since there is no remote.

## Suite

Fifty-six checks, all passing, unchanged from the inaugural session. No test
was added this session, and that is a gap rather than a virtue: the sampler
and the transform are new code and their correctness rests on the validation
run rather than on unit tests. The validation is stronger evidence than unit
tests would be, since it checks exact facts against three independent
predicates and four closed form quantities. It is also a single run rather
than a suite that a later change would re-run automatically. If
`analysis/core.py` changes, the validation must be re-run by hand, and
nothing in this repository currently forces that.

## Defects

Two added, five and six, both in `DEFECTS.md`.

The plan that governs the validation fixed a tolerance and never fixed the
draw counts, so the counts were declared in the code before the run rather
than filled silently into the plan afterwards. And an acceptance test was
briefly written against a bound on its own standard error rather than the
standard error, which widens the window and makes the test easier to pass.
That was caught by reading the code before any result was committed, fixed,
and the run repeated. The two runs draw the same numbers, because the fix
consumes no randomness, and the reported means are identical between them.

Defect three is closed by this session's registrations, as described above.
Defects one, two and four stand as recorded.

## What is pending

**One thing, and it is not a decision.** The repository on the forge does not
exist yet. When it does, the remote is attached, the first two steps of the
house procedure are re-run over the history as it then stands, and the push
follows with its address, visibility, both heads and the confirmation that
the trees are identical.

The next session is the analysis session. It reads the received sequence
under the third party manifest, runs the two preconditions, and then, and
only then, reads the observed value and runs the seven declared tests.

## What is not claimed

That the sampler is uniform on the family. `VALIDATION-PLAN.md` says in
advance what a pass does and does not establish, and the narrow claim is the
one made here: every draw is in the family by three independent predicates,
and six exactly known quantities came out right.

That the four facts derived in section (b) are new. The background review is
still unstarted and no novelty claim is made about anything.

Nothing about design, intention or ancient knowledge, and nothing about the
writer of the audited footnote.
