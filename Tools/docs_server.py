#!/usr/bin/env python3
"""Tiny static viewer for the Nagram Extera documentation tree.

Serves the repository's Markdown files (README.md and the documentations/
folder) as styled HTML on port 5000. This is a development convenience for
browsing the docs in a workspace preview pane; it is not part of the app
itself and is not shipped in any release artifact.
"""

from __future__ import annotations

import html
import http.server
import os
import re
import socketserver
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "documentations"
PORT = int(os.environ.get("PORT", "5000"))

PAGE_CSS = """
:root {
  color-scheme: light dark;
  --bg: #0b0d10;
  --panel: #11151a;
  --fg: #e6edf3;
  --muted: #8b949e;
  --accent: #4ea1ff;
  --border: #1f242c;
  --code-bg: #161b22;
}
@media (prefers-color-scheme: light) {
  :root {
    --bg: #f6f8fa; --panel: #ffffff; --fg: #1f2328;
    --muted: #57606a; --accent: #0969da;
    --border: #d0d7de; --code-bg: #eef1f4;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0; font: 15px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI",
       Helvetica, Arial, sans-serif;
  background: var(--bg); color: var(--fg);
}
.layout { display: grid; grid-template-columns: 280px 1fr; min-height: 100vh; }
nav {
  background: var(--panel); border-right: 1px solid var(--border);
  padding: 24px 18px; position: sticky; top: 0; height: 100vh; overflow: auto;
}
nav h1 { font-size: 16px; margin: 0 0 4px; }
nav p.tag { color: var(--muted); font-size: 12px; margin: 0 0 18px; }
nav h2 { font-size: 11px; text-transform: uppercase; letter-spacing: .08em;
         color: var(--muted); margin: 18px 0 6px; }
nav a { display: block; color: var(--fg); text-decoration: none;
        padding: 6px 8px; border-radius: 6px; font-size: 14px; }
nav a:hover { background: var(--code-bg); }
nav a.active { background: var(--accent); color: #fff; }
main { padding: 32px 48px; max-width: 980px; }
article a { color: var(--accent); }
article h1, article h2, article h3 { line-height: 1.25; }
article h1 { border-bottom: 1px solid var(--border); padding-bottom: 8px; }
article h2 { margin-top: 2em; border-bottom: 1px solid var(--border);
             padding-bottom: 6px; }
article code { background: var(--code-bg); padding: 1px 6px; border-radius: 4px;
               font-size: 13px; }
article pre { background: var(--code-bg); padding: 14px 16px; border-radius: 8px;
              overflow: auto; font-size: 13px; }
article pre code { background: transparent; padding: 0; }
article table { border-collapse: collapse; width: 100%; margin: 1em 0; }
article th, article td { border: 1px solid var(--border); padding: 8px 12px;
                         text-align: left; }
article th { background: var(--code-bg); }
article blockquote { border-left: 4px solid var(--accent); margin: 1em 0;
                     padding: 4px 14px; color: var(--muted); }
footer { color: var(--muted); font-size: 12px; margin-top: 48px;
         border-top: 1px solid var(--border); padding-top: 14px; }
@media (max-width: 760px) {
  .layout { grid-template-columns: 1fr; }
  nav { position: static; height: auto; }
}
"""


def list_docs() -> list[tuple[str, str]]:
    pages = [("/", "README")]
    if DOCS_DIR.is_dir():
        for p in sorted(DOCS_DIR.glob("*.md")):
            pages.append((f"/{p.relative_to(ROOT).as_posix()}", p.stem))
    return pages


def render_markdown(text: str) -> str:
    """A deliberately small Markdown renderer.

    Pulling in `markdown` or `mistune` would mean a package install for a
    workspace preview that nobody ships. The subset implemented below covers
    every construct the docs actually use (headings, lists, tables, fenced
    code, blockquotes, inline code, bold, italic, links).
    """
    html_lines: list[str] = []
    in_code = False
    code_buf: list[str] = []
    in_table = False
    table_buf: list[str] = []
    in_list = False
    list_tag = ""

    def flush_table() -> None:
        nonlocal in_table, table_buf
        if not table_buf:
            in_table = False
            return
        rows = [r for r in table_buf if r.strip()]
        if len(rows) < 2:
            html_lines.extend(rows)
        else:
            header = [c.strip() for c in rows[0].strip().strip("|").split("|")]
            body_rows = [
                [c.strip() for c in r.strip().strip("|").split("|")]
                for r in rows[2:]
            ]
            out = ["<table><thead><tr>"]
            out += [f"<th>{inline(c)}</th>" for c in header]
            out.append("</tr></thead><tbody>")
            for r in body_rows:
                out.append("<tr>")
                out += [f"<td>{inline(c)}</td>" for c in r]
                out.append("</tr>")
            out.append("</tbody></table>")
            html_lines.append("".join(out))
        table_buf = []
        in_table = False

    def close_list() -> None:
        nonlocal in_list, list_tag
        if in_list:
            html_lines.append(f"</{list_tag}>")
            in_list = False
            list_tag = ""

    def inline(s: str) -> str:
        # Protect inline HTML tags (<a>, <br>, <img>, <div>, etc.) and HTML
        # entities from being html-escaped, then restore them after escaping.
        placeholders: list[str] = []

        def stash(match: re.Match) -> str:
            placeholders.append(match.group(0))
            return f"\x00{len(placeholders) - 1}\x00"

        s = re.sub(r"</?[a-zA-Z][^<>]*>|&[a-zA-Z]+;|&#\d+;", stash, s)
        s = html.escape(s, quote=False)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(
            r"!\[([^\]]*)\]\(([^)]+)\)",
            lambda m: f'<img alt="{html.escape(m.group(1))}" src="{html.escape(m.group(2))}">',
            s,
        )
        s = re.sub(
            r"\[([^\]]+)\]\(([^)]+)\)",
            lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>',
            s,
        )
        s = re.sub(r"\x00(\d+)\x00", lambda m: placeholders[int(m.group(1))], s)
        return s

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            if in_code:
                html_lines.append(
                    "<pre><code>" + html.escape("\n".join(code_buf)) + "</code></pre>"
                )
                code_buf = []
                in_code = False
            else:
                close_list()
                flush_table()
                in_code = True
            continue
        if in_code:
            code_buf.append(raw)
            continue

        if "|" in line and re.match(r"^\s*\|.*\|\s*$", line):
            close_list()
            in_table = True
            table_buf.append(line)
            continue
        if in_table:
            flush_table()

        if not line.strip():
            close_list()
            html_lines.append("")
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            close_list()
            level = len(m.group(1))
            html_lines.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue

        if line.startswith("> "):
            close_list()
            html_lines.append(f"<blockquote>{inline(line[2:])}</blockquote>")
            continue

        m = re.match(r"^(\s*)([-*])\s+(.*)$", line)
        if m:
            if not in_list or list_tag != "ul":
                close_list()
                html_lines.append("<ul>")
                in_list, list_tag = True, "ul"
            html_lines.append(f"<li>{inline(m.group(3))}</li>")
            continue
        m = re.match(r"^(\s*)\d+\.\s+(.*)$", line)
        if m:
            if not in_list or list_tag != "ol":
                close_list()
                html_lines.append("<ol>")
                in_list, list_tag = True, "ol"
            html_lines.append(f"<li>{inline(m.group(2))}</li>")
            continue

        if re.match(r"^-{3,}$", line):
            close_list()
            html_lines.append("<hr>")
            continue

        close_list()
        if re.match(r"^\s*</?(div|p|section|article|header|footer|hr|br|img|center|details|summary)\b", line, re.I):
            html_lines.append(line)
        else:
            html_lines.append(f"<p>{inline(line)}</p>")

    if in_code:
        html_lines.append("<pre><code>" + html.escape("\n".join(code_buf)) + "</code></pre>")
    flush_table()
    close_list()
    return "\n".join(html_lines)


def page(title: str, body_html: str, current: str) -> bytes:
    nav_links = "".join(
        f'<a href="{href}" class="{"active" if href == current else ""}">{label}</a>'
        for href, label in list_docs()
    )
    out = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Nagram Extera docs</title>
<style>{PAGE_CSS}</style>
</head><body>
<div class="layout">
  <nav>
    <h1>Nagram Extera</h1>
    <p class="tag">Documentation preview</p>
    <h2>Pages</h2>
    {nav_links}
  </nav>
  <main>
    <article>{body_html}</article>
    <footer>Rendered locally from the repository — this server is a workspace
    convenience and is never shipped with the app.</footer>
  </main>
</div>
</body></html>"""
    return out.encode("utf-8")


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:  # noqa: D401
        print("[docs] " + fmt % args, flush=True)

    def do_GET(self) -> None:  # noqa: N802
        path = unquote(self.path.split("?", 1)[0])
        if path in ("/", "/index", "/index.html"):
            target = ROOT / "README.md"
            current = "/"
            title = "README"
        elif path.startswith("/documentations/") and path.endswith(".md"):
            target = (ROOT / path.lstrip("/")).resolve()
            current = path
            title = target.stem
            if ROOT not in target.parents:
                self.send_error(403)
                return
        else:
            self.send_error(404, "Not a documentation page")
            return

        if not target.is_file():
            self.send_error(404, f"Missing: {target}")
            return

        body = render_markdown(target.read_text(encoding="utf-8"))
        payload = page(title, body, current)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)


class ReusableServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def main() -> None:
    with ReusableServer(("0.0.0.0", PORT), Handler) as srv:
        print(f"[docs] serving Nagram Extera documentation on http://0.0.0.0:{PORT}", flush=True)
        srv.serve_forever()


if __name__ == "__main__":
    main()
