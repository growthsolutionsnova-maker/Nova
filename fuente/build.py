#!/usr/bin/env python3
"""Assemble NOVA index.html from src/ blocks and embed fonts as base64."""
import base64, glob, os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/tmp/claude-0/-home-claude/06c518f2-8d74-5523-b3f1-427d6d599d5e/scratchpad/fonts"
font_files = {
    "FONT_INTER": f"{FONTS}/fontsource-variable-inter-5.3.0/files/inter-latin-wght-normal.woff2",
    "FONT_CG": f"{FONTS}/fontsource-variable-cormorant-garamond/files/cormorant-garamond-latin-wght-normal.woff2",
    "FONT_CG_I": f"{FONTS}/fontsource-variable-cormorant-garamond/files/cormorant-garamond-latin-wght-italic.woff2",
}
blocks = sorted(p for p in glob.glob(f"{ROOT}/src/[a-z]-*.html"))
html = "".join(open(p, encoding="utf-8").read() for p in blocks)
if "<body" not in html:  # only head so far -> append style-tile preview
    html += open(f"{ROOT}/src/_preview-a.html", encoding="utf-8").read()
elif "</body>" not in html:  # footer block not built yet -> temporary tail for preview
    tail = ('<section class="section" style="min-height:60vh"><div class="container center">'
            '<p class="eyebrow eyebrow--center">Preview</p><p class="lead" style="margin:16px auto 0">'
            'Next blocks will continue here.</p></div></section></main>')
    parts = html.split("<script>\n/* ====", 1)
    html = parts[0] + tail + ("<script>\n/* ====" + parts[1] if len(parts) > 1 else "") + "</body></html>"
fonts_css = open(f"{ROOT}/src/_fonts.css", encoding="utf-8").read()
# Fonts load at the end of <body>: text paints immediately with the fallback, then swaps (faster first paint).
html = html.replace("</body>", "<style>" + fonts_css + "</style>\n</body>", 1)
for key, path in font_files.items():
    html = html.replace("{{%s}}" % key, base64.b64encode(open(path, "rb").read()).decode())
imgs_png = {}
html = html.replace("{{IMG_LOGO}}", "data:image/png;base64," + base64.b64encode(open(f"{ROOT}/img/logo-nav.png", "rb").read()).decode())
for key, path in imgs_png.items():
    html = html.replace("{{%s}}" % key, "data:image/png;base64," + base64.b64encode(open(f"{ROOT}/{path}", "rb").read()).decode())
imgs = {"IMG_TREE_D":"img/tree-d.jpg","IMG_TREE_M":"img/tree-m.jpg","IMG_ALEGRIA_D":"img/alegria-d.jpg","IMG_ALEGRIA_M":"img/alegria-m.jpg"}
for key, path in imgs.items():
    html = html.replace("{{%s}}" % key, "data:image/jpeg;base64," + base64.b64encode(open(f"{ROOT}/{path}", "rb").read()).decode())
import json
ns = {}; exec(open(f"{ROOT}/i18n.py", encoding="utf-8").read(), ns)
dic = {"es": {k: v[0] for k, v in ns["T"].items()}, "pt": {k: v[1] for k, v in ns["T"].items()}}
html = html.replace("{{I18N}}", json.dumps(dic, ensure_ascii=False).replace("</", "<\\/"))
out = sys.argv[1] if len(sys.argv) > 1 else f"{ROOT}/index.html"
open(out, "w", encoding="utf-8").write(html)
print(out, f"{len(html.encode())/1024:.1f} KB")
