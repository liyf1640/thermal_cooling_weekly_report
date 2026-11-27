"""pptxgenjs 产物后处理：python postprocess.py in.pptx out.pptx
1. 项目符号统一染成红色（pptxgenjs 不支持 bullet 颜色）
2. 去掉 ZIP 里的目录条目（云盘打开 / 协同编辑会出问题）"""
import re
import sys
import zipfile

RED = "C00000"
src, dst = sys.argv[1], sys.argv[2]
BU = f'<a:buClr><a:srgbClr val="{RED}"/></a:buClr>'

with zipfile.ZipFile(src) as zi, zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zo:
    for it in zi.infolist():
        if it.filename.endswith("/"):
            continue
        data = zi.read(it.filename)
        if re.fullmatch(r"ppt/slides/slide\d+\.xml", it.filename):
            xml = data.decode("utf-8")
            # pPr 内顺序：lnSpc/spcBef/spcAft → buClr → buSzPct → buFont → buChar
            xml = re.sub(r"(<a:pPr[^>]*>(?:(?!</a:pPr>).)*?)(<a:buSzPct)", lambda m: m.group(1) + BU + m.group(2), xml)
            data = xml.encode("utf-8")
        zo.writestr(it, data)
print("wrote", dst)
