# Applications: predictions, structural proposals and unusual measurements

Applications connects the earlier modelling ideas to analytical questions. A model can predict how an analyte behaves, help rank possible identities, propose a structure, or prioritise an unusual record for review. These are different outputs with different evidence requirements. Their value depends on the measurement, the reference data and the decision made afterwards.

## Presentation and practicals

The [Applications presentation](../slides/4_Applications_compomics.pptx) first develops CompOmics examples in mass-spectrometry-based proteomics, then introduces NMR-Solver, Raman microorganism identification and PXRDGen. The practicals focus on outlier detection: [Strawberry student](../notebooks/TD3_strawberry_student.ipynb), [Strawberry answers](../notebooks/TD3_strawberry_solution.ipynb), [Tox21 student](../notebooks/TD3_tox21_student.ipynb) and [Tox21 answers](../notebooks/TD3_tox21_solution.ipynb).

| Lecture section | Analytical question |
|---|---|
| Slides 2–16 | Can predicted retention, fragmentation and mobility strengthen peptide identification? |
| Slides 17–22 | What can structural representations and transfer learning add? |
| Slides 23–33 | How can metadata, reanalysis and visualisation support biological interpretation? |
| Slides 35–37 | Which molecular structure explains NMR observations? |
| Slides 38–40 | Can Raman fingerprints distinguish microorganisms? |
| Slides 41–43 | Which crystal structure explains a powder-diffraction pattern? |

The guided Strawberry practical and independent Tox21 practical return to the same eight-feature inputs used earlier. Their detectors do not learn the previous classification targets. Instead, they ask whether a measurement or descriptor pattern is unusual relative to a chosen reference group.

## 1. From measured signals to candidate identities

In liquid chromatography–mass spectrometry (LC-MS), a peptide produces several kinds of evidence. Its chromatographic signal indicates retention behaviour, its precursor signal provides mass-related information, fragmentation produces a tandem mass spectrum, and ion-mobility separation can provide another property. Identification compares observations with plausible candidates; quantification estimates amounts from appropriate signals after the relevant processing and assignments.

Some candidate properties follow directly from a known composition, such as theoretical mass. Other properties depend on more complicated behaviour and can be predicted from examples. The presentation uses retention time, fragment-ion intensities and collision cross section to show how machine learning enriches the expected signal for each candidate. Agreement between predicted and observed properties can support a ranking, but none of those agreements alone proves the identity.

| Predicted quantity | What is compared | What remains to establish |
|---|---|---|
| Retention behaviour | Predicted and observed chromatographic position | Calibration and applicability to this LC method |
| Fragment intensities | Expected and measured tandem-MS patterns | Match specificity and identification-error control |
| Collision cross section (CCS) | Expected and observed mobility-related behaviour | Charge, calibration and coverage of relevant structures |

## 2. Retention prediction and DeepLC

[DeepLC](https://doi.org/10.1038/s41592-021-01301-5) predicts peptide retention behaviour using a representation that includes atomic composition and can encode modifications. This allows a model to use information about a modification rather than treating every unfamiliar modification name as an entirely unknown symbol. The lecture contrasts that approach with applying a single fixed retention shift to all instances of a modification.

Calibration maps predictions to a particular measurement setup. Transfer learning instead updates model parameters using task-specific examples. These procedures have different roles: adjusting a prediction scale does not necessarily learn a new structure–retention relationship, while fine-tuning can change that relationship. Both need reference measurements that remain separate from the final evaluation used to support a claim.

The peptide project in Part 5 is a small model-building exercise on calibrated iRT targets. It does not run DeepLC or require reproducing its published performance. A prediction error reported in iRT units cannot be read directly as minutes. Students choose their own representation and models, then explain what their particular comparison supports.

## 3. Fragmentation, ion mobility and rescoring

MS²PIP predicts fragment-ion intensities for peptides under specified modelling conditions. The mass positions of theoretical fragments and their expected intensities contribute different information: a candidate may have plausible mass positions yet disagree with the measured intensity pattern. A prediction is useful when it improves discrimination under an appropriate evaluation, rather than merely producing a realistic-looking spectrum.

Ion mobility separates ions according to their gas-phase behaviour. CCS provides a property related to an ion's interaction with the surrounding gas; charge and molecular conformation matter. The lecture shows atomic-composition-based prediction for modified peptides and the combination of retention, fragmentation and mobility evidence. A strong aggregate correlation does not imply equally small errors for every charge state or modification.

[MS²Rescore](https://github.com/compomics/ms2rescore) and the TIMS²Rescore example combine evidence to reassess candidate peptide matches. The score is part of an identification procedure, not a direct experimental truth. The accepted identification set still needs error control. False discovery rate concerns the expected fraction of incorrect identifications among accepted results, which differs from classification accuracy and from confidence in one particular candidate.

## 4. Structural representations and interpretation

A graph describes atoms as nodes and bonds as edges, retaining connectivity that a short descriptor table can lose. A graph neural network learns representations by exchanging and combining information along those connections. The lecture uses peptide graphs to show how molecular structure can influence prediction and how a pretrained model might be adapted to another measurement context.

Saliency or contribution maps highlight parts of an input associated with a model's output. These maps can help ask whether a learned pattern is chemically plausible, but an attribution is not a causal experiment. Correlated inputs, the training data and the attribution method affect what is highlighted. Mechanistic conclusions need evidence beyond a coloured structural diagram.

Several examples in this lecture are presented as developing research rather than completed universal benchmarks. Their role is to illustrate questions about representation, transfer and interpretation. A result from one study should not be converted into a general claim that graph models always outperform simpler alternatives.

## 5. Metadata and reanalysis are part of the workflow

Consistent metadata make analytical results interpretable across datasets. Information about specimens, acquisition and processing provides the context needed to evaluate a prediction or revisit an identification. The lesSDRF example addresses this supporting problem: organising metadata is useful even when the tool itself is not the predictive model under discussion.

The lecture also shows reanalysis and interpretation resources, including Scop3PTM, PTMVision and Tabloid Proteome. Predictors can support renewed examination of public measurements, but candidate modifications and biological associations remain dependent on identification quality and metadata. A tissue predictor or association network can suggest follow-up hypotheses; its output does not by itself establish cell composition, a disease mechanism or causation.

## 6. NMR: inferring molecular structure

Nuclear magnetic resonance (NMR) measures responses of suitable nuclei in a magnetic field after radiofrequency excitation. Chemical shifts reflect local chemical surroundings. Under appropriate measurement conditions, integrated ¹H signals provide relative proton counts. The real ethanol spectrum in the lecture connects these ideas to a measured signal rather than a schematic trace. Structure elucidation asks which arrangement of atoms explains the observations, while accounting for overlap, solvent signals and other experimental information.

[NMR-Solver, Jin et al. (2026)](https://doi.org/10.1038/s41467-026-71315-0), combines candidate retrieval, fragment-based molecular search and forward chemical-shift prediction. Its NMRNet component is an SE(3)-equivariant transformer using atomic types and three-dimensional coordinates. The network predicts shifts for proposed structures; the surrounding search compares those predictions with the supplied NMR observations. This is a hybrid inference procedure, rather than a language model simply translating a spectrum into a structure string.

The lecture pairs supported laboratory assignments with a documented failure for a strained molecule. Incorrect forward-predicted shifts made a wrong structure appear more consistent with the data. A plausible spectral match therefore remains a structural hypothesis requiring chemical assessment and, where relevant, independent evidence such as two-dimensional NMR or high-resolution mass spectrometry. The quality of the inverse search depends on the quality of its forward predictor.

## 7. Raman: recognising vibrational fingerprints

Raman spectroscopy examines light scattered with a change in energy associated with molecular vibrations. Peak positions and their combined intensity pattern can provide a chemical fingerprint. Different compounds or cells can share many features, so the task often requires recognising a pattern rather than finding one exclusive peak. The introductory curves in the presentation are explicitly schematic; they should not be mistaken for experimental results from the study.

The [Li et al. (2026) study](https://doi.org/10.1038/s41467-025-66996-y) combines cell enrichment, single-cell Raman measurements and a one-dimensional residual CNN. It combines predictions from multiple measured cells for identification. The reported 95.1% isolate-level accuracy concerns 342 clinical isolates, with spectra from an isolate kept together during validation. This grouping is important because many spectra from the same isolate are not independent examples of new isolates.

The separate selected clinical-positive comparison gives agreement for 99 of 120 samples, or 82.5%, against culture and MALDI-TOF identification. These denominators and evaluation settings differ. The lecture also shows poor performance for some species, so the overall score should not be read as uniform reliability or established readiness for every clinical population. The example links spectral modelling to sampling, aggregation and group-specific error analysis.

## 8. Powder X-ray diffraction: inferring crystal structure

Powder X-ray diffraction (PXRD) records intensity at scattering angles associated with a crystal's repeating atomic arrangement. Peak positions provide information about spacings, while intensities depend on atoms and their positions. Peaks can overlap, making the inverse problem harder than reading a list of isolated features. The relevant input includes the diffraction pattern and available chemical or crystallographic information.

[PXRDGen, Li et al. (2025)](https://doi.org/10.1038/s41467-025-62708-8), uses an encoder to extract pattern information, a conditional generative model to propose atomic arrangements, and Rietveld refinement to improve agreement with diffraction data. The framework considers diffusion- and flow-based generation. The highlighted MP-20 benchmark uses simulated patterns, inorganic structures with at most 20 atoms per primitive cell, known unit-cell parameters and 20 candidates per case.

In the reported refinement benchmark, 7,946 of 8,238 valid entries were matched, and 7,304 structures were subsequently refined. These are different stages, not three interchangeable success rates. The denominator excludes invalid entries, and the benchmark conditions limit the conclusion. The presentation identifies complex oxides and organic crystals as areas needing further development. A close diffraction fit still requires assessment of chemical plausibility and possible alternatives.

## 9. Outlier detection: a different kind of question

An outlier is unusual relative to a reference and a representation. It need not be incorrectly measured, chemically impossible or unsafe. A legitimate rare sample may be flagged, and a problematic sample can resemble the reference closely enough to escape a flag. The scientific meaning of the reference group must therefore be stated before interpreting the output.

An isolation forest repeatedly divides examples using randomly chosen feature cut-offs. Isolated examples often become separated after relatively few cuts, whereas examples among many neighbours tend to require longer routes. Consider the illustrative values 1.0, 1.1, 1.2, 1.3 and 8.0: a cut at 4 separates 8.0 immediately. Repeating random partitions across many trees reduces reliance on one lucky cut and can detect unusual combinations of several features.

A random forest classifier learns splits using target classes and combines class estimates. An isolation forest learns partitions from features and combines effective isolation lengths. Similar names do not mean that they answer the same question. Its `-1` output denotes a flag and `1` denotes no flag; neither output is an assay class.

The supplied `contamination=0.05` setting positions the flagging boundary so that approximately 5% of reference training records are flagged. It does not measure adulteration prevalence, toxicity prevalence or the proportion that must be flagged in a new test group. Changing this setting changes the screening rule, so it requires justification before using the detector operationally.

## 10. The two practical reference groups

| Practical | Reference used to fit the detector | Records screened | Meaning of a flag |
|---|---|---|---|
| Strawberry | 280 Strawberry records from the original training group | The same 197 test spectra used earlier | Unusual relative to those Strawberry window means |
| Tox21 | All 4,643 original training compounds, including both assay classes | The same 1,161 test compounds used earlier | Unusual relative to the familiar descriptor patterns |

Strawberry includes only its recorded Strawberry training samples because its question concerns resemblance to that reference. Tox21 includes both assay classes because unusual descriptors are not defined by Active or Inactive status. Both return to the original Foundations training group, including records previously used for validation. The detector and its setting are fixed rather than selected using those validation outcomes.

The test targets are added to the review table after flagging. For Strawberry, a recorded authentic sample can be flagged and a NON-Strawberry sample can escape detection. For Tox21, Active is not a ground-truth target for descriptor outliers. Its flag-by-target table is therefore not a confusion matrix for assay prediction, and no assay-classification accuracy should be calculated from its flags.

The plots display only part of the evidence. Two descriptor axes cannot show every relationship used by an eight-feature detector, and a comparison with a training mean does not reveal the whole decision. Different descriptor units also prevent direct comparison of raw deviations across columns. Useful follow-up includes checking the source record, sample handling, structure parsing, instrument controls and, where justified, another measurement or assay.

## 11. Limits and follow-up

Both practicals reuse earlier test records for teaching and do not establish independent external validation. The Strawberry file lacks specimen, supplier and batch groups; the Tox21 random split can share chemical families across groups. A flag can prioritise work, but releasing every unflagged product or declaring every unflagged compound safe would exceed the evidence.


Across all examples, identify the measurement, the learned input–output relationship, the validation unit and the proposed laboratory decision. Then separate what the result demonstrates from the additional measurements needed to support a claim about identity, structure, safety or a new analytical method. The [LLM Tools notes](../../05_LLM_Tools/notes/Part5_LLM_notes.md) carry this responsibility into a student-designed project.
