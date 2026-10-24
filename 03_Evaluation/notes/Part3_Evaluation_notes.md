# Evaluation: deciding which predictions to trust

A model's training score describes how well it fits examples already used for learning. Evaluation asks a different question: how well will a fixed prediction procedure work on examples excluded from its development? These notes follow the lectures on regularisation, decision trees and ensembles, then connect them to the Strawberry and Tox21 comparisons.

## Presentations and practicals

| Material | Main ideas |
|---|---|
| [Regularisation and failure modes](../slides/3_1_regularization.pptx) | Underfitting, overfitting, bias, distribution change, leakage and validation |
| [Decision trees](../slides/3_2_DecisionTrees.pptx) | Learning splits, class impurity and tree structure, illustrated with Iris |
| [Ensemble learning](../slides/3_3_ensemble_learning.pptx) | Bagging, random forests, boosting and the bias–variance intuition |
| Strawberry Evaluation: [student](../notebooks/TD2_strawberry_student.ipynb), [answers](../notebooks/TD2_strawberry_solution.ipynb) | Compare trees, a forest and a full-spectrum CNN |
| Tox21 Evaluation: [student](../notebooks/TD2_tox21_student.ipynb), [answers](../notebooks/TD2_tox21_solution.ipynb) | Compare assay classifiers and inspect missed Active results |

The practicals start with a brief recap of Foundations. They reuse its prepared data and test records to make the teaching sequence comparable. That reuse is explicitly a classroom demonstration, rather than a new independent assessment each time.

## 1. Three groups with different jobs

Training examples determine learned parameters, such as tree cut-offs or network weights. Validation examples guide choices, such as model type, maximum depth or training duration. Test examples assess the final choice after those decisions are fixed. If test outcomes guide another round of choices, the examples have become part of development and no longer provide an untouched final check.

| Practical | Training | Validation | Test |
|---|---:|---:|---:|
| Strawberry Evaluation | 588 | 196 | 197 |
| Tox21 Evaluation | 3,482 | 1,161 | 1,161 |

The original Foundations training group is divided to create training and validation groups, while the test membership stays the same. All candidate models within one comparison use the same groups. This makes score differences easier to interpret because an easier or harder set of samples is not being substituted for one model. Class stratification preserves approximate class proportions, but it does not separate batches, suppliers or related chemical structures.

Cross-validation repeats the training/validation comparison across several partitions. In five-fold cross-validation, each fold acts as validation once while the remaining folds provide training data. Learned preprocessing must be refitted inside each training fold. The lectures explain cross-validation; the current Strawberry and Tox21 practicals use a single fixed validation group rather than implementing it. Results from that group should not be described as cross-validated estimates.

## 2. Five failure modes

| Failure mode | What happens | Analytical-chemistry illustration | Useful evidence |
|---|---|---|---|
| Underfitting | The model or representation misses a useful relationship | A straight calibration line misses a curved response | Poor training and validation performance relative to a useful baseline |
| Overfitting | The model follows accidental training details | A deep tree isolates individual noisy spectra | Training improves much more than validation |
| Bias in the data | Some relevant conditions have poor or misleading coverage | Most authentic samples come from one supplier | Coverage and error rates examined by relevant group |
| Out of distribution | Intended inputs differ from those studied | A model is applied to a new chemical family or LC method | Comparison of training conditions with intended use |
| Information leakage | Information from held-aside outcomes enters development | The same compound measurement is present in training and testing | Audit of sampling units, overlapping records and preparation |

These mechanisms can occur together. A supplier-dependent classifier can overfit acquisition artefacts and then fail on a new supplier. A leakage-contaminated test can conceal that weakness by making performance appear better than it is. A large score by itself therefore cannot diagnose why the model appears successful.

### Underfitting and overfitting

Underfitting occurs when the available representation or model cannot capture an important pattern. Training and validation may both be poor, although model flexibility is not the only possible explanation: incorrect targets or unsuitable features can also limit both scores. Adding layers or depth cannot recover information that has already been discarded from the inputs.

Overfitting occurs when changes improve training fit without comparable improvement on excluded examples. In an accuracy plot, training rises while validation levels off or falls. In an error plot, training error falls while validation error stops improving or increases. The direction of the vertical axis matters, and a widening gap is a warning rather than an explanation of the underlying experimental cause.

The bias–variance discussion uses another meaning of bias. Model bias describes systematic limitations from assumptions that are too restrictive; variance describes sensitivity to the particular training examples. Bias in sampling concerns which examples or conditions are represented. The concepts are related but should not be treated as interchangeable definitions. Better coverage, suitable features and appropriate regularisation address different parts of the problem.

### Distribution change

Interpolation predicts among conditions represented in the data. Extrapolation extends beyond them, for example to much longer peptides, a new molecular scaffold or a different gradient. A point can lie inside the range of every individual descriptor yet have an unfamiliar combination or structure. An apparently ordinary two-dimensional scatter plot does not establish that all relevant patterns are represented.

A random chemical split may be appropriate for some intended populations but insufficient for claims about entirely new chemical families. Similarly, repeated spectra from one specimen do not establish performance on new specimens. The evaluation design should follow the scientific claim rather than treating a random row split as universally correct.

### Information leakage

The clearest overlap example is testing on a measurement already used for training. Related examples require care too: replicate injections of the same compound can cross an ordinary row split, allowing the model to recognise familiar chemistry. Keeping all replicates together by compound prevents this particular overlap when the goal is prediction for new compounds.

Very similar molecules across groups are not automatically leakage in every study. They do, however, make a claim about unfamiliar scaffolds harder to support. Grouping by chemical family tests that stronger claim more directly. The notes therefore distinguish literal duplicate overlap from a mismatch between the split and the intended novelty of future inputs.

Leakage also occurs through preparation and selection. Scaling on the whole table uses information from the held-aside distribution; choosing features using all targets uses held-aside outcomes even more directly. Repeatedly choosing the best test score lets the test guide the analysis. These procedures differ in how much information they expose, but all compromise the intended separation of development and final evaluation.

## 3. How a tree chooses questions

A classification tree looks for a feature and threshold that divide training examples into groups with less mixed targets. Impurity measures this mixture. A pure group contains one class and has impurity zero. For two equally common classes, Gini impurity is 0.5 and entropy is 1 bit. Both measures favour class separation, although their numerical scales differ.

For class proportions `p₁, p₂, …`, Gini impurity is `1 − sum(p²)`. A candidate split is scored using the child impurities, weighted by the number of examples in each child. A tiny pure group should not receive the same importance as a very large mixed group. The algorithm selects a useful local split and repeats the process in the resulting groups; it does not search every possible complete tree.

Tree depth limits the number of questions along a route. A minimum leaf size limits how small a final training group can become. Removing the depth limit while allowing one-sample leaves lets the tree fit extremely specific examples. In the current practicals, the unrestricted trees already use the default minimum leaf size of one, so a larger minimum leaf size is not holding back the overfitting demonstration.

## 4. Regularisation limits unnecessary flexibility

Regularisation changes the training objective or model structure to discourage overly specific solutions. For linear models, an L2 penalty adds a term based on squared coefficient sizes to the prediction loss. The model then balances fitting training targets against keeping coefficients from becoming unnecessarily large. Ridge regression in the instructor's peptide example illustrates this idea later in the course.

The penalty strength is a setting to choose during development. Too little restriction can leave the model sensitive to noise; too much can prevent it from fitting useful relationships. A depth limit plays a related structural role for trees. These controls can help generalisation but do not fix unrepresentative sampling, missing chemistry or leakage by themselves.

## 5. Why combine trees?

A random forest builds varied trees from random samples of the training examples and random feature subsets considered at each split. Sampling with replacement means some examples can occur more than once in one tree's training sample. The variation matters: combining identical trees would repeat the same errors rather than reduce their influence.

For the supplied classifiers, each tree supplies class-support estimates and the forest averages them. If three trees give Strawberry support of 0.8, 0.6 and 0.4, their average is 0.6 and favours Strawberry. That number concerns one prediction; it is not the forest's accuracy across a validation dataset. The forest still needs to be evaluated on excluded examples, even if it fits training data almost perfectly.

Bagging combines models trained on resampled datasets to reduce sensitivity to a particular sample. Boosting builds models sequentially so later models address shortcomings of the current ensemble. AdaBoost changes the importance given to examples, whereas gradient boosting adds models that reduce the current loss, often described through residuals or gradients. These are lecture concepts; the current practicals fit a random forest, not a boosting model. Neither approach guarantees that adding more models improves validation performance.

## 6. The Strawberry comparison

The small tree, unrestricted tree and random forest all receive the eight fixed spectral-window means. The small CNN instead receives the 235 measured positions in their original order. It learns eight filters, each spanning five neighbouring signals, then pools and combines their responses. Its eight filters are learned local patterns, not the eight predefined windows used by the trees.

All models use the same sample groups, but the CNN has access to more spectral detail. A difference in score therefore reflects both algorithm and representation, rather than a controlled comparison of algorithms on identical feature inputs. The full-spectrum scaler learns from training spectra only. The fixed 30-epoch CNN fit is assessed afterwards on validation data; the notebook does not implement validation-based early stopping for this run.

Validation accuracy selects a model, and the code then evaluates that fixed choice on test records. A constant NON-Strawberry rule provides a simple comparison. The confusion matrix separates false acceptances from false rejections, because passing a sample inconsistent with its claim and unnecessarily flagging an authentic product have different consequences. The dataset cannot identify a specific adulterant or establish product purity.

## 7. The Tox21 comparison

The three classifiers use the same eight structure-derived descriptors and the same class-balancing rule. Each rarer Active compound receives more training importance so that the two classes have equal total influence during fitting. The displayed ordinary accuracy still counts each evaluated record equally. It is not balanced accuracy, and it can favour a model that misses an important fraction of Active outcomes.

The teaching selection rule is highest validation accuracy. A laboratory screening objective would also need to consider missed Active outcomes, false alarms and the costs of follow-up. An always-Inactive rule provides a particularly useful warning: it can be correct for many records while detecting no Active compounds. The chosen model's confusion matrix should therefore be read alongside its overall score.

## 8. Reading the depth curves honestly

Both Evaluation notebooks illustrate depths 1 through 30 after the original model choice and test check are finished. The training and test curves demonstrate how increasingly specific rules behave on the same teaching split. Choosing a new depth at the test curve's highest point would turn that plot into model selection and require further untouched data for a final check.

In the supplied Strawberry example, the tree reaches 100% training accuracy by depth 18. The Tox21 unrestricted tree reaches roughly 99.7% at depth 25 because some different compounds share identical descriptor values and have opposite targets. No split on those eight inputs can distinguish such records. Near-perfect training fit still does not establish reliable performance on new examples.

The Tox21 training accuracy need not rise at every depth: the fitting criterion uses class weights, while ordinary accuracy counts compounds equally. Read the overall pattern rather than assuming each downward step is a programming error. The plots also use zoomed vertical axes; small numerical differences can appear visually large. Check the stated accuracy values as well as the apparent distances.

## 9. What an evaluation can support

A single split provides one estimate for one sample population and procedure. With 197 Strawberry test records, changing one correct prediction changes accuracy by about 0.005. Small score differences can therefore concern only a few observations. Reading the errors, sample counts and design is more informative than declaring a universal winner from a short ranking.

A defensible conclusion identifies the target, the excluded evaluation group, the main error types and the populations still untested. The next topic, [Applications](../../04_Applications/notes/Part4_Applications_notes.md), changes the question from predicting a target to prioritising unusual records for review. The [LLM project](../../05_LLM_Tools/notes/Part5_LLM_notes.md) asks students to design their own comparison while preserving these distinctions.

Dataset details and split provenance: [Strawberry](../../datasets/strawberry/README.md) and [Tox21](../../datasets/tox21/README.md). Definitions of the implemented estimators are available in the [scikit-learn tree documentation](https://scikit-learn.org/stable/modules/tree.html) and [ensemble documentation](https://scikit-learn.org/stable/modules/ensemble.html).
