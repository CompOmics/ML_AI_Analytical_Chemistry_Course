# Assessed project: brief

**Machine Learning and AI for Analytical Chemistry (3 ECTS)**
Continuous-assessment component. Weight: 40 % of the final mark (coefficient 1.2;
the written exam is the remaining 60 %, coefficient 1.8). Work in pairs (binome).

## Goal

Produce a documented Google Colab notebook that solves a small machine learning
problem on analytical-chemistry data, together with a short report and an
LLM-use appendix. The project exercises every competency of the course: building
features, training and evaluating a model honestly, interpreting it, and using
LLMs as adaptive tools while staying in control of correctness.

## Choose one option

**Option A - Prediction (regression or classification).**
Build a model that predicts a property from features, for example retention time
or a physicochemical property from molecular descriptors, or a class from a
spectrum. You must use a leakage-free split (split by molecule or by group where
replicates exist) and report an honest, cross-validated estimate. A worked
solution for Option A is provided as `project_solution.ipynb`.

**Option B - Spectral classification (deep learning allowed).**
Classify 1D spectra (IR, Raman, NMR, or mass spectra) into known classes with a
classical baseline and, if you wish, a small 1D CNN. Justify the architecture and
evaluate it against the baseline.

**Option C - Critique and repair.**
Take a deliberately flawed analysis (leakage, scaling on all data, a single split
reported as validated) provided by the instructor, find every flaw, explain why
each inflates performance, fix them, and report the corrected, honest result.

## Required notebook structure

Use the eight sections in `project_template_student.ipynb`:

1. Problem and data description (what, from where, licence).
2. Exploratory analysis.
3. Preprocessing and splitting, with an explicit justification of the split.
4. Modelling: a baseline plus one improved model.
5. Evaluation: cross-validation and at least one uncertainty estimate.
6. Interpretation: feature importance or error analysis.
7. LLM-use appendix: key prompts, what the model got wrong, how you verified.
8. Conclusion: a short, honest critical summary.

## Deliverables

- The completed Colab notebook (`.ipynb`), runnable top to bottom.
- A short report of 3 to 5 pages (may be exported from the notebook) covering
  method, data and licensing, results, and a critical evaluation.
- The LLM-use appendix (section 7) completed.

## Rules

- LLM use is required and assessed; it must be documented in the appendix.
- Data and code licences must be respected and stated (Part 2).
- The split must be leakage-free; results reported on data the model has not seen
  (Part 3).
- Do not hard-code credentials or tokens.

## Assessment

Marked out of 20 against the rubric in `rubric.md`. A short oral question per pair
may be used to confirm authorship and understanding. Session 2 (rattrapage)
re-sits the written exam only; the project mark is retained.
