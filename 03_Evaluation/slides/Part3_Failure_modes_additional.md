# Evaluation: additional slides on failure modes

Eleven additional slides in the style of the existing Evaluation lecture. These use new analytical-chemistry examples and require no programming.

Suggested placement: replace the current overview and information-leakage slides 4–5 with this sequence, immediately after the Failure modes divider. Continue with the existing generalisation slide afterwards. The original deck remains separate.

All numerical calibration and water-matrix examples here are illustrative. The calibration data are simulated, and the water-matrix results are hypothetical. None are results from the practicals.

---

## Slide 1: Five ways a model can fail

| Failure mode | What goes wrong? | Useful check |
| --- | --- | --- |
| Underfitting | The model misses a useful pattern. | Training and validation performance |
| Overfitting | The model fits accidental details. | The training–validation gap |
| Bias in the data | Some conditions have poor coverage. | Sampling and performance by group |
| Out of distribution | New conditions differ from those studied. | The intended conditions of use |
| Information leakage | Training and test information overlap. | Split units and data preparation |

### Speaker notes

Use five concrete questions: can the model describe the training pattern, does the pattern transfer, whose samples does the dataset represent, do new samples match the conditions studied, and was the final evaluation independent? Here bias means systematic problems in sampling, measurement or targets. Statistical bias in the bias–variance discussion is a different use of the word and connects to underfitting. Poor coverage does not inevitably cause poor performance, but it limits the evidence for performance in that group. A gap alone cannot diagnose every cause. Validation-based model selection is an intended part of development. Leakage compromises data intended to provide an independent check, or introduces information unavailable under the intended prediction conditions.

Sources
https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html
https://doi.org/10.6028/NIST.SP.1270
https://doi.org/10.1038/s43246-024-00731-w
https://doi.org/10.1016/j.patter.2023.100804

---

## Slide 2: Underfitting

- A straight line misses the detector response curve.
- Training and validation both improve with a suitable curved model.
- Figure: calibration standards, straight-line model and degree-2 model.

### Speaker notes

All calibration data in this insert are simulated, not experimental observations. The response follows 0.1 + 1.8(1 − exp(−2c)) plus independent Gaussian noise with SD 0.035 arbitrary units. Twelve evenly spaced training standards span 0–1 mg/L. Eighty independent validation measurements span 0.015–0.985 mg/L. Random seed 42 fixes the illustration. Compare model degrees 1 and 2. Root mean squared error is a typical error magnitude, in response units, so lower is better. Degree 1: Training error 0.118
Validation error 0.112. Degree 2: Training error 0.039
Validation error 0.037. Do not interpret low training and validation performance as proof of underfitting in every study: weak features, noisy targets and measurement problems can also cause it. A real laboratory may dilute samples or use a validated narrower linear range rather than fit a curve.

Sources
https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html
https://scikit-learn.org/stable/modules/learning_curve.html

---

## Slide 3: Overfitting

- The flexible curve fits accidental measurement variation.
- Near-zero training error does not guarantee good validation performance.
- Figure: the same standards with degree-11 and degree-2 models.

### Speaker notes

The degree-11 polynomial interpolates the twelve training observations. Its training error is approximately zero and its validation error is 0.078 response units. The degree-2 model has validation error 0.037. The very flexible model therefore predicts the independent validation observations less well despite fitting training almost perfectly. The curves use the same standards and axis meaning as the preceding slide. Underfitting and overfitting describe failure to transfer useful structure, not simply a universal threshold for model size. The known noise-free response exists only because this is a simulation.

Sources
https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html
https://scikit-learn.org/stable/modules/learning_curve.html

---

## Slide 4: Calibration complexity and validation

- Increasing flexibility reduces training error.
- Validation identifies a useful complexity before a separate final test.
- Figure: training and validation RMSE for degrees 1–11.

### Speaker notes

This curve fits each polynomial to the same twelve training standards and evaluates the same eighty independent validation measurements. It uses no practical notebook data. Degree 3 gives the lowest validation error in this particular simulation. Treat the selected setting as fixed before a new independent test. Validation performance after searching several degrees is not an unbiased final performance estimate. The slide does not show a final test score. A broad U-shape is an illustration rather than a universal law. Do not equate more complex models automatically with worse generalisation.

Sources
https://scikit-learn.org/stable/modules/learning_curve.html

---

## Slide 5: Bias from uneven data coverage

- Training mostly covers drinking water.
- Hypothetical test results: 900 drinking-water samples at 95%, 100 river-water samples at 50%.
- Overall: (855 + 50) / 1,000 = 90.5%.

### Speaker notes

This is a hypothetical analytical-chemistry scenario, not a measured result from strawberry or Tox21. Assume the training collection covers drinking water much more thoroughly than river water. Matrix-dependent interferences are a plausible concern, not an experimentally established cause in this illustration. The test example contains 855 correct drinking-water predictions and 50 correct river-water predictions, giving 905/1000 = 90.5% overall. Unequal performance alone does not identify its cause. Inspect sampling, measurement methods and target quality for each matrix, and obtain representative labelled measurements. A more complex model or class weights cannot supply missing matrix coverage. Here bias means systematic data or measurement problems, not the mathematical high-bias description of an overly restrictive model. Matrix groups are not target classes.

Sources
https://doi.org/10.6028/NIST.SP.1270

---

## Slide 6: Out-of-distribution predictions

- Known standards span 0–1 mg/L.
- A model prediction at 2 mg/L lies beyond the studied concentration range.
- Other shifts include a new instrument, matrix, or chemical family.

### Speaker notes

The plotted new sample is a hypothetical model prediction, not a measured response. The original degree-2 calibration model now extends beyond the 0–1 mg/L range used for training and validation. In this illustration concentration is the known input to a forward response model, as with calibration standards. Quantifying an unknown sample from its measured response would require the appropriate inverse calibration procedure. Out-of-distribution means a change relative to the joint conditions and examples represented during development. A fresh sample is not automatically OOD merely because it was not in training. OOD samples can also involve unfamiliar combinations while individual feature values remain inside their old ranges. A random split within the original conditions does not establish performance after a shift. Check the new conditions experimentally, dilute into a validated range when appropriate, or extend and revalidate the method. An outlier flag can request review but cannot guarantee detection of all OOD cases.

Sources
https://doi.org/10.1038/s43246-024-00731-w
https://doi.org/10.1038/s41467-020-17112-9

---

## Slide 7: A test sample already used for training

| Stage | Example |
| --- | --- |
| Training | A: authentic, B: adulterated, C: authentic |
| Claimed test | Predict specimen B again, hiding its target. |

### Speaker notes

This is a hypothetical example. Train the classifier on the features and recorded targets of milk specimens A, B and C. Then ask it to predict the same feature record for B. Hiding B’s target during this prediction does not undo its earlier use in training. A correct prediction could reflect memorisation of an example and answer already seen. It does not demonstrate performance on new specimens. The model is not guaranteed to predict B correctly, but that uncertainty does not make B an independent test. Predicting training records is legitimate when checking training fit. The methodological error is reporting those predictions as an independent test or allowing training/test overlap to support a claim about new specimens. An exact copy of B under another row number remains the same example. Keep genuinely independent specimens outside model development, including learned preprocessing and model choice. Validation may legitimately guide model choice, while the final test checks the fixed workflow. The next slide makes the overlap less obvious by using another scan of the same specimen.

Sources
https://scikit-learn.org/stable/modules/cross_validation.html
https://doi.org/10.1016/j.patter.2023.100804

---

## Slide 8: Replicate spectra across the split

| Split | Training data | Evaluation data |
| --- | --- | --- |
| By spectrum | Specimen A: scans 1 and 2 Specimen B: scans 1 and 2 | Specimen A: scan 3 Specimen B: scan 3 |
| By physical specimen | All scans from specimens A and B | All scans from specimens C and D |

### Speaker notes

This is a hypothetical sampling example, with no claimed accuracy. The preceding slide reused the exact training example. Here the evaluation record is a different scan, but still comes from a specimen used for training. Suppose each powdered-milk specimen produces three repeat NIR spectra. The intended task is classification of genuinely new physical specimens. Splitting spectra can put near-replicates of the same specimen in both groups. Their shared composition, preparation and instrument effects can make evaluation easier than the intended task. Group all repeat measurements of a specimen together when splitting, and keep those groups together within cross-validation. If the intended claim concerns new production lots, farms or acquisition days, the grouping unit may need to be larger. Independent evaluation requires enough independent groups, not just many repeated scans. The small A–D example illustrates membership only and is not a sufficient real validation study.

Sources
https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data
https://doi.org/10.1016/j.patter.2023.100804

---

## Slide 9: Preparation can leak information

| Step | Leaking approach | Independent check |
| --- | --- | --- |
| Choose bands | Select bands using targets from the complete dataset. | Select bands using training targets. |
| Scale features | Calculate means and spreads using every sample. | Learn from training samples. Apply unchanged to others. |
| Fill missing signals | Use every sample to estimate replacement values. | Estimate replacements from training samples. |

### Speaker notes

These are illustrative preprocessing choices for a spectral or chromatographic feature table. Select bands, learn scaling and estimate missing-value replacements from training data. Apply those learned rules unchanged to validation and final-test samples. When using cross-validation, repeat the learning of these steps within each training fold. Validation can compare candidate workflows. Test results must not choose among them. A fixed operation on one spectrum, such as a transformation defined in advance using that spectrum alone, does not automatically leak information. The issue is what information the transformation learns or uses. Scaling on all samples can leak feature-distribution information even without using targets. Pipelines help keep learned transformations inside the correct fitting partition.

Sources
https://scikit-learn.org/stable/common_pitfalls.html#data-leakage

---

## Slide 10: The failure determines the next check

| Failure mode | Useful evidence | Possible next step |
| --- | --- | --- |
| Underfitting | The model misses training structure. | Try a suitable model or informative inputs. |
| Overfitting | Training improves much more than validation. | Choose model flexibility with validation. |
| Bias in the data | Errors differ across sample groups. | Check sampling and fill coverage gaps. |
| Out of distribution | New conditions differ from those studied. | Validate under the new conditions. |
| Information leakage | Training and test information overlap. | Rebuild and evaluate with independent data. |

### Speaker notes

These are useful warning signs rather than definitive diagnostic tests. Check a meaningful baseline and the quality of features and targets. Leakage may produce very good reported scores without a conspicuous training–validation gap. Audit specimen identities, feature selection and preprocessing even when the scores agree. If test information influenced development, redesign the workflow and obtain an independent final check. Biased coverage and distribution shift often overlap: a matrix may be underrepresented during development and more common during deployment. They describe different aspects of the problem, so several answers can be relevant. Keep model choice within training/validation roles and reserve independent testing for the fixed choice.

Sources
https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html
https://scikit-learn.org/stable/modules/learning_curve.html
https://doi.org/10.6028/NIST.SP.1270
https://doi.org/10.1038/s43246-024-00731-w
https://doi.org/10.1016/j.patter.2023.100804

---

## Slide 11: Five short cases

- 1. A straight calibration line misses a consistent bend, even for its training standards.
- 2. A flexible calibration curve fits every standard but predicts new standards less well.
- 3. Overall accuracy looks good, but samples from one water matrix perform much worse.
- 4. A calibration model predicts samples at concentrations beyond the range studied.
- 5. A model trains on milk specimens A, B and C. Its reported test uses specimen B.

### Speaker notes

Suggested discussion answers. 1: underfitting is plausible because the straight-line model cannot describe the consistent curvature. Compare a suitable curve or a narrower validated linear range. 2: overfitting. Compare training and validation errors and choose a simpler model through validation. 3: investigate bias or coverage and measurement differences across matrices. The gap alone does not prove a particular cause, and a deployment shift may overlap. Inspect per-matrix sample counts, interferences, reference measurements and errors. 4: out-of-distribution extrapolation. Obtain independent measurements at the new range or bring samples into a validated range. 5: specimen B already entered training. Its prediction measures training fit and cannot serve as an independent test of new specimens. Use specimens excluded from model development and keep all replicate scans of a specimen together. Predicting B is not itself wrong; the claim of an independent test is wrong. These cases assess interpretation rather than coding. Ask for a reason with each answer and accept well-supported overlapping failure modes.

Sources
https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html
https://doi.org/10.6028/NIST.SP.1270
https://doi.org/10.1038/s43246-024-00731-w
https://scikit-learn.org/stable/modules/cross_validation.html
https://doi.org/10.1016/j.patter.2023.100804
