# Tox21 reference data for the three guided practicals

`tox21.csv.gz` is an unchanged backup of the public CSV distributed by
DeepChem's Tox21 loader. Each notebook reads that same public file directly
with pandas and calculates eight descriptors with RDKit. The notebooks use
the **DeepChem-distributed Tox21 data**; they do not require installation of
the DeepChem Python package. Internet access is needed for the supplied
installation and loading cells.

## Records, endpoint and cleaning

The downloaded file contains 7,831 records, 12 assay-result columns, a
`mol_id` and a SMILES structure string. All three practicals use only
**SR-MMP**, the mitochondrial membrane potential assay endpoint:

- `1` becomes **Active**; `0` becomes **Inactive**.
- Missing assay results are unknown, not Inactive. Excluding these 2,021
  records leaves 5,810 records with an SR-MMP result and a structure string.
- RDKit 2025.09.6 cannot read six of these structures. Their source IDs are
  `TOX24723`, `TOX24552`, `TOX24622`, `TOX7518`, `TOX28892` and `TOX28623`.
  The notebooks count and exclude them explicitly.
- The retained subset contains **5,804 records: 4,886 Inactive and 918 Active**.
  A canonical-SMILES check found no identical structures repeated in this subset.
  Different structures can still share the same eight descriptor values.

These labels describe this assay's recorded outcome. Inactive does not mean
safe, and Active does not establish human toxicity. Other endpoints, assay
conditions and exposure are outside this teaching exercise. This single-task
subset is not the full Tox21 multitask benchmark.

## The same eight features throughout

Each row represents one retained source record. Features are calculated from
its structure, rather than measured concentrations or assay responses.

| Notebook column | RDKit calculation | Meaning |
|---|---|---|
| Mass | `MolWt` | Molecular weight, g/mol |
| LogP | `MolLogP` | Predicted octanol/water partition coefficient on a log scale |
| H_donors | `NumHDonors` | Hydrogen-bond donor count |
| H_acceptors | `NumHAcceptors` | Hydrogen-bond acceptor count |
| Polar_area | `TPSA` | Topological polar surface area, Å² |
| Rotatable_bonds | `NumRotatableBonds` | Rotatable bond count |
| Aromatic_rings | `NumAromaticRings` | Aromatic ring count |
| Heavy_atoms | `HeavyAtomCount` | Non-hydrogen atom count |

The RDKit release is pinned in a short installation cell. Structures are read
as supplied; fragments, salts and charges are not removed. Descriptor choices
are fixed teaching inputs, not chemical features optimised on test results.
Neither `mol_id`, SMILES nor the assay label enters the feature table.
Each notebook previews source records and draws the first four retained
structures. A separate preview links source IDs and reference labels to the
eight descriptor values, followed by a Mass/LogP plot coloured by assay label.

## How the practicals connect

| Practical | Learning samples | Checking samples |
|---|---|---|
| Foundations | 4,643 training records | 1,161 test records |
| Evaluation | 3,482 training records; 1,161 validation records choose a model | The same 1,161 test records |
| Applications | The original 4,643 training records form the descriptor reference group | The same 1,161 test records |

All splits use `random_state=42` and preserve approximately the class
proportions. These are random teaching splits, not DeepChem's default
scaffold split. Related chemical families can occur in different groups.
Reuse of the test group across practicals is a classroom comparison rather
than fresh independent validation.

Foundations fits one tree with a two-question depth limit. Evaluation compares
that model with a deep tree and a 100-tree random forest. Their fixed
`class_weight="balanced"` setting gives both classes equal total training
weight without changing record counts. Validation accuracy selects the model
in the exercise; missed Active results and false alarms are also discussed.
Accuracy alone does not establish usefulness for screening the rare class.

Applications fits an isolation forest to **all training compounds**, including
both assay classes. It learns usual descriptor patterns without assay labels.
The fixed `contamination=0.05` setting places a boundary to flag about 5% of
training reference records. It does not estimate toxicity prevalence. Flags
and assay predictions answer different questions; the flag-by-assay-label
table is not a classifier confusion matrix.

## Provenance, attribution and backup

- [Tox21 challenge: original programme and assay tasks](https://tripod.nih.gov/tox21/challenge/about.jsp).
- [Tox21 public data and tools](https://tox21.gov/data-and-tools/).
- [DeepChem Tox21 loader](https://github.com/deepchem/deepchem/blob/master/deepchem/molnet/load_function/tox21_datasets.py).
- [Exact public CSV address](https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/tox21.csv.gz).
- [RDKit molecular descriptor documentation](https://www.rdkit.org/docs/GettingStartedInPython.html#list-of-available-descriptors).

Snapshot retrieved 2026-10-16; compressed size: 122,925 bytes.

- Compressed SHA-256:
  `45d09792492ce049039dd24aa27b07fc79ce20c573187d4d90bcd178c0c0d360`.
- Uncompressed SHA-256:
  `7d7e7facd853a63e79ddce4e9c3fcb7a0d83a1c300b603031c0f2c64fbe77761`.

The upstream address is not a versioned GitHub file. The checksummed backup
records the exact input used for the saved outputs. For offline teaching,
an instructor can adapt `pandas.read_csv` to read this local gzip file and
install the pinned RDKit release beforehand. Original data attribution and
terms remain separate from the course-code licence.
