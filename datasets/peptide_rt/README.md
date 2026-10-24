# Peptide retention-index data for Part 5

The LLM practical uses 6,000 experimentally derived peptide retention indices
from the DLOmix example file `proteomTools_train_val.csv`. DLOmix connects this
resource to the ProteomeTools synthetic peptide measurements (PXD004732).
The source contains 34,000 distinct peptide sequences, with no missing values
or noncanonical amino-acid characters in this pinned version.

| Column | Meaning |
|---|---|
| `sequence` | Peptide sequence in the standard one-letter amino-acid alphabet |
| `irt` | Experimentally derived, calibrated retention index; dimensionless |

An iRT of 50 is not a retention time of 50 minutes. Conversion to an experimental
time requires calibration for a particular LC method. The two-column file does
not carry modification annotations, run IDs, batch IDs or detailed LC settings.
Do not infer that plain sequence strings describe all chemical modifications.

## Source and attribution

- [Pinned DLOmix CSV](https://raw.githubusercontent.com/wilhelm-lab/dlomix/f67623048c8692823cff88c3a7521123697af781/example_dataset/proteomTools_train_val.csv)
- Source commit: `f67623048c8692823cff88c3a7521123697af781`.
- [ProteomicsML description](https://proteomicsml.org/datasets/retentiontime/DLOmix_RT.html).
- Zolg et al. (2017), [Building ProteomeTools based on a complete synthetic human proteome](https://doi.org/10.1038/nmeth.4153).
- Credit the original ProteomeTools experimental authors and the Wilhelm-lab DLOmix contributors.
- The CSV is distributed in the [MIT-licensed DLOmix repository](https://raw.githubusercontent.com/wilhelm-lab/dlomix/f67623048c8692823cff88c3a7521123697af781/LICENSE).
  Its notice is retained in [SOURCE_LICENSE.txt](SOURCE_LICENSE.txt).
  The course repository licence does not replace the source notice.

## Classroom preparation

The notebooks load the pinned source, preview it and select 6,000 rows using
`sample(n=6000, random_state=42)`. Each sequence occurs only once. Students choose
and document their own training/validation/test split and keep it fixed across
comparisons. The instructor example uses 3,600 training, 1,200 validation and
1,200 test peptides. This differs from the upstream benchmark partitions; it is
not a reproduction of DLOmix results. Similar sequences can still cross groups,
and there are no run or batch groups available for a stronger split.

[peptides_6000.csv.gz](peptides_6000.csv.gz) is a backup of exactly this sample,
with the original columns and target scale retained. No targets were simulated.
For an offline run, upload this backup to Colab and replace the data-loading cell
with `raw_data = pd.read_csv("peptides_6000.csv.gz")`; the following sample cell
will then shuffle those rows again, so instead set `data = raw_data.copy()` there
to retain the supplied snapshot order (and the split used in the instructor example).

Run `python datasets/peptide_rt/prepare_data.py` from the repository root to
regenerate the snapshot. [provenance.json](provenance.json) records the source
and snapshot hashes. Preparation used pandas 3.0.6. Compression or formatting
changes in other library versions can change the compressed-file hash without
changing the underlying data.

The instructor example uses composition features that do not encode amino-acid
order; students may choose a different representation. Reported errors concern
the supplied retention-index scale and the chosen evaluation split;
they do not establish performance for new modifications or another LC method.
