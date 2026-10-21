from pathlib import Path
import json,subprocess,re
R=Path(__file__).resolve().parents[1]
def g(*a):return subprocess.check_output(['git',*a],cwd=R,text=True)
prs=json.loads((R/'data/prs.json').read_text())
assert len(prs)==20
assert len(g('for-each-ref','--format=%(refname)','refs/heads/amendment/').splitlines())==20
for p in prs:
 assert len(g('rev-list','--parents','-n','1',p['merge']).split())==3
 before=g('show',p['base']+':CONSTITUTION.md');after=g('show',p['head']+':CONSTITUTION.md')
 for f in p['files']:
  assert f['before'] in before and f['after'] in after
 assert g('rev-parse',p['branch']).strip()==p['head']
text=(R/'CONSTITUTION.md').read_text()
assert len(re.findall(r'^### Статья ',text,re.M))==142
assert not re.search(r'<ref|\{\{якорь',text)
print('PASS: 20 branches, 20 two-parent merges, stored article text matches Git snapshots, 142 article slots. Not a legal-source audit.')
