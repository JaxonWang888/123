# 鞍座图纸生成器 V10

Windows 10/11 x64 离线单文件程序，无需 AutoCAD、Python 或联网运行。

## 下载

- **[单文件 EXE，直接下载运行](https://github.com/JaxonWang888/123/raw/refs/heads/main/releases/saddle-generator-v10.exe)**
- [完整程序包：说明、示例 DWG/DXF/PDF、参数和验证报告](https://github.com/JaxonWang888/123/raw/refs/heads/main/releases/saddle-offline-v10.zip)
- [完整对应源码和构建脚本](https://github.com/JaxonWang888/123/raw/refs/heads/main/releases/saddle-source-v10.zip)
- [SHA-256 校验值](releases/SHA256SUMS.txt)

将 EXE 放入 `C:\Users\20202012\Desktop\鞍座自动生成` 后双击运行。说明、示例与源码不是运行依赖。

![V10 界面](releases/preview-v10.png)

## 本次更新：文字样式统一为 HM-ASME

- 所有 CAD 文字及尺寸显示块文字使用 HM-ASME，当前文字样式也设为 HM-ASME。
- HM-ASME 保持 Arial 常规体；中文单行文字通过 MTEXT 内部字体格式指定宋体，保持可编辑与中文显示。
- 尺寸样式继续使用 HM-ASME 1-1，全局比例随图纸比例同步。
- 保留之前角度尺寸定位、文字位置和 Unicode 编码修复。

请使用 V10 重新生成新的 DWG/DXF 文件，已有旧文件不会自动更新。

![黑白图纸与放大图](releases/drawing-v10.png)

DXF 为 2004 格式；DWG 含原生折弯半径扩展实体，请使用支持此标注类型的 CAD。

主图毫米模型 1:1，所有尺寸为 CAD 原生 DIMENSION / LARGE_RADIAL_DIMENSION，使用 HM-ASME 1-1，图层为“6 尺寸线-管口号外圆（细实线）”，全局比例等于图纸比例。仅长圆孔的放大复制图采用标示放大比例，标注仍显示孔的实际尺寸。中文宋体，英文数字 Arial。

保留之前的外筋板接触点、截平端面、实际投影、镜像侧腹板、对称孔、独立内筋板间距、非交叠原生剖面、自动比例具体值和滚动重绘。仍不生成 Note、BOM、泡泡号、Ls、向视符号及过程角度；排气孔、缺口、地脚孔注释和焊接符号保留，注释连接使用普通箭头和线条。

## 验证与使用范围

Windows EXE 在 Wine 10 中完成 177 项交互/导出检查；42 份常规 CAD 文档和 8 份比例文档独立审计错误与修复均为 0。独立重生成角度尺寸恢复为 450/650 mm 弧半径；1:2.5、1:5、1:25、1:40 的实体和样式全局比例均核对一致。25 份 DWG 原始文字流通过 Unicode 与字体检查，21 份 PDF 保持黑白矢量。完整数据和验证报告在程序包内。

当前环境没有 AutoCAD Mechanical 2018，尚未进行该软件的实机打开、重生成、编辑、保存和打印验收。默认参数仅作演示，不执行强度计算。PDF 文字转为字体轮廓，CAD 文字和标注可编辑。

GNU LibreDWG 及程序遵循 GPL-3.0-or-later；许可证和完整对应源码随包提供。历史版本在 releases 目录保留。
