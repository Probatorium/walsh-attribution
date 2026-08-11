# Decisions

Decisions that change what this lane does, who took them and when. A decision
that is not written here did not happen.

A decision is not the same as a design choice made inside the signed
preregistration. Those are fixed by `PREREGISTRATION.md` and are not
decisions to be taken again. This file records the choices that were left
open on purpose, and the ones that belong to Alexis rather than to the
apparatus.

---

## Decisions taken

All four decisions this register opened with were taken in session two, on
2026-08-11, by Alexis Garcia Hurtado. Each is recorded below with what it
changed and what it did not.

### Decision one: the name is `walsh-attribution`

- **Decider**: Alexis Garcia Hurtado. **Date**: 2026-08-11, session two.
- **Grounds**: the measured occupancy of `spectral-attribution` reported in
  `NAME-GATE.md`. The compound is taken by exact string, as a public
  repository name and as a term of art in machine learning interpretability.
- **What changed**: the name of the lane and of the repository Alexis
  creates on the forge.
- **What did not change**: the signed preregistration, which still opens
  `Repository: spectral-attribution` and is not amended. It declared the name
  provisional and defined everything extensionally, which is why the rename
  costs nothing in the design. The local checkout directory also keeps its
  old name, which `CONTACT-RULES.md` treats as an accident of one machine.
- **The measurement that produced it is not deleted.** `NAME-GATE.md` still
  carries its queries, its limits, its findings, its verdict and the rejected
  candidate with the reason for rejection.

### Decision two: a remote is authorised

- **Decider**: Alexis Garcia Hurtado. **Date**: 2026-08-11, session two.
- **What is authorised**: creating a remote named `walsh-attribution`,
  attaching it, and publishing this history to it, subject to the house
  procedure being run first and reported.
- **The house procedure, required before the first push**: a one line log of
  every commit; a sweep of every blob of every commit for secrets, tokens and
  personal paths; and `git ls-remote` to confirm the remote is empty. After
  the push: address, visibility, local head, remote head, and confirmation
  that the trees are identical.
- **Scope**: the authorisation is for publishing this history. It does not
  authorise a change of visibility, a release, or a deposit, and it does not
  make every later push automatic.
- **Execution state at the close of session two**: the house procedure ran
  and its output is in `SESSION-REPORT-002.md`. The remote could not be
  attached, because the repository did not exist yet on the forge: at the
  time of the check, neither `github.com/Probatorium/walsh-attribution` nor
  `github.com/theoriginaliching/walsh-attribution` resolved, while other
  repositories under the same accounts did resolve with the same credentials.
  Nothing was created by this lane, because decision two says Alexis creates
  the repository. The push was therefore pending on that one act and on
  nothing else.
- **Executed in session three.** Alexis created the repository, public and
  empty. The house procedure was re-run over the history as it then stood,
  the remote was attached, the remote was confirmed empty, and the history
  was pushed. Address, visibility, both heads and the confirmation that the
  trees are identical are in `SESSION-REPORT-003.md`.
- **Not covered, and stated again because it is easy to assume otherwise**:
  the commits made after that push. They are local until publishing them is
  asked for, and the house procedure runs again over what is new.

### Decision three: the artefacts stay in English

- **Decider**: Alexis Garcia Hurtado. **Date**: 2026-08-11, session two.
- **Grounds**: the deposit under audit, the neighbouring deposits and the
  cited works are in English, and an audit of an English footnote that a
  reader cannot line up against the footnote is worth less.
- **Consequence**: no forward Spanish version is prepared, and the note in
  `SESSION-REPORT-001.md` about that possibility is closed.

### Decision four: the expected shape of this lane is the intended one

- **Decider**: Alexis Garcia Hurtado. **Date**: 2026-08-11, session two.
- **What was accepted**: that the likely headline of this lane is
  deflationary. On the declared prior, `H_resid` is expected to be refuted,
  the informative content is then the attribution magnitude rather than a
  significant tail, and raising the sample size cannot change that.
- **Why this mattered enough to be a decision**: `PREREGISTRATION.md` is
  signed and can only be superseded, not edited. A change of intent after the
  analysis session would have been expensive. It was taken before that
  session, which is the point.
- **Consequence**: the analysis session proceeds as designed, and a
  deflationary result is reported as a result rather than as a
  disappointment.

---

## Decisions open

**None.**

Two things that are pending are not decisions and are recorded as execution
state rather than as open questions: the creation of the forge repository,
which belongs to Alexis under decision two, and the first push, which follows
from it automatically once the repository exists.
