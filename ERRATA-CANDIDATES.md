# Errata candidates for the deposit under audit

Three candidates, prepared here and applied nowhere. This repository does not
touch the package of the deposit under audit, does not open any branch of it,
and does not write to it. `CONTACT-RULES.md` rule one forbids all of that and
`PREREGISTRATION.md` section (g) forbids it again for the specific case where
this lane concludes against the footnote.

What this document is: three entries in a form that can be carried, by
Alexis, into that package's own errata process whenever he wants. The package
carries an `ERRATA.md` at its deposit tag, so the process exists and this is
not an invitation to invent one.

**This document was opened in session two with two entries and gained a third
in session four.** The opening text said "two" and said that both entries
were found by reading rather than by measuring, which was true of both and is
not true of the third. That text is in the history at the commit that carried
it, and the two sentences below replace it rather than pretending it was
always this.

**No candidate changes a printed number.** Every figure the footnote prints
stands, and the measurement of session three confirmed both of them: the
share recomputed here is the printed one to one decimal, and the printed
baseline is exactly `30/63`. What each entry is about is a sentence.

**The first two candidates are readings, the third is a measurement.**
Candidates one and two were found by opening the prose and the code at the
same tag, before any measurement existed here, and both are recorded in the
signed preregistration. Candidate three could not have been written before
the analysis session, and the closing section of this document says in its
own words that it was not.

**Source read**, for candidates one and two, under `CONTACT-RULES.md` rule
one, at tag `zenodo-v3` of `kingwen-orderings-replication`, deposit
`10.5281/zenodo.21776041`:

| file | git blob | SHA-256 of contents |
| --- | --- | --- |
| `paper.tex` | `35995cfd212cc0e632457e589b0cb1769363a94c` | `9980aa69860dd1253f87180fcfbb305c36a8924886e3c7efb97bc71961b62d55` |
| `verify_paper.py` | `100a0e7e93691b9d0989a6f86788fe22894813d7` | `cb0c923ece64370cec569d03fdb99cc0d325c09aeba2b94d98b373685995546f` |

Nothing in that repository moved. The tag was addressed directly and the
working tree was on its own branch before and after. Candidate three quotes
the same footnote at the same tag and takes its figures from
`results/measurement.json` in this repository.

---

## Candidate one: the signal the footnote describes is not the signal the verifier computes

### The published prose

`paper.tex`, line 241, the footnote to the opening paragraph of the section
"Spectral portraits of the five orderings":

> This convention necessarily differs from the natural single-order signal,
> position maps to King Wen number, used when analyzing the King Wen sequence
> alone

### What the verifier at the same tag computes instead

`verify_paper.py`, lines 856 to 862, in `section_6`:

> ```
> 856    # The single-order convention, stated in Section 6 for contrast.
> 857    kw_numbers = [KW_NUMBER[v] for v in BINARY]
> 858    energy = [0.0] * 7
> 859    for w in range(N):
> 860        coeff = sum(kw_numbers[v] * (-1 if popcount(w & v) & 1 else 1) for v in range(N))
> 861        energy[popcount(w)] += coeff * coeff
> 862    non_dc = sum(energy) - energy[0]
> ```

with `BINARY = list(range(N))` at line 103 and
`KW_NUMBER = {v: i + 1 for i, v in enumerate(KING_WEN)}` at line 158.

So `kw_numbers[v]` is the King Wen number of the hexagram whose six bit value
is `v`, and line 860 indexes the Walsh character by `v`, the hexagram. The
domain of the signal is the hexagram read as an element of the Boolean cube;
the value is the King Wen number of that hexagram. It is the inverse of the
map the prose describes.

### Why the prose cannot be the definition

Read literally, and applied to the King Wen ordering, "position maps to King
Wen number" is the identity: position `k` carries King Wen number `k + 1`.
Indexing a Walsh character by the position and taking that value gives an
affine function of the six coordinates, whose entire non-DC energy sits at
interaction order 1 and whose energy at orders 2 through 6 is exactly zero.
That signal cannot produce the figure the footnote prints, or any figure near
it.

The discrepancy is therefore not a matter of taste in wording. The two
readings give different spectra, and only one of them is the computation the
package asserts.

### Correction proposed, in one sentence

Replace "position maps to King Wen number" with "hexagram maps to its King
Wen number", that is, the signal is indexed by the hexagram read as a six bit
value and takes as its value the position of that hexagram in the received
sequence.

---

## Candidate two: the share and its baseline do not name the same set of orders

### The published prose

`paper.tex`, line 241, the same footnote, continuing:

> with that signal, the Walsh spectrum of the King Wen ordering concentrates
> 77.4 percent of its energy in even interaction orders, against 47.6 percent
> expected for orders $\{2,4\}$ under uniformity, a spectral confirmation of
> the pair rule.

One clause says "even interaction orders". The next says `{2,4}`. The even
interaction orders of a six variable Boolean function are 2, 4 and 6.

### What the verifier at the same tag computes

`verify_paper.py`, lines 863 to 870:

> ```
> 863    even = 100 * (energy[2] + energy[4]) / non_dc
> 864    counts = [0] * 7
> 865    for w in range(N):
> 866        counts[popcount(w)] += 1
> 867    uniform = 100 * (counts[2] + counts[4]) / (sum(counts) - counts[0])
> 868    check("6", "King Wen number signal: even interaction orders carry 77.4 percent",
> 869          round(even, 1), 77.4)
> 870    check("6", "uniform expectation for orders {2,4} is 47.6 percent", round(uniform, 1), 47.6)
> ```

Both quantities are over orders 2 and 4 only. Order 6 is excluded from the
share at line 863 and from the baseline at line 867. The local variable is
named `even`, and that name is the most likely origin of the word in the
prose, since line 868 then carries it into the description of the check.

### The arithmetic that settles which set the printed baseline belongs to

There are `C(6,k)` Walsh characters at interaction order `k`, so among the
sixty-three characters other than the constant one there are 6, 15, 20, 15, 6
and 1 at orders 1 through 6.

- Orders 2 and 4 hold 30 of the 63. `30 / 63 = 0.476190...`, which rounds to
  the printed baseline.
- The even orders 2, 4 and 6 hold 31 of the 63. `31 / 63 = 0.492063...`,
  which does not.

So the printed baseline is the one for `{2,4}`, as its own clause says, and
the word "even" in the preceding clause describes a different set from the
one both figures are computed over.

### Correction proposed, in one sentence

Replace "even interaction orders" with "interaction orders 2 and 4", so that
the reported share and the baseline it is compared against name the same set,
which is the set the package computes both over.

---

## Candidate three: the attribution the footnote makes is offered for a gap it covers about a third of

**This entry was not available when the other two were written, and the
document said so.** Session two wrote, in the closing section below: "Nothing
about the attribution in the same footnote, the clause 'a spectral
confirmation of the pair rule'. That clause is the object of this lane's
measurement and is not an erratum candidate. Whether it is supported is a
question this repository answers by measuring, not by reading, and it has not
measured it yet." It has now measured it. This entry is what came out, and it
rests on the measurement rather than on a reading of the text.

### The published prose

`paper.tex`, line 241, the same footnote, the clause at its end:

> with that signal, the Walsh spectrum of the King Wen ordering concentrates
> 77.4 percent of its energy in even interaction orders, against 47.6 percent
> expected for orders $\{2,4\}$ under uniformity, a spectral confirmation of
> the pair rule.

### What was measured, and where the numbers come from

Every figure below is from `results/measurement.json` in this repository,
produced by `analysis/measure.py` at the sample size and seed fixed in
`PREREGISTRATION.md` section (f), on a sampler validated by two independent
routes before the observed value was read. `RESULTS.md` carries the tables.

Both of the footnote's own figures are confirmed and neither is in question.
The share recomputed here is 77.4 percent to one decimal, and the baseline is
not merely near the printed value but exactly `30/63`, that is 0.476190,
which is the exact mean of this statistic under a free permutation.

The measurement adds the quantity the footnote's comparison cannot contain.
Under a null that permutes the thirty-two received pairs and flips
orientations within them, holding the pair rule fixed and randomising
everything it leaves free:

| quantity | value |
| --- | --- |
| observed focal share | 0.774313 |
| mean under the pair preserving family | 0.580650 |
| mean under uniformity, exact | 0.476190 |
| excess over uniformity | 0.298123 |
| the part the pair rule accounts for | 0.104460 |
| the part it does not | 0.193663 |
| **share of the excess attributable to the pair rule** | **0.3504** |
| **share not attributable to it** | **0.6496** |

Two qualifications belong to the entry and not to a footnote a reader might
add later.

**The residual is not distinguishable from ordinary variation inside that
family under the correction this lane declared in advance.** The observed
value sits at the 95.535 percentile of the pair preserving family. All seven
declared tests, corrected as the signed document fixes, give adjusted p of at
least the declared level, the smallest being 0.312583. So the entry says
nothing about the residual beyond its size, and any wording taken from it
should not either.

**A comparison against uniformity cannot separate the two parts.** This is
the structural point and it is the reason the clause is a candidate at all.
The footnote compares the observed share against what a free permutation
would give. That comparison is correct and it is informative, and it cannot
distinguish the part of the gap that follows from the pair rule from the part
that does not, because the pair rule is not in it. Separating them requires
the conditional null, and the conditional null puts about a third of the gap
on the pair rule.

### Correction proposed, in one sentence

Replace "a spectral confirmation of the pair rule" with a clause that states
what the comparison supports and what it does not, for instance: "a
concentration consistent with the pair rule, which under a pair preserving
null accounts for about a third of the excess over uniformity, the remainder
lying within the ordinary variation of that null."

### What this entry does not say

It does not say the attribution is wrong. Conditioning on the pair rule
raises the expected share by 0.104460, which is a large absolute movement,
so an attribution to the pair rule is an attribution to something real.

It does not say anything about the residual other than its size, for the
reason given above.

It does not say anything about the writer of the footnote, who is the author
of this lane, and `PREREGISTRATION.md` section (g) binds this entry as it
binds every other artefact here.

---

## What is not claimed by any of the three entries

- Nothing about the care, competence or honesty of anyone. The entries are
  about three sentences: what the code at the same tag does instead, in two
  cases, and what a conditional null measures, in the third.
  `PREREGISTRATION.md` section (g) binds this document as it binds every
  other artefact of this lane.
- No claim that these are the only discrepancies in that footnote or anywhere
  else in that package. Three were found while reading and then measuring one
  footnote for one purpose. No sweep was run.

### The sentence this section used to carry, and what became of it

Sessions two and three left the following bullet standing here, and it is
reproduced rather than deleted because it was true when it was written and
because what replaced it is the whole point of the lane:

> Nothing about the attribution in the same footnote, the clause "a spectral
> confirmation of the pair rule". That clause is the object of this lane's
> measurement and is not an erratum candidate. Whether it is supported is a
> question this repository answers by measuring, not by reading, and it has
> not measured it yet.

It has now measured it, and candidate three is what came out. The bullet is
retired by that entry and not by an edit that would have made this document
look as though it had always known.
