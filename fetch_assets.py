#!/usr/bin/env python3
import os
import re
import urllib.request
from urllib.error import URLError, HTTPError

ROOT = os.path.dirname(os.path.abspath(__file__))
HTML_IN = os.path.join(ROOT, "index.html")
HTML_BACKUP = os.path.join(ROOT, "index.backup.html")
ASSETS_DIR = os.path.join(ROOT, "assets")

os.makedirs(ASSETS_DIR, exist_ok=True)

with open(HTML_IN, "r", encoding="utf-8") as f:
    html = f.read()

urls = sorted(set(re.findall(r"https://www\\.figma\\.com/api/mcp/asset/[a-z0-9\\-]+", html)))
url_to_local = {}
failed = []

for u in urls:
    name = u.rsplit("/", 1)[-1]
    req = urllib.request.Request(
        u,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            data = resp.read()
            ctype = (resp.headers.get("Content-Type") or "").lower()

        ext = ".bin"
        if "image/png" in ctype:
            ext = ".png"
        elif "image/jpeg" in ctype:
            ext = ".jpg"
        elif "image/webp" in ctype:
            ext = ".webp"
        elif "image/gif" in ctype:
            ext = ".gif"
        elif "image/svg+xml" in ctype:
            ext = ".svg"

        filename = f"{name}{ext}"
        with open(os.path.join(ASSETS_DIR, filename), "wb") as wf:
            wf.write(data)
        url_to_local[u] = f"assets/{filename}"
    except (URLError, HTTPError, TimeoutError, OSError) as e:
        failed.append((u, str(e)))

for u, lp in url_to_local.items():
    html = html.replace(u, lp)

if not os.path.exists(HTML_BACKUP):
    with open(HTML_IN, "r", encoding="utf-8") as src:
        original = src.read()
    with open(HTML_BACKUP, "w", encoding="utf-8") as f:
        f.write(original)

with open(HTML_IN, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Downloaded: {len(url_to_local)}/{len(urls)}")
print("Updated: index.html (backup: index.backup.html)")
if failed:
    print("Failed URLs:")
    for u, err in failed:
        print(f"- {u} :: {err}")

