#!/usr/bin/env python3
"""Git-backed regressions for Book 6 workflow authority classification."""
import os,re,shutil,subprocess,tempfile,unittest
from pathlib import Path
H=Path(__file__).resolve().parent; P=H/'authorize-scope.py'; F=H/'finalize-package.py'; W=H.parents[2]/'.github/workflows/book-06-proof-export.yml'
BASE='d23d2e745ea0a5fda414321b6c82eda427459a87'; LOCK='LOCKED FOR FIRST-DRAFT PRODUCTION'
LIFE=('books/book-07/README.md','books/book-07/bible/story-memory.md','books/book-07/manuscript/README.md','books/book-07/progress.yaml','progress.yaml','series-outline.md')

def g(r,*a,ok=True):
 x=subprocess.run(['git',*a],cwd=r,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 if ok and x.returncode: raise RuntimeError(x.stdout.decode('utf8','replace'))
 return x
def put(r,p,t='baseline\n'):
 q=r/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(t,encoding='utf8')
def bump(r,p):
 q=r/p;q.write_text(q.read_text(encoding='utf8')+'updated\n',encoding='utf8')

class Repo:
 def __init__(s,chapters=(1,2,3,4),life=LIFE,future=()):
  s.t=tempfile.TemporaryDirectory();s.p=Path(s.t.name);g(s.p,'init','-b','main');g(s.p,'config','user.name','Test');g(s.p,'config','user.email','test@example.invalid')
  for n in chapters:
   put(s.p,f'books/book-07/manuscript/ch-{n:02d}.md',f'existing {n}\n');put(s.p,f'books/book-07/control/chapter-{n:02d}-mission-lock.md',f'# Lock {n}\n{LOCK}\n')
  for n in future: put(s.p,f'books/book-07/control/chapter-{n:02d}-mission-lock.md',f'# Future {n}\n{LOCK}\n')
  for p in life: put(s.p,p)
  for p in ('books/book-05/README.md','books/book-06/manuscript/ch-01.md','books/book-06/export/finalize-package.py','books/book-08/outline.md','books/book-03/package/approved/The-Challenger-cover.jpg','books/book-03/package/metadata.md','.github/workflows/book-03-release-package.yml'): put(s.p,p)
  g(s.p,'add','.');g(s.p,'commit','-m','base');g(s.p,'checkout','-b','repair')
 def close(s): s.t.cleanup()
 def ch(s,n,lock=None,locked=True):
  put(s.p,f'books/book-07/manuscript/ch-{n:02d}.md',f'new {n}\n')
  if lock is not None: put(s.p,f'books/book-07/control/chapter-{lock:02d}-mission-lock.md',f'# Lock {lock}\n{LOCK if locked else "DRAFT MISSION NOTES"}\n')
 def commit(s): g(s.p,'add','-A');g(s.p,'commit','-m','change')

def run(r,base='main'):
 e=r/'.env';env=os.environ.copy();env.update(BOOK6_SCOPE_BASE_REF=base,GITHUB_ENV=str(e));env.pop('GITHUB_BASE_REF',None)
 x=subprocess.run(['python3',str(P)],cwd=r,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 return x.returncode,x.stdout,e.read_text(encoding='utf8') if e.exists() else ''

class T(unittest.TestCase):
 def R(s,**k):
  r=Repo(**k);s.addCleanup(r.close);return r
 def yes(s,r):
  c,o,e=run(r.p);s.assertEqual(c,0,o);s.assertIn('BOOK6_AUTHORITY_MODE=authorized_book7_drafting',e);s.assertIn('BOOK6_SCOPE_BASE_REF=HEAD',e)
 def no(s,r):
  c,o,e=run(r.p);s.assertNotEqual(c,0,o);s.assertNotIn('BOOK6_SCOPE_BASE_REF=HEAD',e)
 def test_source_baseline_fixed(s):
  m=re.search(r'^SOURCE_BASE_SHA\s*=\s*"([0-9a-f]{40})"',F.read_text(),re.M);s.assertIsNotNone(m);s.assertEqual(m.group(1),BASE)
 def test_ordinary_no_override(s):
  r=s.R();bump(r.p,'books/book-06/export/finalize-package.py');r.commit();c,o,e=run(r.p);s.assertEqual(c,0,o);s.assertIn('BOOK6_AUTHORITY_MODE=book6_validation',e);s.assertNotIn('BOOK6_SCOPE_BASE_REF=HEAD',e)
 def test_pr42_and_old_rejection(s):
  r=s.R(chapters=(1,));r.ch(2,2)
  for p in ('books/book-07/README.md','books/book-07/progress.yaml','books/book-07/manuscript/README.md','series-outline.md'): bump(r.p,p)
  r.commit();s.assertIn('books/book-07/manuscript/ch-02.md',g(r.p,'diff','--name-only','main...HEAD').stdout.decode());s.yes(r)
 def test_ch5_pass(s):
  r=s.R();r.ch(5,5);bump(r.p,'books/book-07/README.md');bump(r.p,'books/book-07/progress.yaml');r.commit();s.yes(r)
 def test_two_chapters(s):
  r=s.R();r.ch(5,5);r.ch(6,6);r.commit();s.no(r)
 def test_mismatch_lock(s):
  r=s.R();r.ch(5,6);r.commit();s.no(r)
 def test_missing_lock_no_override(s):
  r=s.R();r.ch(5);r.commit();s.no(r)
 def test_copy(s):
  r=s.R();r.ch(5,5);shutil.copyfile(r.p/'books/book-07/manuscript/ch-01.md',r.p/'books/book-07/manuscript/ch-05.md');r.commit();s.no(r)
 def test_rename_chapter(s):
  r=s.R();g(r.p,'mv','books/book-07/manuscript/ch-04.md','books/book-07/manuscript/ch-05.md');r.ch(5,5);r.commit();s.no(r)
 def test_delete_chapter(s):
  r=s.R();(r.p/'books/book-07/manuscript/ch-04.md').unlink();r.commit();s.no(r)
 def test_future_lock(s):
  r=s.R(future=(5,));r.ch(5);bump(r.p,'books/book-07/control/chapter-05-mission-lock.md');r.commit();s.no(r)
 def test_unlocked(s):
  r=s.R();r.ch(5,5,False);r.commit();s.no(r)
 def test_invalid_base(s):
  r=s.R();r.ch(5,5);r.commit();c,o,e=run(r.p,'missing');s.assertNotEqual(c,0,o);s.assertNotIn('BOOK6_SCOPE_BASE_REF=HEAD',e)
 def test_shallow(s):
  r=s.R();r.ch(5,5);r.commit();t=tempfile.TemporaryDirectory();s.addCleanup(t.cleanup);q=Path(t.name)/'q';x=subprocess.run(['git','clone','--depth','1','--branch','repair',f'file://{r.p}',str(q)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT);s.assertEqual(x.returncode,0,x.stdout.decode());c,o,e=run(q,'main');s.assertNotEqual(c,0,o);s.assertNotIn('BOOK6_SCOPE_BASE_REF=HEAD',e)
 def test_skip_number(s):
  r=s.R();r.ch(6,6);r.commit();s.no(r)
 def test_gapped_base(s):
  r=s.R(chapters=(1,3));r.ch(4,4);r.commit();s.no(r)
 def test_add_lifecycle(s):
  r=s.R(life=tuple(p for p in LIFE if p!='progress.yaml'));r.ch(5,5);put(r.p,'progress.yaml');r.commit();s.no(r)
 def test_delete_lifecycle(s):
  r=s.R();r.ch(5,5);(r.p/'books/book-07/README.md').unlink();r.commit();s.no(r)
 def test_rename_lifecycle(s):
  r=s.R(life=tuple(p for p in LIFE if p!='books/book-07/README.md'));r.ch(5,5);g(r.p,'mv','books/book-07/bible/story-memory.md','books/book-07/README.md');r.commit();s.no(r)
 def test_workflow_order(s):
  x=W.read_text();a=[x.index(n) for n in ('Test Book 6 workflow authority classifier','Classify current workflow authority','Test Book 6 export scope validator','Build and validate Book 6 controlled exports')];s.assertEqual(a,sorted(a))
 def test_pr_no_push(s):
  x=W.read_text();a=x.index('if [ "$GITHUB_EVENT_NAME" = "pull_request" ]; then');b=x.index('git status --porcelain=v1 --',a);c=x.index('exit 0',b);d=x.index('git push origin',c);s.assertTrue(a<b<c<d)

def mod(n):
 def test(s):
  r=s.R();bump(r.p,f'books/book-07/manuscript/ch-{n:02d}.md');r.commit();s.no(r)
 return test
def mixed(p):
 def test(s):
  r=s.R();r.ch(5,5);bump(r.p,p) if (r.p/p).exists() else put(r.p,p);r.commit();s.no(r)
 return test
for n in (1,2): setattr(T,f'test_modify_{n}',mod(n))
for i,p in enumerate(('books/book-06/export/finalize-package.py','books/book-06/manuscript/ch-01.md','books/book-05/README.md','books/book-08/outline.md','books/book-03/package/approved/The-Challenger-cover.jpg','books/book-03/package/metadata.md','.github/workflows/book-03-release-package.yml','books/book-07/package/metadata.md','books/book-07/cover/cover.jpg','books/book-07/listing/copy.md','books/book-07/upload/package.zip','books/book-07/publication/status.md','books/book-07/retailer/form.md','books/book-07/advertising/ad.md','books/book-07/distribution/log.md','notes/unknown.txt'),1): setattr(T,f'test_mixed_{i:02d}',mixed(p))
if __name__=='__main__': unittest.main()
