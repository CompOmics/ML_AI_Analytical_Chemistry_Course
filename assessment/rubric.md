# Assessed project: grading rubric

Total: 20 points. Marked on the notebook, the report, and the LLM-use appendix.

| Criterion | Points | What earns full marks |
|---|---:|---|
| Leakage-free pipeline | 6 | Correct, justified split (by molecule/group where needed); preprocessing and feature selection inside cross-validation; no test information in training. |
| Sound evaluation and honest metrics | 5 | Appropriate metric; cross-validation; at least one uncertainty estimate; results reported once on unseen data, not the best of many tries. |
| Interpretation and error analysis | 3 | Feature importance or error analysis that makes chemical sense and is discussed critically. |
| Quality of LLM use (appendix) | 4 | Prompts recorded; model errors identified; each output verified independently; changes documented. |
| Clarity and reproducibility | 2 | Notebook runs top to bottom; data and licence stated; clear, concise writing. |

## Indicative bands

- 16-20: leakage-free, honestly evaluated, well interpreted, LLM use documented and verified.
- 12-15: mostly correct with a minor evaluation or documentation gap.
- 10-11: works but with a real weakness (e.g. weak split justification or thin appendix).
- below 10: a leakage or evaluation error that invalidates the reported result, or missing appendix.

## Notes for markers

- A genuine, well-diagnosed negative result (an honest "this did not work, and
  here is why") can score highly; an inflated positive result from leakage cannot.
- The LLM-use appendix is the integrity safeguard: marks here require evidence of
  verification, not just a list of prompts.
