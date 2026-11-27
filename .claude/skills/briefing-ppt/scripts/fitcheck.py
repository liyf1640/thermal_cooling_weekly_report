"""按微软雅黑实际字宽模拟换行，估算 pptx 每个文本框所需高度，报告可能溢出的框。
用法：python fitcheck.py deck.pptx"""
import sys
from PIL import ImageFont
from pptx import Presentation
from pptx.util import Emu

sys.stdout.reconfigure(encoding="utf-8")
FONTS = {}


def font(pt, bold):
    key = (pt, bold)
    if key not in FONTS:
        path = "C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc"
        FONTS[key] = ImageFont.truetype(path, int(pt * 10))  # 10 倍精度：1pt = 10 单位
    return FONTS[key]


def para_lines(para, width_pt, indent_pt):
    """返回 (行数, 字号)"""
    runs = [(r.text, (r.font.size.pt if r.font.size else 11), bool(r.font.bold)) for r in para.runs]
    if not runs:
        return 1, 11
    size = max(s for _, s, _ in runs)
    avail = (width_pt - indent_pt) * 10
    lines, cur = 1, 0.0
    for text, s, b in runs:
        f = font(s, b)
        for ch in text:
            w = f.getlength(ch)
            if cur + w > avail:
                lines += 1
                cur = w
            else:
                cur += w
    return lines, size


def check(path):
    prs = Presentation(path)
    for n, slide in enumerate(prs.slides, 1):
        for sh in slide.shapes:
            if not sh.has_text_frame or not sh.text_frame.text.strip():
                continue
            w_pt = Emu(sh.width).pt
            h_pt = Emu(sh.height).pt
            need = 0.0
            for p in sh.text_frame.paragraphs:
                bullet = p._p.find(".//{http://schemas.openxmlformats.org/drawingml/2006/main}buChar") is not None
                lines, size = para_lines(p, w_pt, 12 if bullet else 0)
                spc = p.space_after.pt if p.space_after is not None else 0
                lsm = 1.1
                need += lines * size * 1.3 * lsm + spc  # 雅黑行高约 1.3 倍字号
            flag = "溢出" if need > h_pt else ("偏紧" if need > h_pt * 0.92 else "")
            if flag:
                print(f"slide {n} [{flag}] 需 {need/72:.2f}in / 框 {h_pt/72:.2f}in :: {sh.text_frame.text[:30]}")
    print("检查完毕")


check(sys.argv[1])
