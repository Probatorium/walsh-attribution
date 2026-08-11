# Closing act

Decision by Alexis Garcia Hurtado, 2026-08-11: this lane closes, and it does
not deposit.

This file records what was asked, what was preregistered, the order in which
the seal and the measurement happened, what was measured, which branch of the
signed criterion was met, why nothing is deposited, and why the background
review is deliberately left unopened. It records nothing else.

---

## What was asked

The deposit `10.5281/zenodo.21776041` publishes, in a footnote to its
spectral section, a figure and an attribution: that the Walsh spectrum of the
King Wen ordering concentrates a share of its energy in the named interaction
orders, "against 47.6 percent expected for orders $\{2,4\}$ under uniformity,
a spectral confirmation of the pair rule."

The question of this lane, from `PREREGISTRATION.md` section (a):

> Of the concentration of Walsh energy that the King Wen sequence shows in the
> focal interaction orders, how much is accounted for by the pair rule alone,
> and how much remains once the pair rule is held fixed?

The deposit is by the same author as this lane. That is declared in section 0
of the signed document and this is a self audit.

## What was preregistered, and where its signature is

`PREREGISTRATION.md` is the entire content of the root commit of this
repository:

| | |
| --- | --- |
| root commit | `d385f920161b632154c0daa1344db2d02cc272a7` |
| date | 2026-08-11 |
| blob of the document at the root | `662a730e614c6d54383e09cc189d58292036d16b` |
| blob of the document at the head | the same |
| commits in this history that have ever touched that path | one, the root |

It fixes the signal and the bit convention, both quoted from the deposit at
its tag; the selection bias that produced the focal orders and the reporting
rule that answers it; the two nulls; the attribution as the primary quantity
and the admissibility rule for its ratios; the seven declared tests and their
tails; the refutation criterion, checked for failability in both directions
before signing; the Holm correction; the sample size; the seed; and what this
lane would not claim whatever it found.

It was never amended. Four analytic facts it derives by hand were later
confirmed by a validated sampler. One sentence of its signature is wrong, is
recorded as defect one of `DEFECTS.md`, and was corrected forward rather than
edited.

## The order of the seal and the measurement, verified

The value of a preregistration is the value of its timestamp, and a timestamp
that exists only on the machine that wrote it is worth nothing to a reader.
So the signed document went to a public remote before the measurement it
governs, and both events carry their clock in `EFFORT-LOG.jsonl`.

| clock, UTC, 2026-08-11 | event |
| --- | --- |
| 22:34:51 | house procedure begun over the history as it then stood |
| 22:35:04 | push begun |
| 22:35:06 | push returned, remote head equal to local head, trees identical |
| 22:41:14 | received sequence transcribed into this repository, and the analysis run |

Before 22:35:06 there was no code path by which the observed value could have
been read. No file in this repository held the received sequence, `data/` did
not exist, and the tool that transcribes it had not been written. That is
checkable from the history rather than asserted here.

The remote is `https://github.com/Probatorium/walsh-attribution`, public.

## What was measured, and what came out

One run, at the sample size and seed the signed document fixes, on a sampler
validated by two independent routes in the previous session and confirmed
still current by a standing gate at the moment of the run.

**Both preconditions passed.** The received adjacency pairing is the rotation
and complementation matching, thirty-two blocks of thirty-two. The focal
share recomputed here is 77.4 percent to one decimal, the figure the audited
footnote prints. Nothing in this lane corrects that figure.

**The attribution, the primary quantity:**

| quantity | value |
| --- | --- |
| observed focal share | 0.774313 |
| mean under the pair preserving family | 0.580650 |
| mean under uniformity, exact | 0.476190 |
| excess over uniformity | 0.298123 |
| the part the pair rule accounts for | 0.104460 |
| the part it does not | 0.193663 |
| share of the excess attributable to the pair rule | 0.3504 |
| share not attributable to it | 0.6496 |

**The full profile by interaction order is the primary report** and is in
`RESULTS.md`. It shows what the focal statistic conceals: the concentration
sits at order 2, at the 95.966 percentile of the family, while order 4 is
slightly below its own family mean at the 46.605 percentile. That observation
has its own section there, with its uncorrected p, with the adjusted p the
criterion is read on, and with the two reasons this lane records it and stops:
isolating it now would be choosing the question after seeing the answer, and
the sequence is one object with no independent sample to test it on. It is
recorded as a permanent observation and explicitly not as future work.

## Which branch of the criterion was met

`PREREGISTRATION.md` section (e):

> `H_resid` is **refuted** if every one of the seven declared tests, after the
> Holm correction of section (f), yields an adjusted p of at least 0.05.

**That branch was met. `H_resid` is refuted.** Every adjusted p is at least
0.05 and the smallest is 0.312583. The observed value sits at the 95.535
percentile of the pair preserving family, which is a place inside the family.

The same section wrote the reading of this outcome in advance, so that it
could not be improved afterwards: the pair rule accounts for part of the
distance from uniformity, what remains is not distinguishable from ordinary
variation inside the family at this sample size under this correction, a
refutation does not make the residual zero, and a residual is not evidence of
anything further merely because it is large. That is the reading this lane
holds to.

Section (e) also predicted, before the run, that refutation was reachable and
expected, that survival would have had to come from a per order test rather
than the focal one, and that raising the sample size could not have moved it.
All three held.

## Why nothing is deposited

**The result refines the reading of a footnote in an earlier work by the same
author, and the place for that is that work's errata, not a new deposit.**

What this lane produced is three things, and none of them is a paper.

1. Two figures of the audited footnote confirmed rather than corrected.
2. A quantity the footnote's own comparison cannot contain, because a
   comparison against uniformity cannot separate what the pair rule
   contributes from what it does not.
3. Three errata candidates, in `ERRATA-CANDIDATES.md`, prepared here and
   applied nowhere: two about prose that does not match the code at the same
   tag, and one about the attribution clause, each with the literal prose,
   the pointer into the source, and a correction in one sentence.

A deposit would publish, as a separate work, a refinement of one clause of
one footnote of an existing deposit by the same author. It would fragment the
record rather than fix it. The errata process of that package exists, it
carries an `ERRATA.md` at its deposit tag, and it is where a reader of that
footnote would look. This repository is public and permanent and can be
cited from there.

Nothing in the audited package was touched by this lane, no branch of it was
opened, and nothing was written to it, which `CONTACT-RULES.md` rule one
requires and `PREREGISTRATION.md` section (g) requires again for exactly the
case where a lane concludes against a footnote.

## Why the background review is left unopened, on purpose

It was never opened. `BACKGROUND-REVIEW.md` has said so since the inaugural
session and still says so, and the ban on novelty claims that follows from it
was written into the signed document rather than into an intention.

**It is not needed, because this lane claims novelty of nothing.** It
measures its own author's published work and prepares corrections to it.
Every object it uses comes from a deposit it cites; the four analytic facts
it derives in section (b) are elementary and are claimed as acceptance tests
rather than as results; and the closing act is an errata candidate, not a
contribution.

A background review is what a lane owes a reader when it says something is
new. This lane says nothing is new. Opening a review in order to confirm that
would be work performed to license a claim that is not being made.

If any figure or fact of this lane were ever carried into a work that does
claim novelty, that work owes the review, and this file is not a substitute
for it.

## What may be said about this repository elsewhere

That it is a preregistered self audit of one footnote, whose signed design
was public before its measurement, and whose result is that the pair rule
accounts for about a third of the excess the footnote attributes to it, with
the remainder not distinguishable from ordinary variation inside the pair
preserving family under the correction declared in advance.

That the observed value and the printed figures of the footnote agree.

Nothing about design, intention, purpose or awareness. Nothing about the
makers of the sequence or their knowledge. Nothing about the meaning,
authenticity, antiquity or authority of the sequence or of any text. Nothing
about any person, including the writer of the audited footnote.
