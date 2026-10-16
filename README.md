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
  each provided as a student version and an instructor/solution version. The
  current strawberry and Tox21 practicals provide all code and interpretation response
  cells; the other student notebooks contain TODO code cells.

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
Click an **Open in Colab** button below or at the top of a guided notebook's
GitHub preview, then run the cells top to bottom. The current Foundations,
Evaluation and Applications practicals are written for students who do not program. They
provide short code cells, plain-language explanations and written questions.
Strawberry Foundations previews the source table and plots spectra before and
after window averaging. Strawberry Evaluation and Applications use a quick
recap with four setup cells, then focus on their new questions.
Tox21 Foundations shows source records, example structures, a descriptor table with recorded targets and a plot of two descriptor values. Its Evaluation and
Applications notebooks use the same quick-recap approach as the strawberry series.
The other student notebooks contain TODO code cells. They use widely available packages
(scikit-learn, pandas, numpy, matplotlib); any extra package is installed in
the first cell.

### How the strawberry practicals connect

Use these practicals in order. They share the same data preparation and 197
test samples. Trees and outlier detection use eight infrared window means;
the Evaluation CNN additionally uses the full 235-position spectra.
Each adds one main idea:

| Practical | Main question | New idea |
|---|---|---|
| Foundations | How do a small tree and neural network predict the recorded class? | Reading spectra, forming features, training and testing |
| Evaluation | Does a model that fits training samples well also work elsewhere? | Overfitting, validation and model choice |
| Applications | Which measurements are unusual compared with Strawberry examples? | Outlier flags and laboratory follow-up |

All three run independently and provide all code in cells of at most ten lines.
Foundations has six written interpretation questions, Evaluation has seven,
and Applications has five. Students run the code unchanged
and write answers in text cells. Shared preparation is repeated so that no
files or variables need to be transferred between notebooks.

Evaluation takes 196 of the original 784 training samples for validation,
leaving 588 for fitting. Applications returns to that original training group
and uses its 280 samples with a Strawberry target as the detector's reference.
The test group stays the same throughout; its reuse supports teaching rather
than fresh independent validation. Applications reports review flags, which
have a different meaning from the class predictions in the first two practicals.

### Foundations practical: strawberry authentication

- [Student Colab notebook](01_Foundations/notebooks/TD1_strawberry_student.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_strawberry_student.ipynb)
- [Instructor version with discussion notes](01_Foundations/notebooks/TD1_strawberry_solution.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_strawberry_solution.ipynb)

The practical first shows the source table and two measured spectra, then
visualises how the same spectra become eight fixed infrared window means.
It introduces an 80/20 training/test split, a small decision tree and a neural
network with one hidden layer of four neurons. Scaling for the network is
learned from training samples only. Six written questions cover the inputs,
the tree's rules, accuracy and the two models' mistakes. All code is supplied
in cells of at most ten lines, with explanations above them. The notebook
downloads a version-pinned data file automatically.
See [data provenance and licence](datasets/strawberry/README.md).

The earlier wine-based `TD1_classical_ML_*` notebooks remain available as legacy
material. The Foundations lecture notes and slides still refer to that earlier
exercise; use the strawberry notebook's introduction for the current practical.

### Evaluation practical: overfitting and model comparison

- [Student Colab notebook](03_Evaluation/notebooks/TD2_strawberry_student.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_strawberry_student.ipynb)
- [Instructor version with discussion notes](03_Evaluation/notebooks/TD2_strawberry_solution.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_strawberry_solution.ipynb)

The practical starts with four short setup cells and a feature-table reminder,
then moves to the training–validation–test split. It reuses the same cleaned
strawberry data. Students compare a small tree, a deep tree and a random forest
using eight window means, then add a small 1D CNN using the full 235-position
spectra. Scaling for the CNN is learned from training spectra only. The table
identifies each model's input, so students can distinguish a pipeline comparison
from an architecture-only comparison. They choose using validation accuracy
and inspect the selected model's test mistakes. A training/test line plot over
tree depths follows the fixed choice as an overfitting illustration; choosing
a depth from that curve would require a new independent final test.
The code is supplied in short cells, with seven written questions and
saved outputs. This introductory version does not include cross-validation,
SVMs or statistical model comparisons.

The Foundations training set is divided into training and validation subsets;
the test partition has the same membership as in Foundations. Its reuse is
explicitly a classroom comparison rather than new independent confirmation.
The earlier `TD2_evaluation_*` notebooks remain available as legacy material.

### Applications practical: outlier detection

- [Student Colab notebook](04_Applications/notebooks/TD3_strawberry_student.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_strawberry_student.ipynb)
- [Instructor version with discussion notes](04_Applications/notebooks/TD3_strawberry_solution.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_strawberry_solution.ipynb)

The practical uses the same strawberry data and eight window means. Four
setup cells recap the preparation from Foundations, then students choose
the Strawberry reference group and begin outlier detection.
One isolation forest learns from the 280 Strawberry training samples
and flags unusual measurements among the same 197 test samples used earlier.
All code is supplied in cells of at most ten lines. Five written questions focus
on choosing a reference group, interpreting flags, inspecting an example and
deciding what laboratory follow-up is needed. Both versions include saved outputs.

A flag indicates a need for investigation; it does not establish adulteration.
The fixed 5% training-reference flagging setting is explained as a teaching
choice, rather than a measurement of adulteration prevalence. The earlier
`TD3_applications_*` notebooks remain available as legacy material. The
Applications lecture notes and slides cover broader examples; this strawberry
notebook is the current practical.

### Parallel Tox21 practicals: molecular descriptors and assay activity

This series follows the same three-step progression with DeepChem's public
Tox21 data. It uses eight readable molecular descriptors and one assay,
SR-MMP. Every practical supplies all code in cells of at most ten lines.
Foundations has nine interpretation questions, Evaluation has six, and
Applications has five. The latter two start with four setup cells and a descriptor-table
reminder, then move to their new material. Instructor copies
include suggested answers and saved outputs. Students do not write or change code.

| Practical | Student notebook | Instructor notebook |
|---|---|---|
| Foundations: classification and molecular generation | [Student](01_Foundations/notebooks/TD1_tox21_student.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_tox21_student.ipynb) | [Instructor](01_Foundations/notebooks/TD1_tox21_solution.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_tox21_solution.ipynb) |
| Evaluation: overfitting and model comparison | [Student](03_Evaluation/notebooks/TD2_tox21_student.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_tox21_student.ipynb) | [Instructor](03_Evaluation/notebooks/TD2_tox21_solution.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_tox21_solution.ipynb) |
| Applications: outlier detection | [Student](04_Applications/notebooks/TD3_tox21_student.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_tox21_student.ipynb) | [Instructor](04_Applications/notebooks/TD3_tox21_solution.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_tox21_solution.ipynb) |

Foundations introduces the Tox21 experiments and explains the SR-MMP target
before loading the data. It illustrates tree learning as a sorting route and
shows how class-balancing importance differs from compound counts.

For molecular generation, students choose aspirin, paracetamol or ibuprofen
from a dropdown, inspect the autoencoder's 512 learned values as a colour grid,
and compare values before and after random changes. The notebook reconstructs
the chosen starting structure and decodes twelve changed latent representations.
Students inspect invalid outputs, repeated structures,
fingerprint similarity and matches against the downloaded Tox21 file. The
existing small tree predicts SR-MMP classes for the valid candidates using
the same eight descriptors. These predictions have no new measured
targets and do not establish overall toxicity or safety. The standard CPU
runtime is sufficient; the model weights download automatically on first use.
Student notebooks retain concise sources and interpretation limits; package
versions, checksums and other provenance details are kept in instructor notes
and the data documentation. Both practical series use target terminology in
the prose, tables and code variables, and explain rounding with numerical examples.

The notebooks calculate descriptors with a pinned RDKit release and read
DeepChem's source CSV directly; installing the DeepChem Python package is not
required. They exclude missing assay results and unreadable structures,
retaining 5,804 records. Foundations and Applications share 4,643 training
records and 1,161 test records; Evaluation sets aside 1,161 of those training
records for validation. Test reuse is a classroom comparison, not fresh
independent validation. Random splits do not separate chemical families.

The series explains why accuracy can hide missed Active results when Inactive
results are more common. In Applications, an isolation forest learns descriptor
patterns from both classes; its flags do not predict assay activity. Neither
an assay prediction nor a flag certifies human safety. See the
[data preparation, provenance and backup](datasets/tox21/README.md).

## Assessment

Continuous assessment is based on an assessed Colab notebook plus a short
report; a terminal written exam covers the lecture material. See `assessment/`
and the unit description (Fiche) for full modalites d'evaluation.
