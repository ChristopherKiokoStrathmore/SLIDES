#!/usr/bin/env python3
"""Inline every dependency into one standalone deck file.

A presentation must not depend on the venue's wifi. GSAP, Three.js, Motion One,
Animate.css and the county table are all embedded, so `covid-capacity-deck.html`
opens from a USB stick, an email attachment or file:// with no server and no
network.

The deck carries no map, so it needs none of the boundary geometry and no D3.
Only the county properties are inlined, which takes the payload from ~72 KB to
under 10 KB.

    python3 presentation/build_deck.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "presentation" / "deck.template.html"
OUT = ROOT / "presentation" / "covid-capacity-deck.html"

PARTS = {
    "__GSAP__": ROOT / "vendor" / "gsap.min.js",
    "__THREE__": ROOT / "vendor" / "three.min.js",
    "__MOTION__": ROOT / "vendor" / "motion.min.js",
    "__ANIMATECSS__": ROOT / "vendor" / "animate.min.css",
}

# only the fields the deck actually reads, so nothing unused ships
FIELDS = ["county", "ckey", "pop", "beds", "beds_per_10k", "largest_share",
          "n_bedded", "lvl5plus"]

html = SRC.read_text(encoding="utf-8")

# The one failure mode that survives a green build: an em dash slipping back
# into the copy. Count on the template, before vendor code (full of them) lands.
strays = html.count("—") + html.count("&mdash;")

geo = json.loads((ROOT / "data" / "web_data.json").read_text(encoding="utf-8"))
counties = [{k: f["properties"][k] for k in FIELDS} for f in geo["features"]]
if len(counties) != 47:
    sys.exit(f"expected 47 counties, got {len(counties)}")

if "__DATA__" not in html:
    sys.exit("template is missing the __DATA__ placeholder")
html = html.replace("__DATA__", json.dumps(counties, separators=(",", ":")))

for token, path in PARTS.items():
    if token not in html:
        sys.exit(f"template is missing the {token} placeholder")
    if not path.exists():
        sys.exit(f"missing build input: {path.relative_to(ROOT)}")

    body = path.read_text(encoding="utf-8")

    # r150's UMD bundle opens with a deprecation console.warn. It is harmless
    # but it is the first thing anyone sees if they open devtools mid-talk.
    if token == "__THREE__" and body.lstrip().startswith("console.warn("):
        body = body.split("\n", 1)[1]

    html = html.replace(token, body)

OUT.write_text(html, encoding="utf-8")

note = f"  [warn] {strays} em dash(es) in copy" if strays else "  [ok] no em dashes in copy"
print(f"built {OUT.relative_to(ROOT)}  ({OUT.stat().st_size / 1024:.0f} KB, self-contained)")
print(note)
