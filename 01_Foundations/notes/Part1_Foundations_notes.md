# Part 1: Foundations of Machine Learning and AI

**Lecture notes (6 h CM + 1 h TD)**
Machine Learning and AI for Analytical Chemistry, M2 Sciences analytiques

These notes accompany the Part 1 slides and the TD1 notebook. Each key point
carries a short worked example drawn from analytical chemistry. These examples
are deliberately different from the wine dataset used in the TD1 notebook, so
that the lecture and the practical reinforce each other rather than repeat.

---

## 1. Concepts: machine learning and artificial intelligence (2 h)

### 1.1 What we mean by the terms

**Artificial intelligence (AI)** is the broad goal of getting computers to
perform tasks that we would call intelligent if a person did them. It is an
umbrella term and, on its own, says little about how a system works.

**Machine learning (ML)** is the subset of AI that matters in practice today. A
machine learning model is a function with adjustable parameters that are fitted
to data, rather than programmed by hand. Instead of writing the rule "if the
retention time is above X and the mass is below Y, then ...", we show the
algorithm many labelled examples and let it find the rule that best reproduces
them.

**Deep learning** is the subset of machine learning that uses neural networks
with many layers. It powers image recognition, speech, and large language
models. We treat it in Section 3.

The relationship is one of nested sets: deep learning is inside machine
learning, which is inside artificial intelligence.

> **Example.** Determining the concentration of an analyte from a UV-Vis
> absorbance using the Beer-Lambert law is not machine learning: the rule is a
> known physical equation. Predicting the liquid-chromatography retention time
> of a molecule from its structure is machine learning: there is no simple
> equation, so we fit a model to thousands of measured retention times. A modern
> retention-time predictor built on a deep neural network (for instance DeepLC)
> is the deep-learning version of the same task.

### 1.2 Why this is relevant to analytical chemistry

Analytical chemistry produces large, structured, high-dimensional measurements:
chromatograms, mass spectra, NMR spectra, ion mobility data. Many tasks once
solved with physical models or expert heuristics can now be addressed by
learning patterns directly from data: predicting retention times, predicting
fragmentation, recognising signals, and flagging anomalies. The appeal is that a
model can capture relationships too complex to write down explicitly. The risk,
developed in Part 3, is that a model can appear to work while having learned the
wrong thing.

### 1.3 The three main learning settings

**Supervised learning.** Each training example has an input (features) and a
known answer (label or target). The model learns to map inputs to answers. Two
sub-cases:

- *Regression*: the target is a continuous number.
- *Classification*: the target is a category.

> **Example (regression).** Predict the gas-chromatography retention index of a
> volatile compound from molecular descriptors, with the measured retention
> index as the target.
> **Example (classification).** Decide whether a pharmaceutical tablet is
> polymorph form A or form B from its Raman spectrum, with the known form as the
> label.

**Unsupervised learning.** The data have no labels. The model looks for
structure on its own, for example grouping similar samples (clustering) or
compressing the data into fewer dimensions. Useful for exploration and quality
control when you do not yet know what you are looking for.

> **Example.** Cluster the GC-MS profiles of olive-oil samples to see whether
> they separate by geographic origin, without telling the algorithm any origin
> labels. This is a common authenticity-screening question.

**Reinforcement learning.** An agent learns by trial and error against a reward
signal. It is central to robotics and game playing and to some experiment-design
problems, but it is not a focus of this course.

> **Example.** Automatically tune the collision energy and isolation window of a
> mass spectrometer to maximise the number of confident identifications, where
> the reward is the identification count.

### 1.4 Features, the central idea

A **feature** is a measurable property of a sample, expressed as a number. The
collection of features for one sample is a **feature vector**. A dataset is then
a table: rows are samples, columns are features, plus one column for the target
in supervised learning.

The quality of the features usually matters more than the choice of algorithm.

> **Example.** An infrared spectrum sampled every 2 cm-1 from 400 to 4000 cm-1
> is a feature vector of about 1800 numbers, one absorbance per wavenumber. A
> molecule can instead be described by computed molecular descriptors (molecular
> weight, number of hydrogen-bond donors, topological polar surface area, and so
> on). The same compound can therefore be represented by very different feature
> sets, and that choice constrains what any model can learn (Part 2).

### 1.5 The machine learning workflow

Every project, regardless of method, follows the same loop. Learn this loop; the
algorithms are interchangeable parts inside it.

1. **Define the task.** What is predicted, from what, and why. Choose regression
   or classification.
2. **Collect and understand the data.** Inspect distributions, missing values,
   and obvious errors before modelling.
3. **Build features.** Clean, transform, and where needed scale the inputs.
4. **Split the data.** Separate training data from data held back for honest
   evaluation. Doing this correctly is the subject of Part 3; doing it wrong is
   the most common cause of misleading results.
5. **Train a model.** Fit the parameters on the training set.
6. **Evaluate.** Measure performance on held-back data with an appropriate
   metric.
7. **Interpret and iterate.** Understand what the model uses, diagnose errors,
   and improve.
8. **Deploy and monitor.** Put the model to use, and watch for the data drifting
   away from what the model was trained on.

> **Example (the loop, end to end).** Goal: flag out-of-specification batches of
> a drug substance from their near-infrared (NIR) spectra. Understand the data:
> check for saturated spectra and baseline drift. Features: the preprocessed NIR
> spectrum. Split: keep whole production campaigns apart so the test set is
> genuinely unseen. Train: a classifier on passing and failing batches.
> Evaluate: measure detection on held-back campaigns. Interpret: confirm the
> model reacts to a real absorption band and not to an instrument artefact.
> Deploy: screen new batches, and watch for drift as raw-material lots change.

### 1.6 When not to use machine learning

Machine learning is not always the right tool. Prefer a simpler approach when a
validated physical or analytical model already exists, when you have very few
samples, when full transparency is legally required, or when a single rule
solves the problem. A good baseline (a linear fit, or even a constant
prediction) is always worth computing first: if a complex model cannot beat it,
the complexity is not justified.

> **Example.** To quantify a single analyte from its absorbance, a linear
> Beer-Lambert calibration is accurate, transparent, and validated. Replacing it
> with a neural network would add opacity and overfitting risk for no benefit.
> Machine learning earns its place only when the relationship is genuinely too
> complex for such a model.

### 1.7 Overfitting in one paragraph (preview of Part 3)

A model that is too flexible can memorise the training data, including its
noise, and then fail on new data. This is **overfitting**. The opposite,
**underfitting**, is a model too simple to capture the real pattern. The whole
discipline of evaluation (Part 3) exists to detect and control this.

> **Example.** A classifier that "predicts" sample origin with suspiciously high
> accuracy may in fact be reading the instrument or batch on which each class
> was measured, because all samples of one class happened to be run on the same
> day. It has memorised an artefact, not learned chemistry, and it will collapse
> on samples measured elsewhere. Good performance on data the model has already
> seen proves almost nothing.

---

## 2. Classical machine learning models (2 h)

These methods are not obsolete. For tabular analytical data with tens to a few
thousand samples, they are often more accurate, faster, and easier to interpret
than deep learning. They should be your default starting point.

### 2.1 Decision trees

A **decision tree** splits the data with a sequence of yes/no questions on the
features. Each internal node asks a question, each branch is an answer, and each
leaf gives a prediction.

> **Example.** Identifying the functional group of an unknown from its infrared
> spectrum. The first split asks "is there a strong band near 1715 cm-1 (C=O
> stretch)?" If yes, a second split on a broad 2500-3300 cm-1 band separates
> carboxylic acids from ketones. If no, a split on a 3200-3550 cm-1 band tests
> for an O-H or N-H group. Each split is a chemically interpretable rule, which
> is the appeal of a single tree.

Strengths: easy to read and explain, needs no feature scaling, handles
non-linear relationships and feature interactions naturally. Weakness: a single
tree grown deep enough will overfit badly, because it can keep splitting until
every training point sits in its own leaf. The next two subsections explain how
a tree is actually built, and how the overfitting is controlled.

### 2.2 How a decision tree is induced

"Induction" is the process of learning the tree from data. Decision trees are
grown by a **greedy, top-down, recursive partitioning** algorithm (the classic
variants are ID3, C4.5, and CART). The recipe is:

1. Start with all training samples at the root.
2. For every feature, and for every candidate split point of that feature,
   measure how much the split would reduce impurity.
3. Choose the single best split (the one with the largest impurity reduction).
4. Partition the samples down the two branches.
5. Repeat steps 2 to 4 on each child node, recursively.
6. Stop when a node is pure, or a stopping rule is met (see below).

It is called *greedy* because it takes the locally best split at each step
without looking ahead; it does not search for a globally optimal tree, which
would be computationally infeasible.

**Measuring impurity.** A node is "pure" if all its samples share one class. The
common impurity measures for classification are:

- **Entropy:** H = - sum over classes of p log2(p), where p is the fraction of
  the node belonging to each class. H is 0 for a pure node and 1 bit for a
  50/50 two-class node.
- **Gini index:** G = 1 - sum of p squared. Similar behaviour, slightly cheaper
  to compute; it is the default in scikit-learn's CART.

**Information gain** is the reduction in entropy achieved by a split:
IG = H(parent) - sum over children of (n_child / n_parent) * H(child).
The algorithm picks the split with the highest information gain.

> **Worked example.** Eight honey samples, four pure (P) and four adulterated
> (A). The parent node is a 4/4 mix, so H(parent) = 1.00 bit.
>
> Candidate split 1, a stable-isotope test "is delta-13C above the threshold?":
>
> | branch | samples | A | P |
> |--------|---------|---|---|
> | yes | 4 | 3 | 1 |
> | no | 4 | 1 | 3 |
>
> Each child has H = -(0.75 log2 0.75 + 0.25 log2 0.25) = 0.81 bit. The weighted
> child entropy is (4/8)(0.81) + (4/8)(0.81) = 0.81, so IG = 1.00 - 0.81 = 0.19.
>
> Candidate split 2, "is the colour dark?", happens to give two children that
> are each still 2/2, so H = 1.00 in both and IG = 0.00. The algorithm therefore
> chooses the isotope test, because it carries more information about
> adulteration. It would then recurse on each branch, looking for the next best
> split.

**Continuous features.** A feature such as retention time has no natural yes/no
form. The algorithm sorts the unique values, considers the midpoints between
consecutive values as candidate thresholds, evaluates the information gain of
each, and keeps the best "feature <= threshold" test. This is why trees handle
numeric analytical measurements directly, without scaling.

**Stopping criteria.** Growth stops when a node is pure, when no split improves
impurity, or when a user limit is reached: a maximum depth, a minimum number of
samples per leaf, or a minimum impurity decrease. These limits are the simplest
defence against overfitting (called pre-pruning).

**Pruning.** An alternative is to grow the tree fully and then cut back the
branches that do not improve performance on held-back data (post-pruning). CART
uses **cost-complexity pruning**, governed by a parameter (ccp_alpha in
scikit-learn) that trades tree size against accuracy. Pruning is how a single
tree is kept from memorising noise; the random forest in the next subsection
takes a different route to the same goal.

### 2.3 Random forests

A **random forest** is an ensemble of many decision trees whose predictions are
averaged (for regression) or voted (for classification). Two sources of
randomness make the trees differ from one another:

- each tree is trained on a random bootstrap sample of the data (sampling with
  replacement), and
- at each split only a random subset of the features is considered.

Averaging many diverse, individually noisy trees cancels much of their error.
This is why random forests are accurate, robust, and require little tuning. They
also provide a built-in **feature importance** estimate, which is valuable for
interpretation. The cost is that the ensemble is no longer as directly readable
as a single tree.

> **Example.** Predict whether a compound is likely to be genotoxic from a few
> hundred molecular descriptors. A random forest handles the many correlated
> descriptors gracefully, and its feature-importance ranking might highlight the
> presence of an aromatic nitro group, which is chemically plausible and gives
> the chemist a sanity check on the model.

### 2.4 Support vector machines and support vector regression

A **support vector machine (SVM)** for classification looks for the boundary
that separates two classes with the widest possible **margin**, the gap between
the boundary and the nearest samples. Those nearest samples are the "support
vectors"; they alone determine the boundary. When classes are not linearly
separable, the SVM uses the **kernel trick**: a kernel function implicitly maps
the data into a higher-dimensional space where a linear boundary becomes
possible. The common radial basis function (RBF) kernel allows curved
boundaries. **Support vector regression (SVR)** applies the same machinery to
continuous targets.

Strengths: effective in high-dimensional spaces and with limited samples, which
suits some spectral problems. Weaknesses: sensitive to feature scaling (always
scale first), sensitive to its tuning parameters, and slower on large datasets.

> **Example.** Decide whether a drinking-water sample exceeds a contaminant
> threshold from features such as conductivity (hundreds of microsiemens per
> centimetre) and a trace-metal concentration (a few micrograms per litre).
> Without scaling, conductivity dominates the distance calculation purely
> because its numbers are larger; standardising the features puts both on an
> equal footing so the SVM can use them fairly.

### 2.5 k-means clustering

**k-means** is the standard unsupervised method for grouping samples. You choose
the number of clusters, k. The algorithm then alternates two steps until stable:
assign each sample to its nearest cluster centre, then move each centre to the
mean of the samples assigned to it. Limitations: you must choose k in advance,
the result depends on the random starting positions, it assumes roughly round
clusters of similar size, and it requires the features to be scaled.

> **Example.** Group the trace-element fingerprints of honey samples (measured by
> ICP-MS) into clusters and check whether the clusters correspond to floral or
> regional origin. Because element concentrations span several orders of
> magnitude, the data must be scaled first, or a single high-concentration
> element would control every distance.

### 2.6 Choosing among them

A rough guide for tabular data: start with a random forest as a strong, low-
effort baseline. Use a single decision tree when interpretability is the
priority. Use SVM/SVR when you have many features and few samples and have scaled
the data. Use k-means (or other clustering) when you have no labels and want to
explore structure. In all cases, compare against a trivial baseline.

---

## 3. Deep learning, by intuition (2 h)

The goal here is understanding, not implementation. You should leave able to read
an applications paper and know roughly what each architecture does and when it is
appropriate. We keep the mathematics light.

### 3.1 Neural networks: the common foundation

A **neural network** is built from simple units ("neurons"). Each unit forms a
weighted sum of its inputs, adds an offset, and passes the result through a
non-linear **activation function**. Units are arranged in **layers**; the output
of one layer feeds the next. "Deep" means many layers. The non-linearity is
essential: stacking linear operations alone would collapse to a single linear
function. Training works by **gradient descent with backpropagation**: a **loss
function** measures the error, and the error is propagated backwards to adjust
each weight, repeated over many passes ("epochs"). Deep networks are data-hungry
and often underperform classical methods on small tabular data.

> **Example.** A fluorescence sensor whose response saturates at high analyte
> concentration is not linear, so a Beer-Lambert fit fails at the top of the
> range. A small neural network can learn the full non-linear calibration curve
> from many standard measurements, extending quantitation into the saturating
> region.

### 3.2 Convolutional neural networks (CNNs)

A **convolutional neural network** is designed for data with grid or sequence
structure where local patterns matter and can appear at different positions:
images (2D) and spectra (1D). The key idea is the **convolutional filter**, a
small set of weights slid across the input to detect a local motif (an edge in
an image, a peak shape in a spectrum) wherever it occurs. Early layers detect
simple motifs; later layers combine them. Reusing the same filter across all
positions means far fewer parameters and tolerance to shifts.

> **Example.** A 1D CNN reads a Raman spectrum and classifies a plastic fragment
> as polyethylene, polypropylene, or polystyrene, recognising the characteristic
> band pattern even if it is slightly shifted by instrument calibration. The same
> idea underlies peak detection in LC-MS, where a CNN learns the shape of a true
> chromatographic peak against noise.

### 3.3 Transformers and the attention mechanism

The **transformer** is the architecture behind modern large language models, and
increasingly behind models for molecules and spectra. Its central idea is
**attention**: when processing one element of a sequence, the model learns how
much to attend to every other element, capturing long-range relationships. It
processes all positions in parallel and scales well to large datasets, which is
why it has become dominant. Transformers are also the foundation of the **large
language models** (LLMs) that Part 5 treats as practical tools.

> **Example.** Predicting the fragmentation spectrum of a peptide from its amino-
> acid sequence (as Prosit does) needs the model to relate residues that are far
> apart in the sequence but close in the folded ion. Attention captures exactly
> these long-range dependencies, which is why transformer-style models predict
> peptide spectra and retention times well.

### 3.4 Graph neural networks and autoencoders (brief)

**Graph neural networks (GNNs)** operate on data shaped as graphs: nodes
connected by edges. A molecule is naturally a graph, with atoms as nodes and
bonds as edges, so GNNs predict molecular properties directly from structure.
Each node repeatedly updates its representation by exchanging information with
its neighbours.

> **Example.** Predict the collisional cross section (CCS) of a small molecule in
> ion mobility directly from its molecular graph, without first computing
> hand-crafted descriptors.

**Autoencoders** are networks trained to reconstruct their own input after
compressing it through a narrow "bottleneck", which forces a compact
representation. They are used for dimensionality reduction, denoising, and
anomaly detection. A **variational autoencoder (VAE)** is a probabilistic version
whose smooth internal space can also be sampled to generate new examples.

> **Example.** Train an autoencoder on normal process-NMR spectra; a spectrum
> that reconstructs poorly is flagged as an anomaly, signalling an unexpected
> impurity or a process fault.

### 3.5 Classical versus deep, a practical summary

Reach for deep learning when the data are large, high-dimensional, and have
spatial or sequential structure (images, spectra, long sequences), and when you
have the labelled volume and compute to support it. Reach for classical methods
when the data are tabular and modest in size, when interpretability matters, or
when you need a strong result quickly. In this course you build classical models
hands-on (TD1) and meet deep models mainly through their applications (Part 4).

---

## Key terms

- **Feature / feature vector**: numeric description of a sample.
- **Label / target**: the answer to be predicted.
- **Supervised / unsupervised learning**: with / without labels.
- **Regression / classification**: continuous / categorical target.
- **Overfitting / underfitting**: too flexible / too simple a model.
- **Induction**: learning a model (here, a tree) from data.
- **Greedy recursive partitioning**: the top-down tree-growing algorithm.
- **Entropy, Gini index, information gain**: impurity measures and the reduction
  used to choose splits.
- **Pruning**: cutting back a grown tree to fight overfitting.
- **Ensemble**: many models combined (e.g. a random forest of trees).
- **Margin, kernel, support vectors**: the ingredients of an SVM.
- **Activation, loss, gradient descent, backpropagation**: how a neural network
  learns.
- **Convolutional filter**: a reusable local-pattern detector in a CNN.
- **Attention**: the mechanism letting a transformer weigh all positions.

## Further reading

- Hastie, Tibshirani, Friedman, *The Elements of Statistical Learning* (free
  PDF) for the classical methods and a fuller treatment of tree induction.
- The scikit-learn user guide for practical, example-driven explanations.
- A review of machine learning in analytical chemistry / mass spectrometry, to
  be assigned, for domain context (see Part 4).
