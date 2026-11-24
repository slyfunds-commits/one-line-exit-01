#!/usr/bin/env python3
"""One-Line Exit R1 entry: "The Mother's Objection".

The stated reason (family) is a fabrication, confessed in the last beat --
but the confession comes from the invented person herself, via HR
(P4 wronged-party testifies + P10 familiar-phrase hijack + P1 self-sealing).
Reversal test: "we have never met" re-reads "care for my mother" -- the
reason collapses, the mother denies the relationship.
"""

import os

ENTRY = "I am resigning to care for my mother, who has written to HR to say we have never met."

# Gate: 1 to 140 characters, no trailing newline.
assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} outside 1-140"
assert ENTRY == ENTRY.strip(), "entry has leading/trailing whitespace"
# Reversal check: the last beat must redefine the earlier beats.
assert ENTRY.endswith("we have never met."), "punch must land in the last words"
assert "mother" in ENTRY and "HR" in ENTRY, "setup must name the family and the workplace"
# Second-beat check: "written to HR" is the second laugh -- the mother went
# to HR, a specific workplace detail, not just a denial. Economy: the punch
# sits in the last 4 words; the line must parse in a single read-aloud.
assert ENTRY.count(" ") >= 10, "line too terse to carry setup + turn"
assert len(ENTRY.encode("utf-8")) == len(ENTRY), "entry must be pure ASCII (no multi-byte chars)"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
