"""Transcribe the received King Wen sequence from the deposit under audit.

`CONTACT-RULES.md` rule seven and `THIRD-PARTY-MANIFEST.md`: the sequence
enters as received data, mechanically extracted and not typed, marked as
received, never recomputed here, and credited to the deposit it came from.

It is extracted rather than copied by hand so that a transcription error is
not one of the ways this lane can be wrong. Anyone with a checkout of the
neighbour can run this and reproduce the file byte for byte.

The local checkout is passed on the command line and is stored nowhere. The
repository and the tag identify the source.

Usage:
    python tools/receive_kingwen.py --kingwen-checkout PATH
"""

import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "analysis"))

import neighbour

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data" / "king-wen-received.json"

SOURCE_FILE = "verify_paper.py"
SYMBOL = "KING_WEN"
LITERAL = re.compile(r"^KING_WEN\s*=\s*(\[[^\]]*\])", re.MULTILINE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kingwen-checkout", required=True)
    a = ap.parse_args()

    blob, blob_digest = neighbour.read_at_ref(
        a.kingwen_checkout, neighbour.KINGWEN_TAG, SOURCE_FILE)
    text = blob.decode("utf-8")

    match = LITERAL.search(text)
    if not match:
        raise SystemExit(f"{SYMBOL} not found in {SOURCE_FILE} at "
                         f"{neighbour.KINGWEN_TAG}")
    values = ast.literal_eval(match.group(1))

    # Checks on the transcription, not on the sequence. Recomputing the
    # sequence is exactly what receiving it forbids.
    if len(values) != 64:
        raise SystemExit(f"transcription has {len(values)} entries, not 64")
    if len(set(values)) != 64:
        raise SystemExit("transcription has repeated entries")
    if not all(isinstance(v, int) and 0 <= v < 64 for v in values):
        raise SystemExit("transcription has an entry outside a six bit value")

    payload = {
        "what": "the received King Wen sequence, position to hexagram value",
        "status": "received data, never recomputed in this lane",
        "convention": ("line 1 is the bottom line and the most significant "
                       "bit, a solid line is one, so Kun is 0 and Qian is 63, "
                       "as stated in the header of the source file"),
        "origin_repository": "kingwen-orderings-replication",
        "origin_deposit": "10.5281/zenodo.21776041",
        "origin_ref": neighbour.KINGWEN_TAG,
        "origin_file": SOURCE_FILE,
        "origin_symbol": SYMBOL,
        "origin_file_sha256": blob_digest,
        "extracted_by": "tools/receive_kingwen.py",
        "values": values,
    }
    TARGET.parent.mkdir(exist_ok=True)
    body = json.dumps(payload, indent=2) + "\n"
    TARGET.write_text(body, encoding="utf-8", newline="\n")

    print(f"source     {neighbour.KINGWEN_TAG}:{SOURCE_FILE}")
    print(f"           sha256 {blob_digest}")
    print(f"written    {TARGET.relative_to(ROOT)}")
    print(f"           sha256 {hashlib.sha256(body.encode()).hexdigest()}")
    print(f"neighbour still on its own branch: "
          f"{'yes' if neighbour.branch_of(a.kingwen_checkout) else 'unknown'}")
    print("checks on the transcription: sixty-four entries, all distinct, "
          "all inside a six bit value")
    return 0


if __name__ == "__main__":
    sys.exit(main())
