# Strawberry authentication reference data

`fruit_purees.csv.gz` is a lossless gzip snapshot of the distributed
`MIR_Fruit_purees.csv` file. It is retained as an attributed backup for instructors.
The simplified Foundations, Evaluation and Applications notebooks each download the same
version-pinned CSV directly, using one short `pandas.read_csv` call. Internet
access is required for their unchanged loading cells. For offline teaching, an
instructor can adapt that call to read this local gzip file with `header=None`.

## Measurements and labels

The original CSV stores 983 spectra in columns and 235 wavenumbers in rows
(approximately 899.327–1802.564 cm⁻¹). Its first row provides class labels:
351 Strawberry and 632 NON-Strawberry. The first column contains wavenumbers.
The numerical values are supplied spectral signals; their processing and
absolute physical signal units are not established by this CSV.

NON-Strawberry combines other fruit purées and strawberry mixtures adulterated
with fruits or sugar solutions. No sample-level adulterant, concentration,
supplier, harvest-year or replicate-group metadata are included. Positional
sample IDs assigned by the notebooks do not identify physical specimens.

Two records (`sample_0366` and `sample_0844`, using positional IDs) have exactly
the same numerical spectrum but opposite class labels. The notebooks exclude
both ambiguous records, leaving 981 observations (350 Strawberry and 631
NON-Strawberry). They do not choose which label is correct. This eliminates
exact numerical overlap, but does not establish
independence of physical specimens. Eight predefined, contiguous 113 cm⁻¹
windows cover 899–1803 cm⁻¹. Their means are teaching summaries rather than
optimised bands or direct analyte concentrations. Foundations uses an 80/20
stratified training/test split (784/197 observations). Evaluation subdivides
the 784 training observations into 588 training and 196 validation observations,
preserving the same 197 test observations. These are teaching splits rather
than the original paper's validation design.

Foundations displays the source table and two individual spectra before
forming the eight features, then plots those same samples' window means.
The source CSV mixes text labels and numeric measurements in its columns:
`header=None` preserves the label row, and one `astype(float)` converts the
remaining rows to numbers. The revised preparation gives the same features
and sample groups as the Evaluation and Applications notebooks.

Foundations fits a small decision tree and a neural network with eight inputs
and one hidden layer of four neurons. The network's `StandardScaler` learns
from the 784 training samples and applies the same transformation to the
197 test samples. Both models have fixed teaching settings; their test results
illustrate accuracy and different kinds of mistake rather than tune a model.

The simplified Evaluation practical compares training and validation accuracy
for a small tree, a deep tree and a random forest, then tests the model chosen
using validation accuracy. Its code does not perform cross-validation or SVM
scaling. Test outcomes were already seen in Foundations; their reuse is a
classroom comparison rather than fresh independent validation. No additional
source data or snapshot is needed for Evaluation.

The Applications practical reuses the Foundations split. Its isolation forest
learns only from the 280 labelled Strawberry training samples, without using
the test samples or teaching examples of NON-Strawberry. A fixed
`contamination=0.05` setting places the flagging boundary using the training
reference samples; it does not estimate adulteration prevalence. The detector
then flags measurements in the same 197-sample test group. Reference test
labels are revealed afterwards to discuss flagged authentic samples and
NON-Strawberry samples that escaped a flag. Reuse of this test group remains
a classroom demonstration, not independent validation. Flags indicate
follow-up priorities rather than product authenticity or adulterant identity.

## Provenance and attribution

- Holland, J. K., Kemsley, E. K. and Wilson, R. H. (1998). *Use of Fourier
  transform infrared spectroscopy and partial least squares regression for the
  detection of adulteration of strawberry purées.* Journal of the Science of
  Food and Agriculture, 76, 263–269.
  [Publication record](https://research-portal.uea.ac.uk/en/publications/use-of-fourier-transform-infrared-spectroscopy-and-partial-least-/).
- Shu, H., Tang, H., Zhang, H. and Zheng, W. (2019). *Data for: Spectra Data
  Classification with Kernel Extreme Learning*, version 1.
  [Mendeley Data deposition](https://doi.org/10.17632/frrv2yd9rg.1).
- [Download mirror](https://github.com/zwbben/SpectroscopyData), commit
  `4db9b8168fac1185973d1e7888d51f7f33f94857`.
  [Exact source file](https://raw.githubusercontent.com/zwbben/SpectroscopyData/4db9b8168fac1185973d1e7888d51f7f33f94857/MIR_Fruit_purees.csv).
- Uncompressed file: 2,768,456 bytes; SHA-256:
  `d9602ad4f9909d73aa59653a5921c177911629320f048a2bd387b27339a263fd`.

## Data licence

The Mendeley deposition specifies **Creative Commons Attribution-NonCommercial
3.0** ([CC BY-NC 3.0](https://creativecommons.org/licenses/by-nc/3.0/)) and requests
acknowledgement of the original sources. This licence applies to the data
snapshot and is separate from the repository's code licence. The source CSV
content has not been changed; gzip compression is used only for storage.
Transposition, deduplication, window averaging and splitting occur in the
notebooks and are documented there.
