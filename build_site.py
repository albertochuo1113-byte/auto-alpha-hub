import os, glob

posts = sorted(glob.glob("posts/*.md"), reverse=True)
items_html = ""

for p in posts:
    with open(p, "r", encoding="utf-8") as f:
        lines = f.readlines()
    title = p.replace("posts/", "").replace(".md", "")
    for line in lines:
        if line.startswith("title:"):
            title = line.replace("title:", "").strip().strip('"').strip("'")
            break
    items_html += f'<li><a href="{p}">{title}</a></li>\n'

index_html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alberto's Alpha Hub | 自動化資產情報站</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 750px; margin: 40px auto; padding: 0 20px; line-height: 1.6; color: #222; }}
        h1 {{ border-bottom: 2px solid #eaeaea; padding-bottom: 12px; }}
        ul {{ list-style-type: none; padding-left: 0; }}
        li {{ padding: 10px 0; border-bottom: 1px solid #f0f0f0; }}
        a {{ text-decoration: none; color: #0969da; font-weight: 500; font-size: 1.1rem; }}
        a:hover {{ text-decoration: underline; }}
        .badge {{ background: #f6f8fa; padding: 4px 8px; border-radius: 4px; font-size: 0.85rem; color: #57606a; }}
    </style>
</head>
<body>
    <h1>🚀 Alberto's Alpha Hub <span class="badge">AI 24/7 自動運轉</span></h1>
    <p>聚焦自營交易風控、AI 自動化工作流與數位資產增長。</p>
    <ul>
        {items_html}
    </ul>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("SUCCESS: index.html generated!")
