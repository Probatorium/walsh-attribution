# Validation of the sampler and of the transform, declared before either runs

`PREREGISTRATION.md` section (f) makes this validation a precondition: the
sampler must pass both routes before any p-value or any percentile is read,
and if the two routes disagree the run stops and the disagreement is the
result.

This document fixes what the two routes are, what each one checks, what
counts as a pass, and what counts as a disagreement. It is written in the
inaugural session, before any sampler exists in this repository, so that no
acceptance test can be chosen after seeing what the sampler produces.

Nothing in this document has been run.

---

## The order of operations, fixed here

1. Validate the transform against exact facts on known inputs. Route two,
   part one.
2. Validate the sampler against the published predicate. Route one.
3. Validate the sampler against exact facts about its own output law. Route
   two, part two.
4. Only then read the received sequence, run the preconditions of section
   (d), and read the observed statistic.
5. Only then run the declared tests.

The received sequence is not read at steps one to three. Every check below
that could otherwise be applied to it is applied to draws and to synthetic
inputs, and the corresponding check on the received sequence happens at step
four as part of the preconditions. This ordering exists so that no acceptance
threshold can be nudged by having already seen the number the lane is about
to report.

---

## Route one: against the published predicate of the family

The family `N1` of `PREREGISTRATION.md` section (d) is the pair preserving
null published as rung P1 of a deposited ladder. That deposit carries its own
membership predicate, written from its own printed definition, and it is read
only at its deposit tag under `CONTACT-RULES.md` rule four.

- **Source**: `null-ladder`, tag `zenodo-10.5281-zenodo.21750029`, file
  `ladder_containment.py`, symbols `in_P1`, `assemble` and `decompose`.
- **How it is executed**: the blob is read at the tag through git, written to
  a scratch file outside this repository, and imported from there. Nothing
  read enters this history. The SHA-256 of exactly what was executed is
  reported with the result, so a later run can tell whether it ran the same
  bytes.

### The checks

1. Every draw of this lane's sampler satisfies the published predicate.
2. Every draw satisfies this lane's own membership predicate, which is
   written independently from the definition in `PREREGISTRATION.md` section
   (d) and not from the published one. That independence is what makes
   agreement evidence rather than tautology.
3. The two predicates agree draw for draw, not merely in aggregate.
4. The published decomposition recovers the pair permutation and the
   orientation vector that this sampler actually chose, so that agreement is
   not an accident of two functions both returning true.
5. Witnesses outside the family are refused by both predicates, and at least
   one witness inside the family is accepted by both. The witnesses are fixed
   here: one hexagram exchanged across two pairs; the whole arrangement
   rotated by one position; a free shuffle of all sixty-four positions; and,
   as the positive control, a within pair flip, which is in the family and
   must be accepted.

A pass requires every check, at every draw. One disagreement is a failure.

---

## Route two: against facts derived before anything was run

The four facts are derived in `PREREGISTRATION.md` sections (b.1) to (b.4).
They were derived by hand, they are unverified computationally, and they were
written into a signed document precisely so that they can fail visibly.

### V0, the transform, on an input whose spectrum is known exactly

Under the single order signal, the binary ordering gives `f(v) = v + 1`,
which is an affine function of the six coordinate functions and therefore a
combination of the constant character and the six characters of order 1
alone. Every coefficient at order 2 and above is exactly zero.

- **Check**: for the binary ordering, all non-DC energy lies at order 1, and
  the energy at orders 2 to 6 is exactly zero.
- **Tolerance**: none. Exact integer arithmetic, exact zero.
- **Why this check first**: it exercises the transform without exercising the
  sampler, so a failure here localises immediately. It also uses no draw and
  no received data.

### V1, the constant denominator, from (b.1)

- **Check**: the non-DC energy of every draw, from both nulls, equals
  `1397760` exactly.
- **Tolerance**: none. Exact integer arithmetic on integer valued signals.
- **On failure**: stop. Either the transform or the signal construction is
  wrong, and no quantity computed from either can be trusted.
- **The corresponding check on the received sequence** runs at step four, not
  here.

### V2, the convention invariance, from (b.2)

- **Check**: the unnormalised energy at each interaction order is identical
  under all four bit conventions, for a batch of draws and for the binary
  ordering.
- **Tolerance**: none. Exact equality of integers.
- **On failure**: this is the one failure in this document that is not a
  stop. `PREREGISTRATION.md` section (f) fixes the branch in advance: all
  four conventions are carried and the declared test set has twenty-eight
  members instead of seven. The failure is also recorded in `DEFECTS.md` as a
  wrong prediction in a signed document, because that is what it would be.

### V3, the free null mean, from (b.3)

- **Check**: over the declared draws from `N0`, the sample mean of the focal
  share agrees with `30/63`, and the sample mean of the share at each order
  `k` agrees with `C(6,k)/63`.
- **Tolerance**: four standard errors of the sample mean, the standard error
  taken from the sample's own dispersion. Fixed here, before the run.
- **On failure**: stop.
- **What this also settles**: the deposit's printed baseline. If V3 passes,
  the figure the footnote gives as "expected under uniformity" is confirmed
  here as the exact mean of this statistic under `N0`, and the corresponding
  registry record moves from cited-unverified to superseded.

### V4, the pair preserving mean at order 6, from (b.4)

- **Check**: over the declared draws from `N1`, the sample mean of the
  unnormalised energy at order 6 agrees with `45056`, and equivalently the
  sample mean of the share at order 6 agrees with `44/1365`.
- **Tolerance**: four standard errors of the sample mean, the standard error
  taken from the sample's own dispersion. Fixed here, before the run.
- **On failure**: stop.
- **Why order 6 and not the focal orders**: an acceptance test sited on
  orders 2 or 4 could be tuned, consciously or not, to flatter the number
  this lane exists to report. Order 6 carries no test in section (e) and no
  conclusion of this lane turns on it, so it cannot be. The reasoning is in
  `PREREGISTRATION.md` (b.4) and is repeated here because it is the reason
  this check is worth having at all.

### V5, stream independence

Section (f) declares three streams spawned from one seed sequence, in a fixed
order. Spawning the third must leave the first two unchanged.

- **Check**: the first draws of the two null streams are identical whether
  two streams are spawned or three.
- **Tolerance**: none. Exact equality.
- **On failure**: stop. The declared seed would not mean what the signed
  document says it means.

---

## What counts as a disagreement between the routes

The two routes check different things and cannot contradict each other
directly. The disagreement the preregistration is guarding against is this:
one route passing while the other fails, on the same sampler, in the same
run. Concretely, either of these is a stop:

- Route one passes and any of V1, V3, V4 or V5 fails. The draws are members
  of the family and their law is not what the family's law is, which means
  the sampler is not uniform on it.
- Route two passes and route one fails. The draws have the right moments and
  are not members of the family, which is the more dangerous of the two
  because the moments are the thing a careless run would check.

In either case the run stops, no observed value is read, and the failure is
the reported result of the session.

---

## Inheritance from the closed lane, item by item

`CONTACT-RULES.md` rule two requires that the verifications of the closed
lane be inherited where they transfer and that the reason be declared where
they do not. This is that accounting.

### Inherited in design, re-run in execution

**The shape of route one.** Handing every draw to a published predicate,
checking it against an independently written one, checking the round trip
through the published decomposition, and using witnesses on both sides of the
boundary: that design is taken from the closed lane and is not reinvented
here.

It is re-run rather than inherited as a result. That lane validated its own
sampler. This lane's sampler is different code, written for the opposite
direction of the same map, as `PROVENANCE.md` explains. A verification of
another program's output says nothing about this one's, and treating it as if
it did would be exactly the failure mode that makes reuse dangerous.

### Not inherited, with the reason

- **That lane's analytic acceptance test.** It checked the exact mean of a
  discordance count over the same family. That is a different functional of
  the same distribution, and a sampler can reproduce the mean of one linear
  functional and be wrong for another. It transfers nothing to a spectral
  statistic, which is why this lane derived its own facts in
  `PREREGISTRATION.md` section (b) rather than leaning on that one.
- **That lane's membership predicate.** This lane writes its own from its own
  signed definition. Reusing that lane's predicate would make check two of
  route one agree with check one by construction, and an agreement that
  cannot fail is not evidence.
- **That lane's Monte Carlo results, figures, conventions and percentiles.**
  None of them is about this statistic, and none of them enters here as
  established. The figure gate holds this rule mechanically for anything that
  reaches a commit message.

---

## What this validation does not establish, declared

- **That the sampler is uniform on the family.** It establishes that every
  draw is in the family, and that four exactly known quantities come out
  right. A sampler can pass all of that and still be non uniform in some
  direction none of these functionals sees. The claim made after a pass is
  the narrow one: the declared checks passed.
- **That the received sequence is correct.** It is received data under
  `CONTACT-RULES.md` rule seven, it is never recomputed here, and no check in
  this document bears on it.
- **That the deposit's implementation is correct.** This lane audits the
  attribution the footnote makes, not the code that produced its figure. If
  precondition P2 finds a disagreement between the printed figure and the one
  recomputed here, that is reported as a finding about the deposit, and it is
  a finding about a number, not an audit of a program.
