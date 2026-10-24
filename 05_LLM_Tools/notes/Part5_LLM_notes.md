# LLM tools: sequence models and responsible model building

This topic connects sequence modelling and pretrained representations to the use of large language models (LLMs) as research assistants. The practical asks students to design a peptide retention-index predictor with an LLM's help. Students choose the representation, model and improvements, then explain how they checked the result.

## Presentations and practical

| Material | Main ideas |
|---|---|
| [Recurrent neural networks and transformers](../slides/5_1_recurrent-neural-networks-transformers.pptx) | Ordered data, numerical encodings, memory and attention |
| [Foundation models](../slides/5_2_foundation-models.pptx) | Pretraining, self-supervision and fine-tuning |
| [LLMs as research tools](../slides/Part5_LLM_slides.pptx) | Useful tasks, hallucinations, prompts and verification |
| Peptide project: [student notebook](../notebooks/TD4_peptide_RT_student.ipynb), [instructor example](../notebooks/TD4_peptide_RT_solution.ipynb) | Design, build and assess a model using student-written prompts |

The student notebook supplies one cell to load and preview the data and two empty code workspaces. Students can add cells as their analysis develops. The instructor notebook contains one worked implementation for discussion, rather than a required algorithm or a score every student should reproduce.

## 1. Sequence order carries information

A sequence is an ordered collection of elements. DNA, peptide strings, time-dependent signals and text all have meaningful order, although their elements and scientific interpretation differ. Rearranging the same words can change a sentence's meaning. Rearranging the same amino acids can change a peptide's behaviour even if its overall composition stays the same.

A model needs a numerical representation of those elements. The lectures compare manual features, one-hot encoding and learned embeddings. The choice affects what information is available to the prediction procedure. Calling every representation a list of numbers is technically true but misses the important question of which distinctions those numbers retain.

| Representation | Intuition | Consequence |
|---|---|---|
| Manual features | Calculate properties such as counts or selected chemical summaries | Easy to inspect, but can discard position and context |
| One-hot encoding | Use a separate indicator for each possible symbol | Identifies symbols without inventing a numerical order between them |
| Learned embedding | Represent symbols or sequences by values learned during training | Can capture useful similarities, but depends on the model and training objective |

One-hot encodings can retain sequence order when kept position by position; summing their counts removes it. Embeddings are not automatically better chemical features, and similarity in an embedding does not prove identical experimental behaviour. In Part 5, students should be able to explain the information retained by their chosen representation.

## 2. Recurrent networks use a running state

A recurrent neural network (RNN) processes a sequence one element at a time. After each element, it updates an internal hidden state using the current input and the previous state. This state acts as a learned summary of what has been read so far. The same recurrent calculation is reused along the sequence, allowing inputs of different lengths.

The network can produce a prediction at each step or one prediction for the whole sequence. Predicting a retention index from a peptide is a sequence-to-one task; producing an output associated with each residue is a different output arrangement. The type of target determines which form is appropriate.

A basic RNN can struggle to preserve useful information across long sequences. Long short-term memory networks (LSTMs) and gated recurrent units (GRUs) use gates to control which information is retained or updated. These mechanisms improve the handling of longer dependencies but do not guarantee that every distant relationship is learned correctly.

## 3. Attention connects relevant positions

Attention calculates weighted combinations of representations from different positions. A position can therefore draw on relevant context rather than relying only on a single running summary. In a transformer, attention works together with other transformations and information about position to model relationships across the input. The order still needs to be represented; attention alone does not recover it from an unordered collection.

The available context depends on the task and attention mask. A causal text generator predicts a token using the preceding context rather than seeing future tokens in that same prediction step. A masked-token model can use surrounding positions that remain visible. Saying that every transformer always sees every part of a complete sequence would therefore be misleading.

The sequence lectures motivate these ideas using words, genomes and proteins. They do not require students to train a transformer in the retention project. A small model with an understandable representation is an appropriate starting point when the scientific question and available data support it.

## 4. Pretraining and fine-tuning have different purposes

Pretraining learns reusable patterns from a large collection of examples. A self-supervised task obtains its training target from the data itself, for example by hiding a symbol and asking the model to predict it. This still provides a learning signal, but does not require a person to annotate a separate outcome for every example. Pretraining can also use other objectives, including supervised ones.

Fine-tuning adapts learned parameters to a more specific task using relevant examples. A broadly pretrained representation can reduce the amount of task-specific data needed, but the benefit depends on how well the earlier learning transfers. A large pretrained model does not remove the need for evaluation on data excluded from the adaptation procedure.

The foundation-model presentation illustrates transfer from general images to skin-lesion classification and from large transcriptomic collections to specific biological tasks. These examples explain reuse of learned representations, rather than establishing that every pretrained model is equally general. Domain coverage and the downstream objective still matter.

Prompting a chat assistant is different from fine-tuning the prediction model. A prompt supplies context and instructions for an interaction; it does not by itself update the assistant's stored parameters. In the practical, the assistant helps write code, while the separate retention predictor learns from the peptide training targets. The LLM's fluent explanation is not a substitute for that predictor's measured validation performance.

## 5. Why fluent answers can be wrong

An LLM produces text according to learned patterns and the supplied context. Its output can be useful for explanation, drafting or code generation without being guaranteed correct. A hallucination is a plausible-looking statement, reference or result that lacks the required support. Confident wording is not a verification method, and asking the same assistant to confirm an answer does not provide independent evidence.

The lecture uses fabricated references and code errors as examples. A citation can have a realistic title and DOI format while failing to resolve to the claimed paper. A numerical result can be formatted correctly even though its calculation or units are wrong. Important claims therefore need checks against the data, executable calculations or the actual source.

A pretrained model can also lack information about a new tool version or an experimental context absent from its input. Supplying a clear error message or a few actual table rows can help repair a response. It does not ensure that the revised code answers the intended scientific question, so a successful run still needs interpretation.

## 6. Prompting as a sequence of decisions

A useful prompt gives the assistant enough context to understand the task, the available data and the requested output. For the retention project, that includes the table name, the meanings of `sequence` and `irt`, the numerical target, the CPU setting and the student's level of programming experience. Stating constraints helps avoid unnecessary dependencies or an unsuitable project scale.

Begin by asking for options and their trade-offs before requesting implementation. Students then choose an approach they can explain. Requesting a whole analysis at once can obscure decisions about representation, splitting, metrics and model selection. Smaller requests make those decisions easier to inspect and make failures easier to locate.

| Stage | A useful request | Evidence to inspect |
|---|---|---|
| Planning | Suggest understandable approaches and explain the choices | Whether the proposal matches the scientific target and available data |
| Features | Explain how the chosen representation handles a short example | An independently worked example and the resulting feature values |
| Training | Generate code using only the designated training inputs | Which data are passed to preparation and fitting |
| Comparison | Report training and validation results for the same split | The actual scores, baseline and sample groups |
| Repair | Address a specific error or incorrect behaviour | Whether the repair fixes the issue without changing the question |
| Interpretation | Explain the supplied results and their limitations | Numerical claims, units and consistency with the plots |

The exact prompts belong to the students. The notebook's starter is a way to begin a discussion, not a required wording or a specification of particular algorithms. An unhelpful first response can lead to a better question, and a failed attempted improvement can still provide an informative comparison.

## 7. The peptide-retention project

The data-loading cell selects 6,000 distinct sequences from a fixed DLOmix example file containing 34,000 records. The target is experimentally derived iRT, a calibrated retention index without time units. Negative values are possible, and an iRT of 50 does not mean 50 minutes. The file does not include run identifiers, detailed LC conditions or modification annotations.

Students define their own representation and compare a simple baseline with at least one learned model. A baseline that predicts the same value for every peptide checks how much useful information the sequence-based model adds. Its constant should be determined from training data, rather than chosen using test targets. The choice of model should follow the intended task and be supported by results, rather than by an assistant's claim that a particular architecture is more advanced.

The analysis needs separate training, validation and test groups. Identical sequences should not cross groups, and the same groups should be kept when comparing approaches. Preparation settings and model parameters are learned from training examples. Validation helps assess a deliberate change; the final test checks the fixed decision. Students choose and document their split rather than being required to copy the partition in the instructor example.

Mean absolute error is one useful regression metric. For a target of 50 and a prediction of 42, the absolute error is 8; MAE averages such distances. It has the target's units, so here it is expressed in iRT units. It is not a percentage of correct classes, a maximum error bound or evidence that every prediction falls within that distance.

A predicted-versus-recorded plot makes errors visible. Points on the diagonal match their recorded targets; points away from it reveal deviations that an average can hide. Examining large errors can suggest questions about the representation, unusual sequences or recorded targets, but cannot identify the cause automatically. A prediction for a new sequence without a measured target cannot establish its accuracy.

## 8. What verification should demonstrate

Verification should connect a claim to evidence independent of the assistant's assertion. If a feature function counts residues, a hand-worked short peptide provides a known answer. If code uses a split, inspect overlap of the relevant identifiers and the arguments used for fitting. If a result is reported, trace it to the actual prediction table and calculation rather than a value written into a sentence by the LLM.

Passing a small check establishes a specific property, not correctness of the entire workflow. A model can return the right number of predictions while having been trained on test targets. Code can avoid duplicate sequences while still evaluating very similar peptides on both sides. Combining checks with scientific reasoning is therefore necessary, especially when grouping metadata are absent.

A proposed revision should be compared using validation results. If it performs worse, retain that result and explain the decision to keep the earlier model or baseline. Using the final test to choose another revision changes the role of that test. Further model development then needs untouched evaluation data rather than presenting the reused test score as independent confirmation.

## 9. Other research uses and responsibilities

For literature work, an LLM can suggest search terms, explain terminology or help compare ideas, but a reference should be checked in the original publication or a reliable bibliographic record. Confirm what the source actually measured and which conditions supported the claim. A summary can omit an important denominator or limitation even when its individual sentences sound reasonable.

For documents, the assistant can draft, restructure or reformat text, while the author checks every scientific statement, number and instrument setting. For data analysis, the same principle applies to executable code and its outputs. Generated content should remain traceable to its inputs and to the decisions made by the researcher.

The practical permits LLM assistance and requires an honest record of it. The lecture distinguishes this permitted use from the prohibition on generative AI and connected devices in the written examination. The current [course grading information](../../README.md#grading) assigns the continuous-assessment component to the three quizzes; the day 5 notebook is the practical activity.

## 10. A finished project tells a coherent story

The completed student notebook should contain its scientific goal, chosen representation, working analysis, validation comparison, fixed test result and plot, answers to the five interpretation questions, and a short prompt log. The log records important prompts, what was accepted or changed, and the evidence used to check it. If assistance came from the instructor rather than an actual chat interaction, it should be recorded that way.

A suitable conclusion states what worked on this dataset and which intended uses remain untested. Count-based features can lose residue order; other representations have different limitations. The available split does not establish performance for another LC method, unrepresented modifications or an unrelated peptide population. These boundaries connect the project back to [Data](../../02_Data/notes/Part2_Data_notes.md) and [Evaluation](../../03_Evaluation/notes/Part3_Evaluation_notes.md).

Dataset provenance and reuse information are recorded in the [peptide-data documentation](../../datasets/peptide_rt/README.md). The instructor's implementation is one possible model-building route. Students' work should be assessed through the clarity of their choices, the quality of their checks and the evidence supporting their conclusions.
