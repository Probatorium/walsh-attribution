# Manifest of files this lane did not produce

Every file this lane did not produce and that has entered the working copy is
listed here, under rule seven of `CONTACT-RULES.md`. Entries are written at
the moment of entry. A file present and absent from this table is a rule
violation, not an oversight.

Required for each entry: file name, origin, exact retrieval address,
retrieval date, SHA-256 digest, licence or rights status as stated by the
source, and the use this lane makes of it.

---

## Current contents

One entry, the one this manifest expected. It entered in session three, at
the moment of entry, before it was used for anything.

### `data/king-wen-received.json`

| field | value |
| --- | --- |
| origin | `kingwen-orderings-replication`, the deposit under audit, `10.5281/zenodo.21776041` |
| retrieval address | tag `zenodo-v3`, file `verify_paper.py`, symbol `KING_WEN` |
| access | read only, addressed at the tag; the neighbour's working tree was not moved and was confirmed still on its own branch afterwards |
| retrieval date | 2026-08-11 |
| SHA-256 of the source file at the tag | `cb0c923ece64370cec569d03fdb99cc0d325c09aeba2b94d98b373685995546f` |
| SHA-256 of the file written here | `148646d3c7b82b5e8612d38bfa5d22fc4a8b102f0d28ad6565d7454e71bf9bf4` |
| rights | same lane, same author; the deposit carries a licence file at its tag, and this is a transcription of a factual sequence rather than of expression |
| use | the received King Wen order, the object of the whole analysis |
| status | received data, never recomputed in this lane |

**How it was transcribed.** Mechanically, by `tools/receive_kingwen.py`,
which reads the blob at the tag through git and extracts the named symbol. It
was not typed. A copying error is therefore not one of the ways this lane can
be wrong, and the tool can be run again by anyone with a checkout to
reproduce the file byte for byte.

**What was checked on entry.** Sixty-four entries, all distinct, each inside
a six bit value. Those are checks on the transcription, not a recomputation
of the sequence.

**What was not checked on entry, deliberately.** Whether the adjacency
pairing of the sequence is the rotation and complementation matching. That is
precondition P1 and it ran in the analysis, where it belongs, and passed.

**Where the local checkout path went.** Nowhere. The tool takes it on the
command line and stores it in no file.

---

## Third party files

**None.** No file from outside this lane's own author has entered this
working copy, and nothing under `vendor/` exists.

The apparatus reused from a closed lane is recorded in `PROVENANCE.md` and
not here, and the distinction is deliberate: those files were read and
rewritten, with the changes stated, so what is in this repository is this
lane's text with a declared origin. Nothing was copied byte for byte, so
there is no foreign blob to digest. If that ever changes, the file enters
here with its digest like anything else.

---

## The entry this manifest expected, and what became of it

Sessions one and two named this entry in advance, before it existed, so that
its arrival would be expected rather than improvised. It arrived in session
three and is recorded above with its two digests. What was promised of it
held: it was extracted mechanically and not typed, it was checked on entry
for sixty-four distinct six bit values and for nothing else, the check that
was deliberately deferred to the analysis was deferred there and passed
there, and the local checkout path went nowhere.

The forward looking text that stood here is not reproduced. It is in the
history at the commits that carried it, which is where a promise belongs once
it has been kept.
