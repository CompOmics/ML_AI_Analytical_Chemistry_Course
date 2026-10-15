# Part 5: LLMs as adaptive research tools

**Lecture and tutorial notes (3 h TD)**
Machine Learning and AI for Analytical Chemistry, M2 Sciences analytiques

These notes accompany the Part 5 slides and the TD4 notebook. Part 5 is hands-on:
the goal is that you can use a large language model (LLM) as a competent
assistant for scientific work, while staying in control of correctness and
within the rules. The assessed project (see the assessment folder) is introduced
and started in this session.

---

## 1. Principles and good practice (about 1 h)

### 1.1 What an LLM is, and is not

A large language model predicts plausible continuations of text. It is fluent and
broad, but it has no built-in notion of truth: it produces what is likely, not
what is verified. Treat it as a fast, knowledgeable, and sometimes confidently
wrong assistant, never as an authority.

### 1.2 Strengths and weaknesses

Strengths: drafting and rewriting text, explaining concepts, generating and
debugging code, translating between formats, and exploring an unfamiliar area
quickly. Weaknesses: it invents facts and references (hallucination), is
sensitive to how it is asked, can be subtly wrong in ways that look right, and
its knowledge has a cutoff and gaps.

> **Example.** Asked for the reference that introduced a method, an LLM may return
> a plausible-looking citation with a real author, a real journal, and a DOI that
> does not exist. The form is perfect; the fact is invented.

### 1.3 Hallucination and verification

Because the model can be wrong, every output that matters must be verified
against an independent source: run the code, check the reference exists, confirm
the number against the data. Build a habit of a verify loop: prompt, read the
draft critically, verify it, then iterate. The verification is your work; the
draft is the model's.

> **Example.** An LLM writes a function to compute a mass from a peptide sequence.
> Before trusting it, you test it on a peptide whose mass you know. If the test
> passes, you keep it; if not, you fix it. The test, not the fluency, earns your
> trust.

### 1.4 Prompt hygiene

The quality of the answer depends on the prompt. Good prompts give context, state
the goal precisely, supply examples, specify the desired format and length, and
ask for step-by-step reasoning when useful. Iterating on the prompt is normal.

> **Example.** "Write Python to read this CSV of m/z and intensity, find peaks
> above 5 percent of the base peak, and return them as a DataFrame sorted by
> intensity" yields usable code; "analyse my data" does not.

### 1.5 The boundary set by the fraud policy

The programme regulations treat unauthorised use of generative AI as a fraud
offence. In this course the rule is deliberately asymmetric and must be stated
clearly: LLM use is required and assessed in the project, and prohibited in the
terminal written exam. Inside the project, you must also document your LLM use (an
appendix of prompts and how you verified each output), which is both good
practice and the integrity safeguard.

---

## 2. Using LLMs for the work (about 2 h, hands-on)

### 2.1 Code generation

The most reliable scientific use of LLMs is generating code that you then run and
test. This covers scripts for data processing, analysis, and visualisation, and
sometimes whole small applications. The workflow is always the same: describe the
task precisely, get the code, run it, test it on a case with a known answer, and
iterate.

> **Example.** Generating a Colab cell that loads a chromatogram, baseline-
> corrects it, detects peaks, and plots them, then checking the detected peaks
> against a manual count on one file before trusting the script on the rest.

### 2.2 Literature and knowledge exploration

LLMs are useful for getting oriented in an unfamiliar area, summarising a
concept, or suggesting search terms and directions. They are not a citation
source: every reference must be confirmed in a real database.

> **Example.** Using an LLM to explain the difference between DDA and DIA
> acquisition and to suggest review articles to look for, then finding and
> reading those reviews in PubMed rather than citing the model.

### 2.3 Improvement, generation, and automation of documents

LLMs help draft, restructure, and tidy documents: reports, method sections,
figure captions, and repetitive text. The author remains responsible for the
content, including any claims and numbers.

> **Example.** Drafting the boilerplate of a methods section from bullet points,
> then checking every instrument setting and value against the actual experiment
> before submission.

### 2.4 The assessed project

The continuous-assessment project is introduced here and built on these skills.
You will produce a documented Colab notebook (data processing, analysis, and
visualisation) plus a short report, with an appendix recording your key prompts
and how you verified each output. Full details, options, and the rubric are in the
assessment folder.

---

## Key terms

- **Large language model (LLM)**: a model that predicts plausible text.
- **Hallucination**: a fluent but false output, often an invented reference.
- **Verify loop**: prompt, read critically, verify independently, iterate.
- **Prompt hygiene**: context, precise goal, examples, format, length.
- **LLM-use appendix**: documented prompts and verification, required in the project.
- **Fraud-policy boundary**: LLM use required in the project, banned in the exam.

## Further reading

- Anthropic prompt-engineering documentation for practical prompting technique.
- Your institution's regulations on generative AI and academic integrity.
- The assessment folder for the project brief, rubric, and template notebook.
