# Data: from an analytical measurement to a model input

These notes develop the data questions encountered in the Strawberry, Tox21 and peptide-retention practicals. They connect Foundations to Evaluation: understanding a model requires knowing how its table was assembled, what each column means and which information was available before prediction.

## Materials used in these notes

| Material | Data concepts illustrated |
|---|---|
| [Strawberry Foundations](../../01_Foundations/notebooks/TD1_strawberry_student.ipynb) | Source-table orientation, spectra, conflicting records and window means |
| [Tox21 Foundations](../../01_Foundations/notebooks/TD1_tox21_student.ipynb) | Missing outcomes, structure parsing, calculated descriptors and learned representations |
| [Strawberry Evaluation](../../03_Evaluation/notebooks/TD2_strawberry_student.ipynb) | Training-only scaling and ordered full-spectrum inputs |
| [Tox21 Evaluation](../../03_Evaluation/notebooks/TD2_tox21_student.ipynb) | Class imbalance and limits of random chemical splits |
| [Peptide-retention project](../../05_LLM_Tools/notebooks/TD4_peptide_RT_student.ipynb) | Sequence representations, source provenance and a numerical target |

There is no separate Data presentation in the current course folder. The examples and preparation steps below are drawn from these practicals and their dataset documentation.

## 1. A row needs a scientific meaning

A table row might describe a physical specimen, an injection, a spectrum, a compound record or a peptide sequence. These are not interchangeable sampling units. Two injections from the same specimen are additional measurements of that specimen, not necessarily independent evidence about two different specimens. The meaning of a row determines how the data should be split and what a reported score can support.

The Strawberry practical treats one recorded spectrum as one observation, but the source lacks physical-specimen and batch identifiers. Tox21 supplies compound records and assay summaries rather than raw cellular images or fluorescence traces. The peptide project supplies distinct sequence strings and retention indices without run metadata. These limitations restrict the validation designs available from the files.

## 2. Separate inputs, targets and metadata

Inputs must be available when the prediction will be made. Targets describe the outcome to learn or check, while metadata describe origin, acquisition or organisation. A source identifier can be essential for tracing errors without belonging in the feature table. An assay outcome, identification score or processing result can create leakage if it contains information unavailable at the intended prediction stage.

| Role | Strawberry example | Tox21 example | Peptide example |
|---|---|---|---|
| Input | Infrared signals or their window means | Molecular structure or its descriptors | Amino-acid sequence or its representation |
| Target | Recorded purée class | Recorded SR-MMP class | Recorded `irt` value |
| Traceability information | Position in the source table | `mol_id` | Source and sampling procedure |
| Important information absent | Supplier and specimen groups | Complete assay traces and biological context | Run, batch and detailed LC conditions |

A target is a recorded reference outcome, not an infallible statement about every future situation. A purée category does not identify an adulterant. An Inactive assay result does not establish safety. An iRT value is a calibrated index without time units, not a retention time in minutes on any chosen instrument.

## 3. Inspect the source before transforming it

A file extension does not establish its internal layout. A comma-separated values file (CSV) can place samples in rows or columns, include an extra identifier column, or combine text and numerical entries. Before selecting model inputs, inspect the column names, several records, the table shape and the meanings of the units. Silent assumptions at this stage can produce a plausible-looking table containing the wrong values.

In the Strawberry source, targets are in the first row, wavenumbers in the first column and spectra in the remaining columns. `header=None` preserves that target row when reading. The numerical portion is converted from text to floating-point numbers, and transposition makes samples become rows. These operations change the arrangement and representation of the values rather than creating new measurements.

In Tox21, `smiles` contains a textual description of atoms and bonds, while `SR-MMP` contains 0, 1 or a missing outcome. A SMILES string is not a feature vector until a numerical representation is calculated. A successful structure parser confirms that the recorded string can be read under its rules; it does not verify the experimental identity, purity or assay activity of the compound.

## 4. Missing values and conflicting records

A missing target means that the supervised outcome is unavailable. Replacing it with a negative class invents a measured result and changes the learning problem. The Tox21 practical excludes records without an SR-MMP result and counts structures that cannot be read. The notes and conclusions should therefore refer to the retained subset, rather than implying that every original source record entered the model.

Missing input values raise a different question. Depending on the experiment, an absent value could mean a failed measurement, a quantity below detection or information that was never collected. Zero is only appropriate when it has the correct scientific meaning. If a model uses an estimated replacement, the replacement rule must be learned from training data and then applied consistently to other groups.

Conflicting duplicates require investigation rather than an arbitrary choice of the preferred target. Two Strawberry records contain exactly the same numerical spectrum with opposite recorded classes. Removing both leaves 981 observations and avoids pretending that the file resolves the conflict. It does not establish that all remaining measurements come from independent physical specimens.

Different molecular structures can also share the same eight descriptors. That is information loss in the representation, not proof that the source structures are duplicates. If their targets differ, a classifier using only those inputs cannot separate that pair. This distinction explains why a deep Tox21 tree need not achieve exactly 100% training accuracy.

## 5. Three ways to represent chemical information

### Measured signals

A measured spectrum is an ordered set of signals associated with physical positions, such as wavenumbers. A one-dimensional CNN can use neighbouring positions together. If those columns are shuffled, their chemical ordering changes even though the same numerical values remain in the table. A valid input representation therefore includes both the values and their intended arrangement.

The source does not establish absolute physical units for the Strawberry signal values. The notebooks call them supplied spectral signals rather than claiming that an entry is a concentration or a fully documented absorbance measurement. Wavenumber still has its stated unit, cm⁻¹; uncertainty about signal processing should not erase known axis information.

### Calculated descriptors and fixed summaries

The eight Strawberry features are means over predefined spectral windows. They provide a small, readable table but blur local details. They are not eight identified compounds or eight measured concentrations. Their boundaries are fixed teaching choices, not bands selected because they happen to separate the test targets.

Tox21 uses descriptors calculated from structure: molecular weight, predicted LogP, hydrogen-bond counts, polar surface area, rotatable bonds, aromatic rings and heavy atoms. Units differ across these columns. A difference of ten in molecular weight cannot be compared directly with a difference of ten in polar area as if they described the same quantity. The relevant structure representation, including fragments and charges retained by the notebook, also affects the calculations.

### Learned representations

An encoder can learn a numerical representation that supports reconstruction or prediction. CDDD's 512 latent values are one example. Such values can be useful without each coordinate corresponding to a named chemical property. Their meaning depends on the model and training task; visual proximity or a large latent value should not be interpreted as direct biological evidence.

The peptide project leaves representation choices to students. Counts and length are easy to inspect but discard residue order. A position-based encoding can retain order but requires handling different sequence lengths. A learned embedding can contain additional information, but its provenance and training conditions must be understood. There is no representation that is automatically best for every dataset and purpose.

## 6. Split before learning preparation settings

Data preparation can itself learn from examples. A standard scaler estimates each feature's mean and spread; an imputer estimates replacement values; feature selection can use a relationship with the targets. These fitted steps belong inside the training procedure. Validation and test data receive the transformations already learned, rather than helping determine them.

For standard scaling, a value is expressed as its difference from the training mean divided by the training standard deviation. The unit change does not create new chemical information. It makes numerical magnitudes more comparable for models that are sensitive to scale. Trees generally do not need this transformation to choose thresholds, whereas the supplied neural networks use it.

Fixed operations that do not learn from the dataset have a different role. Calculating a predetermined descriptor for a molecule or applying fixed spectral-window boundaries does not estimate a parameter from held-aside targets. This does not justify choosing those boundaries after inspecting test performance: once test outcomes influence a choice, the test has entered model development.

## 7. Independence and representativeness

The split should match the intended prediction. To predict a new injection of an already studied compound, a within-compound design answers one question. To predict a previously unseen compound, keeping replicate injections of the same compound on both sides can give an overly optimistic answer. For new chemical families, grouping related structures may be more informative than an ordinary random split.

Class stratification keeps class proportions approximately similar across groups. It does not separate suppliers, batches or chemical families. A random seed makes a particular split reproducible, but it does not make that split representative of every future population. When important grouping metadata are absent, the limitation should be stated rather than treated as solved.

## 8. Provenance, reuse and reproducibility

A usable analysis records where the data came from, which version was used, what was removed and how the inputs were calculated. A pinned source commit or a checksummed snapshot helps identify the exact file. A source link alone can change over time, while a reproducible file still needs a scientifically appropriate validation design. Technical repeatability and scientific generalisation are different properties.

The repository documents each dataset separately: [Strawberry](../../datasets/strawberry/README.md), [Tox21](../../datasets/tox21/README.md) and [peptide retention indices](../../datasets/peptide_rt/README.md). The Strawberry deposition specifies CC BY-NC 3.0; the peptide snapshot retains the source repository's licence notice. The course-code licence does not replace source-data terms. Attribution, preparation choices and the limits of the retained subset belong in the analysis record.

Display rounding is another small but useful distinction. `round(2)` shows two decimal places in a table; it need not change the values used to train or predict. Rounding the actual feature inputs, changing column order or silently converting units can change a model's results. The same named features and preparation must be used when predicting new samples.

## 9. Questions to carry into Evaluation

Before fitting a model, be able to identify one sampling unit, each feature's meaning, the target's origin and the information missing from the file. Explain which preparation steps learn from the training group and which are fixed calculations. Then state what population the held-aside examples represent and which future populations remain untested.

The [Evaluation notes](../../03_Evaluation/notes/Part3_Evaluation_notes.md) develop the consequences of these choices for model selection, leakage, bias and out-of-distribution use. The [LLM Tools project](../../05_LLM_Tools/notes/Part5_LLM_notes.md) asks students to make and document these choices themselves with an assistant.
