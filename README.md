# 鞍座图纸生成器

Windows 10/11 x64 离线单文件程序，无需安装 AutoCAD 或联网运行。

## 下载

- [下载离线程序包（约 3.4 MB）](https://github.com/JaxonWang888/123/raw/refs/heads/main/releases/saddle-offline.zip)
- [下载完整对应源码（约 12 MB）](https://github.com/JaxonWang888/123/raw/refs/heads/main/releases/saddle-source.zip)

解压程序包，将其中的“鞍座图纸生成器.exe”放到 `C:\Users\20202012\Desktop\鞍座自动生成`，双击运行。说明、示例和源码均不是程序运行依赖。

## 功能与范围

左侧输入腹板型式、筋板和地脚孔数量、几何尺寸；右侧实时预览并支持缩放和平移。支持 A0～A4 纸张、自动推荐或手动设置比例，以及 DWG/DXF 导出。模型尺寸以毫米为单位保持 1:1，比例控制图框排版。

当前为带尺寸的参数化三视几何绘图版，尚未完整复刻原模板的接地件详图、全部焊缝符号和 BOM，不进行承载与强度计算。原图大量尺寸为占位符，默认值及示例仅供演示。详细范围、测试记录和使用方法见程序包内说明。

实际 Windows EXE 在 Wine 兼容环境中完成 105 项检查，32 组 DWG 回读、几何比对和 DXF 审计通过；尚未在用户 Windows 实机或 AutoCAD 中验证。

## 许可证

程序及对应源码按 GPL-3.0-or-later 提供。源码包包含程序源码、GNU LibreDWG 对应源码、构建脚本和测试；第三方许可证随包提供。
