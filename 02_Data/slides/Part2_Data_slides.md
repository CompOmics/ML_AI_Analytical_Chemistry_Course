# Part 2: Data - origin, rights, and quality (slide deck)

Markdown equivalent of `Part2_Data_slides.pptx` (12 slides). One section per slide.

---

## Slide 1 — Title
**Machine Learning and AI for Analytical Chemistry**
Part 2: Data - origin, rights, and quality. M2 Sciences analytiques · 2 h lectures.

## Slide 2 — Roadmap for Part 2
1. **Data for training** — where data come from, their characteristics, licensing of code and data, and intellectual property.
2. **Levels and quality** — levels of information, how AI hides the base, poisoning the well, FAIR stewardship, model documentation.

## Slide 3 — Where the data come from
- **Your own lab** — instruments you control: known conditions, limited coverage.
- **Public repositories** — depositions and libraries: broad coverage, varied quality and licences.
- **Literature** — papers and supplementary data: useful but often poorly structured.
- **Simulated / augmented** — fills gaps, risks unrealistic patterns.

> Example: a retention-time model trained on your lab, on ProteomeXchange/PRIDE, or on the NIST library covers different compounds and conditions.

## Slide 4 — Characteristics to check first
- **Coverage & balance** — are all classes/ranges represented, or is one dominant?
- **Label quality** — pipeline labels carry the pipeline's errors.
- **Batch & instrument effects** — one instrument/operator/season can leak into the model.
- **Metadata** — acquisition conditions must be recorded, or data cannot be reused.

> Example: MS/MS spectra from several instruments differ systematically; a model may learn the instrument, not the chemistry.

## Slide 5 — Licensing: code and data are separate

| | Permissive / open | Restrictive |
|---|---|---|
| **Code** | MIT, Apache-2.0 (broad reuse) | GPL (share-alike derivatives) |
| **Data** | CC0, CC-BY (use, attribute) | CC-BY-NC (no commercial use) |

**Credentials:** never hard-code API tokens; use environment variables or a config file kept out of version control.

> Example: a fragmentation model trained on CC-BY-NC spectra cannot be shipped commercially; the data licence propagates to the model.

## Slide 6 — Intellectual property and ownership
Beyond the licence, ask who is legally entitled to the data. Instrument data produced under a service contract, a collaboration, or industrial funding may belong to a party other than the person who ran the sample. Clarify ownership and consent before training a model that will be shared or published.

> Example: raw LC-MS files acquired for a paying client are usually the client's property; training a public model on them needs permission.

## Slide 7 — Section divider
**Levels and quality of information** — from raw signal to knowledge, and who keeps the base trustworthy.

## Slide 8 — Levels of information, and where AI looks
(Figure: a four-tier pyramid — raw spectra (mzML) → peaks/features → identifications → knowledge — with an arrow showing AI delivering the top directly.)

Data exist from raw signal to interpreted knowledge; each level is derived from the one below, losing detail. AI tools increasingly deliver the top directly, pushing the foundational data out of view. **If the model is wrong at the bottom, the error is invisible at the top, where the user looks.**

## Slide 9 — Data quality and "poisoning the well"
Shared foundational data are a single point of failure. Because models and downstream users all depend on the same source, an error at the source propagates everywhere; a mislabelled library entry is copied into every model and analysis that trusts it, and is hard to trace because the source looks authoritative.

> Example: one misannotated reference spectrum makes every tool that trusts the library repeat the same wrong identification.

## Slide 10 — Who maintains the base? FAIR stewardship
(Figure: the four FAIR pillars — Findable, Accessible, Interoperable, Reusable.)

Sustained curation is a real cost carried by repositories, consortia and standards bodies. FAIR data are Findable, Accessible, Interoperable and Reusable; persistent identifiers and standard formats make this practical.

> Example: ProteomeXchange/PRIDE give stable accessions; mzML/mzSpecLib give interoperability; a USI points to one exact spectrum.

## Slide 11 — Documenting models and datasets
**Model cards** — structured documentation that travels with a model: intended use, training data and its licence, evaluation, known limitations. Version both data and models for reproducibility.

**Why it matters** — a future user must know what a model learned from, what it is for, and where it breaks. Community resources such as ProteomicsML share documented models and datasets.

> Example: a published retention model with a model card stating training set, licence, column and error lets another lab judge fit before use.

## Slide 12 — Key takeaways
- A model is only as good, and as legal, as the data behind it.
- Check origin, balance, label quality, batch effects and metadata first.
- Code and data carry separate licences; data licences propagate to the model.
- AI can hide the foundational data, so errors at the base go unseen.
- FAIR stewardship and model cards keep the shared base trustworthy.
