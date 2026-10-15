# Datasets

The TD notebooks use datasets that load without any manual download, so no large
files are stored here.

- Part 1 (TD1): Wine recognition dataset (sklearn.datasets.load_wine). Results
  of a chemical analysis of wines grown in the same region of Italy but derived
  from three different cultivars. Thirteen continuous features are quantities
  determined by chemical analysis (alcohol, malic acid, ash, alcalinity of ash,
  magnesium, total phenols, flavanoids, nonflavanoid phenols, proanthocyanins,
  colour intensity, hue, OD280/OD315 of diluted wines, proline); the target is
  the cultivar (3 classes, 178 samples). Chosen because it is genuinely
  analytical-chemistry data, ships with scikit-learn, and trains in seconds.
  Reference: Forina, M. et al., via the UCI Machine Learning Repository.

Later parts will add retention-time, solubility, and spectral datasets,
downloaded at runtime from stable public sources.
