# Machine Learning and AI for Analytical Chemistry

Course materials for the M2 teaching unit, Master 2 Chimie — Sciences analytiques
(3 ECTS, 15 h lectures / 6 h practicals).

Coordinator: Lennart Martens. Instructors: Lennart Martens, Robbin Bouwmeester and Jérôme Pansanel.

## Getting started

- All materials and links to them are below
- Practicals are done in the form of notebooks; we recommend you can run them on google colab (requires a google account) or locally (we can help you with the installation, but this is much more involved)
- Answers for all practicals are available
- Complete the Foundations quiz after day 2, the Evaluation quiz after day 3 and the Applications quiz after day 4. Each quiz follows the lecture and both corresponding practicals.
- Based on timing we might change when specific subjects are discussed

## Grading

The three quizzes together count for 40% of the final mark. The written exam
counts for the remaining 60%. The LLM-assisted project is part of the day 5
practical.

## Lecture notes

These notes follow the current presentations and practicals, with consistent
terminology and explanations for students who do not program. The Data notes
bring together the preparation and representation choices used in the practicals.

| Topic | Notes |
|---|---|
| Foundations (days 1 and 2) | [Foundations notes](01_Foundations/notes/Part1_Foundations_notes.md) |
| Data | [Data notes](02_Data/notes/Part2_Data_notes.md) |
| Evaluation | [Evaluation notes](03_Evaluation/notes/Part3_Evaluation_notes.md) |
| Applications | [Applications notes](04_Applications/notes/Part4_Applications_notes.md) |
| LLM tools and the peptide project | [LLM Tools notes](05_LLM_Tools/notes/Part5_LLM_notes.md) |

## Course overview

| Day | Main question | Materials | Quiz |
|---|---|---|---|
| 1. Foundations | How does a model learn to predict from data? | [Lectures and practicals](#day-1-foundations) | Foundations quiz follows day 2 |
| 2. Foundations and Data | How do neural networks learn, and how do we prepare and reuse data? | [Lectures and practicals](#day-2-foundations-and-data) | [Foundations quiz](https://forms.gle/EYMPYgqdB4GiHHZN7) |
| 3. Evaluation | Which model should we trust on new examples? | [Lectures and practicals](#day-3-evaluation) | [Evaluation quiz](https://forms.gle/NrJCVNiXqYFhpYPM9) |
| 4. Applications | Which measurements or compounds need a closer look? | [Lectures and practicals](#day-4-applications) | [Applications quiz](https://forms.gle/nnajgJVD9WouWYkM7) |
| 5. LLM tools | How can LLMs support research while we check their outputs? | [Lectures and practical](#day-5-llm-tools) | — |

[Grading](#grading) · [Lecture notes](#lecture-notes) · [Datasets](#datasets)

### Day 1: Foundations

<details>
<summary>Introduction, regression and Foundations practicals</summary>

#### Lectures

| Topic | Slides |
|---|---|
| Introduction to machine learning | [PowerPoint](01_Foundations/slides/1_1_introduction.pptx) |
| Regression | [PowerPoint](01_Foundations/slides/1_2_regression.pptx) |
| Logistic regression | [PowerPoint](01_Foundations/slides/1_3_logistic_regression.pptx) |

[Lecture notes](01_Foundations/notes/Part1_Foundations_notes.md)

#### Practicals

Begin with the data, features and small decision tree in the Strawberry notebook,
working through the steps together with the instructor. Then complete the
corresponding steps in the Tox21 notebook independently. Continue both notebooks
on day 2 for neural networks and molecular generation.

| Practical and format | Student notebook | Run the practical | Answers |
|---|---|---|---|
| Strawberry (guided): is this strawberry purée? | [Notebook](01_Foundations/notebooks/TD1_strawberry_student.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_strawberry_student.ipynb) | [Notebook with answers](01_Foundations/notebooks/TD1_strawberry_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_strawberry_solution.ipynb) |
| Tox21 (independent): predict activity and propose molecules | [Notebook](01_Foundations/notebooks/TD1_tox21_student.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_tox21_student.ipynb) | [Notebook with answers](01_Foundations/notebooks/TD1_tox21_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_tox21_solution.ipynb) |

#### Continue on day 2

[Foundations continued and Data](#day-2-foundations-and-data). The Foundations
quiz follows the second day.

[Browse all Foundations materials](01_Foundations/)

</details>

### Day 2: Foundations and Data

<details>
<summary>Neural networks, Data, continued practicals and Foundations quiz</summary>

#### Lectures

| Topic | Materials |
|---|---|
| Neural networks | [PowerPoint](01_Foundations/slides/1_4_Neural%20networks.pptx) |
| Convolutional neural networks | [PowerPoint](01_Foundations/slides/1_5_convolutional-neural-networks-new.pptx) |
| Data: preparation, representations, quality and reuse | [Data notes](02_Data/notes/Part2_Data_notes.md) |

[Foundations lecture notes](01_Foundations/notes/Part1_Foundations_notes.md)

The Data topic brings together the preparation and representation choices used
in the practicals, alongside data quality, formats and reuse.

#### Continue the Foundations practicals

Continue both notebooks using your saved answers from day 1. Together with the
instructor, compare a small neural network with the tree in the Strawberry
practical. Independently complete the Tox21 practical, using a pretrained
autoencoder to propose related molecules and predict their assay classes.

| Practical and format | Student notebook | Continue in Colab | Answers |
|---|---|---|---|
| Strawberry (guided) | [Notebook](01_Foundations/notebooks/TD1_strawberry_student.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_strawberry_student.ipynb) | [Notebook with answers](01_Foundations/notebooks/TD1_strawberry_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_strawberry_solution.ipynb) |
| Tox21 (independent) | [Notebook](01_Foundations/notebooks/TD1_tox21_student.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_tox21_student.ipynb) | [Notebook with answers](01_Foundations/notebooks/TD1_tox21_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_tox21_solution.ipynb) |

#### End-of-day quiz

[Take the Foundations quiz — five questions](https://forms.gle/EYMPYgqdB4GiHHZN7)

[Browse all Foundations materials](01_Foundations/) · [Browse all Data materials](02_Data/)

</details>

### Day 3: Evaluation

<details>
<summary>Lecture slides, practicals and quiz</summary>

#### Lectures

| Topic | Slides |
|---|---|
| Regularisation and failure modes: underfitting, overfitting, bias, out of distribution and information leakage | [PowerPoint](03_Evaluation/slides/3_1_regularization.pptx) |
| Decision trees | [PowerPoint](03_Evaluation/slides/3_2_DecisionTrees.pptx) |
| Ensemble learning | [PowerPoint](03_Evaluation/slides/3_3_ensemble_learning.pptx) |

[Lecture notes](03_Evaluation/notes/Part3_Evaluation_notes.md)

#### Practicals

Compare models using training and validation results, then check the fixed
choice on test records. Work through the Strawberry practical together with the
instructor, then complete the Tox21 practical independently. Tree-depth plots
illustrate overfitting. The Strawberry practical also compares a small CNN using
the full spectra.

| Practical and format | Student notebook | Run the practical | Answers |
|---|---|---|---|
| Strawberry (guided): which model should we trust? | [Notebook](03_Evaluation/notebooks/TD2_strawberry_student.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_strawberry_student.ipynb) | [Notebook with answers](03_Evaluation/notebooks/TD2_strawberry_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_strawberry_solution.ipynb) |
| Tox21 (independent): compare models and inspect mistakes | [Notebook](03_Evaluation/notebooks/TD2_tox21_student.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_tox21_student.ipynb) | [Notebook with answers](03_Evaluation/notebooks/TD2_tox21_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_tox21_solution.ipynb) |

#### End-of-day quiz

[Take the Evaluation quiz — five questions](https://forms.gle/NrJCVNiXqYFhpYPM9)

[Browse all Evaluation materials](03_Evaluation/)

</details>

### Day 4: Applications

<details>
<summary>Lecture slides, practicals and quiz</summary>

#### Lectures

| Topic | Slides |
|---|---|
| Applications: proteomics, NMR, Raman and powder diffraction | [PowerPoint](04_Applications/slides/4_Applications_compomics.pptx) |

[Lecture notes](04_Applications/notes/Part4_Applications_notes.md)

#### Practicals

Use an isolation forest to flag unusual measurements or descriptor patterns.
Work through the Strawberry practical together with the instructor, then complete
the Tox21 practical independently. Interpret the flags and decide what laboratory
follow-up is needed. A flag requests review; its presence or absence does not
establish purity or safety.

| Practical and format | Student notebook | Run the practical | Answers |
|---|---|---|---|
| Strawberry (guided): which purées need a closer look? | [Notebook](04_Applications/notebooks/TD3_strawberry_student.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_strawberry_student.ipynb) | [Notebook with answers](04_Applications/notebooks/TD3_strawberry_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_strawberry_solution.ipynb) |
| Tox21 (independent): which compounds look unusual? | [Notebook](04_Applications/notebooks/TD3_tox21_student.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_tox21_student.ipynb) | [Notebook with answers](04_Applications/notebooks/TD3_tox21_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_tox21_solution.ipynb) |

#### End-of-day quiz

[Take the Applications quiz — five questions](https://forms.gle/nnajgJVD9WouWYkM7)

[Practical guidance](04_Applications/README.md) · [Browse all Applications materials](04_Applications/)

</details>

### Day 5: LLM tools

<details>
<summary>Lecture slides and practical</summary>

Use LLMs to support research while documenting prompts, checking outputs and
keeping responsibility for the analysis.

In the peptide practical, build your own retention-index model with an LLM.
The notebook supplies the data and an open project brief. Choose your features
and model, compare with a baseline, and try an improvement using validation data
before the final test. Explain your decisions and document your prompts and checks.

| Topic | Slides |
|---|---|
| Recurrent neural networks and transformers | [PowerPoint](05_LLM_Tools/slides/5_1_recurrent-neural-networks-transformers.pptx) |
| Foundation models | [PowerPoint](05_LLM_Tools/slides/5_2_foundation-models.pptx) |
| LLMs as research tools: overview | [PowerPoint](05_LLM_Tools/slides/Part5_LLM_slides.pptx) · [PDF](05_LLM_Tools/slides/resources/Part5_LLM_slides.pdf) |

[Lecture notes](05_LLM_Tools/notes/Part5_LLM_notes.md) · [Figures](05_LLM_Tools/slides/resources/)

| Practical | Student notebook | Run the practical | Answers |
|---|---|---|---|
| Peptide retention-time prediction: prompt, build and verify | [Notebook](05_LLM_Tools/notebooks/TD4_peptide_RT_student.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/05_LLM_Tools/notebooks/TD4_peptide_RT_student.ipynb) | [Worked example](05_LLM_Tools/notebooks/TD4_peptide_RT_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/05_LLM_Tools/notebooks/TD4_peptide_RT_solution.ipynb) |

[Module overview](05_LLM_Tools/README.md) · [Browse all LLM materials](05_LLM_Tools/)

</details>

## Datasets

| Dataset | Used for | Documentation and download |
|---|---|---|
| Strawberry fruit purées | Spectral classification and outlier detection | [Background, preparation and licence](datasets/strawberry/README.md) · [CSV download (.gz)](datasets/strawberry/fruit_purees.csv.gz) |
| DeepChem Tox21 | Assay prediction, molecular generation and descriptor outliers | [Background, preparation and provenance](datasets/tox21/README.md) · [CSV download (.gz)](datasets/tox21/tox21.csv.gz) |
| Peptide retention indices (DLOmix / ProteomeTools) | LLM-assisted regression project in Part 5 | [Background, preparation and provenance](datasets/peptide_rt/README.md) · [Classroom CSV backup (.gz)](datasets/peptide_rt/peptides_6000.csv.gz) |

Each practical loads its data automatically and can be started independently.
Within the Strawberry and Tox21 series, the three notebooks reuse preparation
and test records for teaching;
this reuse is not new independent validation. Tox21 assay predictions do not
establish overall toxicity or human safety. Dataset licences are documented
separately from the [course repository licence](LICENSE).

[All datasets and download guidance](datasets/README.md)
