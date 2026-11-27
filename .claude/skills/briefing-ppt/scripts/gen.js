// 周报要点 PPT 生成器：node gen.js content.json out.pptx
// pptxgenjs 从当前工作目录的 node_modules 加载（先在工作目录 npm install pptxgenjs@4）
// images[].path 相对 content.json 所在目录解析
// 文本标记：**蓝色粗体**（关键字）  ##蓝色粗体##（数字，同色）；红色只用于题目、小标题、项目符号  段落以 "- " 开头为项目符号
const fs = require("fs");
const path = require("path");
const { createRequire } = require("module");
let pptxgen;
try { pptxgen = createRequire(path.join(process.cwd(), "noop.js"))("pptxgenjs"); }
catch { pptxgen = require("pptxgenjs"); }

const [, , contentPath, outPath] = process.argv;
const deck = JSON.parse(fs.readFileSync(contentPath, "utf8"));
const BASE = path.dirname(path.resolve(contentPath));

const FONT = "Microsoft YaHei";
const RED = "C00000", BLUE = "0055E6", BLACK = "000000", GREY = "7F7F7F";
const W = 13.333, H = 7.5, M = 0.4;
const BODY = 11, LABEL = 12, TITLE = 22;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.theme = { headFontFace: FONT, bodyFontFace: FONT };
pres.title = deck.title || "周报要点";

function runs(text, base) {
  // 把一段带标记的文本拆成 runs
  // 中文与强调标记之间不留空格（"把 **热串扰** 本身" → "把**热串扰**本身"）
  const CJK = "[\\u4e00-\\u9fff\\u3000-\\u303f\\uff00-\\uffef“”]";
  text = text
    .replace(new RegExp(`(${CJK}) +(\\*\\*|##)(?=${CJK})`, "g"), "$1$2")
    .replace(new RegExp(`(?<=${CJK})(\\*\\*|##) +(${CJK})`, "g"), "$1$2");
  const out = [];
  const re = /\*\*(.+?)\*\*|##(.+?)##|\[(.+?)\]\((.+?)\)/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push({ text: text.slice(last, m.index), options: { ...base } });
    if (m[1]) out.push({ text: m[1], options: { ...base, bold: true, color: BLUE } });
    else if (m[2]) out.push({ text: m[2], options: { ...base, bold: true, color: BLUE } });
    else out.push({ text: m[3], options: { ...base, color: BLUE, hyperlink: { url: m[4], tooltip: m[4] } } });
    last = re.lastIndex;
  }
  if (last < text.length) out.push({ text: text.slice(last), options: { ...base } });
  return out;
}

function paragraphs(lines, size, spaceAfter) {
  const all = [];
  lines.forEach((ln, i) => {
    const isBullet = ln.startsWith("- ");
    const base = { fontFace: FONT, fontSize: size, color: BLACK, paraSpaceAfter: spaceAfter };
    const rs = runs(isBullet ? ln.slice(2) : ln, base);
    // 段首引导词（"- **问题**：…"）用红色，句中其余加粗仍为蓝色
    const body = isBullet ? ln.slice(2) : ln;
    if (/^\*\*[^*]+\*\*[：:]/.test(body)) rs[0].options.color = RED;
    // pptxgenjs 遇到带 bullet 的 run 就另起一段：只能放在段首 run 上
    if (isBullet) rs[0].options.bullet = { indent: 12 };
    else if (i > 0) rs[0].options.bullet = false;
    if (i < lines.length - 1) rs[rs.length - 1].options.breakLine = true;
    all.push(...rs);
  });
  return all;
}

function dashedBox(slide, x, y, w, h, name) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h, objectName: name, rectRadius: 0.08,
    fill: { type: "none" },
    line: { color: RED, width: 1.25, dashType: "dash" },
  });
}

function titleBar(slide, title) {
  slide.addText(title, {
    x: M, y: 0.25, w: W - 2 * M, h: 0.7, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: TITLE, bold: true, color: RED, valign: "middle",
  });
}

// 标签 + 正文的虚线框
function labeledBox(slide, x, y, w, h, label, lines, size) {
  dashedBox(slide, x, y, w, h, label + "框");
  slide.addText(label, {
    x: x + 0.12, y: y + 0.06, w: w - 0.24, h: 0.3, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: LABEL, bold: true, color: RED, valign: "middle",
  });
  slide.addText(paragraphs(lines, size || BODY, 2), {
    x: x + 0.12, y: y + 0.38, w: w - 0.24, h: h - 0.44, isTextBox: true, margin: 0,
    valign: "top", lineSpacingMultiple: 1.05,
  });
}

function imageSlot(slide, x, y, w, h, hint) {
  slide.addShape(pres.shapes.RECTANGLE, {
    x, y, w, h, objectName: "图片预留位",
    fill: { color: "F2F2F2" }, line: { color: "BFBFBF", width: 0.75, dashType: "sysDash" },
  });
  slide.addText(hint || "图片预留位（原文示意图 / 结构图）", {
    x, y, w, h, isTextBox: true, align: "center", valign: "middle",
    fontFace: FONT, fontSize: 10, color: GREY,
  });
}

// 图片横排：等高缩放、整体居中，每张图下方一行图注
// images: [{ path, px: [宽, 高], caption }]
function placeImages(slide, slot, images) {
  const CAP = 0.28, GAPX = 0.25;
  let h = slot.h - CAP;
  const ratios = images.map((im) => im.px[0] / im.px[1]);
  let totalW = ratios.reduce((a, r) => a + r * h, 0) + GAPX * (images.length - 1);
  if (totalW > slot.w) {
    h *= (slot.w - GAPX * (images.length - 1)) / (totalW - GAPX * (images.length - 1));
    totalW = slot.w;
  }
  let x = slot.x + (slot.w - totalW) / 2;
  const y = slot.y + (slot.h - CAP - h) / 2;
  images.forEach((im, i) => {
    const w = ratios[i] * h;
    slide.addImage({ path: path.resolve(BASE, im.path), x, y, w, h, altText: im.caption, objectName: "原文图" + (i + 1) });
    slide.addText(im.caption, {
      x: x - 0.2, y: y + h + 0.03, w: w + 0.4, h: CAP - 0.03, isTextBox: true, margin: 0,
      fontFace: FONT, fontSize: 9, color: GREY, align: "center", valign: "top",
    });
    x += w + GAPX;
  });
}

const TOP = 1.1, BOTTOM = H - 0.35, GAP = 0.15;
const innerW = W - 2 * M - GAP;
const LW = innerW * 0.7, RW = innerW * 0.3;
const RX = M + LW + GAP;

function researchSlide(s) {
  const slide = pres.addSlide();
  titleBar(slide, s.title);
  const ch = BOTTOM - TOP;
  // 左：技术介绍
  dashedBox(slide, M, TOP, LW, ch, "技术介绍框");
  slide.addText("技术介绍", {
    x: M + 0.15, y: TOP + 0.08, w: 3, h: 0.36, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 14, bold: true, color: RED, valign: "middle",
  });
  const textH = s.introH || 2.55;
  slide.addText(paragraphs(s.intro, s.introSize || BODY + 1, s.introSpace ?? 5), {
    x: M + 0.15, y: TOP + 0.5, w: LW - 0.3, h: textH, isTextBox: true, margin: 0,
    valign: "top", lineSpacingMultiple: 1.1,
  });
  const imgY = TOP + 0.5 + textH + 0.12;
  const slot = { x: M + 0.15, y: imgY, w: LW - 0.3, h: BOTTOM - imgY - 0.15 };
  if (s.images && s.images.length) placeImages(slide, slot, s.images);
  else imageSlot(slide, slot.x, slot.y, slot.w, slot.h, s.imageHint);
  // 右：五框
  const labels = ["研究团队", "技术优势", "当前状态", "业务建议", "信息来源"];
  const keys = ["team", "advantage", "status", "suggestion", "source"];
  const weights = s.rightWeights || [0.9, 1.15, 1.1, 1.2, 0.75];
  const sum = weights.reduce((a, b) => a + b, 0);
  const avail = ch - GAP * 4;
  let y = TOP;
  labels.forEach((lb, i) => {
    const h = (avail * weights[i]) / sum;
    labeledBox(slide, RX, y, RW, h, lb, s[keys[i]], i === 4 ? 9 : BODY - 0.5);
    y += h + GAP;
  });
  if (s.notes) slide.addNotes(s.notes);
}

function industrySlide(s) {
  const slide = pres.addSlide();
  titleBar(slide, s.title);
  const ch = BOTTOM - TOP;
  // 左 7：2×2 产业要点框
  const bw = (LW - GAP) / 2, bh = (ch - GAP) / 2;
  s.items.forEach((it, i) => {
    const x = M + (i % 2) * (bw + GAP), y = TOP + Math.floor(i / 2) * (bh + GAP);
    labeledBox(slide, x, y, bw, bh, it.label, it.lines, BODY);
  });
  // 右 3：业务建议 / 信息来源
  const sh = ch * 0.62;
  labeledBox(slide, RX, TOP, RW, sh, "业务建议", s.suggestion, BODY - 0.5);
  labeledBox(slide, RX, TOP + sh + GAP, RW, ch - sh - GAP, "信息来源", s.source, 9);
}

for (const s of deck.slides) (s.type === "industry" ? industrySlide : researchSlide)(s);

pres.writeFile({ fileName: outPath }).then(() => console.log("wrote", outPath));
