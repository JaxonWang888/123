"""Package V36 from its final rebuilt EXE and matching corresponding source."""
from pathlib import Path
import argparse,zipfile,hashlib,json,shutil
ap=argparse.ArgumentParser();ap.add_argument('project',type=Path);ap.add_argument('release',type=Path);a=ap.parse_args();p=a.project.resolve();out=a.release.resolve();out.mkdir(parents=True,exist_ok=True)
sha=lambda data:hashlib.sha256(data).hexdigest()
exe=(p/'dist/鞍座图纸生成器.exe').read_bytes();dwg=(p/'reference/bom-template-original.dwg').read_bytes();v=json.loads((p/'handoff/verification-v36.json').read_text())
assert sha(exe)==v['exe_sha256'] and dwg in exe
assert '原生标注版 V36'.encode('utf-16le') in exe
source=out/'saddle-source-v36.zip'
with zipfile.ZipFile(source,'w',zipfile.ZIP_DEFLATED,9) as z:
 for dirname in ('src','tests','tools','reference','licenses','third_party','handoff'):
  for f in sorted((p/dirname).rglob('*')):
   if f.is_file() and not any(s in ('.git','__pycache__') for s in f.relative_to(p).parts) and f.suffix not in ('.exe','.pyc','.o','.pdb'):
    z.write(f,'saddle-generator/'+f.relative_to(p).as_posix())
 z.write(p/'README.md','saddle-generator/README.md')
 for f in sorted((p/'dist').glob('*.md')):z.write(f,'saddle-generator/dist/'+f.name)
shutil.copy2(p/'dist/鞍座图纸生成器.exe',out/'saddle-generator-v36.exe')
offline=out/'saddle-offline-v36.zip'
with zipfile.ZipFile(offline,'w',zipfile.ZIP_DEFLATED,9) as z:
 for name in ('鞍座图纸生成器.exe','使用说明.md','图纸分析.md','更新记录.md','验证报告.md'):z.write(p/'dist'/name,'鞍座自动生成/'+name)
 for f in sorted((p/'licenses').rglob('*')):
  if f.is_file():z.write(f,'鞍座自动生成/licenses/'+f.relative_to(p/'licenses').as_posix())
 z.write(p/'reference/bom-template-original.dwg','鞍座自动生成/明细栏样式来源.dwg')
 z.write(p/'reference/bom-style-source-v30.json','鞍座自动生成/bom-style-source-v30.json')
 z.write(p/'handoff/verification-v36.json','鞍座自动生成/verification-v36.json')
 z.write(source,'鞍座自动生成/sources/'+source.name)
for f in (source,offline):
 with zipfile.ZipFile(f) as z:assert z.testzip() is None
(out/'SHA256SUMS-v36.txt').write_text(''.join(f'{sha(f.read_bytes())}  {f.name}\n' for f in (out/'saddle-generator-v36.exe',source,offline)))
print(json.dumps({f.name:{'bytes':f.stat().st_size,'sha256':sha(f.read_bytes())} for f in (out/'saddle-generator-v36.exe',source,offline)},indent=2))
