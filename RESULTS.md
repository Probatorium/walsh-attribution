# Results

One run, at the sample size and the seed `PREREGISTRATION.md` section (f)
fixes, of the design that document signs. Raw output in
`results/measurement.json`. Nothing here was chosen after seeing a figure.

The order in which this happened is part of the result and is recorded in
`EFFORT-LOG.jsonl` with its clock. The signed preregistration was pushed to a
public remote, and the push returned, before the observed value was read. The
validation of the sampler had passed in the previous session and was still
current, which the fifth standing gate checks rather than the author
remembering.

---

## The preconditions of section (d)

**P1 passes.** The adjacency pairing of the received King Wen sequence, the
thirty-two unordered pairs occupying positions one and two, three and four,
and so on, is the same set partition as the matching that pairs each figure
with its 180 degree rotation, and with its complement when the figure is
rotation symmetric. Thirty-two blocks in common out of thirty-two. So the
family this lane samples is the family of the received pairing and of that
matching at once, and the phrase "the pair rule" refers to the same object in
both readings.

**P2 passes.** The focal share recomputed here from the received sequence is
77.4 percent to one decimal, which is the figure the audited footnote prints.
The deposit's number is confirmed, and this is the first thing to say about
it: nothing in what follows is a correction of that figure.

**The constant of (b.1) holds on the received sequence too.** Its non-DC
Walsh energy is 1397760, the value every arrangement of sixty-four
consecutive integers must have.

---

## The primary report: the whole profile, orders 1 to 6

Shares of non-DC Walsh energy. The pair preserving family is `N1`, the free
null is `N0`, and each percentile is the fraction of draws strictly below the
observed value.

| order | observed | `N1` mean | `N1` sd | percentile in `N1` | `N0` mean | percentile in `N0` |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 0.041392 | 0.072465 | 0.054617 | 34.708 | 0.095191 | 13.310 |
| 2 | 0.502999 | 0.290338 | 0.111918 | 95.966 | 0.237951 | 99.882 |
| 3 | 0.142811 | 0.242176 | 0.095472 | 14.674 | 0.317537 | 0.832 |
| 4 | 0.271314 | 0.290312 | 0.111585 | 46.605 | 0.238331 | 68.694 |
| 5 | 0.041300 | 0.072624 | 0.054717 | 34.410 | 0.095159 | 13.289 |
| 6 | 0.000183 | 0.032086 | 0.044188 | 4.479 | 0.015832 | 8.000 |

The profile is the primary report because the focal orders were selected by
inspection in earlier work, and section (c) fixed in advance that every order
would be reported whatever it showed. It shows something the focal pair
conceals, and this is a description of the table rather than a test:

**the concentration sits at order 2, not across orders 2 and 4.** The
observed share at order 2 is above its family mean and sits at the 95.966
percentile of the family. The observed share at order 4 is slightly below its
family mean and sits at the 46.605 percentile, which is an ordinary place for
it to be. A statistic that adds the two carries one order that is far up its
family and one that is where the family puts it.

That observation has its own section below, which gives its uncorrected p,
records that it does not survive the correction this document's design fixes,
and states why this lane records it and stops there.

The share at orders 2, 4 and 6 together, the reading that "even interaction
orders" would name literally, is recoverable from this table by adding three
numbers, and section (c) fixed in advance that it would be reported and never
promoted. It is 0.774496, which differs from the focal statistic by the
0.000183 at order 6.

---

## The focal statistic

| quantity | value |
| --- | --- |
| observed share at orders 2 and 4 | 0.774313 |
| mean under the pair preserving family | 0.580650 |
| standard deviation under that family | 0.115773 |
| percentile of the observed in that family | 95.535 |
| mean under the free null, exact by (b.3) | 0.476190 |
| percentile of the observed in the free null | 99.980 |

The free null column is descriptive. `N0` carries no test, is excluded from
the correction, and is here to provide the baseline the attribution is
measured from, which section (b.3) derives exactly and the validation of the
previous session confirmed.

---

## The attribution, which is the primary quantity of section (d)

The decomposition is a definition fixed in the signed document before
anything was measured, not a choice made afterwards among defensible ones.

| quantity | value |
| --- | --- |
| excess, observed minus the free null mean | 0.298123 |
| explained, pair family mean minus the free null mean | 0.104460 |
| residual, observed minus the pair family mean | 0.193663 |
| **A**, the share of the excess the pair rule accounts for | **0.3504**, interval 0.3487 to 0.3521 |
| **R**, the share it does not | **0.6496**, interval 0.6479 to 0.6513 |

The ratios are reported because the excess is far more than four Monte Carlo
standard errors from zero, which is the admissibility rule section (d) fixed
in advance. The intervals are Monte Carlo error on the family mean and
nothing else: the free null mean is exact and the observed value is a
constant of the received sequence, so the family mean is the only quantity
here carrying simulation error. They are not confidence intervals for a
population parameter and nothing in this lane treats them as such.

**In words.** Conditioning on the pair rule moves the expected share from
0.476190 to 0.580650. The observed share is 0.774313. So the pair rule
accounts for about a third of the distance from uniformity to what was
observed, and about two thirds of that distance is not accounted for by it.

---

## The seven declared tests

All under the pair preserving null, tails fixed in section (e) before
anything was measured, Holm step down at a family wise level of 0.05 over the
seven, as section (f) fixes.

| test | statistic | tail | raw p | adjusted p |
| --- | --- | --- | ---: | ---: |
| T0 | share at orders 2 and 4 | one sided, upper | 0.044655 | 0.312583 |
| T1 | share at order 1 | two sided | 0.584892 | 1.000000 |
| T2 | share at order 2 | two sided | 0.049820 | 0.312583 |
| T3 | share at order 3 | two sided | 0.299649 | 1.000000 |
| T4 | share at order 4 | two sided | 0.872436 | 1.000000 |
| T5 | share at order 5 | two sided | 0.580282 | 1.000000 |
| T6 | share at order 6 | two sided | 0.232134 | 1.000000 |

Two raw values sit just below 0.05 and both are reported at full precision
rather than described. The correction is what the signed document says the
criterion is read on, it was fixed before the numbers existed, and the
seven-member test set was fixed by a verification with a determinate answer,
namely the convention invariance of (b.2), which held.

The one sided direction of T0 was chosen in knowledge of a prior exploration,
and `PREREGISTRATION.md` section 0 declares that prior and that choice. This
is a confirmatory measurement with a declared prior. It is not blind.

---

## The signed criterion, and which branch was met

`PREREGISTRATION.md` section (e):

> `H_resid` is **refuted** if every one of the seven declared tests, after the
> Holm correction of section (f), yields an adjusted p of at least 0.05.

**That branch was met. `H_resid` is refuted.** Every adjusted p is at least
0.05 and the smallest of them is 0.312583.

`H_resid` was: once the pair rule is held fixed, the observed concentration of
Walsh energy is still atypical. It is refuted in the sense the document
defines and in no other.

The same document, in the same section, wrote in advance what this outcome
would mean and what it would not, so that neither could be improved after the
fact:

> If the point estimate of `A` comes out well below one while `H_resid` is
> refuted, the only reading this lane is permitted is the one written here in
> advance: the pair rule accounts for part of the distance from uniformity,
> and what remains is not distinguishable from ordinary variation inside the
> pair preserving family at this sample size under this correction. A
> refutation of `H_resid` does not make the residual zero, and this document
> will not be read as saying so. Equally, a residual with a large point
> estimate is not evidence of anything further merely because it is large.

That is the reading, and this lane holds to it. The residual is about two
thirds of the excess by magnitude, and the observed value is at the 95.535th
percentile of the family, which is a place inside the family rather than
outside it.

Section (e) also predicted the outcome, before the run: refutation was
reachable and expected, survival would have had to come from a per order test
rather than from the focal one, and raising the sample size could not have
moved it. All three held.

---

## The order 2 observation, and why this lane stops at recording it

### What the profile shows

The observed share at interaction order 2 is 0.502999, against a pair
preserving family mean of 0.290338, and it sits at the 95.966 percentile of
that family. The observed share at order 4 is 0.271314, against a family mean
of 0.290312, and it sits at the 46.605 percentile, which is an ordinary place
in the family. The focal statistic adds one of each.

### What the declared test says about it

Order 2 carries T2, one of the seven declared tests, two sided as fixed in
section (e). Its uncorrected p is 0.049820. **It does not survive the
correction the signed document fixes.** Its adjusted p is 0.312583, which is
also the smallest adjusted p in the whole set, and the criterion of section
(e) is read on adjusted values. So this observation changed nothing about the
verdict and is not offered as changing anything.

Both numbers are printed here at full precision rather than described,
because an uncorrected p just under a threshold is exactly the quantity that
prose can be made to carry further than it should.

### Why this lane does not isolate it

Two reasons, and each is sufficient on its own.

**Isolating it now would be choosing the question after seeing the answer.**
Section (c) of the signed document exists because the focal orders had
already been selected by inspection once, in earlier work, and the whole
apparatus of this lane is built to stop that happening twice. A test of order
2 alone, specified after order 2 was seen to be the interesting one, is the
same act that section (c) was written to prevent. The full profile was
reported precisely so that this observation would be visible without being
promoted, and promoting it now would spend the protection that made it
visible.

**There is no independent sample to test it on.** The King Wen sequence is
one object. There is no second sequence, no held out half, and no future
data: whatever is done with this observation would be done on the same
sixty-four positions that produced it. That is not a limitation of this
lane's design. It is a property of the object, and it is permanent.

### Its status, which is final rather than deferred

This is an observation, recorded so that a reader has it. **It is not future
work and this lane does not list it as such.** A lane that ends by naming a
promising direction it discovered in its own data has, in effect, published a
hypothesis it selected after seeing the answer and left someone else to pay
for it.

If anyone does pursue it, the honest form is a preregistration written before
looking at this table, on an object where the answer is not already known,
and this lane makes no claim about what such a study would find. Nothing here
is evidence for a hypothesis about order 2. It is a description of one column
of one table.

---

## What this says about the audited footnote

The footnote says the King Wen Walsh spectrum concentrates a share of its
energy in the named interaction orders "against 47.6 percent expected for
orders {2,4} under uniformity, a spectral confirmation of the pair rule."

Three statements, in the order the measurement settles them.

1. **Its two figures are right.** The share recomputed here is the printed
   one to one decimal, and the baseline is not merely close to the printed
   figure but exactly 30/63 under the free null, which the previous session
   confirmed against a derivation made before any of it was run.
2. **The pair rule does move the baseline, and by a lot in absolute terms.**
   Conditioning on it raises the expected share by 0.104460. An attribution
   to the pair rule is not an attribution to nothing.
3. **It does not account for most of the gap it is offered as the
   explanation of.** About 0.35 of the excess over uniformity is attributable
   to the pair rule under the definition fixed in section (d), and about 0.65
   is not. The comparison the footnote makes is between the observed value and
   uniformity, and a comparison against uniformity cannot separate those two
   parts. Separating them is what this lane was for.

What the measurement does not support is reading the residual as anything
further. It is not distinguishable from ordinary variation inside the family
under the declared correction, and the signed document forbade dressing it up
in advance.

---

## What is not claimed

Nothing about design, intention, purpose or awareness. Nothing about whether
the makers of the sequence possessed or lacked any mathematical knowledge.
Nothing about the meaning, authenticity, antiquity or authority of the
sequence or of any text. Nothing about any person, including the writer of
the audited footnote, who is the author of this lane.

No claim of novelty about anything, including the four exact facts derived in
section (b), because the background review of this lane has not been opened.

The object of study is a permutation of sixty-four objects, a function on the
six dimensional Boolean cube built from it, and the energy of that function
in a fixed basis. The results speak about that object and about the two
families of section (d), and about nothing else.
