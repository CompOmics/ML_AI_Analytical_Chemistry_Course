# Part 4: Applications in analytical chemistry

[Lecture notes](notes/Part4_Applications_notes.md) · [PowerPoint](slides/4_Applications_compomics.pptx)

The presentation covers applications in proteomics, NMR, Raman spectroscopy
and powder diffraction. Work through the Strawberry practical with the
instructor, then complete the Tox21 practical independently.

## Current practical: strawberry outlier detection

- [Student notebook](notebooks/TD3_strawberry_student.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_strawberry_student.ipynb)
- [Instructor notebook with suggested answers](notebooks/TD3_strawberry_solution.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_strawberry_solution.ipynb)

All code is supplied in short cells of at most ten lines, with explanations,
two figures and five written interpretation questions. Four setup cells recap
the data preparation from Foundations, with one feature-table reminder, before
students choose the Strawberry reference group. The two figures focus on a
flagged sample and the overall screening results. The notebook runs independently
in Google Colab with the standard CPU runtime.

It reuses the same cleaned strawberry data, eight infrared window means and
197-sample test partition as Foundations and Evaluation. One isolation forest
learns from 280 Strawberry training samples. Students interpret its
flags, inspect a flagged example and compare flags with recorded targets.
These reference samples come from the original 784-sample Foundations training
group, including the samples used for validation in Evaluation. The flagging
setting is chosen in advance; the boundary is learned to flag about 5% of the
training reference samples. This does not estimate adulteration prevalence or prescribe
the fraction of test samples flagged.

The notebook explicitly distinguishes these review flags from the class
predictions and classification accuracy used in the earlier practicals.
A one-feature random-cut example explains why a separated value can be
isolated quickly, and why the forest combines route lengths over many trees.

The exercise treats flags as prompts for follow-up. Neither a flag nor its
absence certifies product purity. The reused classroom test set does not
provide new independent validation. See the [data provenance and licence](../datasets/strawberry/README.md).

## Parallel practical: Tox21 descriptor outliers

- [Student notebook](notebooks/TD3_tox21_student.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_tox21_student.ipynb)
- [Instructor notebook with suggested answers](notebooks/TD3_tox21_solution.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CompOmics/ML_AI_Analytical_Chemistry_Course/blob/main/04_Applications/notebooks/TD3_tox21_solution.ipynb)

All code is supplied in cells of at most ten lines, with two figures and five
written interpretation questions. Four setup cells recap the data preparation
from Foundations, with one descriptor-table reminder, before students choose
the reference group and begin outlier screening.
It reuses the eight Tox21
descriptors and 1,161 test compounds from Foundations and Evaluation.

One isolation forest learns from all 4,643 original training records, including
both Active and Inactive assay classes. Its flags identify unusual descriptor
patterns, not assay activity. Students inspect a flagged structure's descriptors
and explain why unflagged does not mean safe. The notebook explicitly
distinguishes this reference group from the Strawberry-only reference group
in the strawberry practical. See [data preparation and provenance](../datasets/tox21/README.md).
The same random-cut illustration and interpretation question explain isolation
lengths, with the reference group kept distinct from assay activity.
