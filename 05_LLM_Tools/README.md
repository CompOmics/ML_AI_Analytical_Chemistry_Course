# Part 5: LLMs as research tools

[Lecture notes](notes/Part5_LLM_notes.md)

Use an LLM to help build a peptide retention-index predictor, while checking
its code and explanations. This practical follows the Foundations, Evaluation
and Applications notebooks and uses a new analytical-chemistry dataset.

## Practical

| Version | Notebook | Open in Colab |
|---|---|---|
| Student | [Peptide retention-time practical](notebooks/TD4_peptide_RT_student.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/05_LLM_Tools/notebooks/TD4_peptide_RT_student.ipynb) |
| Answers and reference implementation | [Instructor notebook](notebooks/TD4_peptide_RT_solution.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/05_LLM_Tools/notebooks/TD4_peptide_RT_solution.ipynb) |

The student notebook is an open project brief. It supplies one cell to load real
peptide data, two empty code workspaces, and questions to guide the analysis.
Students use their own prompts to choose sequence features and a model, build a
baseline, compare validation results, and try a deliberate change before the
final test. No algorithm or parameter settings are prescribed.

Students ask an LLM to write code in manageable pieces and check what it does.
They justify their choices, produce a prediction plot, answer five questions,
and keep a short prompt log. The instructor notebook contains one possible
worked solution, rather than a required student workflow. There is no modelling
or fallback implementation in the student notebook.

No paid subscription, API key or GPU is required by the practical. If students
cannot access an LLM, the instructor can discuss their plan and provide an
example response. Record that assistance honestly in the log.

The target is iRT, a calibrated retention index without time units, rather than
minutes. See the [dataset documentation and backup](../datasets/peptide_rt/README.md)
for provenance and limits. The practical is part of day 5; the three course
quizzes, rather than this notebook, make up the 40% continuous-assessment mark.

## Lectures

- [Recurrent neural networks and transformers](slides/5_1_recurrent-neural-networks-transformers.pptx)
- [Foundation models](slides/5_2_foundation-models.pptx)
- [LLMs as research tools](slides/Part5_LLM_slides.pptx)
