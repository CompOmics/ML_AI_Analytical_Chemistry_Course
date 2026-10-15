# Part 3: Evaluation of trained models (slide deck)

Markdown equivalent of `Part3_Evaluation_slides.pptx` (14 slides). One section per slide.

---

## Slide 1 — Title
**Machine Learning and AI for Analytical Chemistry** — Part 3: Evaluation of trained models. M2 Sciences analytiques · 3 h lectures + 1 h tutorial.

## Slide 2 — Roadmap for Part 3
1. **Failure modes** — bias, overfitting and underfitting, information leakage, generalisation.
2. **Control and validation** — dataset roles, cross-validation, complexity and pruning, feature selection, explainable AI.
3. **Uncertainty** — uncertainty quantification and calibration for defensible decisions.

## Slide 3 — Section divider
**Failure modes** — how a model can look good and be wrong.

## Slide 4 — Bias, overfitting, underfitting
**Bias** — a model reproduces the skew of its training data: accurate where data are dense, worse elsewhere, while the average still flatters.
**Overfitting vs underfitting** — overfitting memorises noise and fails to generalise; underfitting is too simple. The signature of overfitting is a large train-to-test gap.

> Example: a contaminant classifier trained on summer samples performs worse in winter; the headline accuracy hides the gap.

## Slide 5 — Information leakage (the dangerous one)
Leakage is when information unavailable at prediction time slips into training, inflating measured performance. The model looks excellent until it meets genuinely new data. Two classic leaks: replicates or adducts of the same molecule on both sides of the split; and scaling or feature selection done on the whole dataset before splitting.

> Example: in retention prediction, split by molecule so no compound appears in both train and test; otherwise the model recognises, not predicts.

## Slide 6 — Generalisation is the goal
Generalisation is performance on data the model has never seen, drawn from the conditions where it will actually be used. Everything else in this part exists to estimate generalisation honestly.

> Example: the only score that matters is the one on samples measured after the model was built, on a new batch or instrument.

## Slide 7 — Section divider
**Control and validation** — estimating generalisation, and steering complexity.

## Slide 8 — The three dataset roles
(Figure: Training | Validation | Test bands.)
Train fits the model; validation tunes choices and compares models; the test set is touched once, at the very end. Reusing the test set to make choices turns it into a training set and inflates the result.

## Slide 9 — Cross-validation
(Figure: 5-fold cross-validation grid, the test fold rotating.)
When data are scarce, one split is wasteful and noisy. k-fold rotates the test part so every sample is tested once; average the folds. Grouped CV keeps all measurements of one entity in one fold, preventing leakage.

> Example: with 150 spectra, 5-fold CV uses all of them; group by compound if several spectra share a compound.

## Slide 10 — Model complexity and pruning
(Figure: U-shaped test error vs monotonic training error, with a best-generalisation point.)
Error against complexity is U-shaped: too simple underfits, too complex overfits. Pruning a tree, limiting depth, or adding regularisation moves toward the sweet spot; cross-validation locates it.

> Example: cross-validated accuracy peaks at a moderate tree depth, then declines; choose that depth.

## Slide 11 — Feature selection and analysis
Fewer, well-chosen features often generalise better than many: selection reduces overfitting and improves interpretability. Crucial caveat: selection must happen inside the cross-validation, on training data only, or it leaks.

> Example: picking the ten most discriminating m/z bins helps, but choosing them on the whole dataset before splitting inflates the score.

## Slide 12 — Explainable AI
An accurate but opaque model is hard to trust in a regulated setting. Explainable AI (feature importances, SHAP values, partial dependence) describes what drives a prediction, letting a chemist check the model relies on sensible signals.

> Example: SHAP showing a toxicity model keys on a known reactive substructure builds trust; keying on a sample-id artefact reveals leakage.

## Slide 13 — Uncertainty and calibration
A prediction without an uncertainty is of limited use for a decision. Uncertainty quantification attaches a credible range or probability. Calibration checks that stated probabilities match observed frequencies: among 80 %-confidence predictions, about 80 % should be correct.

> Example: a calibrated 95 % non-compliance flag supports a defensible decision; an overconfident uncalibrated 99 % invites unjustified action.

## Slide 14 — Key takeaways
- Good scores on seen data prove nothing; only generalisation counts.
- Leakage is the most common inflator; split by molecule, scale inside the split.
- Use train/validation/test roles; touch the test set once.
- Cross-validation (grouped where needed) gives stable estimates and finds complexity.
- Report uncertainty, and check it is calibrated.
