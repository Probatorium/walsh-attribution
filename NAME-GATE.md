# Term gate: is `spectral-attribution` occupied

Run: 2026-08-11, in the inaugural session, after the root commit and after the
contact rules, because the root commit holds the preregistration and nothing
else. It was run before any quantity of either null family was computed and
before the received sequence was read into this repository.

This is a term gate, not a literature review. It asks one narrow question: is
the name already carrying a meaning that would collide with the one this lane
intends. It does not survey the field, it does not establish priority, and it
does not begin the background review, which remains unstarted. See
`BACKGROUND-REVIEW.md`.

## Method and its limits, stated before the results

- One engine, one pass, English only, executed 2026-08-11.
- Queries are declared verbatim below and were fixed before their results
  were read.
- Not run, and therefore not claimed: a full text search of arXiv, a Google
  Scholar pass, a MathSciNet or zbMATH lookup, a search in any language other
  than English, a check of trademark or package name registries, a survey of
  repository name registries beyond what the engine surfaced.
- Because of the above, a negative finding here means "not found by these
  queries", and never "does not exist". A positive finding, that a name is
  taken, is the stronger kind of result this method can return, and it is the
  result it returned.

## Declared queries

The first block was fixed before any result was read.

- Q1: `"spectral attribution" statistics term`
- Q2: `"spectral attribution" null model permutation test`
- Q3: `"spectral attribution" arxiv`
- Q4: `"attribution analysis" variance decomposition conditional null model statistics`
- Q5: `Walsh spectrum "interaction order" energy permutation null hypothesis Boolean function`

The second block was added after the first was read, and the reason is
recorded rather than left to be inferred. It was not added to improve the
verdict on `spectral-attribution`: the first block had already settled that
question against the name, and nothing in the second block could reverse it.
It gates candidate replacements.

- Q6: `"pair-rule-spectrum" OR "pair rule spectrum" term`
- Q7: `"walsh attribution" OR "walsh-attribution" method`

## What came back

### The exact compound is taken, as a name and as a method family

Q3 returned a public repository at `github.com/gabrielkasmi/spectral-attribution`,
that is the exact hyphenated compound this lane proposed to use, already in
use as a repository name.

Q1, Q2 and Q3 together returned a live and growing body of work in machine
learning interpretability that uses "spectral attribution" as a compound in
its ordinary technical sense: attribution of a model's prediction to
components of a spectral decomposition. Named instances the queries surfaced:

- Spectral Integrated Gradients, arXiv:2605.19607, which builds integration
  paths from a singular value decomposition and was accepted to KDD 2026.
- A wavelet scale attribution method that represents a model decision in the
  space and scale domain.
- A frequency aware attribution method operating on an energy driven spectral
  cutoff, arXiv:2510.03245.
- Spectral relevance analysis, used as a meta analysis over attribution maps.

This is not a distant collision. It is the same two words, in the same order,
meaning a different thing, in an active field with a high publication rate.

### The sense this lane intends, and where it does live

Q4 confirms that "attribution" in the sense this lane means it, apportioning
an observed excess between a factor and a residual, is at home in variance
decomposition and in the family of methods that compare a marginal against a
conditional model. That association is correct and is the one this lane
wants. It is simply not the association that the compound "spectral
attribution" now carries.

### The basis vocabulary is clean

Q5 returned the Walsh spectrum literature in its own right: Boolean function
cryptography, Walsh and autocorrelation spectra, spectra of permutation
inverse families. Nothing there conflicts with this lane, and nothing there
uses the word "attribution".

### The two candidates gated

- `pair-rule-spectrum`, Q6. **Rejected.** "Pair rule" is heavily occupied in
  developmental biology, where pair rule genes are a standard class of
  segmentation genes in Drosophila and the phrase returns that literature
  first. "Spectrum pair" is separately occupied in speech coding, where line
  spectrum pairs are a standard representation. The candidate collides twice,
  in two unrelated fields, and neither collision is with anything this lane
  means.
- `walsh-attribution`, Q7. **Available on these queries.** The compound
  returned no technical use. Its hits were a person surnamed Walsh in
  advertising measurement, and Walsh codes in code division multiple access,
  neither of which is a term of art competing with this one. It inherits the
  vocabulary of the basis this lane actually uses, and it does not sit in the
  interpretability basin that "spectral" plus "attribution" now occupies.

## Verdict

`spectral-attribution` is **not available**. It is occupied as an exact
repository name and as a compound term of art in a different field.

This is the strong form of the gate's finding, not the weak one. The gate can
only ever say "not found by these queries" when a name appears free; here it
found the name in use, by exact string, in a public repository and in a
current literature.

Recommendation: rename. On the evidence gated here, `walsh-attribution` is
the leading candidate, and `pair-rule-spectrum` is rejected.

## Status of the decision

**DECIDED. `walsh-attribution` is adopted.**

- Date: 2026-08-11, in session two.
- Decider: Alexis Garcia Hurtado.
- Grounds: the measured occupancy of `spectral-attribution` reported above.
  The compound is taken by exact string, as a public repository name and as a
  term of art in a different and active field, and the collision is a
  retrieval collision paid by every future reader.
- Recorded in `DECISIONS.md`, decision one.

Nothing above this line is rewritten to agree with the outcome. In
particular the verdict still says what it said, that the name was occupied
and that `walsh-attribution` was available on the queries run, and the
rejected candidate is still recorded with the reason it was rejected. The
gate is the measurement; this section is the decision the measurement
produced.

**What the rename does not touch.** `PREREGISTRATION.md` is signed and is not
amended. It opens with the line `Repository: spectral-attribution`, and that
line stays exactly as it was signed. The document itself anticipated this: it
declares the name provisional and defines the signal, the statistic and both
nulls extensionally, so no load bearing term changed and no signed text needs
correcting. A reader meeting the old name at the top of the signed document
is meeting the name the document was signed under, which is the correct thing
for a signature to preserve.

**The local checkout directory keeps its old name.** That is an accident of
one machine and `CONTACT-RULES.md` says so in its opening paragraph:
repositories are identified by repository, not by where they sit on a disk.

Three facts bore on the decision and are recorded so that it could be taken
quickly:

1. **Nothing in the design depends on the name.** `PREREGISTRATION.md`
   defines the signal, the statistic and both nulls extensionally and uses no
   name as a load bearing term. A rename would require no amendment of the
   signed text, which is why the gate was run before anything was fixed.
2. **Renaming is free now and stops being free later.** This repository has
   no remote and no deposit. Once either exists, the cost of a rename is a
   broken address rather than a directory move.
3. **The collision is a retrieval collision, not only an aesthetic one.** A
   reader meeting this name cold, and any search engine indexing it, will be
   pulled toward feature attribution for neural networks. That is a cost paid
   by every future reader of this lane, not by its author.

Everything above this section is the measurement that produced the
recommendation, and it stays as written whatever is decided.
