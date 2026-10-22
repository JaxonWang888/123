import pathlib,zipfile,shutil,json,hashlib
project=pathlib.Path('/workspace/restored/saddle-generator');results=pathlib.Path('/workspace/v29-publish');repo=pathlib.Path('/workspace/123');release=pathlib.Path('/workspace/release-v29');release.mkdir(exist_ok=True)
required={'smoke.json':('checks',213),'verification-v29.json':('files',42),'verification-bom.json':('files',42),'verification-compat.json':('files',8),'verification-layout.json':('files',50),'verification-pdf.json':('files',21),'verification-automation.json':('checks',49),'verification-native-bom.json':('checks',28),'verification-no-autocad.json':(None,None)}
for name,(key,n) in required.items():
 data=json.loads((results/name).read_text());assert data['passed'],name
 if key:assert data[key]==n,(name,data)
sha=hashlib.sha256((project/'dist/鞍座图纸生成器.exe').read_bytes()).hexdigest()
(project/'dist/验证报告.md').write_text(f'''# V29 验证报告

- BOM通过原生TABLE命令新建，不复制模板整表。缺失时只补入AcDbTableStyle到ACAD_TABLESTYLE字典，并检查模型数量不变。CAD基础输出不包含预览线框；TABLE创建完成后检查新对象AcDbTable、明细栏样式，再增行填写。内置样式来源字节与上传原DWG一致。
- 28项Windows命令/对话框模拟检查（强制启用断言，含实际子进程对话框读写）：核对SendCommand字符串为_.TABLE并排队指定插入点，插入窗口选择明细栏、从表格样式开始、额外行列0、列宽50/行高14，截图八项复选状态正确；没有模型表格CopyObjects或AddTable调用。检查先插入原生新表后增行、8mm明细行、表头保留、左中与边距2、幂等和失败行为；样式缺失只复制样式对象到样式字典。

- 18组BOM模型检查通过：实际数量、形状分组、固定接地板资料、普通质量空白、圆径10/字高5/居中、与原有图形及文字的圆圈净距、腹板序号在当前鞍座附近、接地板箭头指向直边且避开尺寸文字。含1400底板长、400底板宽、200孔列距的紧凑模型。
- 20组原有结构与参数回归、24组接地板模型检查通过。
- Windows EXE完成213项交互/参数/离线基础导出检查，输出21组DWG/DXF/PDF及4个比例样例。DWG/DXF为待AutoCAD完成原生BOM的基础文件，与.BOM数据一同提供。
- 42份CAD直接/回读检查通过：原有尺寸/图层/结构/接地板保持，42份序号与BOM交接数据检查确认圆径、字高、双向居中、编号对应，且基础CAD中不存在重绘的BOM字段。8份跨比例文件、25份原始DWG文字流、50份尺寸排布、21份黑白矢量PDF检查通过。
- 49项原有COM标注/窗口模拟检查通过。最终EXE实际子进程在无CAD环境提示无法完成处理，原始文件未改写。
- 本环境没有真实AutoCAD Mechanical2018。真实TABLE对话框、样式补入、新表插入、单元格属性及SaveAs2013只经过Windows模拟和代码检查，尚未实机核验。包内DWG/DXF样例尚未执行此阶段；运行配套CMD后需检查日志及原生表格。PDF/PNG是排布缓存预览，不能当作原生表格已导入的证据。
- 1:2.5/1:5为故意超小比例的标注引擎诊断文件，不放置BOM；正常GUI导出总会启动原生TABLE建表阶段。CAD水平边距存储属性值为2；尺寸样式整理可取消，原生TABLE建表仍会执行。

EXE SHA256: `{sha}`
''')
for name in ('鞍座图纸生成器.exe','使用说明.md','更新记录.md','图纸分析.md','验证报告.md'):shutil.copy2(project/'dist'/name,release/name)
shutil.copytree(project/'licenses',release/'licenses',dirs_exist_ok=True)
shutil.copy2(project/'reference/bom-template-original.dwg',release/'明细栏样式来源.dwg')
for t,name in ((0,'腹板在中间'),(1,'腹板在侧面')):
 for ext in ('dwg','dxf','pdf'):shutil.copy2(results/f'case_{t}_0_3_6.{ext}',release/f'基础样例-{name}.{ext}')
 for ext in ('dwg','dxf'):shutil.copy2(results/f'case_{t}_0_3_6.{ext}.BOM数据',release/f'基础样例-{name}.{ext}.BOM数据')
 shutil.copy2(results/f'drawing-{t}.png',release/f'排布预览-{name}.png')
for ext in ('dwg','dxf','pdf'):shutil.copy2(results/f'notch-sample.{ext}',release/f'基础样例-Note8缺口.{ext}')
for ext in ('dwg','dxf'):shutil.copy2(results/f'notch-sample.{ext}.BOM数据',release/f'基础样例-Note8缺口.{ext}.BOM数据')
for ext in ('dwg','dxf'):
 shutil.copy2(results/f'scale_25.{ext}',release/f'基础样例-比例1比25.{ext}')
 shutil.copy2(results/f'scale_25.{ext}.BOM数据',release/f'基础样例-比例1比25.{ext}.BOM数据')
for a,b in [('ui.png','界面预览.png'),('scrolled.png','比例与滚动预览.png')]:shutil.copy2(results/a,release/b)
for name in required:shutil.copy2(results/name,release/name)
(release/'完成样例原生BOM.cmd').write_bytes(('''@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo 需要本机AutoCAD Mechanical 2018。请等待每个自动处理任务结束。
for %%F in ("基础样例-腹板在中间.dwg" "基础样例-腹板在侧面.dwg" "基础样例-Note8缺口.dwg" "基础样例-腹板在中间.dxf" "基础样例-腹板在侧面.dxf" "基础样例-Note8缺口.dxf") do (
 start /wait "" "%~dp0鞍座图纸生成器.exe" --cad-postprocess "%~dp0%%~F" 15 0 0 1
 if errorlevel 1 goto failed
)
start /wait "" "%~dp0鞍座图纸生成器.exe" --cad-postprocess "%~dp0基础样例-比例1比25.dwg" 25 0 0 1
if errorlevel 1 goto failed
start /wait "" "%~dp0鞍座图纸生成器.exe" --cad-postprocess "%~dp0基础样例-比例1比25.dxf" 25 0 0 1
if errorlevel 1 goto failed
echo 完成。请查看同名自动处理日志并检查原生BOM。
pause
exit /b 0
:failed
echo 自动处理未完成，图纸不应作为最终结果。请查看同名日志。
pause
exit /b 1
'''.replace('\n','\r\n')).encode('utf-8'))
(release/'样例说明.txt').write_text('本包DWG/DXF是离线基础导出，尚无原生BOM。请在安装AutoCAD2018的Windows电脑上运行“完成样例原生BOM.cmd”，或使用程序正常导出。成功处理后，DWG中的BOM由TABLE新建且样式为明细栏，且不依赖外部模板。PDF/PNG仅作排布预览。详见验证报告。\n')
(release/'SHA256SUMS.txt').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(release).as_posix()}\n' for p in sorted(release.rglob('*')) if p.is_file() and p.suffix!='.zip' and p.name!='SHA256SUMS.txt'))
offline=release/'saddle-offline-v29.zip'
with zipfile.ZipFile(offline,'w',zipfile.ZIP_DEFLATED,9) as z:
 for p in sorted(release.rglob('*')):
  if p.is_file() and p.suffix!='.zip':z.write(p,'鞍座自动生成/'+p.relative_to(release).as_posix())
source=release/'saddle-source-v29.zip'
with zipfile.ZipFile(source,'w',zipfile.ZIP_DEFLATED,9) as z:
 for dirname in ('src','tests','tools','reference','licenses','third_party'):
  for p in sorted((project/dirname).rglob('*')):
   if p.is_file() and not any(part in ('.git','__pycache__') for part in p.relative_to(project).parts) and p.suffix.lower() not in ('.dwg','.dxf','.png','.jpg','.bmp','.pyc'):z.write(p,'saddle-generator/'+p.relative_to(project).as_posix())
 z.write(project/'reference/bom-template-original.dwg','saddle-generator/reference/bom-template-original.dwg')
 z.write(project/'README.md','saddle-generator/README.md')
 for p in (project/'dist').glob('*.md'):z.write(p,'saddle-generator/dist/'+p.name)
for f in (offline,source):
 with zipfile.ZipFile(f) as z:assert z.testzip() is None
 shutil.copy2(f,repo/'releases'/f.name)
shutil.copy2(offline,repo/'releases/saddle-offline.zip');shutil.copy2(source,repo/'releases/saddle-source.zip');shutil.copy2(project/'dist/鞍座图纸生成器.exe',repo/'releases/saddle-generator-v29.exe');shutil.copy2(results/'ui.png',repo/'releases/preview-v29.png');shutil.copy2(results/'drawing-0.png',repo/'releases/drawing-v29.png');shutil.copy2(project/'README.md',repo/'README.md')
(repo/'releases/SHA256SUMS.txt').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in sorted(p for p in (repo/'releases').iterdir() if p.suffix in ('.zip','.exe'))))
print(json.dumps({'exe_sha256':sha,'packages':{p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (offline,source)}},indent=2))
