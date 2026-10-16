# Datasets

The TD notebooks load their data without a manual download step. Attributed
compressed snapshots provide backups of the strawberry and Tox21 data.

- **Current Part 1 (TD1):** [strawberry authentication](strawberry/README.md).
  The dataset contains 983 infrared spectra of fruit purées labelled Strawberry
  or NON-Strawberry, each with 235 measured wavenumbers. The practical removes
  two identically measured records with conflicting labels and forms eight
  predefined window means. All code is
  supplied; student exercises focus on interpretation. The dataset has its own
  CC BY-NC 3.0 licence, separate from the course-code licence.
- **Current Part 3 (TD2):** the same strawberry data and eight fixed features,
  with a simple training/validation/test comparison of a small tree, a deep tree
  and a random forest. The 197-observation classroom test partition has the same
  membership as in Foundations and is not treated as new independent evidence.
- **Current Part 4 (TD3):** the same strawberry data and eight fixed features.
  An isolation forest learns from the 280 labelled Strawberry samples in the
  Foundations training group, then screens the same 197 test samples. Six
  interpretation questions focus on outliers and laboratory follow-up; all
  code is supplied. Flags do not establish adulteration or certify purity.
- **Parallel Tox21 series (TD1, TD2 and TD3):**
  [DeepChem-distributed Tox21 data](tox21/README.md), using one assay endpoint
  (SR-MMP) and eight readable molecular descriptors calculated with RDKit.
  The three practicals cover one small tree, overfitting and model comparison,
  then descriptor outliers. Each provides all code and six written questions.
  Missing assay results are excluded; the same cleaned 5,804 records and
  1,161-record test group are used throughout. Assay activity and descriptor
  flags are distinct from an overall judgement of toxicity or safety.
- **Legacy Part 1 (TD1):** Wine recognition dataset (sklearn.datasets.load_wine). Results
  of a chemical analysis of wines grown in the same region of Italy but derived
  from three different cultivars. Thirteen continuous features are quantities
  determined by chemical analysis (alcohol, malic acid, ash, alcalinity of ash,
  magnesium, total phenols, flavanoids, nonflavanoid phenols, proanthocyanins,
  colour intensity, hue, OD280/OD315 of diluted wines, proline); the target is
  the cultivar (3 classes, 178 samples). Chosen because it is genuinely
  analytical-chemistry data, ships with scikit-learn, and trains in seconds.
  Reference: Forina, M. et al., via the UCI Machine Learning Repository.

The legacy Evaluation practical uses a scikit-learn diagnostic dataset. The
legacy Applications practical generates illustrative retention data; the
LLM Tools practical generates illustrative peak-detection data within its notebook.
