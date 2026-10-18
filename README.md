# Machine Learning and AI for Analytical Chemistry

Course materials for the M2 teaching unit, Master 2 Chimie — Sciences analytiques
(3 ECTS, 15 h lectures / 6 h practicals).

Coordinator: Lennart Martens. Instructors: Lennart Martens, Robbin Bouwmeester and Jérôme Pansanel.

## Getting started

- Open the materials for your day below. The course runs over five days, with Foundations spread across the first two.
- Complete both the Strawberry and Tox21 practical series, in the order Foundations → Evaluation → Applications.
- Work through each Strawberry practical together with the instructor, then complete the corresponding Tox21 practical independently to apply what you have learned.
- Click an Open in Colab button to run a practical without installing anything locally. The six current practicals provide all code; run the cells and answer the interpretation questions in words.
- Save your own notebook copy to keep your answers. You can also fork this repository if you want an editable copy of all course materials.
- Complete the Foundations quiz after day 2, the Evaluation quiz after day 3 and the Applications quiz after day 4. Each quiz follows the lecture and both corresponding practicals.

## Grading

The three quizzes together count for 40% of the final mark. The written exam
counts for the remaining 60%. The LLM-assisted project is part of the day 5
practical.


## Course overview

| Day | Main question | Materials | Quiz |
|---|---|---|---|
| 1. Foundations | How does a model learn to predict from data? | [Lectures and practicals](#day-1-foundations) | Foundations quiz follows day 2 |
| 2. Foundations and Data | How do neural networks learn, and how do we prepare and reuse data? | [Lectures and practicals](#day-2-foundations-and-data) | [Foundations quiz](https://forms.gle/EYMPYgqdB4GiHHZN7) |
| 3. Evaluation | Which model should we trust on new examples? | [Lectures and practicals](#day-3-evaluation) | [Evaluation quiz](https://forms.gle/NrJCVNiXqYFhpYPM9) |
| 4. Applications | Which measurements or compounds need a closer look? | [Lectures and practicals](#day-4-applications) | [Applications quiz](https://forms.gle/nnajgJVD9WouWYkM7) |
| 5. LLM tools | How can LLMs support research while we check their outputs? | [Lectures and practical](#day-5-llm-tools) | — |

[Grading](#grading) · [Datasets](#datasets) · [Earlier materials](#earlier-materials)

### Day 1: Foundations

<details>
<summary>Introduction, regression and Foundations practicals</summary>

#### Lectures

| Topic | Slides |
|---|---|
| Introduction to machine learning | [PowerPoint](01_Foundations/slides/1_1_introduction.pptx) |
| Regression | [PowerPoint](01_Foundations/slides/1_2_regression.pptx) |
| Logistic regression | [PowerPoint](01_Foundations/slides/1_3_logistic_regression.pptx) |
| Foundations overview deck, covering days 1–2 | [PowerPoint](01_Foundations/slides/Part1_Foundations_slides.pptx) · [PDF](01_Foundations/slides/resources/Part1_Foundations_slides.pdf) |

[Lecture notes](01_Foundations/notes/Part1_Foundations_notes.md) · [Overview slide outline](01_Foundations/slides/Part1_Foundations_slides.md) · [Figures](01_Foundations/slides/resources/)

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

| Topic | Slides |
|---|---|
| Neural networks | [PDF](01_Foundations/slides/2_1_neural-networks.pdf) |
| Convolutional neural networks | [PDF](01_Foundations/slides/2_2_convolutional-neural-networks.pdf) |
| Recurrent neural networks and transformers | [PDF](01_Foundations/slides/2_3_recurrent-neural-networks-transformers.pdf) |
| Data: quality, representations, repositories, formats and reuse | [PowerPoint](02_Data/slides/Part2_Data_slides.pptx) · [PDF](02_Data/slides/resources/Part2_Data_slides.pdf) |

Foundations: [Lecture notes](01_Foundations/notes/Part1_Foundations_notes.md) · [Overview slide outline](01_Foundations/slides/Part1_Foundations_slides.md) · [Figures](01_Foundations/slides/resources/)

Data: [Lecture notes](02_Data/notes/Part2_Data_notes.md) · [Slide outline](02_Data/slides/Part2_Data_slides.md) · [Figures](02_Data/slides/resources/) · [Module overview](02_Data/README.md)

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
| Evaluation of trained models | [PowerPoint](03_Evaluation/slides/Part3_Evaluation_slides.pptx) · [PDF](03_Evaluation/slides/resources/Part3_Evaluation_slides.pdf) |
| Failure modes: underfitting, overfitting, bias, out of distribution and information leakage | [Visual PowerPoint supplement](03_Evaluation/slides/Part3_Failure_modes_visual.pptx) · [Slide outline and teaching notes](03_Evaluation/slides/Part3_Failure_modes_visual.md) |

[Lecture notes](03_Evaluation/notes/Part3_Evaluation_notes.md) · [Main slide outline](03_Evaluation/slides/Part3_Evaluation_slides.md) · [Figures](03_Evaluation/slides/resources/)

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

[Practical guidance](03_Evaluation/README.md) · [Browse all Evaluation materials](03_Evaluation/)

</details>

### Day 4: Applications

<details>
<summary>Lecture slides, practicals and quiz</summary>

#### Lectures

| Topic | Slides |
|---|---|
| Applications in analytical chemistry: retention, fragmentation, identification, ion mobility and NMR | [PowerPoint](04_Applications/slides/Part4_Applications_slides.pptx) · [PDF](04_Applications/slides/resources/Part4_Applications_slides.pdf) |
| CompOmics applications | [PowerPoint](04_Applications/slides/4_Applications_compomics.pptx) |

[Lecture notes](04_Applications/notes/Part4_Applications_notes.md) · [Slide outline](04_Applications/slides/Part4_Applications_slides.md) · [Figures](04_Applications/slides/resources/)

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

| Topic | Slides |
|---|---|
| Recurrent neural networks and transformers | [PowerPoint](05_LLM_Tools/slides/5_1_recurrent-neural-networks-transformers.pptx) |
| Foundation models | [PowerPoint](05_LLM_Tools/slides/5_2_foundation-models.pptx) |
| LLMs as research tools: overview | [PowerPoint](05_LLM_Tools/slides/Part5_LLM_slides.pptx) · [PDF](05_LLM_Tools/slides/resources/Part5_LLM_slides.pdf) |

- [Figures](05_LLM_Tools/slides/resources/)

| Practical | Student notebook | Run the practical | Answers |
|---|---|---|---|
| LLMs as research tools | [Notebook](05_LLM_Tools/notebooks/TD4_LLM_tools_student.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/05_LLM_Tools/notebooks/TD4_LLM_tools_student.ipynb) | [Notebook with answers](05_LLM_Tools/notebooks/TD4_LLM_tools_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/05_LLM_Tools/notebooks/TD4_LLM_tools_solution.ipynb) |

[Module overview](05_LLM_Tools/README.md) · [Browse all LLM materials](05_LLM_Tools/)

</details>

## Datasets

| Dataset | Used for | Documentation and download |
|---|---|---|
| Strawberry fruit purées | Spectral classification and outlier detection | [Background, preparation and licence](datasets/strawberry/README.md) · [CSV download (.gz)](datasets/strawberry/fruit_purees.csv.gz) |
| DeepChem Tox21 | Assay prediction, molecular generation and descriptor outliers | [Background, preparation and provenance](datasets/tox21/README.md) · [CSV download (.gz)](datasets/tox21/tox21.csv.gz) |

Each notebook can run on its own and loads its data automatically. Within
each dataset series, the three notebooks reuse preparation and test records for teaching;
this reuse is not new independent validation. Tox21 assay predictions do not
establish overall toxicity or human safety. Dataset licences are documented
separately from the [course repository licence](LICENSE).

[All datasets and download guidance](datasets/README.md)

## Earlier materials

<details>
<summary>Earlier practicals and slide versions</summary>

These earlier practicals contain coding exercises. The Strawberry
and Tox21 notebooks linked under each day are the current practicals.

| Earlier practical | Student version | Answers |
|---|---|---|
| Classical ML: wine classification | [Notebook](01_Foundations/notebooks/TD1_classical_ML_student.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_classical_ML_student.ipynb) | [Notebook](01_Foundations/notebooks/TD1_classical_ML_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/01_Foundations/notebooks/TD1_classical_ML_solution.ipynb) |
| Model evaluation | [Notebook](03_Evaluation/notebooks/TD2_evaluation_student.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_evaluation_student.ipynb) | [Notebook](03_Evaluation/notebooks/TD2_evaluation_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/03_Evaluation/notebooks/TD2_evaluation_solution.ipynb) |
| Applications | [Notebook](04_Applications/notebooks/TD3_applications_student.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_applications_student.ipynb) | [Notebook](04_Applications/notebooks/TD3_applications_solution.ipynb) · [Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_applications_solution.ipynb) |

- Earlier failure-mode supplement: [PowerPoint](03_Evaluation/slides/Part3_Failure_modes_additional.pptx) · [Teaching notes](03_Evaluation/slides/Part3_Failure_modes_additional.md)
- Some overview slides and lecture notes still refer to these earlier practicals; use the current notebooks for the guided exercises.


#### Earlier project materials

These documents describe the earlier project-based assessment and are retained
as references. Their project grading weights do not apply to the current
assessment: quizzes count for 40% and the written exam for 60%.

- [Earlier project brief](assessment/project_brief.md)
- [Earlier project marking rubric](assessment/rubric.md)
- [Project dataset options](assessment/datasets_README.md)
- [Student project notebook](assessment/project_template_student.ipynb) — [Open in Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/assessment/project_template_student.ipynb) · [Worked example with answers](assessment/project_solution.ipynb) ([Colab](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/assessment/project_solution.ipynb))
- [Earlier assessment overview](assessment/README.md)

</details>
