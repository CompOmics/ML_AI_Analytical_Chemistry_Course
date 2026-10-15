# Machine Learning and AI for Analytical Chemistry

Course materials for the M2 teaching unit "Machine Learning and AI for
Analytical Chemistry" (3 ECTS, 15 h CM / 6 h TD), Master 2 Chimie - Sciences
analytiques.

Coordinator: Lennart Martens. Instructors: Lennart Martens, Jérôme Pansanel.

## How the repository is organised

Each part has its own folder with three subfolders:

- `notes/` — written lecture notes in Markdown.
- `slides/` — presentation decks in PowerPoint (.pptx), each with a Markdown
  equivalent (.md) carrying the same slide-by-slide content. A `resources/`
  subfolder next to each deck keeps the rendered PDF and any SVG figures
  created for that deck, under meaningful filenames.
- `notebooks/` — hands-on tutorial (TD) notebooks in Jupyter/Colab (.ipynb),
  each provided as a student version (with TODO cells) and a solution version.

```
ML_AI_Analytical_Chemistry_Course/
  01_Foundations/      6 h CM + 1 h TD
  02_Data/             2 h CM
  03_Evaluation/       3 h CM + 1 h TD
  04_Applications/     4 h CM + 1 h TD
  05_LLM_Tools/        3 h TD
  assessment/          assessed project brief, rubric, template notebook
  datasets/            small datasets or download scripts used in the TDs
```

## Status

Complete. All five parts are built: lecture notes (Markdown), slide decks (PPTX +
Markdown equivalent), SVG figures and rendered PDFs in each deck's `resources/`,
and the TD notebooks (student + solution) for Parts 1, 3, 4 and 5. The assessed
project (brief, rubric, student template, and a worked Option A solution) is in
`assessment/`. All solution notebooks were executed end to end without error.

## Running the notebooks

The notebooks are designed for Google Colab (no local installation needed).
Open a notebook in Colab, run the cells top to bottom, and complete the TODO
cells in the student version. They use only widely available packages
(scikit-learn, pandas, numpy, matplotlib); any extra package is installed in
the first cell.

## Assessment

Continuous assessment is based on an assessed Colab notebook plus a short
report; a terminal written exam covers the lecture material. See `assessment/`
and the unit description (Fiche) for full modalites d'evaluation.
