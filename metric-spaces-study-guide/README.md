# Metric Spaces & Topology (MATH6310): Study Guide, Sections 0–4

A self-contained revision guide built from the lecture notes. It covers every definition, theorem and proof, a full worked solution to every exercise, trap questions, flashcards and a glossary.

- `MST-Study-Guide.html`: open it in any browser. It works offline because the math is pre-rendered and the fonts are embedded. Solutions are collapsible, and there is a light/dark theme.
- `MST-Study-Guide.pdf`: the same content as a 70-page A4 PDF, with every solution expanded.

## Rebuilding

```bash
npm install
node build.mjs   # src/*.html -> MST-Study-Guide.html (KaTeX pre-rendered)
node pdf.cjs     # HTML -> PDF (needs Playwright + Chromium)
```
