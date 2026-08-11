# Errata candidates for the deposit under audit

Two candidates, prepared here and applied nowhere. This repository does not
touch the package of the deposit under audit, does not open any branch of it,
and does not write to it. `CONTACT-RULES.md` rule one forbids all of that and
`PREREGISTRATION.md` section (g) forbids it again for the specific case where
this lane concludes against the footnote.

What this document is: two entries in a form that can be carried, by Alexis,
into that package's own errata process whenever he wants. The package carries
an `ERRATA.md` at its deposit tag, so the process exists and this is not an
invitation to invent one.

**Neither candidate changes a printed number.** Both figures the footnote
prints stand. What is wrong in each case is the sentence that says what the
figures are of. That is the whole content of both entries and it is stated
first so that nobody reads further expecting a numerical correction.

**Neither candidate is a finding of this lane's analysis.** Both were found
by reading the deposit at its tag in order to write `PREREGISTRATION.md`
section (b), before any measurement existed here, and both are recorded in
that signed document. They are reported as what they are: discrepancies
between prose and code that are visible to anyone who opens both at the same
tag.

**Source read**, for both entries, under `CONTACT-RULES.md` rule one, at tag
`zenodo-v3` of `kingwen-orderings-replication`, deposit
`10.5281/zenodo.21776041`:

| file | git blob | SHA-256 of contents |
| --- | --- | --- |
| `paper.tex` | `35995cfd212cc0e632457e589b0cb1769363a94c` | `9980aa69860dd1253f87180fcfbb305c36a8924886e3c7efb97bc71961b62d55` |
| `verify_paper.py` | `100a0e7e93691b9d0989a6f86788fe22894813d7` | `cb0c923ece64370cec569d03fdb99cc0d325c09aeba2b94d98b373685995546f` |

Nothing in that repository moved. The tag was addressed directly and the
working tree was on its own branch before and after.

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

## What is not claimed by either entry

- Nothing about the care, competence or honesty of anyone. Both entries are
  about two sentences and what the code at the same tag does instead.
  `PREREGISTRATION.md` section (g) binds this document as it binds every
  other artefact of this lane.
- Nothing about the attribution in the same footnote, the clause "a spectral
  confirmation of the pair rule". That clause is the object of this lane's
  measurement and is not an erratum candidate. Whether it is supported is a
  question this repository answers by measuring, not by reading, and it has
  not measured it yet.
- No claim that these are the only discrepancies in that footnote or
  anywhere else in that package. Two were found while reading one footnote
  for one purpose. No sweep was run.
