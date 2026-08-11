# Rigour report, session one

Session identifier: S001. Date: 2026-08-11. Inaugural session.

**No quantity of either null family was sampled in this session, no sampler
exists in this repository, and the received King Wen sequence has not been
read into it.** The lane has measured nothing. That is the intended state at
the end of an inaugural session and it is the fact this report exists to
certify.

The one qualification to that sentence is recorded as defect one and is
repeated here rather than left in the register: the signed preregistration
derives two exact quantities of the two null families by hand, in its section
(b), and its own signature claims it derived none. Nothing was sampled;
something was derived. The signed text says the sweeping thing and then says
the narrow one, and the narrow one governs.

---

## Commits

Eight commits, in this order.

- **Root**, `d385f92`. `PREREGISTRATION.md` and nothing else. Verified: the
  root tree holds that one path. The signature of the document is the hash of
  that commit, and that property only holds because the commit contains the
  document alone. The blob is `662a730e614c6d54383e09cc189d58292036d16b` at
  the root and the same blob at the head, and exactly one commit in this
  history has ever touched that path.
- **Contact rules**, `abb0557`. `CONTACT-RULES.md`.
- **Term gate**, `dc3e090`. `NAME-GATE.md`.
- **Apparatus**, `d568e48`. The four gates, their runner, the hook installer,
  both versioned hooks, the test suite, the attributes and ignore files, both
  logs, and `PROVENANCE.md`. The message names all of them.
- **Standing registers**, `f757cba`. `REFERENCES.md`,
  `BACKGROUND-REVIEW.md`, `THIRD-PARTY-MANIFEST.md`, `DECISIONS.md`.
- **Validation plan**, `40b2588`. `VALIDATION-PLAN.md`.
- **Defect register**, `d71adaa`. `DEFECTS.md`.
- **This report**, which is the eighth and is counted here rather than
  omitted, because the previous lane's inaugural report undercounted itself
  by leaving out the commit that carried it.

All commits are authored under the git identity `alexcat84`, with a trailer
naming the assistant as co-author. That is the truthful attribution and it is
recorded rather than tidied.

**No remote exists.** None was created, none was requested, and
`CONTACT-RULES.md` rule six requires an explicit request from Alexis,
recorded with its date, before one can. Every commit is local only.

## Files

Twenty-four tracked paths. Seven documents of record: the preregistration,
the contact rules, the term gate, the provenance of the reused apparatus, the
validation plan, the defect register and this report. Four standing
registers: references, background review, third party manifest, decisions.
Two logs: the effort log and the figure registry. Seven tools, two hooks, and
the attributes and ignore files.

Nothing under `vendor/` exists, because no third party file has entered. The
manifest records that its contents are empty and names the one entry it
expects.

## The root commit, and the working tree around it

The root commit's tree holds one path. Its working tree did not: the
apparatus was written before the root commit and left untracked, so that the
effort log could be instituted before any work of this session happened
rather than three commits into it.

That is a deliberate departure from how the previous lane did this, and it is
stated rather than presented as identical. The property the signature depends
on is a property of the commit's tree, and it holds. What changes is that no
work of this session sits outside the log, which the previous lane could not
say of its own first three commits.

## State of the chain

The effort log verifies: the chain is intact, every entry recomputes to its
stored digest, every entry links to the one before it, and the session
structure is sound. The head digest at the time of writing is recorded in the
closing entry, which is appended after this file is written and before it is
committed.

Its binding to commits is weaker than its integrity, and that is defect four.
Only the entry for the root commit carries a commit hash; the rest bind to
their work by timestamp and by the artefacts they name. The tracked copy of
the log also lagged the working copy across one commit before the practice
was fixed. Neither of those touches the chain.

## Dash sweep

The gate forbids the long dash everywhere, with no exemption for any file
including its own source, and permits the en dash only between two digits and
only inside `REFERENCES.md`, which is the single registered exemption.

- Working tree, every tracked text file: clean.
- Every blob of every commit: clean.
- Tests: the suite attacks the gate in eight ways, including applying the
  exemption outside the pattern it was granted for and applying it to the
  wrong file. All pass.

## Untouchable gate

- Tree, remotes, config and every blob of every commit: clean. No untouchable
  repository is named, linked or cited anywhere.
- The gate refused its own test suite on the first commit that tried to carry
  it. See defect two. It was fixed by escaping the fixtures through the
  tool's own list rather than by exempting the enforcer.
- Tests: ten, new in this lane, covering the pattern boundaries and the
  allowance. The previous lane had none.

## Figure gate

The registry holds nine figures. Every one of them is cited-unverified, so
the number of figures usable in a commit message is zero. Every commit
message of this session was therefore written without a figure, and every one
passed the gate.

The nine are the two the audited footnote prints, the four the auditor's
unregistered prior exploration produced, its draw count, and the two
constants this lane derived by hand and has not executed. That last pair is
the point of interest: the gate binds the author's own derivations exactly as
it binds someone else's published numbers, and neither can be asserted here
until an artefact in this repository produces it.

The gate was exercised against a message carrying all four of the figures
this lane is most likely to repeat by reflex, together with four identifiers.
It exempted the identifiers, printing the reason and the count for each, and
refused all four figures, naming the object on record for each. One of the
four refusals is the rule doing work no pattern could: the draw count of the
prior exploration is four digits beginning with two and would have passed as
a publication year, and it did not, because a token in the registry is never
exempted by any pattern.

## Suite

Fifty-six checks over the four gates and the two rules that sit inside the
figure gate, the identifier exemptions and the supersession rule. All pass.
Six of them are new in this
lane and hold the figure gate against this lane's own temptations; ten more
are new and attack the untouchable gate's patterns.

## What the preregistration commits this lane to, in brief

The signal is the King Wen number as a function on the six dimensional
Boolean cube, in the bit convention quoted from the deposit under audit. The
statistic is the share of non-DC Walsh energy by interaction order. The focal
statistic is the share at orders 2 and 4, and the full profile at every order
is the primary report, because the focal orders were selected by inspection
in earlier work and the document says so.

Two nulls: free, and the family that preserves the received pairing. The
primary quantity is the attribution, which is defined in the document rather
than chosen afterwards from among the defensible definitions. Seven declared
tests with fixed tails, Holm corrected. Sample size and seed fixed, the seed
tied to an external identifier so that it is not a parameter anyone could
try twice.

Four exact facts are derived in the signed text and are the acceptance tests
of the validation. The one that constrains the pair preserving sampler is
sited at the single interaction order that carries no test and on which no
conclusion of this lane depends, so that it cannot be tuned to flatter the
result.

The refutation criterion was checked for failability before signing, in both
directions, with its arithmetic written out. Refutation is reachable and, on
the declared prior, expected. Survival is reachable through a named route,
the per order tests, and is not expected through the focal one. The document
also states, before the run, that raising the sample size cannot move the
focal p across the threshold, and why, so that neither the sample size nor
the outcome can later be presented as a surprise.

## The declared prior, and what it costs

This measurement is confirmatory with a declared prior. An unregistered
exploration was run before this repository existed, its four figures are
written into the signed document, and the direction of the focal test was
chosen in knowledge of them.

The honest description of what that buys and what it costs is in section 0 of
the preregistration and is not softened here. It buys a one sided test that
is defensible because the knowledge behind it is declared in advance of the
confirmatory run. It costs the lane any claim to blind exploration, and the
document says so in those words.

## What is pending, and belongs to Alexis

Four decisions, all recorded in `DECISIONS.md` with what each is waiting on.

1. **The name.** The term gate returned its strong form: `spectral-attribution`
   is occupied by exact string, as a public repository name and as a compound
   term of art in machine learning interpretability. Renaming is free while
   there is no remote and no deposit. Nothing in the signed design depends on
   the name. The gate's leading candidate is recorded there.
2. **Whether this lane ever has a remote.** None exists. Building a lane was
   not read as an instruction to publish one.
3. **The language of the artefacts.** English, on a judgement made without
   asking, for the reason recorded. The preregistration cannot be amended, so
   a change would be forward.
4. **Whether the expected shape of this lane is the intended one.** The
   design's likely headline is that the pair rule accounts for part of the
   distance from uniformity and that the remainder is not distinguishable
   from ordinary variation inside the family. That is a real result and the
   design establishes it. Confirmation that it is the lane that was wanted is
   cheaper now than after the analysis session, because the document is
   signed and can only be superseded.

## What is not claimed

Nothing about design, intention or ancient knowledge. Nothing about the
writer of the audited footnote, who is the author of this lane. No claim of
novelty of anything, since the background review is unstarted, and in
particular no claim that the four exact facts derived in section (b) are new,
because they are elementary and the review that would establish otherwise has
not been opened.

No figure of the deposit under audit and no figure of the prior exploration
is asserted anywhere in this repository as established. The figure gate holds
that mechanically for commit messages and the registry holds the record.
