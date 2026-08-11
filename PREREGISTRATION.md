# Preregistration

Repository: spectral-attribution
Date of signing: 2026-08-11
Author: Alexis Garcia Hurtado
Status: signed at the root commit, before any quantity of either null family
was computed and before the received sequence was read into this repository

This document is the entire content of the root commit of this repository.
It is signed by that commit. It is not amended. If a part of it turns out to
be badly posed, the defect is declared in a later commit and corrected
forward, leaving this text intact and the defect on the record.

---

## 0. Standing of this document

### What is audited

The deposit `10.5281/zenodo.21776041`, the version whose concept DOI is
`10.5281/zenodo.21609653`, "Statistical Structure of the Historical Orderings
of the I Ching Hexagrams: Pair Rule, Family Gradient, and the Limits of
Demonstrability" (Garcia Hurtado, 2026), publishes in a footnote to its
spectral section a figure and an attribution. The figure is a share of Walsh
energy. The attribution is the clause "a spectral confirmation of the pair
rule".

This lane asks whether that attribution is correct: how much of the reported
concentration the pair rule accounts for, and how much it does not.

The deposit is frozen. Nothing in it is edited, extended or corrected from
here. It is cited, and it is read only at its deposit tag, under
`CONTACT-RULES.md`.

### This is a self audit, and that is declared

The author of the deposit under audit and the author of this lane are the
same person. Nothing about the design below is changed by that fact, and the
fact is stated here rather than left for a reader to notice. The specific
risk it creates is the one this document is built against: an author auditing
his own footnote has an interest in the outcome in both directions, and the
protection is that the design, the tests, their tails, the sample size, the
seed and the refutation criterion are all fixed in this signed text before
anything is measured.

### The prior that exists and biases this lane, declared

Before this repository was opened, and outside any preregistration, an
exploration was run. It drew 2000 members of the family that preserves the
King Wen pairs, computed the share of non-DC Walsh energy in the focal
interaction orders for each, and reported:

| quantity | value |
| --- | --- |
| mean of the family | 0.5786 |
| standard deviation of the family | 0.1170 |
| observed value | 0.7743 |
| percentile of the observed value in the family | 96.1 |

That exploration was not preregistered, its draw count was small, and it is
not a result of this repository. It is written here because it exists and
because it biases everything that follows. Three consequences are binding:

1. **This measurement is confirmatory with a declared prior. It is not blind
   exploration, and this document says so.** The direction of the focal test
   in section (e) is one sided upward, and it is one sided *because* the
   prior above says which way the observed value lies. A one sided test
   chosen in knowledge of the data it will be applied to is only defensible
   if that knowledge is declared in advance of the confirmatory run. It is
   declared here.
2. **No figure above is inherited as established.** Every one of them enters
   `FIGURES.jsonl` as cited-unverified and may not appear in a commit message
   of this repository, nor be asserted in any artefact here, until an
   artefact in this repository has produced it. The same applies to the two
   figures the deposit's footnote prints.
3. **The sample size in section (f) is fixed by this document and is not
   chosen to move a p-value across a threshold.** It is larger than the
   exploration's by two orders of magnitude, and section (e) states, before
   the run, what the larger sample is and is not expected to change.

### What has not begun

The background review of this lane has not been opened. Until it is opened
and closed, this repository asserts the novelty of nothing.

The name `spectral-attribution` is provisional. The term gate was run before
this commit; its declared queries and its outcome are recorded in
`NAME-GATE.md`, committed after `CONTACT-RULES.md`. Nothing in the design
below depends on the name.

---

## (a) The question, in one sentence

Of the concentration of Walsh energy that the King Wen sequence shows in the
focal interaction orders, how much is accounted for by the pair rule alone,
and how much remains once the pair rule is held fixed?

---

## (b) The signal and the convention, declared before anything is computed

### The footnote, quoted literally

From `kingwen-orderings-replication` at tag `zenodo-v3`, file `paper.tex`,
the footnote attached to the opening paragraph of the section "Spectral
portraits of the five orderings". The blob read is
`35995cfd212cc0e632457e589b0cb1769363a94c`, whose contents digest to SHA-256
`9980aa69860dd1253f87180fcfbb305c36a8924886e3c7efb97bc71961b62d55`. Quoted
in full, with the source's own mathematical markup left as it stands:

> This convention necessarily differs from the natural single-order signal,
> position maps to King Wen number, used when analyzing the King Wen sequence
> alone; with that signal, the Walsh spectrum of the King Wen ordering
> concentrates 77.4 percent of its energy in even interaction orders, against
> 47.6 percent expected for orders $\{2,4\}$ under uniformity, a spectral
> confirmation of the pair rule. Both conventions are declared and asserted
> separately.

### The bit convention, quoted from the same source and adopted here

From the header of `verify_paper.py` at the same tag:

> Lines are numbered 1 (bottom) to 6 (top); yang = 1, yin = 0. A hexagram is
> the 6-bit integer whose most significant bit is line 1, so Kun = 0 and Qian
> = 63.

This lane adopts that convention and names it: bottom line most significant,
solid line as one. It is fixed here. Section (b.2) below states, and section
(f) makes contingent on a verification, the reason this lane carries one
convention where a rank based lane would have to carry four.

### The signal, stated as this lane will implement it

Let `V` be the sixty-four hexagrams, identified with the group `(Z/2)^6` by
the convention just quoted. For an ordering `S` of the sixty-four hexagrams,
the single order signal is the function

    f_S : V -> R,    f_S(v) = 1 + (the position of v in S)

so that `f_S(v)` is the King Wen number of `v` when `S` is the King Wen
sequence. The Walsh coefficient at character `w` in `V` is

    c_w(S) = sum over v in V of f_S(v) * (-1)^popcount(w AND v)

the interaction order of `w` is `popcount(w)`, the energy at order `k` is the
sum of `c_w(S)^2` over the characters of that order, and the reported share
at order `k` is that energy divided by the total energy over all characters
except `w = 0`.

### A discrepancy in the footnote's own prose, declared now rather than found later

The footnote describes the signal as "position maps to King Wen number". Read
literally, and applied to the King Wen ordering, that map is the identity: it
sends position `k` to `k + 1`, its Walsh spectrum is a pure first order tone,
and it could not produce the reported figure. The deposit's own verifier at
the same tag does what is written above instead: it indexes the character by
the hexagram and takes the King Wen number as the value.

This lane adopts the implementation, not the prose, and records the
discrepancy here, before measuring, so that it cannot later be presented as a
discovery of this lane's own analysis. The prose of a footnote is loose; the
code at the same tag is not. Which of the two a reader takes to be the
definition changes the answer completely, so the choice is made in writing
and in advance.

### Which orders the footnote means, and why this document fixes the set now

The footnote says "even interaction orders" and then names `{2,4}` in the
same sentence for its baseline. Those are different sets: the even orders are
2, 4 and 6. The arithmetic settles which one the printed baseline belongs to.
There are `C(6,k)` characters of order `k`, so among the sixty-three
characters other than `w = 0` there are 6, 15, 20, 15, 6 and 1 at orders 1 to
6. Orders 2 and 4 hold 30 of the 63, and `30 / 63` is `0.476190...`; the even
orders hold 31 of the 63, and `31 / 63` is `0.492063...`. The printed
baseline is the first.

The focal set of this lane is therefore `{2,4}`, fixed here. The set
`{2,4,6}` is reported as a declared secondary in the full profile of section
(c), and it is not permitted to become the headline of this lane whatever it
turns out to be.

### Three analytic facts, derived by hand before signing and stated so they can fail

These are predictions, not results. Each is derived below in a form a reader
can check. None has been verified computationally at the time of this commit.
They are written here so that if one of them is wrong, the failure is visible
against a prior commitment and is recorded as a defect rather than absorbed.

**(b.1) The denominator is a constant, not a random quantity.** For any
bijection `f` from `V` onto sixty-four consecutive integers, Parseval for the
unnormalised Walsh transform on sixty-four points gives

    sum over all w of c_w^2 = 64 * sum over v of f(v)^2

and `c_0 = sum over v of f(v)`. With the values 1 to 64, the sum of squares
is 89440 and the sum is 2080, so the total is `64 * 89440 = 5724160`, the DC
term is `2080^2 = 4326400`, and

    non-DC energy = 5724160 - 4326400 = 1397760

for every arrangement, without exception. Adding a constant to `f` changes
only `c_0`, so the same value follows from the 0 to 63 labelling: `64 * 85344
- 2016^2 = 1397760`. Two consequences are used below. The share at any order
is a linear function of the unnormalised energy at that order, so the
statistic has no random denominator; and the observed non-DC energy is an
exact integer that every draw and the received sequence alike must reproduce,
which makes it the cheapest possible check that the transform is implemented
correctly.

**(b.2) The profile by order does not depend on which of the four bit
conventions is used.** A convention is fixed by two choices: which end of the
figure carries the most significant bit, and which line type is one.
Reversing the bit order is a permutation of the coordinates of the cube; if
`pi` is that permutation then `c_w` becomes `c_pi(w)`, and `popcount` is
invariant under a coordinate permutation, so the energies are permuted within
each order and the total at each order is unchanged. Exchanging the meaning
of the line types replaces `v` by `v XOR 63`, which multiplies `c_w` by
`(-1)^popcount(w)`, leaving every `c_w^2` untouched. Hence all four
conventions give the same profile by interaction order.

The consequence for this lane is a simplification the rank based question did
not permit: one convention, not four, and no convention multiplicity in
section (f). The prediction is verified computationally before it is relied
on, and section (f) fixes what happens to the multiplicity if it fails.

**(b.3) Under the free null the mean of the focal statistic is exactly
`30/63`.** Under a uniform random bijection from `V` onto the sixty-four
values, and for any character `w` other than 0, the sign pattern of `w` is
balanced, with thirty-two values of each sign; any two balanced patterns
differ by a permutation of the domain; and the law of `f` is invariant under
permutations of the domain. So `c_w^2` has the same expectation for every `w`
other than 0. With (b.1) the total is fixed at 1397760, so

    E[energy at order k] = C(6,k) / 63 * 1397760

exactly, and since the denominator is constant the expectation of the share
is exact too:

    E[share at orders 2 and 4 under the free null] = 30/63 = 10/21

which is `0.476190...`. The deposit's baseline is therefore not an
approximation and not a simulation estimate: it is the exact mean of this
statistic under uniformity. This lane will still estimate it by simulation,
as an acceptance test of the free null sampler against a number fixed in
advance.

**(b.4) Under the pair preserving family the mean of the order 6 energy is
exactly 45056.** The single character of order 6 is `w = 63`, and
`(-1)^popcount(63 AND v)` is the parity of the weight of `v`. Every block of
the pairing has constant weight parity: reversal of a figure preserves its
weight, and complementation of a six line figure sends weight `k` to `6 - k`,
which has the same parity. There are thirty-two hexagrams of even weight, so
sixteen blocks are even and sixteen are odd, and the signs sum to zero over
blocks. Because the character is constant on each block, the orientation
inside a block cannot change the coefficient at all, and with the block at
slot `j` occupying positions `2j` and `2j+1`, the block contributes
`chi(b) * (4j + 1)`. Hence

    c_63 = 4 * sum over blocks b of chi(b) * sigma(b)

where `sigma` is the uniform random permutation of the thirty-two slots and
`chi` is the fixed sign vector with sixteen of each sign. Its mean is zero.
For a uniform permutation, the variance of `sum c_b * sigma(b)` is
`(sum of squared centred c) * (sum of squared centred slots) / 31`, that is
`32 * 2728 / 31 = 2816` exactly, so

    E[c_63^2] = 16 * 2816 = 45056

and, dividing by the constant of (b.1), the expected share at order 6 under
the family is `45056 / 1397760 = 44/1365`, which is `0.032234...`, exactly
twice the uniform expectation of `1/63`.

This is the analytic acceptance test of the pair preserving sampler, and it
is deliberately sited at an order that is not focal. An acceptance test on
orders 2 or 4 could be tuned, consciously or not, to flatter the result this
lane is about to report. One on order 6 cannot: order 6 is reported in the
profile, it carries no test in section (e), and no outcome of this lane turns
on it.

---

## (c) The selection bias, written out

Orders 2 and 4 were not chosen from the design of the question. They were
chosen by looking at the spectrum in earlier work and noticing where the
energy sat. The deposit's own footnote shows the trace of that: it says
"even" in one clause and `{2,4}` in the next, which is what a set selected by
inspection rather than by construction looks like when it is written down.

The design consequence is fixed here and is not optional.

1. **The primary analysis reports the complete profile.** The share of non-DC
   Walsh energy at every interaction order from 1 to 6, for the received
   sequence and for both nulls of section (d), with the family mean, the
   standard deviation, the empirical support and the percentile at every
   order. It is reported whatever it shows, including at orders where it is
   unremarkable, and including at orders where it is inconvenient.
2. **The focal statistic is the share at orders 2 and 4, preespecified
   here.** It is one number, it is fixed in section (b), and it is the one
   the attribution of section (d) is computed on.
3. **The multiplicity correction runs over every order measured**, not over
   the focal statistic alone. Section (f) fixes the correction, the size of
   the test set and the rule that settles that size.
4. **The set `{2,4,6}` is reported and is never promoted.** Because the full
   profile is reported, the share over the even orders is recoverable by any
   reader from the same table. It is reported there as a declared secondary.
   It cannot become the headline, and no claim of this lane rests on it.

The purpose of reporting the full profile is not completeness for its own
sake. It is that a lane which reports only the orders that were selected by
inspection cannot be distinguished, by a reader, from a lane that selected
them after seeing this run.

---

## (d) The two nulls, and the attribution, which is the primary quantity

### The pair rule, as the source states it

From `paper.tex` at `zenodo-v3`, the introduction: the received text
"arranges the 64 hexagrams in the King Wen sequence, an ordering that
proceeds in 32 pairs: each pair is related by 180-degree rotation, or by
complementation when the figure is rotation-symmetric."

### Null N0, free

`N0` is the uniform distribution over all permutations of the sixty-four
hexagrams. It fixes nothing. It is the null the deposit's baseline of 47.6
percent refers to, and by (b.3) the mean of the focal statistic under it is
exactly `30/63`.

### Null N1, pair preserving

`N1` is the uniform distribution over the family of arrangements that
preserve the received adjacency pairing: the thirty-two unordered pairs that
occupy positions one and two, three and four, and so on to sixty-three and
sixty-four, survive as pairs, in any order of the pairs, in either
orientation within each pair.

A member is generated by exactly two free choices: a permutation of the
thirty-two pairs into the thirty-two pair slots, and an orientation for each
pair. Every such choice gives a distinct member and every member arises from
exactly one choice, so the family holds `32! * 2^32`, that is
`1130138339199322632554990773529330319360000000` members, about
`1.13 * 10^45`. That cardinal is definitional arithmetic on the declared
design, not a measurement.

`N1` is defined by the received adjacency pairing and not by any theorem
about which pairing that is. The design therefore does not depend on the
matching being the rotation and complementation matching. Whether it is, is a
fact worth reporting and is reported under P1 below, but nothing here rests
on it.

Enumeration of `N1` is not available at any scale. Uniform sampling from it
is available exactly, because both free choices can be sampled exactly: a
uniform permutation of thirty-two objects, and thirty-two independent fair
bits. There is no rejection step, no approximation and no burn-in, so Monte
Carlo error is the only error and section (f) quantifies it.

### The preconditions, reported whatever they say

- **P1.** Whether the adjacency pairing of the received sequence is the
  matching that pairs each figure with its 180 degree rotation, and with its
  complement when the figure is rotation symmetric. Reported either way. It
  does not stop the lane, because `N1` is defined by the received pairing
  itself; it changes what the phrase "the pair rule" refers to in the
  reporting, and if it fails, the report says the family conditions on the
  received adjacency pairing and says that this is not the matching the
  source describes.
- **P2.** Whether the focal statistic, recomputed here from the received
  sequence, agrees with the figure the footnote prints. If it disagrees, the
  disagreement is reported as a finding about the deposit, and this lane's
  own recomputed value, not the printed one, is the one carried forward
  everywhere below.

### The attribution, which is what this lane is for

Write `E_obs` for the observed focal statistic recomputed here, `m0` for the
mean of the focal statistic under `N0` and `m1` for its mean under `N1`. The
three quantities reported as the primary result are

    excess    = E_obs - m0        the whole distance from uniformity
    explained = m1   - m0         the part the pair rule alone produces
    residual  = E_obs - m1        the part that survives the pair rule

and, when the ratio is admissible under the rule below, the two shares

    A = explained / excess        attributable to the pair rule
    R = residual  / excess        not attributable, and A + R = 1

**This decomposition is a definition, not a discovery.** It defines "what the
pair rule explains" as the shift in the null mean produced by conditioning on
the pairing and nothing else. Other definitions exist, including ones based
on variance rather than on means, and they would give different numbers. The
definition is fixed here so that the number cannot be selected afterwards
from among several defensible ones.

`m0` is exact by (b.3), so it carries no error. `E_obs` is a constant of the
received sequence. The only quantity carrying Monte Carlo error is `m1`, so
`A` and `R` are affine functions of `m1` and the interval for them is the
image of the interval for `m1`. The reported interval is `m1` plus and minus
1.96 Monte Carlo standard errors, mapped through the affine relation. It
quantifies simulation error and nothing else; it is not a confidence interval
for a population parameter, and the report says so where it prints it.

**Admissibility rule for the ratio, fixed now.** If `|excess|` is smaller
than four Monte Carlo standard errors of `m1`, the ratios `A` and `R` are not
reported at all and only `excess`, `explained` and `residual` are. A ratio
whose denominator is not distinguishable from zero is not a quantity, and
this rule exists so that the decision to print it or not is made before the
number is seen.

### What else is reported

- The percentile of `E_obs` under `N1`, at the focal statistic and at every
  order. This is the quantity the declared prior above puts near 96.
- The percentile of `E_obs` under `N0`, at the focal statistic and at every
  order, reported descriptively. `N0` carries no test in section (e) and is
  excluded from the correction: its role is the baseline `m0` and the
  verification of (b.3), not inference.
- The full profile of section (c) under both nulls.

---

## (e) The refutation criterion, and the check that it can fail

### The hypothesis under test

`H_resid`: once the pair rule is held fixed, the observed concentration of
Walsh energy is still atypical. In plain words, the pair rule does not
account for what the footnote attributes to it, and something the family does
not contain remains.

### The declared tests, all under `N1`

- **T0, focal.** The share at orders 2 and 4. One sided, upper tail. The
  direction is fixed here, and it is fixed in knowledge of the declared prior
  of section 0, which is exactly why that prior is declared.
- **T1 to T6, per order.** The share at each interaction order from 1 to 6.
  Two sided, by the absolute deviation from the family mean.

Seven tests. The Monte Carlo p-value estimator is fixed in section (f). The
tails are fixed here and are not chosen after seeing a figure. No other test
is run; any further quantity is labelled exploratory in the report, is
excluded from the correction, and cannot support any claim.

### The criterion

`H_resid` is **refuted** if every one of the seven declared tests, after the
Holm correction of section (f), yields an adjusted p of at least 0.05.

`H_resid` **survives**, in the limited sense of not being refuted, if at least
one declared test yields an adjusted p below 0.05, and the report then names
which test, which order and which direction.

### Verification that the criterion can fail, performed before signing

This check is done explicitly and in both directions, and its arithmetic is
written out so that a reader can repeat it without running anything.

**Can `H_resid` be refuted? Yes, and on the declared prior it is the expected
outcome.** The prior of section 0 puts the observed value at the 96.1st
percentile of the family, that is a one sided tail of about 0.039. Holm's
first step requires the smallest raw p to fall below `0.05 / 7`, about
0.0071. A raw p near 0.039 does not, and if no per order test is far more
extreme than the focal one, every adjusted p lands at or above 0.05 and the
hypothesis is refuted. Refutation is therefore reachable, and it is reachable
by the most likely state of the world.

**Raising the sample size does not change this, and that is stated in
advance.** A Monte Carlo tail probability near 0.039 stays near 0.039 as the
draw count rises; what falls is its standard error, not its value. The sample
size of section (f) buys precision and nothing else. It is written here so
that no later reader can suppose the sample size was chosen in the hope of
moving the focal p across the Holm threshold, and so that this lane cannot
raise it afterwards for that purpose.

**Can `H_resid` survive? Yes, but essentially not through the focal test, and
that asymmetry is declared rather than concealed.** At 2000 draws the
standard error of a tail near 0.039 is about 0.004, so the true tail would
have to be about seven standard errors below the exploration's estimate to
reach the Holm threshold. That is not a state of the world this design should
plan for. Survival must therefore come from a per order test, and those are
genuinely open at signing: nothing measured anywhere bears on where the
observed energy at orders 1, 3, 5 or 6 sits inside this family. Fact (b.4)
shows that the family is far from uniform order by order, since it doubles
the order 6 expectation exactly, so there is ample room for a per order share
to sit far in either tail. Two sided tests at those orders can reach the Holm
threshold on their own account.

**What would be a defect is a criterion no outcome could fail.** By the first
paragraph above, refutation is reachable and expected; by the third, survival
is reachable through a definite, named route. The criterion discriminates.

### The distinction this lane will not blur

Attribution is a magnitude. Refutation is a statement about a tail. They can
point in different directions and, on the declared prior, they are likely to.

If the point estimate of `A` comes out well below one while `H_resid` is
refuted, the only reading this lane is permitted is the one written here in
advance: the pair rule accounts for part of the distance from uniformity, and
what remains is not distinguishable from ordinary variation inside the pair
preserving family at this sample size under this correction. A refutation of
`H_resid` does not make the residual zero, and this document will not be read
as saying so. Equally, a residual with a large point estimate is not evidence
of anything further merely because it is large.

---

## (f) Multiplicity, sample size and seed, fixed here

**The test set.** Seven tests, as declared in section (e), all under `N1`.
The correction rule is Holm's step down procedure at a family wise level of
0.05 across that set. Holm does not require the tests to be independent, and
they are not: the focal statistic is the sum of two of the six per order
shares, and by (b.1) the six shares sum to one exactly.

If the convention invariance of (b.2) fails its verification, all four bit
conventions are carried and the test set has twenty-eight members. If it
holds, the set has seven. No other value is permitted, and the choice between
seven and twenty-eight is settled by a verification with a determinate answer
and not by inspection of any p-value.

**Sample size.** 200000 draws from `N1` and 200000 draws from `N0`. This is
fixed. It is not increased after seeing a result, and it is not decreased.

**Seed.** 21776041, the record number of the deposit under audit. The seed is
tied to an external identifier so that it is not a free parameter that could
be tried more than once. The generator is the PCG64 bit generator, seeded
from a seed sequence on that integer, with independent streams spawned in
this declared order: stream 0 for `N1`, stream 1 for `N0`, stream 2 for the
validation of the sampler.

**Monte Carlo p-value estimator.** `p = (1 + number of draws at least as
extreme) / (1 + number of draws)`. It never returns zero and it is
conservative. A p reported at its floor is reported as being at its floor and
never as a zero.

**Monte Carlo error and the indeterminacy rule.** At this sample size the
standard error of a tail probability near the thresholds in use is below
0.0005, which is small against the smallest corrected threshold above. No
result whose verdict would turn on Monte Carlo error alone will be declared;
if one arises, it is reported as indeterminate at this sample size, and the
sample size is not raised to resolve it.

**No adaptive stopping. No sequential looks.** One run per null, with the
declared seed, reported whatever it yields.

**The validation precondition.** The sampler must pass both routes of the
validation declared for this lane before any p-value or any percentile is
read: the published membership predicate of the family, read at its deposit
tag, and the analytic facts of section (b). If the two routes disagree, the
run stops and the disagreement is the result. The observed value is read only
after the validation passes.

---

## (g) What will not be claimed

Whatever the figures do, this repository will not claim, suggest, imply or
frame as an open possibility:

- that the King Wen sequence was designed, or was not designed;
- that any intention, purpose or awareness lay behind its ordering;
- that its makers possessed, or lacked, knowledge of binary representation,
  of Boolean functions, of harmonic analysis, or of any other mathematical
  content;
- that a spectral outcome bears on the meaning, authenticity, antiquity or
  authority of the sequence or of any text;
- that a refutation or a survival of `H_resid` says anything about a person.

The object of study is a permutation of sixty-four objects, a function on the
six dimensional Boolean cube built from it, and the energy of that function
in a fixed basis. The results speak about that object and about the two
families defined in (d), and about nothing else.

Two further prohibitions are specific to this lane, because it audits a
published sentence written by the author of this lane:

- **Nothing will be said about the writer of the footnote.** A finding that
  an attribution is unsupported is a finding about that attribution. It is
  not a finding about care, competence or honesty, and no wording in any
  artefact of this lane will invite that reading.
- **Nothing will be corrected in the deposit from here.** If this lane
  concludes that the footnote's attribution is not supported, the conclusion
  is recorded in this repository. Whether the deposited work is ever amended,
  and by what procedure, is a separate decision belonging to its author in
  that capacity, and it is not taken here.

Additionally, and until the background review of this lane is opened and
closed, no claim of novelty, priority or first result of any kind is made
here about anything.

---

## Signature

This text is signed by the root commit of this repository. The commit author,
its timestamp and its hash are the signature. Any later change to this text
would change that hash and would be visible as such, which is the property
the signature relies on.

No quantity of `N0` or `N1` has been computed at the time of this commit. The
received King Wen sequence has not been read into this repository. The only
arithmetic performed before signing is the arithmetic written out in sections
(b) and (d), which is definitional or analytic, concerns no sample, and is
checkable by hand from this text alone.
