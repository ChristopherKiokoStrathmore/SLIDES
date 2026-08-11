#!/usr/bin/env python3
"""Render TALKING-POINTS.md to a print-ready PDF.

Presenters hold this on paper while they speak, so it is typeset for paper and
not for a screen: ink on white, each speaker starting on a fresh page, and the
spoken lines set apart from the notes about them so nobody reads a stage
direction out loud by mistake.

The markdown here uses a small, known subset (headings, tables, blockquotes,
bullets, ordered lists, rules, bold/italic/code), so this converts that subset
directly rather than pulling in a dependency the marker would have to install.

    python3 presentation/build_talking_points_pdf.py
"""
import html
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "presentation" / "TALKING-POINTS.md"
TMP = ROOT / "presentation" / "_talking-points.print.html"
OUT = ROOT / "presentation" / "TALKING-POINTS.pdf"

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]


def inline(s: str) -> str:
    """Escape, then re-introduce only the inline marks we actually use."""
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    return s


def cells(row: str):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def quote(text: str) -> str:
    """Spoken lines and stage directions must not look alike.

    The worst thing that can happen on stage is a presenter reading a note to
    themselves out loud. A line that opens with a quotation mark is scripted
    speech and gets the loud treatment; anything else is a direction and is set
    quietly, in italic, with no colour.
    """
    kind = "say" if text.lstrip().startswith(("\"", "&quot;")) else "note"
    return f'<blockquote class="{kind}">{inline(text)}</blockquote>'


def convert(md: str) -> str:
    lines = md.split("\n")
    out, i = [], 0

    while i < len(lines):
        ln = lines[i]

        # table: a header row followed by a |---|---| rule
        if ln.lstrip().startswith("|") and i + 1 < len(lines) and \
                re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            head = cells(ln)
            i += 2
            body = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                body.append(cells(lines[i]))
                i += 1
            out.append("<table><thead><tr>" +
                       "".join(f"<th>{inline(c)}</th>" for c in head) +
                       "</tr></thead><tbody>")
            for r in body:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table>")
            continue

        # blockquote
        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").strip())
                i += 1
            out.append(quote(" ".join(x for x in buf if x)))
            continue

        # ordered list. Items may hold a spoken line, and may be separated by
        # blank lines: without the lookahead below each item becomes its own
        # <ol> and the printed list reads "1. 1. 1.".
        if re.match(r"^\d+\.\s", ln):
            items = []
            while i < len(lines):
                cur = lines[i]
                if re.match(r"^\d+\.\s", cur):
                    items.append([re.sub(r"^\d+\.\s+", "", cur)])
                    i += 1
                elif items and cur.startswith("   ") and cur.strip():
                    items[-1].append(cur.strip())
                    i += 1
                elif not cur.strip():
                    j = i
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and (re.match(r"^\d+\.\s", lines[j]) or
                                           (lines[j].startswith("   ") and lines[j].strip())):
                        i = j
                    else:
                        break
                else:
                    break
            out.append("<ol>")
            for blocks in items:
                out.append("<li>")
                for b in blocks:
                    out.append(quote(b.lstrip(">").strip()) if b.startswith(">")
                               else f"<p>{inline(b)}</p>")
                out.append("</li>")
            out.append("</ol>")
            continue

        # bullets
        if ln.startswith("- "):
            out.append("<ul>")
            while i < len(lines) and lines[i].startswith("- "):
                out.append(f"<li>{inline(lines[i][2:])}</li>")
                i += 1
            out.append("</ul>")
            continue

        if ln.startswith("#"):
            lvl = len(ln) - len(ln.lstrip("#"))
            out.append(f"<h{lvl}>{inline(ln[lvl:].strip())}</h{lvl}>")
            i += 1
            continue

        if ln.strip() == "---":
            out.append("<hr>")
            i += 1
            continue

        if ln.strip():
            buf = []
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(
                    ("#", ">", "- ", "|")) and lines[i].strip() != "---" \
                    and not re.match(r"^\d+\.\s", lines[i]):
                buf.append(lines[i].strip())
                i += 1
            out.append(f"<p>{inline(' '.join(buf))}</p>")
            continue

        i += 1

    return "\n".join(out)


CSS = """
@page { size: A4; margin: 17mm 15mm 16mm; }
*{box-sizing:border-box}
body{
  font-family:"Segoe UI",system-ui,-apple-system,sans-serif;
  font-size:10.2pt; line-height:1.5; color:#16181d; margin:0;
  -webkit-print-color-adjust:exact; print-color-adjust:exact;
}
h1{font-size:19pt;line-height:1.15;letter-spacing:-.02em;margin:0 0 4pt}
h1 em{font-style:normal;color:#b3312a}
h2{font-size:13.5pt;letter-spacing:-.01em;margin:16pt 0 6pt;padding-bottom:3pt;
   border-bottom:1.5pt solid #16181d}
/* every speaker, and every slide, starts on a clean page: nobody wants to turn
   a page mid-sentence while six people are watching them */
h1,h2{page-break-before:always;break-before:page}
h1:first-of-type,h2:first-of-type{page-break-before:auto;break-before:auto}
/* a slide divider is a heading plus one line, so it must not burn a page of
   its own: keep it with the first speaker of that slide */
h1 + blockquote + h2{page-break-before:avoid;break-before:avoid}
h1 + p, h1 + p + p{color:#4a4f57}
hr{border:0;border-top:.6pt solid #d3d6dc;margin:12pt 0}
p{margin:6pt 0}
ul,ol{margin:6pt 0 6pt 16pt;padding:0}
li{margin:4pt 0}
strong{font-weight:650}
code{font-family:Consolas,ui-monospace,monospace;font-size:9pt;background:#f0f1f4;
  padding:.5pt 3pt;border-radius:2pt}

/* say this out loud */
blockquote.say{
  margin:7pt 0; padding:7pt 10pt 7pt 12pt;
  border-left:2.5pt solid #b3312a; background:#faf6f5;
  font-size:11pt; line-height:1.45; color:#16181d;
}
blockquote.say strong{color:#8f251f}
blockquote.say::before{
  content:"SAY"; display:block; font-size:6.6pt; letter-spacing:.14em;
  color:#b3312a; font-weight:700; margin-bottom:2pt;
}
/* do not say this out loud */
blockquote.note{
  margin:6pt 0; padding:2pt 0 2pt 11pt; border-left:1.5pt solid #c3c7ce;
  color:#5b616b; font-style:italic; font-size:9.6pt;
}

table{width:100%;border-collapse:collapse;margin:8pt 0;font-size:9.2pt}
th{text-align:left;font-size:7.6pt;letter-spacing:.09em;text-transform:uppercase;
   color:#5b616b;font-weight:700;padding:0 6pt 4pt 0;border-bottom:1pt solid #16181d}
td{padding:5pt 6pt 5pt 0;border-bottom:.6pt solid #e2e5ea;vertical-align:top;line-height:1.4}
tr{break-inside:avoid}
blockquote,table,h2,h3{break-inside:avoid}
h3{font-size:11pt;margin:11pt 0 4pt}
"""


def main():
    if not SRC.exists():
        sys.exit(f"missing {SRC}")

    body = convert(SRC.read_text(encoding="utf-8"))
    TMP.write_text(
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
        "<title>Talking points, How prepared is Kenya for a disease outbreak?</title>"
        f"<style>{CSS}</style></head><body>{body}</body></html>",
        encoding="utf-8")

    chrome = next((c for c in CHROME_CANDIDATES if pathlib.Path(c).exists()), None) \
        or shutil.which("chrome") or shutil.which("google-chrome")
    if not chrome:
        sys.exit("Chrome not found. The styled HTML is at "
                 f"{TMP.relative_to(ROOT)}; open it and print to PDF.")

    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={OUT}", TMP.as_uri()],
                   check=True, capture_output=True, timeout=120)

    TMP.unlink(missing_ok=True)
    print(f"built {OUT.relative_to(ROOT)}  ({OUT.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
