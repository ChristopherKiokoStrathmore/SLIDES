#!/usr/bin/env python3
"""Inject data/web_data.json into src/app.template.html and write index.html.

The data is embedded rather than fetched so the page works from file:// with no
server and no CORS headaches - an examiner can double-click index.html offline.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
tpl = (ROOT / "src" / "app.template.html").read_text()
data = (ROOT / "data" / "web_data.json").read_text()

if "__DATA__" not in tpl:
    sys.exit("template is missing the __DATA__ placeholder")

out = ROOT / "index.html"
out.write_text(tpl.replace("__DATA__", data))
print(f"built {out.relative_to(ROOT)}  ({out.stat().st_size / 1024:.0f} KB)")
