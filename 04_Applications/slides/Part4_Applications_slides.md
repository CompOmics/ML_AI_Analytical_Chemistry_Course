# Part 4: Applications in analytical chemistry (slide deck)

Markdown equivalent of `Part4_Applications_slides.pptx` (13 slides). One section per slide.

---

## Slide 1 — Title
**Machine Learning and AI for Analytical Chemistry** — Part 4: Applications in analytical chemistry. M2 Sciences analytiques · 4 h lectures + 1 h tutorial.

## Slide 2 — Roadmap for Part 4
1. **Worked examples** — retention, fragmentation, identification and rescoring, and CCS in ion mobility.
2. **Short survey** — a priori optimisation of targeted and untargeted MS, ML for NMR, current developments.

## Slide 3 — Section divider
**Worked examples** — retention, fragmentation, identification, ion mobility.

## Slide 4 — Where ML touches the LC-MS pipeline
(Figure: LC-MS pipeline — Separation, Ionisation/fragmentation, Acquisition, Peak detection, Identification — with an ML touchpoint under each: retention prediction, fragmentation prediction, a priori optimisation, signal detection (CNN), rescoring/CCS.)
The same model families from Part 1 reappear across the pipeline; the predictors fit together into one identification workflow.

## Slide 5 — Chromatographic retention prediction
A model learns retention from structure and conditions, then predicts it for new compounds. Main use: filter candidate identifications; a candidate whose predicted retention is far from observed is unlikely. Judge it on the predicted-vs-measured diagonal, and split by molecule (Part 3). (Figure: predicted-vs-measured scatter with y=x.)

> Example: DeepLC predicts peptide retention (incl. modified peptides); small-molecule descriptor models play the same filtering role.

## Slide 6 — Fragmentation prediction in MS
Given a peptide or molecule, a model predicts the fragment ions and their intensities (the expected MS/MS spectrum). Comparing predicted with observed gives a similarity score that strengthens identification. (Figure: predicted-vs-observed mirror plot.)

> Example: MS2PIP and Prosit predict fragment-ion intensities; the mirror plot shows the match feeding identification scoring.

## Slide 7 — Identification and rescoring
Turning spectra into confident identifications is itself an ML problem. Predicted retention and fragmentation become features that re-rank candidate matches (rescoring), raising the number of confident identifications at a fixed error rate.

> Example: Percolator and pipelines such as MS2Rescore combine search scores with predicted RT and fragmentation, controlling the FDR.

## Slide 8 — Collisional cross section in ion mobility
An ion's collisional cross section (CCS) reflects its size and shape. Predicting CCS from structure adds an orthogonal property: a candidate must now match in mass, retention, and CCS, which sharpens untargeted identification.

> Example: a candidate whose predicted CCS disagrees with the measured ion-mobility value is rejected.

## Slide 9 — Section divider
**Short survey** — planning experiments, NMR, and what is next.

## Slide 10 — A priori optimisation of MS analysis
ML can plan the experiment before acquisition. Targeted: predict which peptides or transitions are observable and well-behaved, and target the best ones. Untargeted: schedule acquisition and prioritise informative precursors.

> Example: predicting peptide detectability and best transitions lets a targeted method be designed in silico, saving instrument time.

## Slide 11 — Machine learning for NMR
NMR is a rich, structured signal well suited to learning. Models assist with automated peak picking, spectral prediction from structure, compound classification, and reaction or mixture monitoring, using the same workflow and the same evaluation caution as the MS examples.

> Example: a recent review surveys ML across NMR, from resonance assignment to quantitative analysis (Prog. NMR Spectrosc., 2025).

## Slide 12 — Current developments
**Foundation models** — large models pretrained on very large spectral or molecular corpora, then adapted to specific tasks with less labelled data.
**Integrated identification** — combining predicted retention, fragmentation and CCS into a single identification framework rather than separate filters.
(Refresh each year; the field moves quickly.)

## Slide 13 — Key takeaways
- ML assists across the whole LC-MS pipeline, reusing the Part 1 model families.
- Predicted retention, fragmentation and CCS are orthogonal constraints on identification.
- Rescoring turns these predictions into more confident identifications at fixed FDR.
- NMR and a priori experiment design are active, growing areas.
- Evaluate every applied model with the Part 3 cautions (leakage, grouping).
