import os
import re
import html

BASE = "/Users/gan-m2/Desktop/PaperGuru/UnusPay-区块链数据-信用-行为/2026-07-08_四分支探索"

def collect_files():
    """Collect all .md files with their relative paths"""
    files = []
    for root, dirs, filenames in os.walk(BASE):
        # Skip hidden dirs
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in sorted(filenames):
            if f.endswith('.md') and not f.startswith('.'):
                fullpath = os.path.join(root, f)
                relpath = os.path.relpath(fullpath, BASE)
                files.append((relpath, fullpath))
    return files

def md_to_html(text):
    """Very basic MD to HTML conversion"""
    # Escape HTML first
    text = html.escape(text)
    
    # Headers
    text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    
    # Bold and italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    
    # Bold alternate syntax (__text__)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)
    
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    
    # Code blocks
    text = re.sub(r'```(?:\w*\n)?(.*?)```', r'<pre><code>\1</code></pre>', text, flags=re.DOTALL)
    
    # Horizontal rules
    text = re.sub(r'^---$', r'<hr>', text, flags=re.MULTILINE)
    
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    
    # Tables - basic support (mark them without full conversion; they'll display well enough)
    # Convert pipe tables to pre blocks or just leave them
    
    # Line breaks - join consecutive non-empty lines within a paragraph
    lines = text.split('\n')
    result = []
    in_table = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Handle tables
        if stripped.startswith('|') and stripped.endswith('|'):
            if not in_table:
                in_table = True
                result.append('<table>')
            cells = [c.strip() for c in stripped[1:-1].split('|')]
            is_header = all(re.match(r'^[-:\s]+$', c) for c in cells)
            if is_header:
                continue  # skip separator row
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
    
    # Wrap consecutive non-empty, non-tag lines in <p> tags
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

# Collect files
files = collect_files()

# Build TOC
toc_items = []
for relpath, fullpath in files:
    parts = relpath.split('/')
    depth = len(parts)
    name = parts[-1].replace('.md', '')
    anchor = relpath.replace('/', '_').replace('.md', '').replace(' ', '_')
    toc_items.append((depth, name, anchor, relpath))

# Build HTML
html_parts = []
html_parts.append('''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>四分支探索 - 完整文档集</title>
<style>
  :root {
    --bg: #0d1117;
    --bg-secondary: #161b22;
    --border: #30363d;
    --text: #c9d1d9;
    --text-secondary: #8b949e;
    --accent: #58a6ff;
    --accent-hover: #79c0ff;
    --green: #3fb950;
    --orange: #d2991d;
    --red: #f85149;
    --purple: #a371f7;
    --code-bg: #1c2128;
    --heading: #f0f6fc;
    --link: #58a6ff;
    --table-header: #1c2128;
    --table-row-alt: #161b22;
  }
  
  * { margin: 0; padding: 0; box-sizing: border-box; }
  
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    font-size: 16px;
  }
  
  #sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: 320px;
    height: 100vh;
    background: var(--bg-secondary);
    border-right: 1px solid var(--border);
    overflow-y: auto;
    z-index: 100;
    padding: 20px;
  }
  
  #sidebar h2 {
    color: var(--heading);
    font-size: 18px;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
  }
  
  #sidebar nav a {
    display: block;
    color: var(--text-secondary);
    text-decoration: none;
    padding: 4px 0;
    font-size: 13px;
    transition: color 0.15s;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  #sidebar nav a:hover { color: var(--accent-hover); }
  #sidebar nav a.level-1 { padding-left: 0; font-weight: 600; color: var(--text); }
  #sidebar nav a.level-2 { padding-left: 16px; }
  #sidebar nav a.level-3 { padding-left: 32px; }
  #sidebar nav a.level-4 { padding-left: 48px; font-size: 12px; }
  
  #content {
    margin-left: 340px;
    padding: 40px 60px;
    max-width: 1000px;
  }
  
  .doc-section {
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 32px;
    margin-bottom: 24px;
    background: var(--bg-secondary);
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
    background: var(--code-bg);
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.9em;
    font-family: 'SF Mono', 'Fira Code', 'Fira Mono', Menlo, Consolas, monospace;
  }
  .doc-section pre {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 16px;
    overflow-x: auto;
    margin: 12px 0;
    font-size: 13px;
    line-height: 1.5;
  }
  .doc-section pre code {
    background: none;
    padding: 0;
  }
  .doc-section table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 14px;
  }
  .doc-section th {
    background: var(--table-header);
    padding: 8px 12px;
    text-align: left;
    border: 1px solid var(--border);
    color: var(--heading);
  }
  .doc-section td {
    padding: 8px 12px;
    border: 1px solid var(--border);
  }
  .doc-section tr:nth-child(even) td { background: var(--table-row-alt); }
  .doc-section strong { color: var(--heading); }
  .doc-section em { color: var(--orange); }
  
  .file-path {
    color: var(--text-secondary);
    font-size: 12px;
    font-family: monospace;
    margin-bottom: 16px;
    padding: 6px 10px;
    background: var(--code-bg);
    border-radius: 4px;
    display: inline-block;
  }
  
  .nav-toggle {
    display: none;
    position: fixed;
    top: 12px;
    left: 12px;
    z-index: 200;
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    color: var(--text);
    font-size: 20px;
    padding: 8px 12px;
    border-radius: 6px;
    cursor: pointer;
  }
  
  .branch-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 600;
    margin-right: 8px;
  }
  .badge-a { background: rgba(88,166,255,0.15); color: var(--accent); }
  .badge-b { background: rgba(163,113,247,0.15); color: var(--purple); }
  .badge-c { background: rgba(63,185,80,0.15); color: var(--green); }
  .badge-d { background: rgba(210,153,29,0.15); color: var(--orange); }
  
  @media (max-width: 900px) {
    #sidebar { transform: translateX(-100%); transition: transform 0.3s; width: 280px; }
    #sidebar.open { transform: translateX(0); }
    #content { margin-left: 0; padding: 20px; }
    .nav-toggle { display: block; }
  }
</style>
</head>
<body>
<button class="nav-toggle" onclick="document.getElementById('sidebar').classList.toggle('open')">&#9776;</button>
<aside id="sidebar">
  <h2>四分支探索文档</h2>
  <nav>
''')

# Build sidebar
for depth, name, anchor, relpath in toc_items:
    cls = f'level-{min(depth, 4)}'
    html_parts.append(f'    <a href="#{anchor}" class="{cls}">{html.escape(name)}</a>')

html_parts.append('''
  </nav>
</aside>
<main id="content">
  <div class="doc-section">
    <h1>2026-07-08 四分支探索 — 完整文档集</h1>
    <p>本页包含全部 22 个 Markdown 文件的渲染内容。共 <strong>6</strong> 个总览文档和 <strong>16</strong> 个分支详细文档。</p>
  </div>
''')

# Build content
for relpath, fullpath in files:
    anchor = relpath.replace('/', '_').replace('.md', '').replace(' ', '_')
    with open(fullpath, 'r', encoding='utf-8') as f:
        raw = f.read()
    
    body_html = md_to_html(raw)
    
    # Determine branch badge
    badge = ''
    if 'Branch_A' in relpath:
        badge = '<span class="branch-badge badge-a">Branch A</span>'
    elif 'Branch_B' in relpath:
        badge = '<span class="branch-badge badge-b">Branch B</span>'
    elif 'Branch_C' in relpath:
        badge = '<span class="branch-badge badge-c">Branch C</span>'
    elif 'Branch_D' in relpath:
        badge = '<span class="branch-badge badge-d">Branch D</span>'
    
    html_parts.append(f'''
  <div class="doc-section" id="{anchor}">
    {badge}<span class="file-path">{html.escape(relpath)}</span>
    {body_html}
  </div>''')

html_parts.append('''
</main>
<script>
  // Close sidebar when clicking on a link (mobile)
  document.querySelectorAll('#sidebar a').forEach(link => {
    link.addEventListener('click', () => {
      document.getElementById('sidebar').classList.remove('open');
    });
  });
  
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
</script>
</body>
</html>''')

output_path = os.path.join(BASE, '四分支探索_完整文档.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(html_parts))

print(f"Generated: {output_path}")
print(f"Total files included: {len(files)}")
