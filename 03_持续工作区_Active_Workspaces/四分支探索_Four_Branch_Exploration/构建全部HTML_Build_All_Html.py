#!/usr/bin/env python3
"""Generate 7 HTML files: 1 overview + 5 branch-specific, matching the new numbered folder structure."""
import os, re, html

BASE = os.path.dirname(os.path.abspath(__file__))

BRANCHES = [
    ("01_Branch_A_RAT", "A", "Branch A · RAT 轨迹框架（序列分析）", "badge-a"),
    ("02_Branch_B_本体论", "B", "Branch B · DeFi 决策本体论", "badge-b"),
    ("03_Branch_C_HAM", "C", "Branch C · 异质预期与演化响应函数", "badge-c"),
    ("04_Branch_D_数据驱动", "D", "Branch D · 数据驱动安全网", "badge-d"),
    ("05_Branch_E_CuspRAT", "E", "Branch E · Cusp RAT 动力系统框架", "badge-e"),
]

# ─── Markdown to HTML ──────────────────────────────────────────────────────
def md_to_html(text):
    text = html.escape(text)
    text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'```(?:\w*\n)?(.*?)```', r'<pre><code>\1</code></pre>', text, flags=re.DOTALL)
    text = re.sub(r'^---$', r'<hr>', text, flags=re.MULTILINE)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)

    lines = text.split('\n')
    result = []
    in_table = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|'):
            if not in_table:
                in_table = True
                result.append('<table>')
            cells = [c.strip() for c in stripped[1:-1].split('|')]
            is_header = all(re.match(r'^[-:\s]+$', c) for c in cells)
            if is_header:
                continue
            is_prev_sep = (i > 0 and lines[i-1].strip().startswith('|') and 
                          all(re.match(r'^[-:\s]+$', c.strip()) for c in lines[i-1].strip()[1:-1].split('|')))
            tag = 'th' if is_prev_sep else 'td'
            result.append('<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>')
            continue
        elif in_table:
            result.append('</table>')
            in_table = False
        if stripped == '':
            result.append('')
        elif stripped.startswith('<h') or stripped.startswith('<table') or stripped.startswith('<pre') or stripped.startswith('<hr') or stripped.startswith('<tr'):
            result.append(stripped)
        elif stripped.startswith('<li') or stripped.startswith('</ul') or stripped.startswith('<ol') or stripped.startswith('<ul'):
            result.append(stripped)
        elif re.match(r'^\d+\.\s', stripped):
            result.append(stripped)
        else:
            result.append(stripped)
    if in_table:
        result.append('</table>')

    final = []
    buf = []
    for line in result:
        if line == '':
            if buf:
                final.append('<p>' + ' '.join(buf) + '</p>')
                buf = []
            final.append('')
        elif line.startswith('<'):
            if buf:
                final.append('<p>' + ' '.join(buf) + '</p>')
                buf = []
            final.append(line)
        else:
            buf.append(line)
    if buf:
        final.append('<p>' + ' '.join(buf) + '</p>')
    return '\n'.join(final)


# ─── CSS ─────────────────────────────────────────────────────────────────────
def css():
    return '''    <style>
      :root {
        --bg: #0d1117; --bg-secondary: #161b22; --border: #303d63;
        --text: #c9d1d9; --text-secondary: #8b949e; --accent: #58a6ff;
        --accent-hover: #79c0ff; --green: #3fb950; --orange: #d2991d;
        --red: #f85149; --purple: #a371f7; --code-bg: #1c2128;
        --heading: #f0f6fc; --link: #58a6ff; --table-header: #1c2128;
        --table-row-alt: #161b22; --teal: #39d2c0;
      }
      * { margin: 0; padding: 0; box-sizing: border-box; }
      body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
        background: var(--bg); color: var(--text); line-height: 1.6; font-size: 16px;
      }
      #sidebar {
        position: fixed; top: 0; left: 0; width: 320px; height: 100vh;
        background: var(--bg-secondary); border-right: 1px solid var(--border);
        overflow-y: auto; z-index: 100; padding: 20px;
      }
      #sidebar h2 {
        color: var(--heading); font-size: 18px; margin-bottom: 16px;
        padding-bottom: 12px; border-bottom: 1px solid var(--border);
      }
      #sidebar .nav-section-title {
        color: var(--accent); font-size: 12px; font-weight: 700;
        text-transform: uppercase; letter-spacing: 0.5px; margin: 16px 0 8px 0;
      }
      #sidebar nav a {
        display: block; color: var(--text-secondary); text-decoration: none;
        padding: 4px 0; font-size: 13px; transition: color 0.15s;
        white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
      }
      #sidebar nav a:hover { color: var(--accent-hover); }
      #content { margin-left: 340px; padding: 40px 60px; max-width: 1000px; }
      .doc-section {
        border: 1px solid var(--border); border-radius: 8px; padding: 32px;
        margin-bottom: 24px; background: var(--bg-secondary);
      }
      .doc-section h1 { font-size: 28px; color: var(--heading); margin-bottom: 8px; }
      .doc-section h2 { font-size: 22px; color: var(--heading); margin: 32px 0 12px; padding-bottom: 8px; border-bottom: 1px solid var(--border); }
      .doc-section h3 { font-size: 18px; color: var(--heading); margin: 24px 0 8px; }
      .doc-section h4 { font-size: 16px; color: var(--text); margin: 16px 0 6px; }
      .doc-section p { margin: 8px 0; }
      .doc-section a { color: var(--link); text-decoration: none; }
      .doc-section a:hover { text-decoration: underline; }
      .doc-section ul, .doc-section ol { margin: 8px 0 8px 24px; }
      .doc-section li { margin: 4px 0; }
      .doc-section hr { border: none; border-top: 1px solid var(--border); margin: 24px 0; }
      .doc-section code {
        background: var(--code-bg); padding: 2px 6px; border-radius: 4px;
        font-size: 0.9em; font-family: 'SF Mono', 'Fira Code', 'Fira Mono', Menlo, Consolas, monospace;
      }
      .doc-section pre {
        background: var(--code-bg); border: 1px solid var(--border); border-radius: 6px;
        padding: 16px; overflow-x: auto; margin: 12px 0; font-size: 13px; line-height: 1.5;
      }
      .doc-section pre code { background: none; padding: 0; }
      .doc-section table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 14px; }
      .doc-section th { background: var(--table-header); padding: 8px 12px; text-align: left; border: 1px solid var(--border); color: var(--heading); }
      .doc-section td { padding: 8px 12px; border: 1px solid var(--border); }
      .doc-section tr:nth-child(even) td { background: var(--table-row-alt); }
      .doc-section strong { color: var(--heading); }
      .doc-section em { color: var(--orange); }
      .file-path {
        color: var(--text-secondary); font-size: 12px; font-family: monospace;
        margin-bottom: 16px; padding: 6px 10px; background: var(--code-bg);
        border-radius: 4px; display: inline-block;
      }
      .branch-badge {
        display: inline-block; padding: 2px 8px; border-radius: 4px;
        font-size: 12px; font-weight: 600; margin-right: 8px;
      }
      .badge-a { background: rgba(88,166,255,0.15); color: var(--accent); }
      .badge-b { background: rgba(163,113,247,0.15); color: var(--purple); }
      .badge-c { background: rgba(63,185,80,0.15); color: var(--green); }
      .badge-d { background: rgba(210,153,29,0.15); color: var(--orange); }
      .badge-e { background: rgba(57,210,192,0.15); color: var(--teal); }
      .page-header {
        border-left: 3px solid var(--accent); padding: 16px 24px; margin-bottom: 32px;
        background: var(--bg-secondary); border-radius: 0 8px 8px 0;
      }
      .page-header.branch-b { border-left-color: var(--purple); }
      .page-header.branch-c { border-left-color: var(--green); }
      .page-header.branch-d { border-left-color: var(--orange); }
      .page-header.branch-e { border-left-color: var(--teal); }
      .page-header h1 { font-size: 28px; margin-bottom: 4px; }
      .page-header p { color: var(--text-secondary); margin: 0; }
      .nav-toggle {
        display: none; position: fixed; top: 12px; left: 12px; z-index: 200;
        background: var(--bg-secondary); border: 1px solid var(--border);
        color: var(--text); font-size: 20px; padding: 8px 12px;
        border-radius: 6px; cursor: pointer;
      }
      @media (max-width: 900px) {
        #sidebar { transform: translateX(-100%); transition: transform 0.3s; width: 280px; }
        #sidebar.open { transform: translateX(0); }
        #content { margin-left: 0; padding: 20px; }
        .nav-toggle { display: block; }
      }
    </style>'''


def head(title):
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
{css()}
</head>'''


# ─── Sidebar Component ───────────────────────────────────────────────────────
def sidebar(nav_links):
    """nav_links: list of (label, href, section_header_or_None)"""
    out = ['<button class="nav-toggle" onclick="document.getElementById(\'sidebar\').classList.toggle(\'open\')">&#9776;</button>',
           '<aside id="sidebar"><h2>四分支探索文档</h2><nav>']
    for label, href, sec in nav_links:
        if sec:
            out.append(f'<div class="nav-section-title">{html.escape(sec)}</div>')
        out.append(f'    <a href="{href}">{html.escape(label)}</a>')
    out.append('</nav></aside>')
    return '\n'.join(out)


def doc_section(body_html, relpath, badge_key=None):
    badge_html = ''
    if badge_key:
        badge_html = f'<span class="branch-badge badge-{badge_key.lower()}">Branch {badge_key.upper()}</span>'
    return f'''
  <div class="doc-section">
    {badge_html}<span class="file-path">{html.escape(relpath)}</span>
    {body_html}
  </div>'''


def footer_js():
    return '''<script>
  document.querySelectorAll('#sidebar a').forEach(link => {
    link.addEventListener('click', () => {
      document.getElementById('sidebar').classList.remove('open');
    });
  });
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth' }); }
    });
  });
</script>'''


# ─── Overview Sidebar ─────────────────────────────────────────────────────────
def overview_sidebar():
    return [
        ("四分支总览页面", "#top", None),
        ("", "", None),
        ("Branch A · RAT 轨迹框架（序列分析）", "../01_Branch_A_RAT/RAT_完整文档.html", "各分支入口"),
        ("Branch B · DeFi 决策本体论", "../02_Branch_B_本体论/本体论_完整文档.html", ""),
        ("Branch C · 异质预期与演化响应", "../03_Branch_C_HAM/HAM_完整文档.html", ""),
        ("Branch D · 数据驱动安全网", "../04_Branch_D_数据驱动/数据驱动_完整文档.html", ""),
        ("Branch E · Cusp RAT 动力系统", "../05_Branch_E_CuspRAT/CuspRAT_完整文档.html", ""),
        ("", "", None),
        ("总览与导航", "#doc_0", "本页目录"),
        ("Branch A 概述", "#doc_1", ""),
        ("Branch B 概述", "#doc_2", ""),
        ("Branch C 概述", "#doc_3", ""),
        ("Branch D 概述", "#doc_4", ""),
        ("交叉讨论与推荐路径", "#doc_5", ""),
    ]


# ─── Branch Sidebar ──────────────────────────────────────────────────────────
def branch_sidebar(current_key, branch_folder, md_count):
    BRANCH_META = {
        "A": ("Branch A · RAT 轨迹框架", "RAT_完整文档.html"),
        "B": ("Branch B · 决策本体论", "本体论_完整文档.html"),
        "C": ("Branch C · 异质预期演化", "HAM_完整文档.html"),
        "D": ("Branch D · 数据驱动安全网", "数据驱动_完整文档.html"),
        "E": ("Branch E · Cusp RAT 动力系统", "CuspRAT_完整文档.html"),
    }
    items = [
        ("返回总览", "../00_总览/总览_完整文档.html", "导航"),
    ]
    for key in ["A", "B", "C", "D", "E"]:
        if key == current_key:
            continue
        label, fname = BRANCH_META[key]
        href = f"../0{key}_Branch_{get_folder_suffix(key)}/{fname}"
        # build a proper path - the folder names are like 01_Branch_A_RAT
        items.append((label, href, ""))
    items.append(("本页文档", "#top", ""))
    for i in range(1, md_count + 1):
        items.append((f"  文档 {i}", f"#doc_{i}", ""))
    return items


def get_folder_suffix(key):
    mapping = {
        "A": "A_RAT",
        "B": "B_本体论",
        "C": "C_HAM",
        "D": "D_数据驱动",
        "E": "E_CuspRAT",
    }
    return mapping[key]


# ─── BUILD OVERVIEW PAGE ──────────────────────────────────────────────────────
def build_overview():
    overview_dir = os.path.join(BASE, "00_总览", "文献")
    if not os.path.isdir(overview_dir):
        print(f"[ERROR] Overview directory not found: {overview_dir}")
        return
    
    md_files = sorted([f for f in os.listdir(overview_dir) if f.endswith('.md')])
    
    parts = [head("四分支探索 — 总览")]
    parts.append('<body>')
    parts.append('<div id="top"></div>')
    parts.append(sidebar(overview_sidebar()))
    parts.append('<main id="content">')
    parts.append('<h1>2026-07-08 四分支探索（五分支版）</h1>')
    parts.append('<p style="color: var(--text-secondary); margin: 8px 0 32px;">UnusPay PhD 研究方向 — 五个候选深化路径的完整文档</p>')
    
    for i, fname in enumerate(md_files):
        fullpath = os.path.join(overview_dir, fname)
        with open(fullpath, 'r', encoding='utf-8') as f:
            raw = f.read()
        body_html = md_to_html(raw)
        parts.append(f'<div id="doc_{i}">')
        parts.append(doc_section(body_html, f"00_总览/文献/{fname}"))
        parts.append('</div>')
    
    parts.append('</main>')
    parts.append(footer_js())
    parts.append('</body></html>')
    
    out_path = os.path.join(BASE, "00_总览", "总览_完整文档.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parts))
    print(f"[OVERVIEW ] Generated: {out_path}")


# ─── BUILD BRANCH PAGE ────────────────────────────────────────────────────────
def build_branch(folder_name, key, title, badge_class):
    branch_path = os.path.join(BASE, folder_name)
    lit_path = os.path.join(branch_path, "文献")
    md_files = sorted([f for f in os.listdir(lit_path) if f.endswith('.md')])
    
    parts = [head(f"{title} — 完整文档")]
    parts.append('<body>')
    parts.append('<div id="top"></div>')
    nav_items = branch_sidebar(key, folder_name, len(md_files))
    parts.append(sidebar(nav_items))
    parts.append('<main id="content">')
    
    # Page header
    header_cls = f"branch-{key.lower()}"
    parts.append(f'<div class="page-header {header_cls}">')
    parts.append(f'<h1>{title}</h1>')
    parts.append(f'<p>{len(md_files)} 篇文档</p>')
    parts.append('</div>')
    
    for i, fname in enumerate(md_files):
        fullpath = os.path.join(lit_path, fname)
        relpath = f"{folder_name}/文献/{fname}"
        parts.append(f'<div id="doc_{i+1}">')
        with open(fullpath, 'r', encoding='utf-8') as f:
            raw = f.read()
        body_html = md_to_html(raw)
        parts.append(doc_section(body_html, relpath, key))
        parts.append('</div>')
    
    parts.append('</main>')
    parts.append(footer_js())
    parts.append('</body></html>')
    
    # Map keys to output filenames
    output_names = {
        "A": "RAT_完整文档.html",
        "B": "本体论_完整文档.html",
        "C": "HAM_完整文档.html",
        "D": "数据驱动_完整文档.html",
        "E": "CuspRAT_完整文档.html",
    }
    out_path = os.path.join(branch_path, output_names[key])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parts))
    print(f"[BRANCH {key} ] Generated: {out_path}")


# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    build_overview()
    build_branch("01_Branch_A_RAT", "A", "Branch A · RAT 轨迹框架（序列分析）", "badge-a")
    build_branch("02_Branch_B_本体论", "B", "Branch B · DeFi 决策本体论", "badge-b")
    build_branch("03_Branch_C_HAM", "C", "Branch C · 异质预期与演化响应函数", "badge-c")
    build_branch("04_Branch_D_数据驱动", "D", "Branch D · 数据驱动安全网", "badge-d")
    build_branch("05_Branch_E_CuspRAT", "E", "Branch E · Cusp RAT 动力系统框架", "badge-e")
    print("\nAll 6 HTML files generated (1 overview + 5 branches).")
