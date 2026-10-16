# Part 3 - Evaluation of trained models (3 h CM + 1 h TD)

Contents:
- `notes/` - lecture notes (Markdown).
- `slides/` - deck (.pptx) and its Markdown equivalent (.md).
- `slides/resources/` - rendered PDF and SVG figures.
- `notebooks/` - TD notebooks, student and instructor/solution versions.

## Current practical: strawberry model evaluation

- [Student Colab notebook](notebooks/TD2_strawberry_student.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_strawberry_student.ipynb)
- [Instructor version with discussion notes](notebooks/TD2_strawberry_solution.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_strawberry_solution.ipynb)

All code is supplied in short cells, each preceded by a plain-language explanation.
Six written questions cover overfitting, fair model comparison, model choice
and interpretation of mistakes. No coding or parameter changes are required.
The opening tables show the source file and the prepared measurements, with
plots of two spectra before and after the eight-feature transformation.

Using the same eight spectral summaries as Foundations, students fit a small
tree, a deep tree and a random forest. They compare training and validation
accuracy in a table and bar chart, choose using validation accuracy, then read
the chosen model's test confusion matrix. Cross-validation, SVMs and statistical
model comparisons are omitted from this introductory version.

The 981 cleaned observations are divided into 588 training, 196 validation and
197 test observations. Test membership matches Foundations; its reuse is a
classroom comparison rather than new independent evidence. Each notebook runs
on its own in a CPU Colab runtime and downloads the version-pinned data file.
The notebook explains why the smaller training group can change the small
tree's results, defines overfitting before asking students to interpret it,
and introduces the outlier-screening question taken up in Applications.

See [data provenance and licence](../datasets/strawberry/README.md). The earlier
`TD2_evaluation_student.ipynb` and `TD2_evaluation_solution.ipynb` use the
scikit-learn diagnostic dataset and remain available as legacy exercises.

## Parallel practical: Tox21 model evaluation

- [Student notebook](notebooks/TD2_tox21_student.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_tox21_student.ipynb)
- [Instructor notebook with suggested answers](notebooks/TD2_tox21_solution.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_tox21_solution.ipynb)

The same simple format, using DeepChem's public Tox21 data: all code supplied
in cells of at most ten lines and six written questions. Source records,
four example structures, a labelled descriptor table and a two-feature plot
introduce the data before modelling.
Eight calculated molecular descriptors predict the SR-MMP assay result.
Students compare a small tree, a deep tree and a random forest, then inspect
the chosen model's missed Active results and false alarms. The notebook
explains the unequal class sizes and the fixed class-balancing setting.

The Tox21 series shares one cleaned subset and test group. Evaluation divides
the Foundations training group into 3,482 training and 1,161 validation records;
the same 1,161 test records remain excluded from model choice. The final
question introduces the descriptor-outlier task in Applications. See
[data preparation and provenance](../datasets/tox21/README.md).
