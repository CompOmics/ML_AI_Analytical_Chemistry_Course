# Foundations: from measurements to learned predictions

These notes follow the Foundations lectures across days 1 and 2. They introduce the ideas needed to interpret the Strawberry and Tox21 practicals without having to write a program. Evaluation develops model comparison in more detail; sequence models and foundation models are covered in the LLM Tools notes.

## Presentations and practicals

| Material | Main ideas |
|---|---|
| [Introduction](../slides/1_1_introduction.pptx) | Experience, task, performance and generalisation; different data and prediction tasks |
| [Decision trees](../slides/1_1a_decision_trees.pptx) | Binary representation, entropy, information gain and learning tree rules |
| [Regression](../slides/1_2_regression.pptx) | Linear models, parameters, loss, gradient descent and polynomial features |
| [Logistic regression](../slides/1_3_logistic_regression.pptx) | Binary classification, sigmoid output and classification loss |
| [Neural networks](../slides/1_4_Neural%20networks.pptx) | Layers, activations, backpropagation, batches and epochs |
| [Convolutional neural networks](../slides/1_5_convolutional-neural-networks-new.pptx) | Local patterns, shared filters and pooling |
| Strawberry practical: [student](../notebooks/TD1_strawberry_student.ipynb), [answers](../notebooks/TD1_strawberry_solution.ipynb) | Predict the recorded purée class from infrared measurements |
| Tox21 practical: [student](../notebooks/TD1_tox21_student.ipynb), [answers](../notebooks/TD1_tox21_solution.ipynb) | Predict an assay outcome, then reconstruct and propose molecular structures |

The Strawberry practical is worked through with the instructor. The corresponding Tox21 practical applies the ideas independently. Both supply their code; the exercises ask for explanations of the inputs, calculations, predictions and limitations.

## 1. What does learning mean?

Machine learning uses examples to adjust a model's behaviour for a specified task. The introductory presentation separates experience, task and performance: which data the model sees, what it should predict, and how success is measured. A useful model must also generalise, meaning that it applies what it learned to examples excluded from training. Reproducing the training answers is insufficient evidence of this ability.

Artificial intelligence is a broad field, machine learning is one approach within it, and deep learning uses neural networks with multiple processing layers. Neural networks have a historical connection to ideas about biological neurons, including the perceptron discussed in the introduction. Their units combine inputs and produce outputs, but modern networks are mathematical models rather than detailed simulations of a brain.

The task determines the target and the appropriate output. Classification predicts a category, such as Strawberry or NON-Strawberry. Regression predicts a number, such as a retention index. Unsupervised methods examine structure without using known targets to teach the prediction; the outlier detector in Applications is an example. Generating a candidate molecular structure is another task again: it should not be confused with measuring that molecule's properties.

## 2. Samples, features, targets and predictions

A sample is one example in the dataset. Features are the numerical inputs describing that example. A target is its recorded outcome, and a prediction is the model's proposed outcome. The target is available when training or checking a supervised model, but a new prediction must be made from inputs available before that target is known.

| Practical | One sample | Features used by the classifier | Target |
|---|---|---|---|
| Strawberry | One recorded fruit-purée spectrum | Eight averages of infrared signal windows | Strawberry or NON-Strawberry |
| Tox21 | One retained compound record | Eight calculated molecular descriptors | Active or Inactive in SR-MMP |

These distinctions prevent several common mistakes. A molecular descriptor is not an assay measurement, and a predicted class is not a newly observed experimental result. A source-record identifier helps trace an example but is not automatically a useful chemical feature. A large input value does not by itself imply high toxicity or a high analyte concentration.

A feature representation retains some information and discards other information. Averaging an infrared window keeps its broad signal level but can lose a narrow peak. Molecular weight and ring counts summarise aspects of a structure but do not describe every bond arrangement. A model cannot recover distinctions that its inputs have removed simply by becoming more complicated.

## 3. Linear regression: learning contributions from inputs

A simple linear model predicts a numerical target with a straight line:

`predicted target = intercept + slope × feature`

The slope and intercept are parameters: numbers learned during fitting. With several features, the prediction adds one weighted contribution per feature. For example, a retention-index model can assign different contributions to sequence length and amino-acid counts. The learned coefficients describe the fitted relationship for the chosen inputs; they do not automatically establish a chemical mechanism.

A loss function measures disagreement between predictions and recorded targets. Mean squared error averages squared prediction errors, so large errors contribute disproportionately. An illustrative prediction of 12 for a target of 10 contributes a squared error of 4. Fitting seeks parameters that reduce the chosen training loss, rather than parameters that merely produce a visually attractive line.

Gradient descent repeatedly adjusts parameters in a direction that reduces the loss locally. The learning rate controls the size of each adjustment. Very large steps can make training unstable; very small steps can make progress slow. The fitted parameters and the learning rate have different roles: parameters are learned values, whereas the learning rate is a training setting.

A straight-line model can miss a curved relationship. The regression presentation introduces polynomial transformations, such as adding a squared feature. The model can then describe curvature even though it remains linear in its coefficients. Greater flexibility can improve training fit while also making the model more sensitive to accidental details, which motivates Evaluation.

## 4. Logistic regression: from a score to a class

A binary classifier needs a way to distinguish two outcomes. Logistic regression first calculates a weighted score and then maps it through a sigmoid function to an output between zero and one. A decision threshold turns that output into a class. The threshold and the output score should be distinguished from accuracy, which summarises correctness across many examples with known targets.

Binary cross-entropy is a loss suited to this task. It penalises a confident wrong prediction especially strongly. Confidence alone is not penalised: a high score for the correct class has a small loss, while a high score for the wrong class has a large loss. This explains the classification-loss curves in the presentation more precisely than saying that the model should avoid certainty in all circumstances.

An output of 0.9 is a model estimate for one example, not a guarantee that this example is correct. Whether such scores correspond to observed frequencies is a separate calibration question. In the practicals, the main checks are accuracy and the different kinds of mistakes, rather than probability calibration.

## 5. A small tree as a readable first model

A decision tree sorts training examples into smaller groups by asking questions about features. At a node, it might ask whether B6 is at or below a learned cut-off. A new sample follows the same sequence of questions until it reaches a final group, called a leaf. That leaf supplies the predicted class using the training examples that reached it.

The decision-tree presentation introduces entropy as a measure of uncertainty in the class proportions. A group containing only one class has entropy zero; a more evenly mixed group has higher entropy. Information gain measures how much a split reduces this uncertainty, using the sizes of the resulting groups to weight their entropies. The lecture uses this idea to explain how a tree chooses useful questions.

The Foundations trees have `max_depth=2`, allowing at most two decisions along a route. The fitting procedure learns the feature choices and cut-offs; the user supplies the depth limit. The plotted tree makes this distinction visible. Following one route explains the model's decision, although a learned cut-off does not by itself establish a chemical cause. Evaluation revisits split quality using Gini impurity and examines what happens when depth restrictions are removed. The supplied notebook trees use Gini impurity; entropy provides another way to measure how mixed a group is.

## 6. Neural networks: combining learned transformations

A neural-network unit forms a weighted sum of inputs, adds an offset, and applies an activation function. A layer contains several units, and the next layer uses their outputs as its inputs. Hidden layers therefore construct internal numerical representations rather than requiring every useful combination of features to be specified in advance.

Nonlinear activations are essential to this flexibility. Stacking linear transformations alone still produces a linear transformation. With nonlinear activations, a network can represent more complex boundaries and curved relationships. A deeper network can express more complicated patterns, but additional layers do not guarantee better predictions on new samples.

Training has a forward calculation and a backward calculation. The forward pass produces predictions and a loss. Backpropagation calculates how the loss depends on the parameters, and an optimiser uses these gradients to update the weights and offsets. An epoch is one pass through the training data; a mini-batch is a smaller group used for one update. Early stopping uses validation performance to decide when to stop, rather than repeatedly checking test performance.

The Strawberry practical uses eight inputs and one hidden layer with four neurons. Its scaler learns feature means and spreads from training samples only, then applies the same transformation to test samples. This keeps numerical scales comparable without allowing the test group to set the transformation. The tree uses the unscaled window means, so the two models' preparation differs even though their sample groups match.

## 7. Convolution: learning local patterns

A convolutional neural network (CNN) applies a small filter at many positions in an ordered input. The same learned weights examine neighbouring pixels in an image or neighbouring signals in a spectrum. The resulting feature map records where a local pattern produces a strong response. Further layers can combine these responses into more complex patterns.

Weight sharing lets one filter recognise a pattern in different positions without learning a separate detector everywhere. Convolution preserves the way a pattern's response moves when the input shifts; pooling can reduce sensitivity to small changes in position. Neither operation guarantees complete invariance to every translation, rotation or change in measurement conditions.

The presentation distinguishes image classification, object detection, segmentation and tracking. These tasks produce different outputs: an image class, a location, pixel-level regions, or identities followed across frames. The Strawberry CNN appears in Evaluation, where it receives the full ordered spectrum rather than the eight fixed window means. Its learned filters and those eight windows are different representations.

## 8. Reading the Strawberry practical

The original table contains 983 spectra, each with 235 measured wavenumbers. Its layout differs from the model table: targets occupy the first row and samples occupy columns. The notebook separates the targets, converts the numerical part once, and transposes the spectra so each sample occupies one row. A preview and two plotted spectra connect the table to the underlying measurement.

Two records have identical numerical spectra but opposite targets. Both are excluded because the file cannot establish which target is correct, leaving 981 observations. The notebook then calculates eight fixed window means and keeps 784 observations for training and 197 for testing. The model predicts the recorded class; NON-Strawberry includes both other fruit purées and adulterated mixtures without identifying each adulterant or its concentration.

Accuracy is the fraction of predictions matching the recorded targets. An accuracy of 0.90 means 90% correct classifications in the evaluated group. The constant NON-Strawberry rule provides a comparison because this is the larger class. In the confusion matrix, rows are recorded targets and columns are predictions. A NON-Strawberry sample predicted Strawberry is a false acceptance; the reverse is a false rejection. Their practical consequences differ even if they contribute equally to ordinary accuracy.

## 9. Reading the Tox21 practical

Tox21 is a programme studying chemical responses in laboratory assays. The practical selects SR-MMP, a stress-response assay concerning mitochondrial membrane potential. The target describes whether an active response was recorded in that assay under its experimental conditions. Active and Inactive are not judgements of overall human toxicity or safety.

Of 7,831 source records, 5,810 have an SR-MMP result and a structure string. Six structures cannot be read with the supplied tools, leaving 5,804 records. Missing outcomes remain unknown rather than becoming Inactive. The features summarise molecular weight, predicted LogP, hydrogen-bond donors and acceptors, polar surface area, rotatable bonds, aromatic rings and heavy atoms. They are calculated from structure rather than measured in the assay.

Inactive compounds are more common than Active compounds. Class balancing gives each rarer Active example greater importance during learning so both classes have equal total training weight. It does not create extra compounds or change ordinary accuracy into balanced accuracy. An always-Inactive rule can have high accuracy while finding no Active compounds, so the confusion matrix remains necessary.

### Reconstruction and molecular proposals

The second part uses pretrained CDDD to encode a molecular structure into 512 latent values and decode it back into a structure description. The encoder weights were learned during pretraining; the 512 values are outputs calculated for the selected molecule, rather than 512 stored model weights. Individual latent values do not have named units such as molecular weight. The colour grid displays their pattern; neighbouring squares do not represent neighbouring atoms, and its colours do not indicate toxicity.

The notebook reconstructs a chosen starting molecule, perturbs its latent representation and decodes proposed structures. Invalid strings, repeated reconstructions and distinct changed candidates are counted separately. A readable structure is not proof of stability, synthetic feasibility or scientific novelty. Absence from the downloaded Tox21 file only establishes absence from that particular reference comparison.

The candidate structures are then passed to the existing classifier after recalculating the same eight descriptors. The classifier does not receive the 512 latent values and is not retrained on the proposals. Because the candidates have no measured assay targets here, their predictions cannot produce a new accuracy estimate. Structural similarity also does not establish equal activity.

The slides introduce variational autoencoders through [Gómez-Bombarelli et al. (2018)](https://doi.org/10.1021/acscentsci.7b00572). The practical instead uses the translation-based molecular representation described by [Winter et al. (2019)](https://doi.org/10.1039/C8SC04175J). The two share an encoding-and-decoding idea but are not the same model or training objective.

## 10. Connecting to the following topics

The Data lecture examines data quality, lifecycle, governance and the software, storage and computing infrastructure that support an analysis. The Foundations practicals introduce the specific feature representations and preparation steps. [Evaluation](../../03_Evaluation/notes/Part3_Evaluation_notes.md) introduces a validation group, stronger overfitting demonstrations and comparison with a CNN. [Applications](../../04_Applications/notes/Part4_Applications_notes.md) reuses the features but changes the question from predicting targets to identifying unusual patterns.

Useful revision questions are whether a quantity is an input, target, learned parameter or chosen setting; which records taught the model; and what evidence would support its use on a new sample. Being able to answer these questions matters more than memorising Python syntax.

Dataset background: [Strawberry](../../datasets/strawberry/README.md) and [Tox21](../../datasets/tox21/README.md).
