# Part 4: Applications in analytical chemistry

**Lecture notes (4 h CM + 1 h TD)**
Machine Learning and AI for Analytical Chemistry, M2 Sciences analytiques

These notes accompany the Part 4 slides and the TD3 notebook. Here the methods of
Parts 1 to 3 are put to work on real analytical problems, with an emphasis on
mass spectrometry, chromatography, ion mobility, and NMR. The aim is that you can
read a current applications paper and judge what the model does, what it was
trained on, and whether it was evaluated honestly.

---

## 1. Worked examples (about 3 h)

### 1.1 Where machine learning touches the LC-MS pipeline

A liquid-chromatography mass-spectrometry experiment is a pipeline: separation,
ionisation and fragmentation, acquisition, peak detection, and identification.
Machine learning now assists at several of these stages, and the same model
families from Part 1 reappear. Keeping the pipeline in mind shows how the
individual predictors below fit together.

### 1.2 Prediction of chromatographic retention

The retention time of a compound depends on its structure and the
chromatographic conditions. A model trained on many measured retention times
learns this relationship and predicts the retention of new compounds. The main
use is to filter candidate identifications: a candidate whose predicted retention
is far from the observed value is unlikely to be correct.

> **Example.** DeepLC predicts peptide retention times from sequence, including
> for modified peptides it has not seen, by learning from the atomic composition
> around each position. In small-molecule work, retention models built on
> molecular descriptors play the same filtering role. The predicted-versus-
> measured scatter, with its diagonal, is the standard way to judge such a model,
> and the evaluation must split by molecule (Part 3).

### 1.3 Prediction of fragmentation in mass spectrometry

Given a peptide or molecule, a model can predict the fragment ions and their
relative intensities, that is, the expected MS/MS spectrum. Comparing the
predicted spectrum with the observed one gives a similarity score that strengthens
identification.

> **Example.** MS2PIP and Prosit predict peptide fragment-ion intensities.
> Overlaying the predicted spectrum against the observed one as a mirror plot
> shows the match at a glance; the similarity feeds into identification scoring.

### 1.4 Identification of signals in mass spectrometry

Turning spectra into confident identifications is itself a machine learning
problem. Predicted retention and predicted fragmentation become features that a
model uses to separate correct from incorrect matches, a step called rescoring.
This raises the number of confident identifications at a fixed error rate.

> **Example.** Rescoring tools (for instance Percolator, and pipelines such as
> MS2Rescore) combine search-engine scores with predicted retention and
> fragmentation to re-rank peptide-spectrum matches, increasing identifications
> while controlling the false discovery rate.

### 1.5 Prediction of collisional cross section in ion mobility

In ion mobility, an ion's collisional cross section (CCS) reflects its size and
shape. Predicting CCS from structure adds an orthogonal property that further
constrains identification, because a candidate must match in mass, retention, and
CCS.

> **Example.** CCS predictors trained on measured ion-mobility data estimate the
> CCS of candidate molecules; a candidate whose predicted CCS disagrees with the
> measured value is rejected, sharpening untargeted identification.

---

## 2. Short survey (about 1 h)

### 2.1 A priori optimisation of targeted and untargeted MS

Machine learning can be used before acquisition to plan the experiment. In
targeted assays, models predict which peptides or transitions will be observable
and well-behaved, so the method targets the best ones. In untargeted work, models
help schedule acquisition and prioritise informative precursors.

> **Example.** Predicting peptide detectability and the best transitions lets a
> targeted method be designed in silico, before a single sample is run, saving
> instrument time and improving sensitivity.

### 2.2 Application of machine learning to NMR

NMR is a rich, structured signal well suited to learning. Models assist with
automated peak picking, spectral prediction from structure, compound
classification, and reaction or mixture monitoring.

> **Example.** A recent review surveys machine learning across NMR, from
> resonance assignment to quantitative analysis
> (https://www.sciencedirect.com/science/article/pii/S0079656525000196). The
> common thread is the same workflow and the same evaluation caution as the MS
> examples.

### 2.3 Current developments

The field moves quickly. Two directions are worth watching: foundation models
trained on very large spectral or molecular corpora that are then adapted to
specific tasks, and the integration of multiple predicted properties (retention,
fragmentation, CCS) into a single identification framework. This section should
be refreshed each year.

---

## Key terms

- **Retention prediction**: estimating chromatographic retention from structure.
- **Fragmentation prediction**: estimating the MS/MS spectrum of a molecule.
- **Rescoring**: re-ranking candidate identifications using predicted properties.
- **Collisional cross section (CCS)**: a size/shape property in ion mobility.
- **Detectability / transition prediction**: planning targeted assays in silico.
- **Foundation model**: a large pretrained model adapted to a downstream task.

## Further reading

- Tools: DeepLC (retention), MS2PIP and Prosit (fragmentation), Percolator and
  MS2Rescore (rescoring), and current CCS predictors.
- Review of machine learning in NMR:
  https://www.sciencedirect.com/science/article/pii/S0079656525000196
- The relevant standards and repositories from Part 2 (ProteomeXchange/PRIDE,
  mzSpecLib) for the data behind these models.
