# MATH6342 Linear Systems: file index

## Official (authoritative), Gordon Blower 2026/7
- Beamer deck (231 frames): `MATH6342 Linear systems beamer (4).pdf` (or any `beamer*`: these are different download versions; the newest has more lines)
- Lecture notes: `MATH6342 lecture notes.pdf`
- The same deck split by chapter (also in `unzipped/MATH6342_Sections/`):
  `00_Introduction`, `01_Linear_Systems_and_Their_Description` (block diagrams, (A,B,C,D) systems),
  `02_Solving_Linear_Systems_by_Matrix_Theory` (determinants, eigenvalues, exp(tA)),
  `03_Laplace_Transforms`, `04_Transfer_Functions_Realization_and_Stability`,
  `05_Feedback_Control`, `06_Appendix_MATLAB_Commands`, `07_Glossary`
- Assessed exercise sheets:
  - AE1 (A1.1 block diagrams for ODE/integral equations, A1.2 …): `MATH6342LinearsystemsAssessedexercise1.pdf`
  - AE2 (eigenvalues, transfer function, companion matrix, observability rank): `MATH6342LinearsystemsAssessedexercise2.pdf` (scanned; transcription in `text/`)
  - AE3 (Laplace transforms, IVP, diagonalisation/exp(tA), positive definite matrices): `MATH6342LinearsystemsAssessedexercise3.pdf` (scanned; transcription in `text/`)

## Step-by-step exam revision guide (newest; built from the official notes, answers checked with sympy)
- `revision_guide/MATH6342_Exam_Revision_Guide.pdf` (62 pages): whole module, an 'In plain words' box opening every subchapter, a symbol/word decoder, full-mark answer layouts, chapters 1-5, a worked example and an exam-style question set for each chapter, proofs checklist, mock paper with full solutions, formula sheet.
  LaTeX source: `revision_guide/MATH6342_Exam_Revision_Guide.tex` + `revision_guide/ch*.tex`.
- `revision_guide/MATH6342_Study_Plan_1450-1920.pdf` (5 pages): timed 14:50-19:20 study plan in 7 blocks (Blocks 0-6), with recall, checklists and a tracker (also Section 2 of the guide). Source: `MATH6342_Study_Plan_1450-1920.tex` + `plan_body.tex`; shared preamble in `preamble.tex`. Build the guide first (the plan reads its .aux for page numbers). `gen_plan.py` generates an alternative subchapter-by-subchapter plan (not the current one).
- Note: frames 119-120 of the official notes list the Jordan blocks as "J2(3) + J2(1) + J2(3)"; the matrix shown is J3(2) + J1(2) + J2(3) (typo in the notes).

## Sai's answers (verify before trusting)
- AE1: `A1_1_ii_block_diagram.pdf/.tex`, `A1_2_block_diagrams.pdf/.tex`, previews `A1_*.png`
- AE2: `MATH6342_Assessed_Exercise_2_Sai_Vanam.pdf`
- AE3: `MATH6342_Assessed_Exercise_3_Sai_Vanam.pdf`

## Revision guides (AI/Sai-made, verify before trusting)
- `MATH6342_Exam_Cheatsheet.pdf/.tex`: cheat sheet + worked examples
- `MATH6342_Rapid_Revision.pdf`: short companion
- `MATH6342_Complete_Exam_Revision_Guide.pdf`, `MATH6342_Linear_Systems_Complete_Study_Guide.html`: full course
- `MATH6342_Detailed_Study_Guide.pdf`: expanded lecture notes (source in `unzipped/MATH6342_Overleaf_Project/`)
- `MATH6342_Visual_LaTeX_Revision_Guide.pdf/.tex`: visual exam guide
- `MATH6342_Linear_Systems_Study_Guide.pdf`: summary guide
- `MATH6342_Slides_41-59_Explained.pdf`: slides 41–59 explained
- `MATH6342_Week1_*.pdf/.tex`: Week 1 lecture guides
