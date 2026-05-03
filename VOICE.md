# VOICE.md

> The voice descriptor for any prose written under the Portfolio portfolio of Dr. Heather Leffew, PhD. This document is the single operative source for prose voice across the portfolio.
>
> The canonical worked specimen is `design_system/ui_kits/case-study/clinical-validation.html`. Where this document and that page disagree, the page is correct, and this document is updated to match.

---

## 0. Before you write

The voice is established before the first sentence is generated, not enforced after a draft exists. The checklist in Section 9 is a gate, not a method. Relying on the gate to produce the voice is what produced the AI-adoption rewrite's structural problems: the surface passed, the architecture was wrong.

The authoring pipeline has two stages, in order. The first runs before any prose is drafted. The second runs once.

1. **Internalize this document.** Every session. Before the first sentence. This document states who is writing, what she sounds like, what she refuses, and what cadence she moves at. It sets the posture. An LLM that has not internalized this document cannot produce the voice.

2. **Run the exit checklist as the exit gate.** After drafting via the `/content-synthesis` workflow, the page is checked against the deterministic surface failures the checklist in Section 9 names. A page that fails the checklist goes back for rewriting, not to the editor.

The remainder of this document operationalizes the voice.
---

## Table of contents

1. Who is writing
2. The argument posture
3. Genre matrix
4. Structure of a methodological piece
5. Positive moves
6. Punctuation and syntax
7. The negative glossary
8. Worked examples
9. The exit checklist

---

## 1. Who is writing

The author is Dr. Heather Leffew. The portfolio collects her writing on applied machine learning, computational psychology, and the architecture of high-stakes prediction systems. Her professional surface area is unusual: clinical neurotherapy, forensic and threat assessment, public-safety analytics, enterprise machine learning at TikTok USDS, and the founding of the data-science function at Spokeo. The voice on the page reflects that range. It is the voice of an applied researcher who has built systems that shipped, who has read the relevant literature, and who is more interested in the mechanism than in the marketing.

The voice is precise, direct, and argument-forward. It does not perform expertise; it makes a case. It does not reach for intensity to compensate for thin technical content. When a piece is dense, it is dense because the underlying argument is dense and the prose is the smallest container that holds it honestly. When a piece is short, it is short because the claim is small and the prose has not been padded.

The voice never talks down to the reader. The reader is intelligent and unfamiliar with this specific specialty. The reader is not stupid, and the reader is not in need of a clever metaphor to understand calibration or class imbalance or feature attribution. The right move is to introduce the term, define it once, and use it.

The voice is third-person by default and first-person when honesty requires it. The grammatical subject of most sentences is the system, the methodology, the problem, or the approach. The author appears as `I` when the author is genuinely the agent of an action that cannot be described impersonally without distortion. `We` is reserved for the field as a whole. `You` is almost never used.

The author is referred to as **Dr. Heather Leffew** on first reference inside any published surface and as **Dr. Leffew** thereafter. The first-name form **Heather** does not appear in published prose. The convention applies across the bio, case studies, editorials, and any third-person reference; it does not constrain the first-person `I` inside methodological pieces, which is the author's own voice rather than a reference to her.

The voice quantifies, then contextualizes. Numbers carry their units and their stakes inside the same sentence or the next one. Synthetic data is labeled as synthetic on first reference. Limits are named, and named in the form a methods reviewer would name them: a specific quantity, a specific threshold, a specific reason that the threshold is what it is. The closing paragraph is quiet, listing what the piece commits to and what the piece does not commit to, and stopping there.

The grammatical subject of most sentences is the system, the methodology, the problem, or the approach being described. First-person `I` appears where the author is genuinely the agent of an action that cannot be impersonalized without distortion: generating a synthetic cohort, considering and rejecting a design choice, deciding what to flag. `We` is reserved for the field as a whole, in the form `we have known since Zadrozny and Elkan (2002) that calibration matters for tree ensembles`. `You` is almost never used; the reader is described, not addressed.

The voice is comfortable with long, clause-rich sentences when the underlying material is connected, attaching subordinate ideas with semicolons, colons, subordinate conjunctions, or participial phrases rather than splitting the connection across two short sentences. Pauses use commas, semicolons, colons, and parentheticals. Hyphens carry compound modifiers. Analogies, when used, are functional and mechanical, naming a specific technical concept the reader can take away (`a two-pass filter`, `a gating mechanism`, `a soft-voting ensemble`). Em dashes and en dashes do not appear in sentences; rhetorical questions, parallel contrarian structures, manufactured tension, and the denigration of prior work do not appear at all.

The reader is intelligent and unfamiliar with this specific specialty. The voice is patient with the unfamiliarity and respectful of the intelligence: it introduces a term, defines it once, and then uses it.

The remainder of this document operationalizes the voice.

---

## 2. The argument posture

The reference posture is an expert who has done the work, formed a professional opinion, and is now presenting the reasoning for it to intelligent peers. Not teaching. Arguing. The reader is a peer who can follow without scaffolding — assumed to be intelligent and capable, not assumed to share the author's exact specialization. The prose explains mechanisms and defines terms not because the reader needs remediation, but because precision is a courtesy and because the right term, defined once, is more useful than a circumlocution repeated throughout.

Six operational rules follow from that posture.

### 2.1 Argument over display

The portfolio exists to make a case, not to perform expertise. A passage that sounds technically impressive but does not advance the argument has failed, regardless of how well it scans. A passage that advances the argument in plain language has succeeded, even if it lacks rhetorical decoration.

The practical consequence is that the prose is complete rather than efficient. A complete explanation of why isotonic regression is the right calibrator for a tree ensemble takes a paragraph; the paragraph is included because the reasoning is part of the argument, not decoration around it. A complete explanation of why the synthetic cohort was constructed with 60 to 80 percent overlap across diagnostic groups takes two sentences; the two sentences are included because the design choice is what the piece commits to.

The voice does not write for the reader who needs to be convinced the author is credible. It writes for the careful peer who wants to follow the reasoning and arrive at the same place.

### 2.2 Mechanism over metaphor

The voice prefers mechanism. When a passage has the choice between describing what the system actually does and reaching for a metaphor that approximates it, the passage describes what the system actually does.

> Correct: A two-step aggregation. Within a domain, the five model families are averaged with soft voting (mean of class probabilities). Across the three domains, the calibrated submodel outputs are averaged with equal weights to produce the final risk score.

> Wrong: Imagine a council of five experts in each room, voting their conscience, and then three rooms voting again to produce the final verdict.

The metaphor in the second version is not technically wrong. It is unnecessary. The first version contains the same information and gives the reader a model that maps directly to the code. A metaphor is acceptable only when it is functional, mechanical, and adds something the literal description cannot. `A gating mechanism`, `a held-out fold`, `a two-pass filter`, and `a soft-voting ensemble` are all metaphors of this kind, and all of them are permitted because each names a specific technical concept that the reader can take away from the page.

Poetic metaphors are not permitted. `A symphony of features`, `a tapestry of behavior`, `the dance between bias and variance`, `the architecture orchestrates`. These are banned without exception. They are also banned in their adjacent forms: `weaves`, `paints`, `unfolds`, `dances`, `sings`, `breathes`. The vocabulary of the visual and performing arts does not appear in Portfolio prose.

Condescending over-simplification is also banned. `Imagine you have a box of marbles, and each marble is a customer` is wrong, even though it is technically a functional analogy. The condescension is in the position the analogy assumes the reader is in. The reader is not a child being walked through arithmetic. The reader is a senior engineer who has not happened to work on this specific subdomain. Introduce the technical term, define it, and proceed.

### 2.3 Quantify, then contextualize

Numbers in Portfolio prose are always reported with their units and their stakes inside the same sentence or the next one. The pattern is: number, unit, what makes it interesting.

> Correct: Reduced core processing time from 150+ hours to 24 to 36 hours, a six- to seven-fold improvement that allowed the team to run weekly model refreshes instead of quarterly.

> Wrong: Significantly improved processing time, enabling more frequent model refreshes.

> Correct: 400K+ violative accounts identified, enabling enforcement on 15K+ accounts without an increase in appeals volume.

> Wrong: Identified hundreds of thousands of violative accounts at scale.

The quantification rule applies even when the number is small or the result is mixed. `The classifier reached 0.79 AUC on the held-out fold; the regressor reached 0.71 R-squared on converted accounts only` is correct. `The models performed well on the held-out fold` is wrong, because it has thrown away the information the reader came for.

When a number is reported on synthetic data, the reference is explicit and the synthetic-data guardrail is enforced. Any AUC above 0.95 on a synthetic cohort designed to preserve clinical ambiguity is flagged in the prose as overfitting the synthesis, not as a strong result.

### 2.4 Sentences carry weight

The voice is comfortable with long, clause-rich sentences when the underlying material is connected. Connection is the test. A sentence that runs four clauses because all four clauses participate in a single argument is correct. A sentence that runs two clauses because the second was added for rhythm is wrong.

The cue is whether each clause earns its place. The clinical-validation page has sentences that run forty to sixty words because each clause carries an architectural commitment, a counterfactual considered and rejected, or a limit on what the synthetic data can tell us. The same page has sentences that run six words because the underlying claim is small. Both are correct, in their place.

The bias under uncertainty is to keep the connection visible. When two ideas are linked by a real causal or methodological relationship, the voice writes them as one sentence with a colon, a semicolon, a participial phrase, or a subordinate clause, rather than splitting them into two short sentences and forcing the reader to reassemble the link. Splitting a connected idea into two clipped sentences is a common LLM failure mode and is resisted explicitly: the cure is richer punctuation and subordinate structure, not shorter sentences.

The related rule, given in full in section 5.1, is that a sentence does not begin with a bare demonstrative (`This`, `That`, `These`, `Those`, sentence-initial `Which`) standing alone as the subject without an anchoring noun. The bare demonstrative at sentence-initial position is the most reliable surface signal that two ideas have been split apart that should have been written as one connected idea, with the antecedent inside the joining clause where it can do its work.

### 2.5 Name limits and design choices plainly

The voice does not paper over seams. Where the trajectory is unusual, the prose says so. Where a synthetic dataset cannot support a performance claim, the prose says so. Where a model family was tried and discarded, the prose says so. Where the deployment context would change the architecture, the prose says so.

The move is always execution, never announcement. The prose does not say "this is an uncomfortable conclusion" or "the synthesis that follows is deliberately difficult." It states the limit or the choice in the sentence where that limit or choice appears, embedded in the argument, sized to exactly what the evidence supports. A sentence that describes the prose as uncomfortable rather than delivering the thing that is uncomfortable is wrong.

> From the bio: Her trajectory from clinical neurotherapy into enterprise data architecture is uncommon but entirely deliberate.

> From clinical-validation: There is a hard guardrail in the notebook: any model reporting AUC > 0.95 on this cohort is flagged as overfitting the synthesis, not as good, the underlying signal is not that separable, by construction.

> From clinical-validation: I considered learning the cross-domain weights and decided not to: with 1,200 synthetic participants at 25% prevalence the meta-learner would mostly be memorizing the synthesis, and the equal-weight prior is more honest about how little the data can tell us.

This habit is what gives the voice its credibility. The reader trusts a writer who names limits, and stops trusting a writer who only reports successes.

### 2.6 Density, not volume

The voice is granular on technical claims and disciplined about the prose around them. A passage that adds a third sentence on the synthetic-data guardrail because the guardrail is a real methods-section concern is correct. A passage that adds a third sentence on what the guardrail feels like, or on how the author thought about the guardrail, or on what the reader should think about the guardrail, is wrong. The first sentence carries information the reader needs; the second carries decoration.

The test, on a sentence-by-sentence basis, is whether the sentence carries a technical commitment, a numerical anchor, a counterfactual considered and rejected, a limit named in the form a methods reviewer would name it, or a structural transition the architecture genuinely needs. A sentence that does none of those things is a sentence that has been added for length and is removed.

The clinical-validation page is the worked example. It is a methodological piece of substantial scope, and it sustains its scope by being granular about every architectural commitment it makes: each model family is named, each calibration choice is named with the reason it was chosen over the alternative, each disagreement-detection threshold is named with the cohort statistic that motivates it, each recommendation-language softening is named with the ensemble-variance condition that triggers it. The page is dense. The page is also short relative to its density, because the prose around the technical claims is ruthless about itself: there are no prefatory paragraphs that promise what is coming, no transitional paragraphs that summarize what was just said, no closing paragraphs that congratulate the reader for following along.

The bias is to add a number, not a sentence. When the author is tempted to expand a passage, the cure is to expand into the technical content (a citation, a quantity, a counterexample, a methodological aside) rather than into the prose surrounding it.

### 2.7 Subjunctive is a tell

The voice does not describe completed work in the subjunctive. Constructions of the form `the architecture I would build`, `if I were designing`, `the system I'd want`, `what I would do if I were starting from scratch` are wrong when the architecture has actually been built, the system actually exists, and the work was actually done. Subjunctive framing of completed work reads as the author hedging her own agency, and it is dishonest about the artifact the page is about.

The cure is the indicative past tense. The pattern is: `I built X`, `X does Y`, `Y is qualified by Z`. The author is the agent of the verbs that describe choices she made; the system is the agent of the verbs that describe what it does at runtime; the qualification names the limits in the form a methods reviewer would name them.

> Wrong: A walk through the architecture I'd build if I were designing a machine-learning assistant for autism screening.

> Correct: A walk through the architecture of a machine-learning assistant for autism screening I built as a voluntary technical demonstration.

> Wrong: These are the rules I'd want a real clinical pipeline along these lines to have to defend in writing before it touched a patient.

> Correct: Six rules a real clinical pipeline along these lines has to defend in writing before it touches a patient.

The subjunctive is permitted in two narrow contexts. The first is genuine counterfactual reasoning, where a design alternative was considered and rejected and the prose is reconstructing the choice: `I considered learning the cross-domain weights and decided not to: with 1,200 synthetic participants at 25% prevalence the meta-learner would mostly be memorizing the synthesis`. The `would` here describes a counterfactual the author actually weighed; it is not retreating from a claim about the system as built. The second is forward-looking work that is genuinely contingent on a precondition: `a real deployment would need a re-calibration cadence and a regression test suite tied to the upstream releases`. The `would` here is appropriate because no real deployment has occurred and the precondition is named.

Outside those two contexts, the subjunctive describing the system itself is wrong. Search the draft for `would build`, `would design`, `would want`, `would have`, `if I were`, `I'd build`, `I'd design`, `I'd want`, `if I had`, and replace each with the indicative past tense if the work was done, or with a declarative present tense if the work is the system as it currently runs. The full gate is in `voice/checklist.md` as gate IX.

---

## 3. Genre matrix

Three genres are written under this voice. The genre determines the front matter, the register, the use of first person, the structure, and the closing convention. A piece that mixes genres without intent reads as confused. A piece that commits to its genre reads as serious work.

### 3.1 Editorial

An editorial argues. It makes a position claim about a technical or institutional question and defends the claim. Editorials are short by Portfolio standards (1,200 to 2,500 words) and they do not contain figures, code blocks, or methodology callouts. They contain prose, citations, and possibly one pull quote.

**Subject of action.** The system, the field, the practice, or the institution being argued about. Not the author. Not the reader.

**Person.** Third-person default. First-person `I` is used when stating a personal commitment that the editorial cannot honestly attribute to the field as a whole.

**Front matter.** Eyebrow (category and date), headline, italic abstract that states the claim, byline. No stats strip; an editorial is not a quantified piece.

**Opening move.** A flat statement of the claim or the condition the claim is responding to. The editorial does not open with a hook, an anecdote, or a question. It states what is true.

**Closing move.** A quiet restatement of the claim. The reader has been walked through the argument; the closing paragraph does not summarize the steps, it states the conclusion the steps support.

**What the reader leaves with.** A position they can hold or reject, with the reasons they would need to do either.

### 3.2 Methodological

A methodological piece walks through a system. It is the genre most pieces on the portfolio inhabit. The clinical-validation page is the canonical specimen. The reader walks through what the system does, how it works, what tradeoffs were made, and what the system commits to and does not commit to.

**Subject of action.** The system, the pipeline, the architecture, or the problem being solved. The author appears as `I` when the author is genuinely the agent of an action that cannot be impersonalized: generating a synthetic cohort, choosing not to learn cross-domain weights, deciding what to flag.

**Person.** Third-person default. First-person `I` allowed and used in moderation. `We` reserved for the field. `You` not used.

**Front matter.** Eyebrow (numbered: `01 / Setup`), headline, italic abstract that names what the system is and what was built, byline grid with cohort, architecture, output. Stats strip optional, used when there are four discrete numerical anchors that orient the reader.

**Opening move.** A statement of what the system does or what the piece is. The clinical-validation opening is the model: `What follows is a design walkthrough for a screening assistant aligned with the ADOS-2 rubric, built and stress-tested on synthetic data as a voluntary demonstration of applied clinical AI methodology.`ligned with the ADOS-2 rubric.` The system is the subject; the author is the agent of the walk.

**Closing move.** A quiet declarative paragraph that states what the system commits to and what it does not. No call to action.

**What the reader leaves with.** A working understanding of the architecture, an ability to reason about whether they would build it the same way, and a clear picture of what it does not do.

### 3.3 Research paper

A research paper reports findings. It follows the canonical structure of academic publication: problem, prior work, method, results, discussion, references. It cites. It uses figures with numbered captions. It reports limitations.

**Subject of action.** The phenomenon being studied, the method being applied, or the result being reported. The author appears as `I` only inside the methods section when describing a choice that cannot be impersonalized.

**Person.** Third-person default, with academic conventions: `the model was trained on a held-out fold`, `the pipeline achieves 0.79 AUC`. `We` reserved for the field. First-person `I` used sparingly inside methods.

**Front matter.** Title, authors, affiliation, abstract (not italicized in research-paper genre, set in body face), keywords, citation block. The abstract is the operative summary; it says what was studied, what was found, and what was concluded, in that order.

**Opening move.** A statement of the problem and why it matters, grounded in prior work. Citations begin in the first paragraph. The research paper does not have a hook; it has a literature.

**Closing move.** A discussion section that names limitations, lays out what the result does and does not establish, and points to what would have to be true for the result to generalize. The discussion ends with a quiet declarative statement of the contribution. No call to future work in the form of `we hope this inspires`; if future work is named, it is named as a specific question that follows from the result.

**What the reader leaves with.** A finding, a method that produced the finding, a clear understanding of what the finding does and does not establish, and a reference list that lets them continue.

### 3.4 Genre boundaries

The three genres are exclusive. A piece is one of them. A methodological piece does not become an editorial because it includes a strong opinion; opinions in methodological pieces are stated as design choices and defended as design choices, not as positions in a debate. A research paper does not become a methodological piece because it walks through a system; the research-paper structure is followed because a finding is being reported.

When a piece is unclear about its genre, the writing reads as drifting. The cure is to commit to a genre at the front-matter stage and let the genre's structure carry the prose.

---

## 4. Structure of a methodological piece

The methodological genre is the most common on the portfolio and the one with the most specific structural conventions. Editorials and research papers are well documented elsewhere; the methodological piece is the genre this design system extends.

### 4.1 Front matter

The front matter sits inside a `band--dark front` section and contains:

- A meta row of bracketed labels carrying orientation only: the subject area (`Clinical & behavioral ML`), any data qualifiers (`Synthetic data`), the read time. The row does not carry a category label or an index number; the article identifies itself through its headline and abstract, not through chrome. The meta row is set in JetBrains Mono, 11px, 0.30em tracking, uppercase, in `--tungsten`.
- The headline, set in Playfair Display 600 at clamp(44px, 5.0vw, 72px), letter-spacing -0.018em. The headline is a complete sentence ending in a period. It describes what the piece is, not what the reader should feel about it.
- The italic abstract, set in Lora italic at 22px, max-width 60ch, color `--platinum`. The abstract is one to three sentences and answers: what the system is, what was built, what was tested, what the reader should expect to take away. It does not include first-person voice unless the piece is genuinely a personal walk-through, in which case `I` is permitted.
- The byline grid: cohort, architecture, output. Each cell carries a JetBrains Mono uppercase label and a body-italic value beneath it. The labels carry tracking 0.20em. The values are sentence-cased in Lora italic.

The headline is a complete sentence. `An ADOS-2-aligned screening pipeline, with the uncertainty kept in.` is correct. `ADOS-2 Pipeline` is wrong; it is a label, not a sentence, and the methodological piece's headline is always a sentence.

### 4.2 Section rhythm

The page alternates between paper and dark bands. The pattern is:

- Front (dark)
- 01 Setup (paper)
- 02 Behavioral features (dark, here treated as `band--ink` for technical content)
- 03 The overlap problem (paper)
- 04 Ensemble (dark)
- 05 Calibration (paper)
- 06 Disagreement detection (dark)
- 07 Recommendation layer (paper)
- 08 Limits and what this is not (paper)
- Back matter (dark)

The alternation is not aesthetic. It is functional: paper bands carry slow narrative passages where the reader is being walked through context, and dark bands carry the dense technical passages where figures, code, and ensembles live. A reader who is scrolling can locate the section they want by the band color before reading a single word.

The eyebrows are numbered `01 /`, `02 /`, and so on, with a slash separator and a section name. The numbering is two-digit even at low counts; `01` is correct, `1` is wrong. The eyebrow color is `--ink-blue` in paper bands and `--sapphire` in dark and ink bands. Tracking is 0.30em.

### 4.3 The drop cap

The first paragraph of the first paper section after the front matter receives a drop cap. No other paragraph receives one. The drop cap is the visual anchor that says `the piece is now beginning`; using it again later dilutes it.

The drop cap is implemented via the `.has-dropcap` class on the paragraph and `::first-letter`. The font size is 5.6em, line-height 0.86, color `--ink-blue` in paper bands and `--sapphire` in dark bands.

### 4.4 Sidenotes

Sidenotes carry caveats, citations, deployment caveats, and parenthetical-but-important content that would clog the main column if it were inline. Sidenotes are numbered, and the numbering restarts at 1 for each piece, not for each section.

The sidenote markup is:

```
<span class="sn"><span class="sn-num">1</span><span class="sn-body">...</span></span>
```

The wrapping paragraph carries the class `col-with-sidenotes`. On wide screens (>= 1080px) the sidenote body floats into the right gutter at the position of the inline marker. On narrow screens the sidenote body opens inline as a footnote when the marker is tapped.

A sidenote should carry information the reader can ignore on first pass without losing the argument. If the sidenote contains content that is required to follow the main argument, the content belongs in the main column, not the gutter. The test is: does the paragraph still make sense if the sidenote disappears? If yes, the sidenote is correctly placed. If no, the content is misfiled.

### 4.5 Glossary terms

Glossary terms carry a dotted underline and a hover tooltip. They are used for jargon the reader is not yet expected to know, and they are introduced once. After the first glossary use, the term is used plainly in subsequent prose.

The glossary markup is:

```
<span class="gloss">ADOS-2<span class="gloss-tip"><b>ADOS-2</b>, Autism Diagnostic Observation Schedule, Second Edition...</span></span>
```

The tooltip body is set in Lora italic at 13.5px and contains a one-paragraph definition. Where applicable the definition includes a citation in the form `(Lord et al., 2012)`. Tooltips are not used for self-promotion or commentary; they are dictionary entries.

A piece typically carries 4 to 12 glossary terms. Fewer than 4 suggests the prose is not introducing technical concepts; more than 12 suggests the prose is over-defining and the reader is being asked to hover too often.

### 4.6 Methodology callouts

A methodology callout is a paper-mode aside that holds a discrete clarification about how the work was done. The callout has a thin left border in the accent color and a small uppercase label.

```
<div class="method">
  <div class="inner">
    <div class="lab">What the synthetic data is for</div>
    Synthetic data is the wrong tool for performance claims and the right tool for studying how a pipeline behaves under controlled ambiguity.
  </div>
</div>
```

A callout earns its block when the content it carries is structurally about the methodology rather than about the argument being made. The clinical-validation page uses callouts for the synthetic-data guardrail, the calibration choice, the model-disagreement threshold, and the recommendation-language softening rule. Each is a methods-section concern that the main prose names but does not stop to develop.

### 4.7 Figures

Figures sit inside `.figure > .frame` and carry a numbered caption underneath. The caption begins with `Fig. 1, ` (in JetBrains Mono uppercase, with the number colored `--ink-blue` or `--sapphire`) and continues with a single sentence describing what the figure shows and why it matters.

Figures are SVG, generated procedurally inside the page, and use the oil paint quartet for categorical color. Sequential and monochrome scales restrict to Phthalo Blue tints. A figure does not use brand chrome colors (sapphire, flare, tungsten) for data marks; brand chrome colors and figure data colors are kept separate.

Captions are full sentences ending in a period. The caption answers: what is plotted, on what axes, and what the reader should notice.

### 4.8 Stats strips

A stats strip is a horizontal grid of four numerical anchors that orient the reader at the top of a paper section. The strip is used at most once per piece, near the front matter or in the first paper section. Each cell contains a value in JetBrains Mono 38px and a label in JetBrains Mono uppercase 10px with 0.22em tracking.

The strip carries hairline top and bottom borders and dividing borders between cells. It does not carry boxes, fills, or shadows.

Use four cells. Three feels incomplete; five wraps. If the piece does not have four sharp anchor numbers, do not force the strip; describe the numbers in prose.

### 4.9 Closing section

The final section carries the eyebrow `Limits and what this is not` (or its equivalent) and contains a quiet enumeration of what the piece does not establish. The closing section is a paper band. The final paragraph is a single declarative sentence or short paragraph that states the contribution of the piece and stops.

The closing does not contain a call to action, a link, or a question. The next-chapter component, if used, sits below the closing as a separate component and is part of the back matter, not part of the prose.

### 4.10 Back matter

The back matter sits in a dark band and contains, in order: a bibliography (numbered, hairline-separated, set in Lora 14.5px), an optional related-pieces grid (three cards), an optional citation graph SVG, and the next-chapter component. Bibliography entries follow the conventions of the field the piece is in; for clinical-validation they follow APA-adjacent format with author, year, title in italics, venue.

---

## 5. Positive moves

A passage in Portfolio prose is built by selecting the move that fits the situation. The moves below cover the recurring writing situations on the portfolio. Each move names the situation, gives the rule, and provides a worked specimen lifted from the canonical page. An authoring agent who is unsure how to begin a passage opens this section and finds the move.

### 5.1 Connecting claims to their explanations

A sentence does not begin with a bare demonstrative pronoun, that is, with `This`, `That`, `These`, `Those`, or sentence-initial `Which` standing alone as the subject without a noun naming what it refers to. The constructions `This is because...`, `This means that...`, `This allows the model to...`, `This works by...`, `That is why...`, `These are the cases where...`, `Which is the reason for...` are wrong, because the bare demonstrative is a surface signal that two ideas have been split apart that should have been written as one connected idea.

The cure is not a different sentence opener. The cure is a different relationship to the previous sentence: attach the clause via a semicolon, a colon, a subordinate conjunction (`which`, `where`, `because`, `since`, `so that`), or a participial phrase, with the antecedent of the demonstrative inside the joining clause where it can do its work.

> Wrong: The pipeline separates conversion probability from expected deal value. This means the two scores can be calibrated independently.

> Correct: The pipeline separates conversion probability from expected deal value, which means the two scores can be calibrated independently.

When `This` is followed immediately by a noun that anchors the demonstrative, the construction is fine: `This pipeline separates conversion probability from expected deal value` is correct, because `pipeline` anchors `This`. When `This` stands alone, the rule applies.

The rule explicitly excludes `It` at sentence-initial position. `It turns out that...`, `It is worth noting that...`, `It happens that...` are idiomatic openers in academic prose and are permitted.

### 5.2 Introducing a system

Open with the system as the grammatical subject. State what it does in declarative form. Name the genre, the scope, and the main commitment in the first or second sentence.

> From clinical-validation: `What follows is a design walkthrough for a screening assistant aligned with the ADOS-2 rubric, built and stress-tested on synthetic data as a voluntary demonstration of applied clinical AI methodology. Every number on this page comes from a synthetic cohort of 1,200 participants generated at 25% ASD prevalence to stress-test the pipeline.`

The first sentence names the genre (`design walkthrough`), the scope (`a screening assistant aligned with the ADOS-2 rubric`), and the system as subject (`What follows`). The second sentence names the data, labels it as synthetic, and gives the count.

### 5.3 Defining a technical term

Introduce the term inside a glossary span on first reference, with a one-paragraph tooltip that gives the definition and, where applicable, a citation in the form `(Author, Year)`. After the first introduction, use the term plainly. Do not redefine, do not apologize for the jargon, and do not gloss the term inline a second time.

### 5.4 Reporting a number

Number, unit, contextualization, in that order, inside the same sentence or the next one. The pattern is: report the number, then say what the number is for, then say what makes it interesting. The contextualization is what converts a number from data into evidence.

> Correct: Reduced core processing time from 150+ hours to 24 to 36 hours, a six- to seven-fold improvement that allowed weekly model refreshes instead of quarterly.

The number, the unit, and the stake are all inside one sentence, joined by a participial phrase that carries the contextualization without breaking into a second sentence.

### 5.5 Acknowledging a limit

Name the limit in the form a methods reviewer would name it: a specific quantity, a specific threshold, a specific reason that the threshold is what it is. Use a colon to attach the threshold to the system that owns it. Use a coordinating conjunction (`and`, `but`, `because`) and a subordinate clause to carry the reason inside the same sentence.

> From clinical-validation: `There is a hard guardrail in the notebook: any model reporting AUC > 0.95 on this cohort is flagged as overfitting the synthesis, not as good, the underlying signal is not that separable, by construction.`

The colon introduces the guardrail. The two appositive phrases (`not as good`, `the underlying signal is not that separable`) are attached by commas. The closing prepositional phrase (`by construction`) seals the sentence with the reason. The whole limit is a single sentence; the reader does not have to assemble it from fragments.

### 5.6 Stating a design choice

State the choice. State what was considered and rejected. State the reason for the rejection in technical terms. The first-person `I` is permitted here because the author is genuinely the agent of the choice. Use a colon to introduce the reason.

> From clinical-validation: `I considered learning the cross-domain weights and decided not to: with 1,200 synthetic participants at 25% prevalence the meta-learner would mostly be memorizing the synthesis, and the equal-weight prior is more honest about how little the data can tell us.`

The sentence runs forty-three words across a coordinating conjunction, a colon, a participial phrase, and a coordinating conjunction joining a second independent clause that carries a subordinate clause of its own. Each clause earns its place: the choice, the rejection, the reason for the rejection, the methodological commitment that follows from the reason. None of it is decoration.

### 5.7 Describing an architecture

Describe what the system does step by step, with each step as a system-as-subject sentence. Use functional analogies (`a two-pass filter`, `a gating mechanism`, `a soft-voting ensemble`) where they name a specific concept the reader can take away. Use transitional connections between steps where the architectural relationship is real, attaching the connection inside a single sentence with a colon, semicolon, or subordinate clause rather than across two short sentences.

> From clinical-validation: `Aggregation is two-step. Within a domain, the five families are averaged with soft voting (mean of class probabilities). Across the three domains, the calibrated submodel outputs are averaged with equal weights to produce the final risk score. There is no neural meta-learner stitching the streams together, just a weighted mean.`

The first sentence is a six-word claim. The second and third sentences are each a single architectural step, with the system as subject and a parenthetical that carries the technical detail. The fourth sentence closes the description by naming what the architecture is not, with a participial phrase (`stitching the streams together`) and a comma-attached corrective (`just a weighted mean`).

### 5.8 Closing a piece

List what the piece commits to, in concrete technical language. List what the piece does not commit to, in the same form. State the contribution in one quiet declarative sentence. Stop.

> From clinical-validation, paraphrased: `The architecture commits to three things: a per-domain submodel structure that survives the cross-feature overlap real assessments contain, an isotonic calibration that does not pretend the synthetic data has more separability than it has, and a recommendation layer that softens its language at the moment the ensemble disagrees. The architecture does not commit to a clinical claim, a deployment context, or a performance number transferable to real recordings. What it offers is a pattern: a way of building these systems that keeps the uncertainty in.`

The first sentence carries three commitments separated by commas, each commitment a noun phrase modified by a subordinate clause. The second sentence mirrors the first in structure and carries the three non-commitments. The third sentence states the contribution in one quiet declarative form, with a colon attaching the elaborating clause. There is no call to action and no link.

---

## 6. Punctuation and syntax

### 6.1 Em dashes and en dashes

Neither punctuation mark appears in Portfolio prose. The em dash (—) is not used inside sentences. The en dash (–) is not used inside sentences. The exception is numeric ranges inside figures, captions, and tables, where the en dash is permitted (`2019-2024` is also acceptable using the hyphen).

The substitutes are:

- The comma, for parenthetical asides that are tightly bound to the sentence: `the architecture, a five-family soft-voting ensemble, was calibrated on a held-out fold`.
- The semicolon, for joining two independent clauses where each could stand on its own: `the classifier reached 0.79 AUC; the regressor reached 0.71 R-squared`.
- The colon, for introducing a clause that expands or specifies the preceding one: `the design choice was simple: average the family outputs with equal weights`.
- The parenthesis, for genuinely parenthetical content that the sentence could survive without: `the synthetic cohort (n = 1,200) was constructed to preserve clinical ambiguity`.

### 6.2 The hyphen

The hyphen is used for compound modifiers (`dual-model pipeline`, `cross-domain weights`, `held-out fold`, `soft-voting ensemble`) and for compound nouns where the convention has settled. The hyphen is never used as a substitute for a missing em dash; if a passage seems to need a dash, the dash is replaced with one of the four substitutes above.

### 6.3 Oxford commas

The Oxford comma is used in every list of three or more items. There are no exceptions.

### 6.4 Casing

- Title Case is used for headlines and section titles: `Machine Learning Leadership and Strategy`, `An ADOS-2-aligned screening pipeline, with the uncertainty kept in.`
- UPPERCASE with wide tracking is used for eyebrows and meta labels: `DATA SCIENCE AND SYSTEMS ARCHITECTURE`, `5 MIN READ`, `01 / SETUP`.
- Sentence case is used for buttons that read as sentences: `Read full biography`. Title Case is used for buttons that are verb-noun directives: `Download PDF`.
- Sentence case is used for prose, captions, and bibliography entries.

### 6.5 Ampersand

The ampersand is allowed in titles and chips when it tightens a compound: `Graph ML & Identity`, `Leadership & AI Strategy`. The ampersand is not used in body prose.

### 6.6 Numbers

Spell out one through nine; use numerals for 10 and above. Exceptions: when the number carries a unit (`5 minutes`, `8 GB`), when the number is part of a technical specification (`a 5-family ensemble`), when consistency with a nearby number requires it (`between 4 and 12 glossary terms`).

Use commas in thousands (`6,000 synthetic accounts`, `400K+ violative accounts`). Use the lowercase suffix for magnitudes: `1B+`, `49TB`, `400K+`.

### 6.7 Citations in prose

Inline citations follow the format `(Author, Year)` for parenthetical reference and `Author (Year)` for narrative reference. `Perochon et al. (2023, Nature Medicine) report AUC ~ 0.90 for autism screening from a multi-feature digital phenotype` is correct. Full citations live in the back matter bibliography.

### 6.8 Code, formulas, and inline technical text

Inline code uses `<code>` and is set in JetBrains Mono. Inline formulas use the same. Technical terms that are not jargon (`sigmoid`, `softmax`, `argmax`, `R-squared`, `AUC`, `PR-AUC`) are set in plain body face. Technical terms that are code identifiers (`scale_pos_weight`, `historical_win`) are set in `<code>`.

Code blocks use the `.code-block` class on dark or paper backgrounds. Code is presented with the level of completeness needed to convey the architectural point and no more; a code block is not a substitute for a notebook.

---

## 7. The negative glossary

The negative glossary is the consolidated list of vocabulary, rhetorical structures, and stylistic moves that do not appear in Portfolio prose. The list is exhaustive within its category. An authoring agent should treat the list as a literal text-search filter at the exit-checklist stage.

### 7.1 Banned vocabulary

The following words and phrases do not appear:

- `passionate about`, `results-driven`, `proven track record`
- `leverage`, `leverages`, `leveraging` (use `use`)
- `utilize`, `utilizes`, `utilizing` (use `use`)
- `unlock`, `unlocks`, `unlocking`
- `empower`, `empowers`, `empowering`, `empowerment`
- `transform`, `transforms`, `transformative`, `transformation` (where it carries marketing register; the academic term `transformation` for a mathematical operation is permitted)
- `cutting-edge`, `revolutionary`, `groundbreaking`, `pioneering`
- `thought leader`, `thought leadership`
- `ecosystem` (in the figurative sense; the biological sense is permitted in scientific contexts)
- `journey` (in the metaphorical sense; literal travel is permitted)
- `space` (in the figurative sense, as in `the AI space`; the mathematical and physical sense is permitted)
- `seamless`, `seamlessly`
- `robust` (where it carries marketing register; the statistical term `robust` is permitted in technical context)
- `powerful` (where it carries marketing register; the technical term `power` for statistical sensitivity is permitted)
- `solution` (where it carries marketing register; mathematical solutions are permitted)
- `industry-leading`, `industry-defining`
- `mechanical`, `rigid`, `detached`, `structural` (where used to denigrate prior work or to perform clinical distance)
- `tactical velocity`, `executive telemetry`
- `chillingly`, `terrifying`, `extreme violations`
- `engineering paralysis`, `unapproachable silo`, `tribal fear`

The banned-vocabulary list is conservative. When in doubt, use a plainer synonym. When a banned word is the precisely correct technical term in a specific context (`robust` in statistical sense; `transformation` in mathematical sense), the technical use is permitted; the marketing use is not.

### 7.2 Banned analogies

The following analogy classes do not appear:

- Performing-arts metaphors: `symphony`, `orchestra`, `concerto`, `dance`, `choreography`, `ballet`.
- Textile metaphors: `tapestry`, `weaving`, `weaves`, `threads`.
- Botanical metaphors that anthropomorphize systems: `the model blooms`, `the data flowers`, `the architecture takes root`.
- Architectural metaphors that anthropomorphize: `the system breathes`, `the pipeline sings`.
- Combat metaphors: `attacks the problem`, `wages war on noise`, `defeats the baseline`.
- Narrative metaphors that personify: `the data tells a story` (the data is described; it does not narrate).
- Condescending metaphors: any analogy that assumes the reader is unfamiliar with elementary concepts. `Imagine you have a box of marbles`, `think of it like a pizza divided into slices`, `it is like sorting laundry`. These are wrong even when the technical content of the analogy is correct.

### 7.3 Banned rhetorical structures

The following rhetorical structures do not appear:

- Parallel contrarian structures: `not X, but Y`, `not just X, Y`, `less X, more Y`, `we do not X, we Y`, `it is not X, it is Y`.
- Manufactured tension: `the question was never X, the question was Y`, `the real X is not X, but Y`.
- Rhetorical questions of any kind, including the kind that organize an explanation: `but what does this mean for the architecture? It means that...`. The question form is replaced with a declarative statement.
- Clickbait headers: `When an AUC is not a success`, `A black box governing billions`, `The problem with X you have not considered`. Headers describe the technical mechanism plainly.
- Bare-demonstrative openers: `This is because`, `This means that`, `This allows`, `This works by`, `That is why`, `These are the cases where`, sentence-initial `Which` used as a relative pronoun without an anchoring noun. The full rule and the cure are in section 5.1: the cure is to attach the clause to the preceding sentence with a semicolon, colon, or subordinate clause, with the antecedent of the demonstrative inside the joining clause. Sentence-initial `It` is excluded from this rule.
- The clipped-pair failure mode: writing two short sentences in succession where one longer sentence with a colon, a semicolon, or a subordinate clause would carry the connection more honestly. `The pipeline separates conversion probability from expected deal value. The two are then multiplied.` is wrong, because the connection between the steps is being deferred to the reader to reassemble. `The pipeline separates conversion probability from expected deal value, then multiplies the two at the end.` is correct, because the connection is on the page where the claim is. The Portfolio voice is comfortable with long, clause-rich sentences when the underlying material is connected; see section 2.4.
- The `In conclusion` / `In summary` / `To wrap up` closer. The piece ends without announcing it is ending.
- The reader-address closing: `Read more`, `Get in touch`, `Learn more about`, `Let us know what you think`. The piece does not invite the reader anywhere.

### 7.4 Banned posture

The following postures do not appear:

- Denigration of prior work to make new work look heroic. The prior architecture is described in objective terms; the new architecture is described in objective terms; the comparison emerges from the reader's reading.
- Performing-distance language: `chillingly cold`, `clinically detached`, `surgical precision`. The prose does not describe its own tone; it earns its tone by the way it writes.
- Self-congratulation. The prose does not call itself rigorous, careful, sophisticated, or thoughtful. It is rigorous, careful, sophisticated, and thoughtful, and the reader is allowed to notice.
- Marketing closings. The piece ends quietly. It does not offer a call to action.

### 7.5 Banned glyphs

- Emoji. None, anywhere, in any context.
- Decorative unicode glyphs (★, ✦, ✶, ❖). The permitted glyphs are the four arrows (→, ↓, ↑, ←) and the JetBrains Mono triangle (▸) used as a list-item marker.

---

## 8. Worked examples

The worked examples below are drawn from `design_system/ui_kits/case-study/clinical-validation.html`, the canonical specimen of the methodological genre. Each example leads with the canonical version and the analysis of why the canonical version works; a contrasting wrong version follows in smaller form, with a one-paragraph note on its specific failures. The wrong versions are constructed for instruction; they do not appear on the live site.

### 8.1 Front-matter abstract

**Canonical, from clinical-validation.**

> A walk through the architecture I'd build if I were designing a machine-learning assistant for autism screening, three behavioral domains, several model families running in parallel, isotonic calibration, ensemble variance as a confidence band, and a recommendation layer whose tone changes when the models disagree. Built and stress-tested entirely on synthetic data designed to preserve the clinical ambiguity real assessments contain.

**Why it works.** The system is the subject of the first sentence (`A walk through the architecture`). First-person `I` is used once, where the author is genuinely the agent (`I'd build`). The list is technical and specific (`isotonic calibration`, `ensemble variance as a confidence band`). The synthetic-data label is on the second sentence. The voice is unhurried and exact. The first sentence runs across seven comma-separated noun phrases and earns its length, because each noun phrase carries an architectural commitment the abstract is announcing.

*For contrast, a wrong version that violates several rules at once:*

*Imagine a world where machine learning could finally unlock the mysteries of autism screening. We are excited to share a transformative approach that leverages cutting-edge ensembles to deliver a seamless, robust solution. In this journey, we will walk you through three domains, several models, and a calibration layer that will revolutionize how clinicians think about uncertainty.*

The first word addresses the reader. The second sentence opens with marketing register (`We are excited`). Banned vocabulary appears in nearly every clause: `unlock`, `transformative`, `leverages`, `cutting-edge`, `seamless`, `robust`, `solution`, `journey`, `revolutionize`. The reader is addressed (`walk you through`). The voice is performing enthusiasm rather than describing a system.
### 8.2 Opening paragraph of section 1

**Canonical, from clinical-validation.**

> What follows is a design walkthrough for a screening assistant aligned with the ADOS-2 rubric, built and stress-tested on synthetic data as a voluntary demonstration of applied clinical AI methodology. Every number on this page comes from a synthetic cohort of 1,200 participants generated at 25% ASD prevalence to stress-test the pipeline. There is no clinical claim and no deployment. The point is to think publicly about what an assistive ML system for this setting would have to commit to in order to be honest about what it does and doesn't know.

**Why it works.** The grammatical subject of the first sentence is `What follows`, which points at the system being described, and the sentence is loaded with three structural commitments at once (genre, scope, alignment to the ADOS-2 rubric). The synthetic-data qualification appears in the second sentence with the count and the reason. Limits are stated immediately and bluntly (`no clinical claim and no deployment`). The closing sentence states what the piece is for in declarative form, with a long subordinate clause carrying the reason the work matters.

*For contrast, a wrong version:*

*Have you ever wondered how machine learning could finally bring clarity to the messy, complex world of autism screening? In this groundbreaking exploration, we will take you on a deep dive through a powerful new pipeline. The reason this matters is because clinicians have been waiting for a solution that is both rigorous and accessible. Buckle up.*

Opens with a rhetorical question. Reader is addressed (`you`). Banned vocabulary throughout (`groundbreaking`, `dive`, `powerful`, `solution`). `The reason this matters is because` is the construction the bare-demonstrative rule (section 5.1) is designed to catch: two ideas have been split into two sentences when one connected sentence would carry the relationship. The closing imperative (`Buckle up`) is a marketing hook.
### 8.3 Acknowledging an uncomfortable choice

**Canonical, from clinical-validation.**

> Aggregation is two-step. Within a domain, the five families are averaged with soft voting (mean of class probabilities). Across the three domains, the calibrated submodel outputs are averaged with equal weights to produce the final risk score. There is no neural meta-learner stitching the streams together, just a weighted mean. I considered learning the cross-domain weights and decided not to: with 400 synthetic participants the meta-learner would mostly be memorizing the synthesis, and the equal-weight prior is more honest about how little the data can tell us.

**Why it works.** Each sentence has a system-as-subject opening (`Aggregation`, `Within a domain`, `Across the three domains`, `There is no neural meta-learner`). The first-person `I` arrives only when the author is genuinely the agent of a discarded design choice (`I considered... and decided not to`). The colon introduces the reason; the reason is honest about a real limit (`400 synthetic participants` is small for a meta-learner). The fifth sentence runs forty-three words across a coordinating conjunction, a colon, a participial phrase, and a coordinating conjunction joining a second independent clause that carries a subordinate clause of its own; each clause earns its place. The voice does not describe itself as careful; it is careful, and the reader can see it.

*For contrast, a wrong version:*

*Aggregation is a sophisticated two-step process that elegantly combines the strengths of multiple model families. We considered a neural meta-learner but ultimately decided that simplicity was the more powerful choice, allowing the system to maintain its robustness while remaining accessible to interpretability tools.*

`Sophisticated`, `elegantly`, `powerful`, `robustness`, `accessible` are all marketing register. The voice describes its own attributes (`sophisticated`, `elegantly`) rather than letting the architecture speak. `We` is used to claim authorship of a design choice; under the rules, `we` is reserved for the field, and the author is the agent of the choice using `I`.
### 8.4 Naming a limit

**Canonical, from clinical-validation.**

> Synthetic data is the wrong tool for performance claims and the right tool for studying how a pipeline behaves under controlled ambiguity. Because I generated the cohort, I know exactly how much overlap, noise, and missingness each model is being asked to handle, and I can tell when a model's reported AUC is suspiciously high. There is a hard guardrail in the notebook: any model reporting AUC > 0.95 on this cohort is flagged as overfitting the synthesis, not as good, the underlying signal is not that separable, by construction.

**Why it works.** First-person `I` is used three times in three sentences, and each use is the author-as-agent of a methods choice (`I generated the cohort`, `I know exactly how much overlap`, `I can tell when a model's reported AUC is suspiciously high`). The first sentence is a single clause balanced on a coordinating conjunction (`and`) that carries the dual claim about what synthetic data is for. The third sentence is forty-two words and runs a colon, then three appositive phrases attached by commas (`not as good`, `the underlying signal is not that separable`, `by construction`); each phrase carries a different facet of why the threshold is what it is. The guardrail is named in the form a methods reviewer would name it: a specific threshold, a specific flagging rule, a specific reason the threshold is what it is.

*For contrast, a wrong version:*

*Our cutting-edge synthetic data approach delivers industry-leading insights into pipeline behavior. The system achieves an impressive 0.97 AUC on held-out data, demonstrating the robustness of our novel architecture. While there are some limitations to synthetic data, our methodology overcomes them through careful design.*

Opens with banned vocabulary (`cutting-edge`, `industry-leading`, `robustness`, `novel`). Reports a 0.97 AUC on synthetic data without flagging it under the guardrail; under the rule, that number should be flagged as overfitting the synthesis, not celebrated. Closes with a hand-wave (`our methodology overcomes them through careful design`) that does not name the methodology or the design.
### 8.5 Closing paragraph

**Canonical, from clinical-validation, paraphrased to the closing convention.**

> The architecture commits to three things: a per-domain submodel structure that survives the cross-feature overlap real assessments contain, an isotonic calibration that does not pretend the synthetic data has more separability than it has, and a recommendation layer that softens its language at the moment the ensemble disagrees. The architecture does not commit to a clinical claim, a deployment context, or a performance number transferable to real recordings. What it offers is a pattern: a way of building these systems that keeps the uncertainty in.

**Why it works.** The first sentence carries three commitments separated by commas, each commitment a noun phrase modified by a subordinate clause; the sentence runs sixty-three words and never feels long, because each clause adds an architectural fact. The second sentence mirrors the first in structure and carries the three non-commitments in the same form. The third sentence states the contribution in one quiet declarative form, with a colon attaching the elaborating clause. There is no call to action and no link.

*For contrast, a wrong version:*

*In conclusion, we are excited to have shared this transformative journey through a powerful new screening pipeline. We hope this work inspires the community to continue pushing the boundaries of what is possible. If you have feedback or want to collaborate, please reach out, and remember to subscribe for future updates.*

Opens with the banned `In conclusion`. Marketing register throughout (`excited`, `transformative`, `journey`, `powerful`, `pushing the boundaries`, `what is possible`). Closes with a reader-address (`If you have feedback... please reach out... remember to subscribe`) that converts the piece into a marketing surface.

---

## 9. The exit checklist

The deterministic exit gate for any prose written under the Portfolio voice. Run every item before submitting a draft. Each item is yes/no; a single failure means the draft is not ready.
Thirty-six items, nine gates.

### I. Punctuation gate

1. **Zero em dashes (—) in sentences.** Search the document for the character `—`. If any are present in prose, replace with a comma, semicolon, colon, or parenthetical. (Em dashes are permitted only inside quoted material, code blocks, or bibliography entries.)
2. **Zero en dashes (–) in sentences.** Same rule. The en dash is allowed in numeric ranges inside figures and tables (`2019–2024`) but never in prose.
3. **Hyphens are fine.** `dual-model`, `cross-domain`, `model-disagreement` are correct. Do not replace hyphens with em dashes to imply emphasis.
4. **Pauses use commas, semicolons, colons, or parentheticals.** Every pause that would have been an em dash maps to one of these four. Default to the comma; reach for the semicolon when the two clauses could each stand alone; reach for the colon when the second clause expands or specifies the first; reach for parentheses when the aside is genuinely parenthetical.
5. **Oxford commas always.** No exceptions.

### II. Grammatical-subject gate

6. **The system, methodology, problem, or approach is the subject of most sentences.** Open the draft and read the first word of every sentence in the first paragraph. If more than one of them is `I`, `We`, or `You`, the paragraph is wrong.
7. **First-person `I` is permitted but secondary.** Use it where the author is genuinely the agent of an action that cannot be described impersonally without distortion (`I generated the synthetic cohort`, `I considered learning the cross-domain weights and decided not to`). Do not use `I` to narrate work that the system itself performs (`I trained the model` is wrong; `the model was trained on a held-out fold` is right).
8. **`We` is reserved for the field, not the author.** `We have known since Zadrozny and Elkan (2002) that…` is correct. `We engineer an integrated dual-model pipeline` is wrong; the pipeline is the subject of that sentence, not the author.
9. **`You` is almost never used.** The reader is not addressed. Exceptions are explicit instructions inside a code block or a `Quick Start` section.

### III. Vocabulary gate

10. **No banned terms.** Run a literal text search for each. Any hit means the draft fails until the term is removed:
    - `passionate about`, `results-driven`, `proven track record`
    - `leverage`, `leverages`, `leveraging` (use `use`)
    - `utilize`, `utilizes`, `utilizing` (use `use`)
    - `unlock`, `unlocks`, `unlocking`
    - `empower`, `empowers`, `empowering`
    - `transform`, `transforms`, `transformative`
    - `cutting-edge`, `revolutionary`, `groundbreaking`, `pioneering`
    - `thought leader`
    - `ecosystem`, `journey`, `space` (in the sense of `the AI space`)
    - `seamless`, `robust`, `powerful`, `solution`
    - `mechanical`, `rigid`, `detached`
    - `industry-leading`
    - `tapestry`, `symphony`, `orchestra`, `dance`, `weaving`
    - `tactical velocity`, `executive telemetry`
    - `chillingly`, `extreme violations`, `engineering paralysis`, `unapproachable silo`, `tribal fear`

11. **No emoji anywhere.** Not in prose, not in headers, not in lists, not in alt text.
12. **No melodramatic intensifiers.** `catastrophic`, `disastrous`, `spectacularly`, `extreme`, `chillingly`, `terrifying`. State what happened in plain language and let the magnitude carry itself.

### IV. Structural-rhetoric gate

13. **No parallel contrarian structures.** Search for the phrase shapes:
    - `Not X, but Y` / `Not just X; Y`
    - `Less X, more Y`
    - `We don't X, we Y` / `It isn't X, it's Y`
    - `The question was never X, the question was Y`
    Any hit means the sentence is rewritten as a direct positive claim.
14. **Headers follow genre.** In methodological pieces and case studies, headers describe the technical mechanism plainly: `Mapping the Resolution Layer` is correct; `When an AUC Is Not a Success` is wrong for those genres. In editorial pieces and position pieces, argumentative headers are correct: they name the specific claim or observation the section makes. The test is not whether the header sounds bold — it is whether the header is specific and earned. Vague hooks ("The Hidden Truth About...") are wrong in any genre; specific argumentative headers ("When the Validity Check Fires") are correct in editorial work.
15. **No rhetorical questions.** Including the kind that organize an explanation. The question form is not used.
16. **No bare-demonstrative sentence openers.** Search for sentences beginning with `This `, `That `, `These `, `Those `, or `Which ` where the next word is not a noun anchoring the demonstrative. Each hit is a signal that the sentence wants to be the second clause of the previous sentence; attach it via semicolon, colon, or subordinate conjunction (`which`, `where`, `because`), with the antecedent inside the joining clause. Sentence-initial `It` is excluded from this rule.
17. **No clipped-pair connections.** Search for adjacent short sentences where the second sentence's first word is a connective or demonstrative referring back to the first (`This`, `That`, `These`, `Those`, `Then`, `So`, `Thus`, `Therefore`, `As a result`). Each hit is a signal that the connection between the two ideas should be carried inside one sentence with a colon, semicolon, or subordinate clause, rather than split across two.
18. **No marketing register in closings.** The final paragraph does not call to action, does not summarize benefits, does not invite the reader to do anything. It states a quiet declarative fact and stops.

### V. Analogy gate

19. **Analogies are permitted only if they are functional or mechanical.** `A two-pass filter`, `a gating mechanism`, `a held-out fold` are correct. `A symphony`, `a tapestry`, `a dance` are wrong.
20. **Analogies are banned if they over-simplify in a condescending direction.** `Imagine you have a box of marbles` is condescending toward a technical reader; do not write it. The reader is assumed to be intelligent and unfamiliar with this specific specialty, not stupid.
21. **The math is the proof, not the analogy.** If a passage relies on an analogy to make its point and the analogy were removed, the technical content should still stand on its own. If it would not, the technical content is incomplete and the analogy is masking it.

### VI. Genre gate

22. **The piece is in one of three genres: editorial, methodological, research paper.** Confirm which. Each has its own front matter, register, and closing convention.
23. **Editorial pieces argue.** They make a position claim and defend it. The claim is in the front matter and the closing reaffirms it without softening.
24. **Methodological pieces walk through a system.** They open with what the system does, walk through how, and end with what the system does and does not commit to.
25. **Research papers report findings on data.** They follow problem, prior work, method, results, discussion. They cite. The synthetic-data guardrail (any AUC > 0.95 on synthetic cohorts is flagged as overfitting the synthesis, not as good) is enforced if synthetic data is used.

### VII. Quantification gate

26. **Numbers carry units and stakes.** `1B+ records` is correct; `lots of records` is wrong; `1B+` without a unit is wrong.
27. **Numbers are contextualized within the same sentence or the next sentence.** `Reduced core processing time from 150+ hours to 24-36 hours` is correct because the reader can see the magnitude of the change. `Reduced processing time substantially` is wrong.
28. **Synthetic data is labeled as synthetic on first reference.** `400 simulated participants`, `6,000 synthetic account records`, never `400 participants` without qualification.

### VIII. Closing gate

29. **The last paragraph does not contain `In conclusion`, `In summary`, `To wrap up`, or any equivalent.** The piece ends; it does not announce the ending.
30. **The last paragraph does not invite the reader anywhere.** No `Read more`, no `Get in touch`, no `Learn more about`. The next-chapter component, if used, is a separate component below the prose and is not part of the closing paragraph.
31. **The last sentence is declarative.** Not interrogative, not imperative, not exclamatory.
32. **The last sentence states the contribution and stops.** It does not summarize the steps, it states the conclusion the steps support, in concrete technical language.

### IX. Authorship gate

33. **The prose describes work that was actually done.** Open the draft and identify every claim that names a system, an architecture, a result, a cohort, or a design choice. For each one, confirm that the underlying artifact exists. The page does not describe a thought experiment as if it were a deployed system, and it does not describe a deployed system as if it were a thought experiment.
34. **First-person `I` appears in the past tense for completed work.** `I built the pipeline`, `I generated the synthetic cohort`, `I considered learning the cross-domain weights and decided not to`. The author is the agent of the verbs that describe choices she made.
35. **The system appears as the grammatical subject in the present tense for what it does at runtime.** `The architecture commits to a per-domain submodel structure`, `the recommendation layer softens its language at the moment the ensemble disagrees`. The system is the agent of the verbs that describe its current behavior.
36. **Subjunctive constructions describe genuine counterfactuals only.** Search the draft for `would build`, `would design`, `would want`, `would have`, `if I were`, `I'd build`, `I'd design`, `I'd want`, `if I had`. Each hit must describe either a design alternative the author actually weighed and rejected (`I considered learning the cross-domain weights and decided not to: the meta-learner would mostly be memorizing the synthesis`), or a forward-looking contingency on a stated precondition (`a real deployment would need a re-calibration cadence`). Subjunctive describing the system itself, when the system was actually built, is wrong; replace with the indicative past tense (`I built X`) or the declarative present (`X does Y`).
37. **Numbers reported in prose match the source artifact.** Open the underlying notebook, dataset, or experiment record. Confirm cohort size, prevalence, AUC, F1, sensitivity, specificity, calibration error, and any other reported number against the source. A number on the page that does not match the source is wrong, regardless of how minor the discrepancy seems; reconcile to the source before submitting.

---

## Appendix A: The grammatical-subject rule, illustrated

The grammatical-subject rule is the load-bearing rule in this document. Most other rules follow from it. The rule is: the system, the methodology, the problem, or the approach is the subject of most sentences. First-person `I` is permitted but secondary. `We` is reserved for the field. `You` is almost never used.

The rule is illustrated by replacing common authorial constructions with their system-as-subject equivalents.

| Authorial form | System-as-subject form |
|---|---|
| `I built a dual-model pipeline that...` | `The pipeline separates conversion probability from expected deal value...` |
| `We engineer an integrated dual-model pipeline.` | `The architecture is integrated and dual-model.` |
| `I trained the classifier on the held-out fold.` | `The classifier was trained on the held-out fold.` |
| `We force the network to respect the minority class.` | `The network is forced to respect the minority class through scale_pos_weight.` |
| `I considered learning the cross-domain weights and decided not to.` | (Permitted as written; the author is the genuine agent of a discarded choice.) |
| `You can see in Fig. 1 that...` | `Fig. 1 shows that...` |
| `We have known since Zadrozny and Elkan (2002) that isotonic regression...` | (Permitted as written; `we` refers to the field.) |

The rule is not a syntactic transformation. It is a posture. The author is not the protagonist of the page. The system is.

## 7. IP Anonymization and Methodological Conversion

**We never sell a product. We never leak a vendor.** The portfolio represents deeply technical work from highly secure environments. Any historical project notes must be anonymized and converted into objective, didactic methodology.

*   **Rule 1: Anonymize All Proper Nouns.** Replace all proprietary vendor names, internal tools, and company names with precise, structural classifications.
    *   *Instead of:* "We used Equifax and Zendesk at Spokeo."
    *   *Write:* "The architecture ingested Tier-4 regulated bureau data and Tier-2 telemetry."
    *   *Instead of:* "PDL and Versium overlap."
    *   *Write:* "External identity aggregators overlap."
*   **Rule 2: Transmute to Methodology.** The focus of a case study is never the product itself. The focus is the epistemic architecture and mathematical trade-offs required to build that class of system.
*   **Rule 3: Eliminate Marketing Pitch.** Strip all product marketing language ("seamless", "revolutionary", "pipeline supremacy"). Use strict architectural terminology ("continuous link-quality scoring", "decoupled architecture").

---

## Appendix B: When this document is wrong

This document is supposed to describe the voice already on the page, and to extrapolate from the canonical specimens to cases the specimens do not cover. When this document and a canonical specimen disagree, the specimen is correct, and this document is updated to match. The canonical specimens are, in priority order:

1. `design_system/ui_kits/case-study/clinical-validation.html` (methodological genre).
2. `index.html` and the executive profile pages (third-person bio register).
3. Any future page authored under direct guidance and ratified.

If a future case is genuinely not covered by this document or by any specimen, the authoring agent should ask, not guess.
