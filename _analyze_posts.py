import os, re, json

posts_dir = 'e:/Repository/geeknite.github.io/_posts'
files = os.listdir(posts_dir)
dated_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}-')
undated = [f for f in files if not dated_pattern.match(f)]
dated = [f for f in files if dated_pattern.match(f)]

results = []
for f in undated:
    path = os.path.join(posts_dir, f)
    if os.path.isdir(path):
        continue
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as fh:
            content = fh.read()
    except:
        continue

    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    fm = fm_match.group(1) if fm_match else ''
    body = content[fm_match.end():] if fm_match else content

    has_title = bool(re.search(r'^title:', fm, re.MULTILINE))
    has_date = bool(re.search(r'^date:', fm, re.MULTILINE))
    has_tags = bool(re.search(r'^tags:', fm, re.MULTILINE))
    has_desc = bool(re.search(r'^description:', fm, re.MULTILINE))

    missing = []
    if not has_title: missing.append('title')
    if not has_date: missing.append('date')
    if not has_tags: missing.append('tags')
    if not has_desc: missing.append('description')
    fm_status = 'OK' if not missing else ','.join(missing)

    hero = bool(re.search(r'\[!\[.*?\].*?\{:\s*\.align-right\s*\}', body))
    aff = len(re.findall(r'site\.constants\.wsib|geeknite\.com', content))
    internal = len(re.findall(r'post_url', content))
    tables = len(re.findall(r'include amazon\.html', content))
    words = len(body.split())

    slug = f.replace('.md','').lower().replace('_','-').replace(' ','-')
    dups = [d for d in dated if slug in d.lower().replace('_','-').replace(' ','-')]
    dup_str = dups[0] if dups else ''

    score = 0
    if fm_status == 'OK': score += 2
    else: score += max(0, 2 - len(missing)*0.5)
    if hero: score += 1.5
    if aff > 0: score += 1.5
    if aff >= 5: score += 0.5
    if internal >= 3: score += 1.5
    elif internal > 0: score += 0.5
    if tables >= 1: score += 1.5
    if words >= 1000: score += 1
    elif words >= 500: score += 0.5
    if not dup_str: score += 0.5
    score = min(10, round(score, 1))

    results.append({
        'file': f,
        'fm': fm_status,
        'hero': hero,
        'aff': aff,
        'internal': internal,
        'tables': tables,
        'words': words,
        'dup': dup_str,
        'score': score
    })

results.sort(key=lambda x: x['score'])
print(json.dumps(results, indent=2))
