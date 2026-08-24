"""Copia i documenti pubblicabili dal repo del tema a questo sito.

I sorgenti vivono in THCabina/docs/ e sono la versione autorevole: qui si
rigenerano, non si modificano a mano. Aggiunge il front matter di Jekyll e
riscrive i riferimenti interni (segnaposto, link .md -> .html).

    python sync.py            # assume ../THCabina accanto a questa cartella
    python sync.py C:/THCabina
"""

import io
import os
import sys

PAGES = [
    ("docs/merchant-guide.md", "guide.md", "Theme guide"),
    ("docs/support-policy.md", "support-policy.md", "Support policy"),
]

REPLACEMENTS = [
    ("[[SUPPORT_FORM_URL]]", "support.html"),
    ("./support-policy.md", "support-policy.html"),
    ("./merchant-guide.md", "guide.html"),
]

here = os.path.dirname(os.path.abspath(__file__))
theme = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, os.pardir, "THCabina")

for src, dest, title in PAGES:
    path = os.path.join(theme, src)
    text = io.open(path, encoding="utf-8").read()
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    if "[[" in text:
        print("ATTENZIONE: segnaposto residui in %s" % dest)
    out = "---\nlayout: default\ntitle: %s\n---\n\n%s" % (title, text)
    io.open(os.path.join(here, dest), "w", encoding="utf-8", newline="\n").write(out)
    print("%s -> %s" % (src, dest))
