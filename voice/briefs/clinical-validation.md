# Brief: clinical-validation.html

> Retroactive brief for the canonical methodology-essay specimen.
> Worked example for future writers in this genre.

**File:** `design_system/ui_kits/case-study/clinical-validation.html`
**Genre:** Methodology essay / working note

---

## 1. The single-sentence thesis

```
THESIS:
A three-domain ensemble screening pipeline aligned with the ADOS-2
rubric, built and stress-tested on synthetic data, can be honest about
what it does and does not know if it commits to per-domain submodels,
isotonic calibration, ensemble variance as a confidence band, and a
recommendation layer that softens its language when the models
disagree.
```

The thesis is long because the page is a methodology essay and the
methodology has four committed-to architectural choices, each of which
the page has to demonstrate. A reader who reads only the thesis and
section 08's closing paragraph arrives at the four commitments.

---

## 2. The genre

- [ ] Executive profile
- [ ] Case study
- [x] **Methodology essay / working note**
- [ ] Thinking tool
- [ ] Research index card
- [ ] Position piece / letter

---

## 3. The speaker

```
SPEAKER:        Dr. Heather Leffew, as the agent of the methodology.
                The system she built is the grammatical subject of most
                sentences; she appears as `I` when the action cannot be
                impersonalized without distortion.
PRIMARY TENSE:  Past tense for the work (the cohort was generated, the
                models were trained), present tense for structural
                claims about the architecture (the recommendation layer
                softens when the ensemble disagrees).
PERSON:         First person `I` used sparingly, system-as-subject
                most often. `We` reserved for the field at large.
                `You` does not appear.
PERSON SHIFTS:  None inside a section.
```

---

## 4. The negative space

```
NOT AN ESTIMATE OF: any real-world clinical performance. The pipeline
                    has not been validated on real participants.
NOT A CLAIM ABOUT:  AUC numbers being clinically meaningful. The
                    synthetic cohort has engineered overlap; any model
                    reporting AUC > 0.95 is flagged as overfitting the
                    synthesis.
NOT A RECOMMENDATION TO: deploy this pipeline. There is no clinical
                    claim and no deployment.
NOT A FORECAST OF:  what a real ADOS-2 automation pipeline would
                    achieve. The page is about the architectural
                    discipline, not the eventual performance.
```

The negative-space declaration appears verbatim in section 01:
*"There is no clinical claim and no deployment. The point is to think
publicly about what an assistive ML system for this setting would have
to commit to in order to be honest about what it does and doesn't
know."*

---

## 5. The structural argument

```
01 / Setup:
     The work is a research prototype, not a product. Synthetic data,
     hard guardrails, four architectural commitments named.

02 / Behavioral features:
     Three domains (social affect, communication, RRB), mapped to
     specific ADOS-2 items, computed from MediaPipe and Whisper-style
     features.

03 / The overlap problem:
     No single feature separates the diagnostic groups. Univariate
     separation is poor by construction. Plural architecture is
     required.

04 / Ensemble:
     Five model families per domain, soft-voted within domain, equal-
     weighted across domains. Why a meta-learner was rejected.

05 / Calibration:
     Isotonic on a held-out fold. Why isotonic and not Platt scaling.
     Reliability diagram.

06 / Disagreement:
     Ensemble variance as the epistemic-uncertainty signal. The
     recommendation language tracks the variance.

07 / Recommendation layer:
     Five-tier risk stratification crossed with four-level confidence.
     The recommendation grid. The softening rule.

08 / What the work commits to:
     Four architectural commitments restated. The closing methodology
     callout: what the work is not.
```

Eight sections, each one a distinct architectural move. The argument
genuinely has eight moves; cutting any one would leave a commitment
undemonstrated.

---

## 6. The opening move

```
OPENING SENTENCE:
What follows is a design walkthrough for a screening assistant aligned
with the ADOS-2 rubric, built and stress-tested on synthetic data as a
voluntary demonstration of applied clinical AI methodology.
```

Names the artifact (a screening assistant), the rubric (ADOS-2), the
data condition (synthetic), and the framing (voluntary demonstration).
The reader knows by sentence one what the page is and what it is not.

---

## 7. The closing move

```
CLOSING SENTENCE:
The architecture above commits to per-domain submodels, isotonic
calibration on a held-out fold, ensemble variance as the disagreement
signal, and a recommendation layer whose tone softens at the moment
the models stop agreeing; the four commitments together are what the
work is, and what the work is not is a deployment.
```

Quiet. The four commitments restated. The negative space restated.
No CTA. No link out.

---

## 8. The refusals (page-specific)

```
THIS PAGE REFUSES:
- To report any AUC > 0.95 on the synthetic cohort without flagging
  it as overfitting the synthesis. The synthesis is engineered to
  preserve clinical ambiguity; clean separability is a tell.
- To claim that any feature, including gaze-to-face percentage, is
  the signature of autism. The page reproduces, on synthetic data,
  the same overlap structure the published literature reports.
- To recommend deployment. The page is a methodology demonstration,
  not a product proposal.
- To use marketing register about the system's capabilities. The
  capabilities are quantified and contextualized; the limits are
  named in the same paragraph.
```

---

## 9. The interactive contract

Not applicable. This page is a methodology essay. Figures are static
SVGs (density curves, ensemble bar charts, calibration plot, the
recommendation grid). The reader reads; the reader does not interact.

If the page were a thinking tool, the recommendation grid in section 07
might become an interactive element where the reader sets a risk tier
and a confidence level and sees the recommendation language. The page
is not a thinking tool, so the grid is static.

---

## 10. The exit gate

After drafting, the page is checked against `voice/checklist.md`. The
canonical specimen scored 41/41 on the most recent audit pass after
five surface-level revisions (drop the `I think` hedge in §01, fix bare
`This` opener in §03, recast a rhetorical question as declarative in
§03, fix bare `Those` opener in §03, fix bare `That` opener in §05).

The page is the gold standard the checklist is calibrated against.

---

## How this brief generalizes

Any methodology-essay page should produce a brief with a similar shape:

- A long thesis sentence, because methodology essays commit to multiple
  architectural choices and each choice is part of the thesis.
- The genre selection (methodology essay / working note).
- A speaker block that uses past tense for the work, present tense for
  the structural claims, and first person `I` sparingly.
- A negative-space declaration that is at least as strong as the
  positive claim. If the page commits to AUC 0.79 on social affect, it
  also commits to flagging AUC > 0.95 as overfitting the synthesis.
- A section spine where each section is one architectural commitment,
  one piece of evidence for that commitment, or one pair of commitment
  + evidence.
- An opening sentence that names artifact, framing, and data condition.
- A closing sentence that restates the commitments and the negative
  space and stops.
- Page-specific refusals tied to the methodology being documented.

The methodology specimen does each of these. Future methodology essays
in the portfolio should produce a brief that matches in shape, even if
the content differs in every line.
