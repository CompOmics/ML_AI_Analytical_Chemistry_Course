# Part 2: Data - origin, rights, and quality

**Lecture notes (2 h CM)**
Machine Learning and AI for Analytical Chemistry, M2 Sciences analytiques

These notes accompany the Part 2 slides. The central message of this part is that
a machine learning model can only be as good as the data behind it, and that the
data carry legal, ethical, and quality obligations that the analyst must
understand. Each key point carries an analytical-chemistry example.

---

## 1. Data for training (1 h)

### 1.1 Where the data come from

A model is trained on examples, and those examples have to come from somewhere.
In analytical chemistry the common sources are: instruments in your own
laboratory, public repositories and spectral libraries, the literature and its
supplementary material, and simulated or augmented data. The origin matters
because it determines coverage, bias, licensing, and trust.

> **Example.** A retention-time predictor can be trained on retention times
> measured in your own laboratory, or on a public deposition in a repository
> such as ProteomeXchange/PRIDE, or on a curated spectral library such as the
> NIST mass spectral library. Each source covers different compounds, columns,
> and conditions, so the choice of source quietly defines what the model will be
> able to predict.

### 1.2 Characteristics of the data

Before modelling, characterise the data. Four properties matter most in
practice:

- **Coverage and balance.** Are all the classes or ranges represented, or is one
  dominant? An imbalanced set teaches the model to favour the majority.
- **Label quality.** Are the targets correct? Labels assigned by an automated
  pipeline carry that pipeline's error rate.
- **Batch and instrument effects.** Were the data acquired on one instrument, one
  operator, one season? Such structure can leak into the model (Part 3).
- **Metadata.** Are the acquisition conditions recorded? Without metadata the
  data cannot be reused or trusted.

> **Example.** A library of MS/MS spectra assembled from several instruments will
> show systematic intensity differences between instrument types. A model that is
> not told which instrument produced each spectrum may learn the instrument
> rather than the chemistry, and then fail on a new instrument.

### 1.3 Licensing of code and of data

Code and data carry separate licences, and both must be respected.

- **Code licences** (for software you reuse): permissive licences such as MIT or
  Apache-2.0 allow broad reuse; copyleft licences such as GPL require derivative
  code to be shared under the same terms.
- **Data licences** (for datasets you train on): Creative Commons variants are
  common, for example CC0 (public domain), CC-BY (use with attribution), and
  CC-BY-NC (no commercial use). A non-commercial licence can prevent you from
  deploying a model commercially even if the model itself is yours.

> **Example.** Training a fragmentation predictor on a spectral library released
> under CC-BY-NC produces a model that you cannot, strictly, ship in a commercial
> product, because the training data forbade commercial use. The licence of the
> data propagates to what you may do with the model.

When writing code that accesses repositories, never hard-code credentials or API
tokens; keep them in environment variables or a configuration file excluded from
version control.

### 1.4 Intellectual property

Beyond licences, ask who owns the data. Instrument data generated under a service
contract, a collaboration, or industrial funding may be owned by a party other
than the person who ran the sample. Clarify ownership and consent before using
data to train a model that will be shared or published.

> **Example.** Raw LC-MS files acquired for an industrial client as part of a
> paid analysis are usually the client's property. Using them to train a public
> model, without permission, is both a legal and an ethical problem, even though
> the files sit on your instrument's hard drive.

---

## 2. Levels and quality of information (1 h)

### 2.1 Levels of information

Analytical data exist at several levels, from raw signal to interpreted
knowledge. A useful ladder for mass spectrometry is: raw spectra (for example
mzML) at the bottom, then detected peaks and features, then identifications
(which compound), and finally biological or chemical knowledge at the top. Each
level is derived from the one below it, and information is lost at every step.

> **Example.** An LC-MS run starts as an mzML file of scans, becomes a list of
> peaks, becomes a set of identified compounds, and finally contributes to a
> statement such as "this metabolite is elevated in the treated group." Each
> arrow upward discards detail that cannot be recovered from the level above.

### 2.2 How AI shifts access, and can hide the base

AI tools increasingly deliver the higher levels directly: a model takes a raw
file and returns identifications, or even conclusions, skipping the intermediate
levels the analyst used to inspect. This is convenient, but it pushes the
foundational data out of view. If the model is wrong at the bottom, the error is
invisible at the top, where the user is looking.

> **Example.** A tool that reads raw spectra and outputs a list of identified
> metabolites is helpful, but if it never exposes the underlying spectra and
> scores, the analyst cannot check whether an identification rests on a strong
> match or a weak one. The base data are hidden behind the convenient answer.

### 2.3 Data quality and "poisoning the well"

Because models and downstream users depend on shared foundational data, errors
in that data propagate widely. A mislabelled entry in a public library is copied
into every model trained on it and every analysis that uses it. This is the
"poisoning the well" problem: one bad contribution at the source contaminates
everything downstream.

> **Example.** A single misannotated spectrum in a widely used reference library
> will cause every tool that trusts the library to make the same wrong
> identification, and the error is hard to trace because the source looks
> authoritative.

### 2.4 Who maintains the base? Stewardship and FAIR

If everyone consumes the foundational data and no one maintains it, quality
decays. Sustained curation is a real cost that someone must carry: repositories,
consortia, and standards bodies. The **FAIR** principles (Findable, Accessible,
Interoperable, Reusable) describe what well-stewarded data should satisfy, and
community infrastructure such as persistent identifiers and standard formats
makes FAIR practical.

> **Example.** In proteomics, ProteomeXchange and PRIDE provide stable
> accessions, the mzML and mzSpecLib standards make data interoperable, and a
> Universal Spectrum Identifier (USI) lets anyone point to one exact spectrum.
> These are the mechanisms that keep the shared base usable rather than letting
> it rot.

### 2.5 Documenting models and datasets

A model and its training data should travel with their documentation, so that a
future user knows what the model learned from, what it is good for, and what its
limits are. **Model cards** and dataset documentation record the intended use,
the training data and its licence, the evaluation, and known limitations.
Versioning both data and models makes results reproducible.

> **Example.** Publishing a retention-time model on a model hub with a model card
> that states the training set, its licence, the chromatographic conditions, and
> the measured error lets another laboratory judge whether the model applies to
> their column before they rely on it. Community resources such as ProteomicsML
> exist to share such documented models and datasets.

---

## Key terms

- **Provenance / origin**: where data came from and how they were produced.
- **Class balance, label noise, batch effect**: data-quality properties.
- **Code licence vs data licence**: separate permissions, both binding.
- **Intellectual property / ownership**: who is legally entitled to the data.
- **Levels of information**: raw signal, peaks, identifications, knowledge.
- **Poisoning the well**: propagation of errors from shared source data.
- **FAIR**: Findable, Accessible, Interoperable, Reusable.
- **Persistent identifier, USI**: stable pointers to data and to single spectra.
- **Model card**: structured documentation of a model and its training data.

## Further reading

- Wilkinson et al., The FAIR Guiding Principles for scientific data management
  and stewardship, Sci. Data, 2016.
- HUPO-PSI standards (mzML, mzSpecLib) and the ProteomeXchange/PRIDE
  documentation.
- Mitchell et al., Model Cards for Model Reporting, 2019, for the model-card
  concept.
