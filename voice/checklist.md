# VOICE.md exit checklist

> The deterministic exit gate for any prose written under the Portfolio voice. Run every item before submitting a draft. Each item is yes/no; a single failure means the draft is not ready.
>
> This file is a companion to `design_system/VOICE.md`. The full reasoning behind every rule lives there. This file exists so an authoring agent can load just the gate when it is finishing a piece.
>
> Thirty-six items, nine gates.

---

## I. Punctuation gate

1. **Zero em dashes (—) in sentences.** Search the document for the character `—`. If any are present in prose, replace with a comma, semicolon, colon, or parenthetical. (Em dashes are permitted only inside quoted material, code blocks, or bibliography entries.)
2. **Zero en dashes (–) in sentences.** Same rule. The en dash is allowed in numeric ranges inside figures and tables (`2019–2024`) but never in prose.
3. **Hyphens are fine.** `dual-model`, `cross-domain`, `model-disagreement` are correct. Do not replace hyphens with em dashes to imply emphasis.
4. **Pauses use commas, semicolons, colons, or parentheticals.** Every pause that would have been an em dash maps to one of these four. Default to the comma; reach for the semicolon when the two clauses could each stand alone; reach for the colon when the second clause expands or specifies the first; reach for parentheses when the aside is genuinely parenthetical.
5. **Oxford commas always.** No exceptions.

## II. Grammatical-subject gate

6. **The system, methodology, problem, or approach is the subject of most sentences.** Open the draft and read the first word of every sentence in the first paragraph. If more than one of them is `I`, `We`, or `You`, the paragraph is wrong.
7. **First-person `I` is permitted but secondary.** Use it where the author is genuinely the agent of an action that cannot be described impersonally without distortion (`I generated the synthetic cohort`, `I considered learning the cross-domain weights and decided not to`). Do not use `I` to narrate work that the system itself performs (`I trained the model` is wrong; `the model was trained on a held-out fold` is right).
8. **`We` is reserved for the field, not the author.** `We have known since Zadrozny and Elkan (2002) that…` is correct. `We engineer an integrated dual-model pipeline` is wrong; the pipeline is the subject of that sentence, not the author.
9. **`You` is almost never used.** The reader is not addressed. Exceptions are explicit instructions inside a code block or a `Quick Start` section.

## III. Vocabulary gate

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

## IV. Structural-rhetoric gate

13. **No parallel contrarian structures.** Search for the phrase shapes:
    - `Not X, but Y` / `Not just X; Y`
    - `Less X, more Y`
    - `We don't X, we Y` / `It isn't X, it's Y`
    - `The question was never X, the question was Y`
    Any hit means the sentence is rewritten as a direct positive claim.
14. **Headers follow genre.** In methodological pieces and case studies, headers describe the technical mechanism plainly: `Mapping the Resolution Layer` is correct; `When an AUC Is Not a Success` is wrong for those genres. In editorial pieces and position pieces, argumentative headers are correct: they name the specific claim or observation the section makes. The test is not whether the header sounds bold — it is whether the header is specific and earned. Vague hooks ("The Hidden Truth About...") are wrong in any genre; specific argumentative headers ("When the Validity Check Fires") are correct in editorial work.
15. **No rhetorical questions.** Including the kind that organize an explanation. The question form is not used.
16. **No bare-demonstrative sentence openers.** Search for sentences beginning with `This `, `That `, `These `, `Those `, or `Which ` where the next word is not a noun anchoring the demonstrative. Each hit is a signal that the sentence wants to be the second clause of the previous sentence; attach it via semicolon, colon, or subordinate conjunction (`which`, `where`, `because`), with the antecedent inside the joining clause. Sentence-initial `It` is excluded from this rule. The full positive form of the rule is in VOICE.md section 5.1.
17. **No clipped-pair connections.** Search for adjacent short sentences where the second sentence's first word is a connective or demonstrative referring back to the first (`This`, `That`, `These`, `Those`, `Then`, `So`, `Thus`, `Therefore`, `As a result`). Each hit is a signal that the connection between the two ideas should be carried inside one sentence with a colon, semicolon, or subordinate clause, rather than split across two. The Portfolio voice is comfortable with long, clause-rich sentences when the underlying material is connected; see VOICE.md section 2.4.
18. **No marketing register in closings.** The final paragraph does not call to action, does not summarize benefits, does not invite the reader to do anything. It states a quiet declarative fact and stops.

## V. Analogy gate

18. **Analogies are permitted only if they are functional or mechanical.** `A two-pass filter`, `a gating mechanism`, `a held-out fold` are correct. `A symphony`, `a tapestry`, `a dance` are wrong.
19. **Analogies are banned if they over-simplify in a condescending direction.** `Imagine you have a box of marbles` is condescending toward a technical reader; do not write it. The reader is assumed to be intelligent and unfamiliar with this specific specialty, not stupid.
20. **The math is the proof, not the analogy.** If a passage relies on an analogy to make its point and the analogy were removed, the technical content should still stand on its own. If it would not, the technical content is incomplete and the analogy is masking it.

## VI. Genre gate

21. **The piece is in one of three genres: editorial, methodological, research paper.** Confirm which. Each has its own front matter, register, and closing convention. See `VOICE.md` section 4.
22. **Editorial pieces argue.** They make a position claim and defend it. The claim is in the front matter and the closing reaffirms it without softening.
23. **Methodological pieces walk through a system.** They open with what the system does, walk through how, and end with what the system does and does not commit to.
24. **Research papers report findings on data.** They follow problem, prior work, method, results, discussion. They cite. The synthetic-data guardrail (any AUC > 0.95 on synthetic cohorts is flagged as overfitting the synthesis, not as good) is enforced if synthetic data is used.

## VII. Quantification gate

25. **Numbers carry units and stakes.** `1B+ records` is correct; `lots of records` is wrong; `1B+` without a unit is wrong.
26. **Numbers are contextualized within the same sentence or the next sentence.** `Reduced core processing time from 150+ hours to 24-36 hours` is correct because the reader can see the magnitude of the change. `Reduced processing time substantially` is wrong.
27. **Synthetic data is labeled as synthetic on first reference.** `400 simulated participants`, `6,000 synthetic account records`, never `400 participants` without qualification.

## VIII. Closing gate

28. **The last paragraph does not contain `In conclusion`, `In summary`, `To wrap up`, or any equivalent.** The piece ends; it does not announce the ending.
29. **The last paragraph does not invite the reader anywhere.** No `Read more`, no `Get in touch`, no `Learn more about`. The next-chapter component, if used, is a separate component below the prose and is not part of the closing paragraph.
30. **The last sentence is declarative.** Not interrogative, not imperative, not exclamatory.
31. **The last sentence states the contribution and stops.** It does not summarize the steps, it states the conclusion the steps support, in concrete technical language.

## IX. Authorship gate

32. **The prose describes work that was actually done.** Open the draft and identify every claim that names a system, an architecture, a result, a cohort, or a design choice. For each one, confirm that the underlying artifact exists. The page does not describe a thought experiment as if it were a deployed system, and it does not describe a deployed system as if it were a thought experiment.
33. **First-person `I` appears in the past tense for completed work.** `I built the pipeline`, `I generated the synthetic cohort`, `I considered learning the cross-domain weights and decided not to`. The author is the agent of the verbs that describe choices she made.
34. **The system appears as the grammatical subject in the present tense for what it does at runtime.** `The architecture commits to a per-domain submodel structure`, `the recommendation layer softens its language at the moment the ensemble disagrees`. The system is the agent of the verbs that describe its current behavior.
35. **Subjunctive constructions describe genuine counterfactuals only.** Search the draft for `would build`, `would design`, `would want`, `would have`, `if I were`, `I'd build`, `I'd design`, `I'd want`, `if I had`. Each hit must describe either a design alternative the author actually weighed and rejected (`I considered learning the cross-domain weights and decided not to: the meta-learner would mostly be memorizing the synthesis`), or a forward-looking contingency on a stated precondition (`a real deployment would need a re-calibration cadence`). Subjunctive describing the system itself, when the system was actually built, is wrong; replace with the indicative past tense (`I built X`) or the declarative present (`X does Y`). The full positive form of the rule is in VOICE.md section 2.7.
36. **Numbers reported in prose match the source artifact.** Open the underlying notebook, dataset, or experiment record. Confirm cohort size, prevalence, AUC, F1, sensitivity, specificity, calibration error, and any other reported number against the source. A number on the page that does not match the source is wrong, regardless of how minor the discrepancy seems; reconcile to the source before submitting.

---

If all 36 items pass, the draft is releasable.
