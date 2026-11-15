"""Anbar_tesvir.xlsx -> ../index.html  (run from tools/: python make_site.py Anbar_tesvir.xlsx)"""
import sys, re, json, pandas as pd
src = sys.argv[1] if len(sys.argv) > 1 else 'Anbar_tesvir.xlsx'
df = pd.read_excel(src).fillna(''); cols = df.columns.tolist()
info, key, prods = [], {}, []
def hidden(r):
    # Hide items whose own name (without brand) has '*' or letters in parentheses, e.g. (A), (T), (S)
    n, b = str(r['Məhsulun adı']), str(r['Qrup'])
    own = n[len(b) + 1:] if n.startswith(b + ' ') else n
    return '*' in own or re.search(r'\([^)]*[^\W\d_][^)]*\)', own) is not None
skipped = 0
for _, r in df.iterrows():
    if hidden(r):
        skipped += 1; continue
    ii = -1
    if not str(r['Status']).startswith('Yox'):
        rec = {k: [r[cols[o + 6 * l]] for l in range(3)] for k, o in zip('fthbsd', range(7, 13))}
        s = json.dumps(rec, ensure_ascii=False)
        if s not in key: key[s] = len(info); info.append(rec)
        ii = key[s]
    prods.append([r['Məhsulun adı'], r['Qrup'], r['Cins'], float(r['Satış qiyməti']), 1 if float(r['Miqdar']) > 0 else 0, ii])
data = json.dumps({'p': prods, 'i': info}, ensure_ascii=False, separators=(',', ':'))
html = open('shop_template.html', encoding='utf8').read().replace('__DATA__', data)
open('../index.html', 'w', encoding='utf8').write(html)
print(len(prods), 'products,', len(info), 'descriptions,', skipped, 'hidden')
