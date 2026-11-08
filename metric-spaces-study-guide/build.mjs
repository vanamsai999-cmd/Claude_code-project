// Build: concatenate src/*.html, pre-render all $...$ / $$...$$ math with KaTeX,
// inline KaTeX CSS + woff2 fonts, generate the l^p unit-sphere SVG.
import fs from 'node:fs';
import path from 'node:path';
import katex from 'katex';

const here = path.dirname(new URL(import.meta.url).pathname);
const srcDir = path.join(here, 'src');
let html = fs.readdirSync(srcDir).filter(f => f.endsWith('.html')).sort()
  .map(f => fs.readFileSync(path.join(srcDir, f), 'utf8')).join('\n');

const macros = {
  '\\R': '\\mathbb{R}', '\\N': '\\mathbb{N}', '\\Q': '\\mathbb{Q}', '\\Z': '\\mathbb{Z}', '\\C': '\\mathbb{C}',
  '\\F': '\\mathcal{F}', '\\Pow': '\\mathcal{P}', '\\eps': '\\varepsilon',
};
const decode = s => s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
let errors = 0;
const render = (tex, display) => {
  try {
    return katex.renderToString(decode(tex), { displayMode: display, macros, throwOnError: true, strict: 'ignore' });
  } catch (e) { errors++; console.error('KaTeX error:', e.message, '\n  in:', tex); return tex; }
};
// Protect <style> and <script> blocks from math processing.
const stash = [];
html = html.replace(/<(style|script)[\s\S]*?<\/\1>/g, m => { stash.push(m); return `\u0000${stash.length - 1}\u0000`; });
html = html.replace(/\$\$([\s\S]+?)\$\$/g, (_, t) => render(t, true));
html = html.replace(/\$([^$]+?)\$/g, (_, t) => render(t, false));
html = html.replace(/\u0000(\d+)\u0000/g, (_, i) => stash[+i]);

// Unit spheres for l^p in R^2.
const ps = [[1, '#2f5bd3', 'p = 1'], [1.5, '#0f7a5c', 'p = 1.5'], [2, '#7a3fc2', 'p = 2'], [4, '#b4471a', 'p = 4'], [Infinity, '#8a6a00', 'p = ∞']];
const S = 110, C = 140;
const pts = p => {
  const out = [];
  for (let k = 0; k <= 720; k++) {
    const t = (k / 720) * 2 * Math.PI, c = Math.cos(t), s = Math.sin(t);
    const n = p === Infinity ? Math.max(Math.abs(c), Math.abs(s)) : Math.pow(Math.pow(Math.abs(c), p) + Math.pow(Math.abs(s), p), 1 / p);
    out.push(`${(C + S * c / n).toFixed(2)},${(C - S * s / n).toFixed(2)}`);
  }
  return out.join(' ');
};
let svg = `<svg viewBox="0 0 430 280" width="100%" style="max-width:430px" role="img" aria-label="Unit spheres for l^p metrics in the plane">`;
svg += `<line x1="10" y1="${C}" x2="270" y2="${C}" stroke="var(--muted)" stroke-width="1"/><line x1="${C}" y1="10" x2="${C}" y2="270" stroke="var(--muted)" stroke-width="1"/>`;
ps.forEach(([p, col, lab], i) => {
  svg += `<polyline points="${pts(p)}" fill="none" stroke="${col}" stroke-width="2"/>`;
  svg += `<line x1="295" y1="${40 + i * 28}" x2="320" y2="${40 + i * 28}" stroke="${col}" stroke-width="3"/><text x="328" y="${45 + i * 28}">${lab}</text>`;
});
svg += `<text x="${C + S + 4}" y="${C - 6}">1</text><text x="${C + 6}" y="${C - S - 4}">1</text></svg>`;
html = html.replace('<!--SPHERES-->', svg);

// Inline KaTeX CSS with embedded woff2 fonts.
const kdir = path.join(here, 'node_modules/katex/dist');
let css = fs.readFileSync(path.join(kdir, 'katex.min.css'), 'utf8');
css = css.replace(/src:url\(fonts\/([^)]+?)\.woff2\) format\("woff2"\)(,url\([^)]+\) format\("[^"]+"\))*/g, (_, name) => {
  const b64 = fs.readFileSync(path.join(kdir, 'fonts', name + '.woff2')).toString('base64');
  return `src:url(data:font/woff2;base64,${b64}) format("woff2")`;
});
html = html.replace('/*KATEX_CSS*/', () => css);

const out = path.join(here, 'MST-Study-Guide.html');
fs.writeFileSync(out, html);
console.log(`Wrote ${out} (${(html.length / 1024).toFixed(0)} KB), KaTeX errors: ${errors}`);
if (errors) process.exit(1);
