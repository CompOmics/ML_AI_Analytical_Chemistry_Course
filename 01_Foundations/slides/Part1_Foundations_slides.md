# Part 1: Foundations of Machine Learning and AI (slide deck)

Markdown equivalent of `Part1_Foundations_slides.pptx` (23 slides). One section per slide. Example callouts and figures are noted in parentheses.

---

## Slide 1 - Title

**Machine Learning and AI for Analytical Chemistry**

Part 1: Foundations of Machine Learning and AI

M2 Sciences analytiques · 6 h lectures + 1 h tutorial
Lennart Martens · Jerome Pansanel

---

## Slide 2 - Roadmap for Part 1

1. **Concepts** - what ML and AI mean, the learning settings, features, and the modelling workflow.
2. **Classical models** - decision trees and how they are induced, random forests, SVM/SVR, k-means.
3. **Deep learning** - neural networks, CNNs, transformers and attention, with GNNs and autoencoders in brief.

---

## Slide 3 - AI, machine learning, deep learning

Three nested ideas:

- **AI** is the broad goal of machine intelligence.
- **ML** fits a function to data instead of hand-coding rules.
- **Deep learning** is ML with many-layered neural networks.

(Visual: concentric ovals, AI > ML > deep learning.)

> **Example:** a Beer-Lambert calibration is a physical rule; predicting LC retention time is ML; DeepLC is its deep-learning version.

---

## Slide 4 - Why this matters for analytical chemistry

- **Rich measurements** - chromatograms, mass, IR, Raman and NMR spectra, ion mobility: large, structured, high-dimensional data.
- **Hard-to-write rules** - models can capture relationships too complex to express as explicit physical or expert rules.
- **New capabilities** - predict retention, fragmentation and CCS; recognise signals; flag anomalies (Part 4).
- **A real risk** - a model can look like it works while having learned the wrong thing (Part 3).

---

## Slide 5 - Three learning settings

- **Supervised** - examples carry known answers (labels). Learn input to answer.
  *Example: GC retention index from descriptors (regression); Raman polymorph A vs B (classification).*
- **Unsupervised** - no labels. Find structure on its own.
  *Example: cluster olive-oil GC-MS profiles to see if they separate by geographic origin.*
- **Reinforcement** - learn by trial and error against a reward.
  *Example: tune MS collision energy to maximise confident identifications. Not a course focus.*

---

## Slide 6 - Features: the central idea

A **feature** is a measurable property of a sample, as a number. A dataset is a table: rows are samples, columns are features, plus the target. A spectrum becomes a vector with one absorbance per wavenumber (an IR spectrum is about 1800 numbers).

| sample | alcohol | flavanoids | proline | -> target |
|--------|---------|-----------|---------|----------|
| wine 1 | 14.2 | 3.06 | 1065 | cultivar 0 |
| wine 2 | 13.2 | 2.76 | 1050 | cultivar 0 |
| wine 3 | 12.4 | 0.92 | 562 | cultivar 1 |

**Key point:** the quality and origin of the features usually matter more than the choice of algorithm (Part 2).

---

## Slide 7 - The machine learning workflow

1. Define the task
2. Understand the data
3. Build features
4. Split the data
5. Train
6. Evaluate
7. Interpret and iterate
8. Deploy and monitor

> **Running example:** flag out-of-spec batches from NIR spectra. Steps 4 and 6 (green) decide whether you can trust the result (Part 3).

---

## Slide 8 - Two cautions to start with

**When NOT to use ML**

- A validated physical model already exists
- Very few samples
- Full transparency is required
- A single rule solves the problem
- Always beat a trivial baseline first

*Example: a linear Beer-Lambert fit beats a neural net for single-analyte quantitation.*

**Overfitting (preview of Part 3)**

A too-flexible model memorises noise and fails on new data. Underfitting is the opposite: too simple to capture the pattern. Good scores on data the model has already seen prove almost nothing.

*Example: a classifier that secretly reads the measurement batch, not the chemistry.*

---

## Slide 9 - Section divider

**Classical machine learning**
Decision trees and their induction · random forests · SVM/SVR · k-means

---

## Slide 10 - Decision trees

A sequence of yes/no questions on the features.

- (+) readable, no scaling, handles non-linearities and interactions.
- (-) a deep single tree overfits badly (controlled by pruning, next slides).

(Visual: a tree splitting on "C=O near 1715?" then "broad 2500-3300?" into carboxylic acid / ketone / O-H,N-H leaves.)

> **Example:** identify a functional group from an IR spectrum by splitting on diagnostic absorption bands.

---

## Slide 11 - How a decision tree is induced

**The induction algorithm**

1. Start with all samples at the root.
2. Try every feature and every split point.
3. Score each split by impurity reduction.
4. Keep the best split; partition the samples.
5. Recurse on each child node.
6. Stop when pure or a limit is reached.

*Greedy: the locally best split now, with no look-ahead.*

**Scoring a split**

- Entropy: H = - Sum p log2 p
- Gini: G = 1 - Sum p^2
- Information gain: IG = H(parent) - weighted H(children)

Pick the highest IG. Continuous features: test midpoints between sorted values.

---

## Slide 12 - Induction: a worked split

8 honey samples: 4 pure (P), 4 adulterated (A). Parent is a 4/4 mix, so **H(parent) = 1.00 bit**.

Split on a delta-13C isotope test:

| branch | n | A | P | child H |
|--------|---|---|---|---------|
| yes | 4 | 3 | 1 | 0.81 |
| no | 4 | 1 | 3 | 0.81 |

IG = 1.00 - 0.81 = **0.19 bit**

**Why this split wins:** a "dark colour?" split gives children each still 2/2, so H = 1.00 and IG = 0.00. The isotope test carries more information, so it is chosen, then the tree recurses. Stop by depth or leaf size; prune to fight overfitting.

---

## Slide 13 - Random forests

Many decision trees, averaged (or voted).

- a bootstrap sample of rows per tree
- a random subset of features per split

Averaging diverse, noisy trees cancels error.

- (+) accurate, robust, gives feature importances.
- (-) less readable than one tree.

(Visual: bar chart of illustrative feature importances.)

> **Example:** flag likely genotoxic compounds from molecular descriptors; importance may highlight an aromatic nitro group.

---

## Slide 14 - Support vector machines (and SVR)

Find the boundary with the widest **margin** between classes; the nearest points (support vectors) set it.

**Kernel trick:** map data to a higher space so a curved boundary becomes possible (RBF kernel).

**SVR** does the same for continuous targets.

Always scale features first.

(Visual: scatter of two separable classes.)

> **Example:** water above a contaminant threshold from conductivity (100s of uS/cm) and a trace metal (few ug/L): scale first.

---

## Slide 15 - k-means clustering (unsupervised)

No labels. Choose k, then repeat until stable:

- assign each sample to its nearest cluster centre
- move each centre to the mean of its members

Remember: choose k; results depend on the start; assumes round, similar-sized clusters; scale the features.

(Visual: scatter of three discovered clusters.)

> **Example:** cluster ICP-MS trace-element fingerprints of honey to probe floral or regional origin (scale first).

---

## Slide 16 - Choosing among them

| Situation | Start with |
|-----------|-----------|
| Tabular data, strong result fast | Random forest |
| Interpretability is the priority | Single decision tree |
| Many features, few samples (scaled) | SVM / SVR |
| No labels, explore structure | k-means / clustering |
| Any situation | A trivial baseline, always |

---

## Slide 17 - Section divider

**Deep learning, by intuition**
Neural networks · CNNs · transformers · (GNNs & autoencoders)

---

## Slide 18 - Neural networks: the foundation

Simple units (neurons): a weighted sum, an offset, then a non-linear activation.

Units form layers; output of one feeds the next. "Deep" = many layers. The non-linearity is essential.

**Training:** a loss measures error; backpropagation and gradient descent adjust weights over many epochs.

(Visual: input/hidden/output network diagram.)

> **Example:** learn a non-linear fluorescence calibration that stays accurate where a Beer-Lambert fit saturates.

---

## Slide 19 - Convolutional neural networks (CNNs)

**The idea:** a small filter slides across the input to detect a local motif wherever it occurs. Early layers find simple motifs; later layers combine them. Few parameters, tolerant to shifts.

**In analytical chemistry:** spectra are 1D sequences of intensities, so a 1D CNN learns peak shapes and patterns regardless of position.

> **Example:** classify a Raman spectrum as PE, PP or PS; the same idea picks true peaks against noise in LC-MS.

---

## Slide 20 - Transformers and attention

The architecture behind modern large language models, and increasingly models of molecules and spectra.

**Attention:** when processing one element, the model learns how much to attend to every other element, capturing long-range relationships.

Processed in parallel, scales to large data. Also the basis of the LLMs in Part 5.

(Visual: tokens of a sequence, all attending to one position to form context.)

> **Example:** predict a peptide's fragmentation spectrum from its sequence (Prosit) using long-range residue relationships.

---

## Slide 21 - Two more to recognise (briefly)

**Graph neural networks** - operate on graphs of nodes and edges. A molecule is a graph (atoms = nodes, bonds = edges), so GNNs predict properties from structure; each node exchanges information with its neighbours.

**Autoencoders** - reconstruct the input through a narrow bottleneck, learning a compact representation. Used for dimensionality reduction, denoising and anomaly detection; a VAE can also generate new examples.

> **Examples:** a GNN predicts CCS from a molecular graph; an autoencoder flags an anomalous process-NMR spectrum.

---

## Slide 22 - Classical or deep? A practical rule

**Reach for deep learning**

- large, high-dimensional data
- spatial/sequential structure (images, spectra)
- enough labels and compute

**Reach for classical**

- tabular, modest-size data
- interpretability matters
- you need a strong result quickly

**Next - TD1:** train a decision tree, random forest, SVM and k-means on real wine-chemistry data.

---

## Slide 23 - Key takeaways

- ML fits functions to data; deep learning is ML with many-layered networks.
- Features and their quality usually matter more than the algorithm.
- A tree is induced by greedy splits chosen on information gain, then pruned.
- Start classical (random forest) and always beat a trivial baseline.
- Good scores on already-seen data prove almost nothing (Part 3).
