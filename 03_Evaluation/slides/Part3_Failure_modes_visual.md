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

## Slide 7: Familiar molecules in the test set

- Training molecules: aniline, phenol and chlorobenzene, with known targets.
- Predicting phenol again reuses a training compound.
- 4-Methylphenol is a new compound but closely resembles phenol. Its extra methyl group is orange.
- Similarity alone is not leakage. A test of new chemical families should keep close analogues together.

### Speaker notes

Hypothetical molecular-property prediction example, with no measured targets or performance claims. Structures identify compounds. A model normally receives a numerical representation or measured features rather than the compound names. Phenol in the second row is exactly the training compound. Reusing its training record and target cannot support an independent test. Distinct measurements of the same compound may also share compound-specific information, as the next slide illustrates. 4-Methylphenol in the third row differs by one para methyl substituent. It is not identical and is not automatically a leakage case. If the intended use is predicting close analogues within familiar chemical families, this can be a relevant test, provided its observations and targets stayed outside all development. If the intended use is generalisation to new chemical families, splitting close analogues across partitions gives limited evidence for that claim and can make the reported result optimistic. Grouping by chemical series, scaffold or similarity can help align the split with the scientific question. A scaffold split is one grouping rule, not a guarantee that every test compound is dissimilar or that all distribution shifts are covered. No equal toxicity, similar activity or guaranteed prediction is implied by visual similarity.

Molecular graph and coordinates: RDKit 2025.09.6. Native editable PowerPoint bonds and atom labels. SMILES: aniline Nc1ccccc1; phenol Oc1ccccc1; chlorobenzene Clc1ccccc1; 4-methylphenol Oc1ccc(C)cc1. Coordinates for phenol and 4-methylphenol share an aligned phenol core. The diagrams are schematic chemical structures, not generated artwork or results from the practicals.

Sources
https://scikit-learn.org/stable/modules/cross_validation.html
https://doi.org/10.1016/j.patter.2023.100804
https://deepchem.readthedocs.io/en/2.8.0/api_reference/splitters.html#scaffoldsplitter

---

## Slide 8: Replicate spectra across the split

- Visual: one phenol specimen branches into three similar spectral traces.
- Scans 1 and 2 enter training. Scan 3 enters the claimed test.
- Grouping by physical specimen keeps all three scans together.

### Speaker notes

Hypothetical sampling diagram, with no claimed accuracy. The three traces are invented schematic sequences. They are not measured spectra of phenol and show no genuine peak assignments or spectral axis values. The structure identifies the compound only. All scans here measure the same physical specimen, so composition, preparation and instrument effects can be shared. Different rows alone do not establish independence. Group repeats of a specimen together before splitting and throughout cross-validation. If the scientific claim concerns new compounds, group all measurements of each compound too. If the claim concerns new chemical families, consider larger chemical groups as discussed on the preceding slide. Many scans do not replace enough independent groups. Molecular structure: phenol, SMILES Oc1ccccc1, with RDKit coordinates and editable PowerPoint bonds and labels.

Sources
https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data
https://doi.org/10.1016/j.patter.2023.100804
https://deepchem.readthedocs.io/en/2.8.0/api_reference/splitters.html#scaffoldsplitter

---

## Slide 9: Preparation can leak information

- Visual: learning bands or scaling from A B C D before splitting lets test D influence preparation.
- In the independent workflow, split first. Only training A B C teaches the preparation rules and model.
- Test D enters prediction only after the rules and model are fixed.

### Speaker notes

This is an editable workflow diagram. A–D identify example records, not predictor columns. The top flow learns preparation rules from the complete dataset and then claims an independent check on D. For supervised band selection, using D’s target leaks outcome information. For scaling, D can influence the feature distribution even without its target. The lower flow keeps D outside all learning steps and applies the fixed rules and fitted model to it afterwards. Estimate missing-value replacements within training too. Within cross-validation, learn each transformation only from that fold’s training partition. Validation may compare candidate workflows, while a final test checks the fixed choice. For visual simplicity these flows omit the validation branch. A fixed operation on a single spectrum using only its own measurements does not automatically leak information. Pipelines help with learned transformations but do not fix overlap between physical specimens.

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
- 5. A model trains on phenol. Its reported independent test reuses the same phenol record.

### Speaker notes

Suggested discussion answers. 1: underfitting is plausible because the straight-line model cannot describe the consistent curvature. Compare a suitable curve or a narrower validated linear range. 2: overfitting. Compare training and validation errors and choose a simpler model through validation. 3: investigate bias or coverage and measurement differences across matrices. The gap alone does not prove a particular cause, and a deployment shift may overlap. Inspect per-matrix sample counts, interferences, reference measurements and errors. 4: out-of-distribution extrapolation. Obtain independent measurements at the new range or bring samples into a validated range. 5: the phenol record already entered training. Its prediction measures training fit and cannot serve as an independent test. Use observations excluded from model development and group replicate measurements together. For a claim about new compounds, also keep each compound in one partition. For a claim about new chemical families, consider grouping related structures. A close analogue is not automatically leakage, but it answers a different question from transfer to unfamiliar chemistry. These cases assess interpretation rather than coding. Ask for a reason with each answer and accept well-supported overlapping failure modes.

Sources
https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html
https://doi.org/10.6028/NIST.SP.1270
https://doi.org/10.1038/s43246-024-00731-w
https://scikit-learn.org/stable/modules/cross_validation.html
https://doi.org/10.1016/j.patter.2023.100804
