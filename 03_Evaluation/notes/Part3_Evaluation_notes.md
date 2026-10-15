# Part 3: Evaluation of trained models

**Lecture notes (3 h CM + 1 h TD)**
Machine Learning and AI for Analytical Chemistry, M2 Sciences analytiques

These notes accompany the Part 3 slides and the TD2 notebook. Evaluation is the
most transferable skill in the course: it is what separates a model you can trust
from one that merely looks good. Each key point carries an analytical-chemistry
example, distinct from the wine dataset used in the notebooks.

---

## 1. Failure modes (1 h)

### 1.1 Bias

A model reproduces the biases of its training data. If the data over-represent
one condition, the model will be most accurate there and worse elsewhere, while
still reporting a flattering average.

> **Example.** A contaminant classifier trained mostly on summer river samples
> may perform poorly on winter samples, because temperature and matrix shift the
> baseline. The headline accuracy hides the seasonal gap.

### 1.2 Overfitting and underfitting

**Overfitting** is a model so flexible it memorises the training data, including
noise, and fails to generalise. **Underfitting** is a model too simple to capture
the real relationship. The signature of overfitting is a large gap between
training performance and test performance.

> **Example.** A deep decision tree predicting compound class from a handful of
> descriptors can reach 100 % on the training set by isolating each molecule,
> yet score poorly on new molecules. The training score is meaningless on its
> own.

### 1.3 Information leakage

**Leakage** is when information that would not be available at prediction time
slips into training, inflating measured performance. It is the most dangerous and
most common error in applied machine learning, because the model looks excellent
until it meets genuinely new data.

> **Example (chemistry-specific).** In retention-time prediction, placing
> different adducts or replicate measurements of the same molecule in both the
> training and test sets lets the model recognise the molecule rather than
> predict its retention. The fix is to split by molecule, so no compound appears
> on both sides. Another classic leak: scaling or feature selection performed on
> the whole dataset before the split, which lets test statistics influence
> training.

### 1.4 Generalisation

Generalisation is the goal: performance on data the model has never seen, drawn
from the conditions where it will actually be used. Everything in this part
exists to estimate generalisation honestly.

---

## 2. Control and validation (1.5 h)

### 2.1 The three dataset roles

Data are split into three roles. The **training set** fits the model. The
**validation set** is used to tune choices such as hyperparameters and to compare
models. The **test set** is touched once, at the very end, to report final
performance. Mixing these roles, especially reusing the test set to make choices,
quietly turns it into a training set and inflates the result.

> **Example.** If you try twenty model settings and report the best one's test
> score, that score is optimistic: you have implicitly fitted to the test set.
> Tune on validation, report once on test.

### 2.2 Cross-validation

When data are scarce, a single split wastes data and gives a noisy estimate.
**k-fold cross-validation** splits the data into k parts, trains on k-1 and tests
on the remaining part, and rotates so every sample is tested once. The average is
a more stable performance estimate. For grouped data, use **grouped
cross-validation** so that all measurements of one entity stay within a single
fold (this prevents the leakage in 1.3).

> **Example.** With only 150 labelled spectra, five-fold cross-validation uses
> all of them for both training and testing across folds, giving a more reliable
> accuracy than one 70/30 split would. If several spectra come from the same
> compound, group by compound so the folds stay honest.

### 2.3 Model complexity and pruning

Performance against complexity follows a U-shape: too simple underfits, too
complex overfits, and the best generalisation sits in between. **Pruning** a tree,
limiting depth, or adding **regularisation** to a model are ways to move toward
that sweet spot. Cross-validation is how you find it.

> **Example.** Increasing the depth of a decision tree improves training accuracy
> monotonically but cross-validated accuracy peaks at a moderate depth and then
> declines; that peak is the depth to choose.

### 2.4 Feature selection and analysis

Fewer, well-chosen features often generalise better than many. Feature selection
removes uninformative or redundant inputs, which reduces overfitting and improves
interpretability. Crucially, selection must happen inside the cross-validation,
on training data only, or it leaks.

> **Example.** Choosing the ten most discriminating m/z bins for a classifier can
> improve generalisation, but if the bins are chosen using the whole dataset
> before splitting, the test score is inflated.

### 2.5 Explainable AI

A model that is accurate but opaque is hard to trust in a regulated analytical
setting. **Explainable AI** methods (feature importances, SHAP values, partial
dependence) describe what drives a prediction, allowing a chemist to check
whether the model relies on sensible signals.

> **Example.** A SHAP analysis showing that a toxicity classifier keys on a known
> reactive substructure increases confidence; one showing it keys on a sample-id
> artefact reveals leakage.

---

## 3. Uncertainty quantification and calibration (0.5 h)

A prediction without an uncertainty is of limited use for a decision. **Uncertainty
quantification** attaches a credible range or probability to each prediction.
**Calibration** checks that stated probabilities match observed frequencies: among
predictions made with 80 % confidence, about 80 % should be correct.

> **Example.** A classifier that flags a water sample as non-compliant with a
> calibrated 95 % probability supports a defensible decision; an uncalibrated
> model that is overconfident at 99 % on cases it often gets wrong is dangerous,
> because the number invites action it cannot justify.

---

## Key terms

- **Bias**: systematic error reflecting skewed training data.
- **Overfitting / underfitting**: too flexible / too simple.
- **Information leakage**: test information seeping into training.
- **Generalisation**: performance on genuinely unseen data.
- **Training / validation / test**: fit / tune / report-once roles.
- **k-fold and grouped cross-validation**: rotating splits, grouped to avoid leakage.
- **Pruning / regularisation**: controlling complexity.
- **Feature selection**: keeping informative inputs only, inside the CV.
- **Explainable AI (SHAP, importances)**: describing what drives predictions.
- **Uncertainty quantification, calibration**: credible ranges, honest probabilities.

## Further reading

- Hastie, Tibshirani, Friedman, The Elements of Statistical Learning, chapters on
  model assessment and selection.
- Kapoor and Narayanan, Leakage and the reproducibility crisis in ML-based
  science, Patterns, 2023.
- The scikit-learn user guide on cross-validation and model evaluation.
