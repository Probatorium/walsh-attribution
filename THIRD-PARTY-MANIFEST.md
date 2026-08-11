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

**None.** No file from any other repository and no third party file has
entered this working copy. Nothing has been transcribed, downloaded or
copied in.

The apparatus reused from a closed lane is recorded in `PROVENANCE.md` and
not here, and the distinction is deliberate: those files were read and
rewritten, with the changes stated, so what is in this repository is this
lane's text with a declared origin. Nothing was copied byte for byte, so
there is no foreign blob to digest. If that ever changes, the file enters
here with its digest like anything else.

---

## The one entry this manifest expects

Named in advance so that its entry is expected rather than improvised.

### `data/king-wen-received.json`, not yet present

| field | value |
| --- | --- |
| origin | `kingwen-orderings-replication`, the deposit under audit |
| retrieval address | tag `zenodo-v3`, file `verify_paper.py`, symbol `KING_WEN` |
| access | read only, addressed at the tag; the neighbour's working tree is not moved, and that it did not move is confirmed after the read |
| rights | same lane, same author; the deposit carries a licence file at its tag, and this is a transcription of a factual sequence rather than of expression |
| use | the received King Wen order, the object of the whole analysis |
| status | received data, never recomputed in this lane |

**How it will be transcribed.** Mechanically, by a tool in this repository
that reads the blob at the tag through git and extracts the named symbol. It
will not be typed. A copying error is therefore not one of the ways this lane
can be wrong, and the tool can be run again by anyone with a checkout to
reproduce the file byte for byte.

**What will be checked on entry.** That the list has sixty-four entries, that
they are distinct, and that each lies in the range of a six bit value. Those
are checks on the transcription, not a recomputation of the sequence, which
would defeat the point of receiving it.

**What will deliberately not be checked on entry.** Whether the adjacency
pairing of the sequence is the rotation and complementation matching. That is
precondition P1 of `PREREGISTRATION.md` section (d), it belongs to the
analysis, and it is reported there whatever it says.

**Where the local checkout path will go.** Nowhere. The tool takes it on the
command line and stores it in no file. The repository and the tag identify
the source; a path on one machine identifies an account.
