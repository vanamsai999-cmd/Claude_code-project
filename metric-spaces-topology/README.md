# Metric Spaces & Topology study notes

- `metric-spaces-topology-ch0-5.pdf`: full LaTeX lecture-style notes, Chapters 0–5
- `metric-spaces-topology-ch3-5.pdf`: Chapters 3–5 only (continuity, completeness, compactness), plus a summary of Chapters 0–2
- `metric-spaces-topology-guide.html`: the earlier HTML version of the notes, for reading in a browser

## Rebuilding the PDFs

Sources are in `latex/`. Every chapter lives in its own file (`ch0.tex` … `ch5.tex`), shared by both documents. You need a TeX Live install with `latexmk`.

```bash
cd latex
latexmk -pdf notes-ch0-5.tex   # build this first
latexmk -pdf notes-ch3-5.tex   # reads Chapter 0-2 references from the full notes
```
