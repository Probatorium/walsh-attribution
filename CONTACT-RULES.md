# Contact rules

Binding from the second commit of this repository. These rules govern how
this lane touches anything outside itself. They are operational, not
aspirational: each one states what may be done, what may not, and how the
permitted action is performed.

**Neighbours are identified by repository, not by where they happen to sit on
a disk.** A local path is an accident of one machine, it identifies a
person's account, and it is not what these rules are about. Finding a local
checkout of a repository, when a rule permits reading it, is a local matter
and is not part of this record.

**The common mechanic for every read only rule below.** The tag or the commit
is addressed directly, and nothing in the neighbour moves:

    git -C <checkout> show <ref>:<file>
    git -C <checkout> ls-tree -r --name-only <ref>

No checkout of the neighbour's working tree to that ref or to anything else.
No branch change. No fetch, no pull, no push, no gc, no reflog expiry run
against it from this lane.

---

## 1. kingwen-orderings-replication

`github.com/theoriginaliching/kingwen-orderings-replication`. The deposit
under audit: `10.5281/zenodo.21776041`, whose concept DOI is
`10.5281/zenodo.21609653`.

- READ ONLY, and only at the tag `zenodo-v3`.
- Recorded as a fact about that repository and not as a comment on it: its
  HEAD is on a branch that is not the deposit, and it carries tags other than
  `zenodo-v3`. None of that is visible to this lane. Only `zenodo-v3` is. If
  HEAD and `zenodo-v3` differ, the tag is what exists for this lane and HEAD
  does not.
- This is the source of three things and of nothing else: the footnote under
  audit, quoted in `PREREGISTRATION.md` section (b); the bit convention,
  quoted in the same section; and the received King Wen sequence, which
  enters under rule seven.
- It is deposited and frozen. It is not edited from here. Nothing is added to
  it: no correction, no erratum, no note, no file, no branch, no tag. This
  holds even if this lane concludes that the footnote's attribution is not
  supported. See `PREREGISTRATION.md` section (g).

## 2. The closed lane whose local checkout is named `pairing-conditioned`

`github.com/Probatorium/pairing-conditioned`, whose forge name was later
changed. Archived and closed by decision of its author. It carries no DOI, no
deposit and no tag.

- READ ONLY, and only at its final head,
  `2fb7127269b5afd26eee91cbf98648c63d8b9fc4`. It is addressed by that commit
  and not by a branch name, so that what this lane read cannot change under
  it.
- **Its sampler of the pair preserving family is reused, by reading, and the
  provenance is declared.** `PROVENANCE.md` records what was read, at which
  commit, with digests, and what this lane does with it. So do the header
  comments of the tools that came from there.
- **Its verifications are inherited where they transfer, and where they do
  not, the reason is declared.** That accounting is in `VALIDATION-PLAN.md`
  and is not left implicit. A reimplementation that quietly inherits a
  verification it has not earned is worse than one with no verification at
  all, because it looks checked.
- **It is not citable, and this is the operative consequence.** It is not
  cited in any artefact of this lane, including anything prepared for
  deposit, because it is not published in the sense that matters: a reader
  cannot obtain a version of it that is fixed, and there is no deposit to
  hold its author to. Where a technique of that lane is used here, it is
  described in this lane's own terms, in full, so that a reader can follow it
  without the missing source.
- The prohibition on citing is not a judgement about the quality of that
  work. It follows only from the fact that it carries no deposit.

## 3. forced-counts

`github.com/Probatorium/forced-counts`. Deposited work,
`10.5281/zenodo.21889328`.

- READ ONLY, and only at the tag `zenodo-v1`.
- Deposited and frozen, on the same terms as rule one.

## 4. null-ladder

`github.com/Probatorium/null-ladder`. Deposited work,
`10.5281/zenodo.21750029`.

- READ ONLY, and only at its deposit tag,
  `zenodo-10.5281-zenodo.21750029`.
- This is the source of the published membership predicate that route one of
  the sampler validation runs against. Nothing read there enters the history
  of this repository; when a module of it has to be executed, it is written
  to a scratch file outside this repository and imported from there, and the
  digest of exactly what was executed is reported.

## 5. Stasis and its sibling repositories

`github.com/Probatorium/stasis`, and the sibling repositories of that lane:
`minimal-verified-paper`, `defect-injection-study`, `stasis-antecedentes`.

- UNTOUCHABLE. Not read, not written, not fetched, not cloned, not linked,
  not depended upon, and not located.
- Identified by repository path and not by a deposit tag, because they have
  no deposit tag. They are not published: no DOI, no deposit, no tag, and
  third party verification of that lane is outstanding.
- **Not citable.** Nothing from those repositories is cited in this lane, in
  any artefact, including anything prepared for deposit.
- This rule is checked mechanically. `tools/untouchable.py` runs with the
  standing gates and fails if any of those repository names appears anywhere
  in the tracked tree or in the history outside the places where declaring
  the rule requires naming them, or if any remote, submodule or alternate of
  this repository points at one of them. Naming one in `REFERENCES.md` or in
  `BACKGROUND-REVIEW.md` is refused separately and loudly, because that would
  be a citation.

## 6. Remote and publication

Rule nine makes this rule the one that records a state of affairs and is
updated when that state of affairs changes. It changed in session two and the
text below is the state after the change. What it said before is in the
history at the commit that carried it.

- **This repository was born with no remote**, and had none through the whole
  inaugural session.
- **A remote is authorised**, by decision two of `DECISIONS.md`, taken by
  Alexis on 2026-08-11. The authorised name is `walsh-attribution`, adopted
  by decision one. The repository on the forge is created by Alexis, not by
  this lane.
- **The authorisation is for publishing this history.** It does not authorise
  a change of visibility, a release, or a deposit, and it does not make every
  later push automatic.
- **The house procedure runs before the first push and its output is
  reported**: a one line log of every commit, a sweep of every blob of every
  commit for secrets, tokens and personal paths, and `git ls-remote` to
  confirm the remote is empty. After the push: address, visibility, local
  head, remote head, and confirmation that the trees are identical.
- **State at the close of session two**: no remote is attached, because the
  repository does not yet exist on the forge. The house procedure ran and is
  reported in `SESSION-REPORT-002.md`. Nothing was created on any forge by
  this lane.
- **State in session three**: Alexis created
  `github.com/Probatorium/walsh-attribution`, public and empty. The house
  procedure was re-run over the history as it then stood and its output is in
  `SESSION-REPORT-003.md`. The remote was attached and the history was
  pushed. The observed value of the statistic had not been read at that
  moment and was not read until after the push returned, which is the
  ordering that gives the signed preregistration a public timestamp earlier
  than the measurement it governs. Both events carry their clock in the
  effort log.
- **What the authorisation still does not cover**: pushes after that one. The
  commits a later session makes are published only when that is asked for
  again, and the house procedure runs again over whatever is new.

## 7. Files that this lane did not produce

Any file this lane did not produce and that enters the working copy is
recorded, whether it comes from a third party or from a neighbour under rules
one to four.

- Third party files live under `vendor/` and stay out of the public history.
  `vendor/` is ignored by version control.
- Every such file is recorded in `THIRD-PARTY-MANIFEST.md`, which is
  versioned, with: the name, the origin, the exact retrieval address, the
  retrieval date, the SHA-256 digest, the licence or rights status as stated
  by the source, and what this lane uses it for.
- The manifest is written at the moment of entry, not afterwards.
- A digest recorded in the manifest is checked before the file is used, on
  every run, and a mismatch is a hard stop.
- Derived data that this lane computes from such a file is not itself foreign
  and may enter the history, provided the manifest entry for its source is
  present and the derivation is in the repository.

### The two named entries this rule anticipates

Neither has entered at the time of writing. Both are named now so that their
entry is expected rather than improvised.

- **The received King Wen sequence**, from `kingwen-orderings-replication` at
  `zenodo-v3`. It enters as a transcription, mechanically extracted and not
  typed, marked as received data, never recomputed here, and credited to the
  deposit it came from. It enters the versioned history rather than `vendor/`
  because a reader must be able to see exactly what was analysed.
- **The sampler read from the closed lane under rule two.** What is reused is
  recorded in `PROVENANCE.md` with digests. Code that this lane writes on the
  basis of what it read is this lane's own and enters the history normally,
  with the provenance stated in its header.

## 8. Standing on the frozen work

- The deposited lanes are cited where they are published. They are not
  continued inside themselves.
- **No figure of another lane is inherited as an established quantity here.**
  If this lane needs a value another lane reported, it recomputes it from
  primary data and reports both, agreement or disagreement. The figure gate
  enforces this on commit messages and `FIGURES.jsonl` holds the record. The
  single exception is data explicitly received rather than derived, under
  rule seven, which is marked as received and is never recomputed by
  definition.
- If this lane finds a defect in a deposited work, that finding is recorded
  here, in this repository, and the deposited work is still not touched.

## 9. Amendment

These rules may be extended by a later commit. Rules one to five and rule
seven may not be weakened, and an exception to them is only valid if it is
recorded in `DECISIONS.md` with its decider and its date, and written out in
the rule itself. Rule six records a state of affairs and is updated when that
state of affairs changes, with the change and its authorisation recorded in
the effort log.
