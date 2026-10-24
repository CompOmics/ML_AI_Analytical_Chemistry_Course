# Datasets

The practicals load their data automatically. The compressed snapshots below
provide backups; each dataset guide documents its source, preparation and terms
of reuse separately from the course repository licence.

| Dataset | Documentation | Classroom backup |
|---|---|---|
| Strawberry fruit purées | [Measurements, targets and preparation](strawberry/README.md) | [CSV (.gz)](strawberry/fruit_purees.csv.gz) |
| DeepChem Tox21 | [Assay, descriptors and provenance](tox21/README.md) | [CSV (.gz)](tox21/tox21.csv.gz) |
| Peptide retention indices | [Source, target scale and preparation](peptide_rt/README.md) | [CSV (.gz)](peptide_rt/peptides_6000.csv.gz) |

## Strawberry: guided practicals

The source contains 983 infrared spectra of fruit purées, each measured at
235 wavenumbers. The target is Strawberry or NON-Strawberry. The practicals
exclude two identically measured records with conflicting targets, leaving
981 samples, and summarise each spectrum with eight predefined window means.

Foundations introduces the data and compares a small decision tree with a
neural network. Evaluation compares small and deep trees, a random forest and
a small convolutional neural network; the latter uses the full spectra.
Applications uses an isolation forest trained on 280 Strawberry samples to
flag unusual measurements for laboratory follow-up. Flags do not establish
adulteration or certify purity.

## Tox21: independent practicals

The three Tox21 practicals use the mitochondrial membrane potential assay
(SR-MMP) and eight molecular descriptors calculated with RDKit. The cleaned
subset contains 5,804 compounds with an Active or Inactive assay target.
Missing assay results are excluded, rather than treated as Inactive.

Foundations fits a small tree, then uses a pretrained autoencoder to propose
related molecules and predicts their assay classes. Evaluation compares models
and illustrates overfitting. Applications flags unusual descriptor patterns.
Assay predictions and outlier flags do not establish overall toxicity or
human safety. These practicals use the DeepChem-distributed data without
requiring the DeepChem package.

Both series provide the code and ask students to interpret the steps and
results. Within each series, all three practicals reuse the same test records
(197 Strawberry samples or 1,161 Tox21 compounds). This supports classroom
comparisons; it does not provide fresh independent validation.

## Peptides: LLM-assisted project

Day 5 uses 6,000 real DLOmix / ProteomeTools peptides with experimentally derived
retention indices. The target is calibrated iRT, without time units, rather
than retention time in minutes.

Students use an LLM to choose sequence features and models, compare with a
baseline, and use validation data to guide a change before the final test.
The student notebook supplies data-loading code and an open project brief.
The instructor notebook provides one possible worked implementation.
