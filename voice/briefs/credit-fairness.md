# Brief: credit-fairness.html

> Forward brief for the second methodology-essay specimen.
> A worked example of writing about an audit that found no
> disparate impact, without inflating the finding into either a
> victory lap or a manufactured controversy.

**File:** `design_system/ui_kits/case-study/credit-fairness.html`
**Source material:** `source_reference/credit-fairness.html`,
`Pm_html/Credit_Fairness/Upstart_Credit_Policy_Report.pdf` and
its companion notebook.

---

## 1. The single-sentence thesis

```
THESIS:
A fair-lending audit modeled on Upstart's underwriting framework
ran two policies against a 100,000-applicant synthetic cohort,
applied three regulatory-inspired screens (the 80% rule on approval,
a 5-point default-deviation flag, a 10% revenue-deviation flag),
and returned no fairness flags on race or immigration status; the
piece is about what the audit had to do to be allowed to return that
finding without it counting as evidence the system is fair.
```

The thesis is long because the headline finding is short. A reader
who reads only the thesis arrives at the structure of the argument:
the audit is interesting because it could have failed in three
different ways, did not, and the page is about what made that
result trustable rather than what made it positive.

---

## 2. The genre

- [ ] Executive profile
- [ ] Case study
- [x] **Methodology essay / working note**
- [ ] Thinking tool
- [ ] Research index card
- [ ] Position piece / letter

This is the second methodology essay in the portfolio. Clinical-
validation is the gold standard for "the system commits to being
honest about what it does not know." Credit-fairness is the gold
standard for "the audit commits to being honest about a negative
finding." The two pages share a chrome and a register; what
differs is the move each one is making.

---

## 3. The speaker

```
SPEAKER:        Dr. Heather Leffew, as the agent of the audit.
                The audit pipeline is the grammatical subject of
                most sentences; the analyst appears as `I` only
                when an architectural choice has to be owned.
PRIMARY TENSE:  Past tense for the audit run (the cohort was
                generated, the model was trained), present tense
                for structural claims about the screens (the 80%
                rule fires when any group's approval rate falls
                below four-fifths of the highest group's rate).
PERSON:         First person `I` used sparingly. System-as-subject
                most often. `We` reserved for the field at large.
                `You` does not appear.
PERSON SHIFTS:  None inside a section.
```

---

## 4. The negative space

```
NOT A CLAIM ABOUT: real Upstart approval data. The cohort is
                   synthetic, generated to match published Upstart
                   distributional summaries; the policies are
                   modeled on the public report.
NOT A CLAIM THAT:  Upstart's production system is fair. The page
                   has no production access. The audit is a
                   methodology demonstration on synthetic data
                   built to match Upstart's stated parameters.
NOT EVIDENCE THAT: a no-flag result generalizes to deployment.
                   A null finding on synthetic data with a
                   78.3%-accurate logistic model is the floor for
                   continued auditing, not the ceiling.
NOT A POSITION ON: whether algorithmic underwriting is fair in
                   general. The page is about what one audit did
                   on one cohort under three named screens.
```

The negative-space declaration appears verbatim near the top of
section 01: *"The audit ran on a synthetic cohort and a logistic
model with 78.3% accuracy; the result is the floor for continued
auditing, not a clearance for the production system, and the page
is written so a reader who skims only the headline cannot mistake
the one for the other."*

---

## 5. The structural argument

```
01 / Setup:
     The audit is a methodology demonstration, not a clearance.
     Synthetic 100,000-applicant cohort. Two policies. Three
     regulatory-inspired screens. The negative-space declaration.

02 / The cohort:
     Generated against Upstart's published distributional
     summaries; financial features and protected-class features
     drawn separately so the model can be trained without the
     latter and audited with them.

03 / The two policies:
     Baseline: 640 credit, 40% DTI, 12 months employment.
     Test: 600 credit, 45% DTI, 6 months employment, college
     graduate, enhanced income verification. The compensating-
     factor logic explained, and the outcome named: a 20.9-point
     drop in approval rate driven primarily by the college
     graduate clause.

04 / The three screens:
     The 80% rule on approval rate; the 5-point default-deviation
     flag; the 10% revenue-deviation flag. Each one named, each
     one tied to a regulatory source (ECOA / Regulation B,
     CFPB examination procedure, internal fair-lending risk
     framework).

05 / The model:
     Logistic regression, 78.3% cross-validated accuracy, trained
     on financial features only with protected-class features
     held out. SHAP applied for explanation, not for inference;
     the three top drivers (income, loan amount, DTI) account
     for roughly 78% of predictive power.

06 / The result:
     No flags on race or immigration. Approval-rate spread
     across race within four points (56.4% Asian to 57.2% Other);
     chi-square on race p=0.83. Default-rate spread within 0.04
     points. Revenue spread within $20 per account. The result
     stated plainly, then contextualized.

07 / What a null finding does and does not earn:
     The argument the page exists to make. A no-flag run is the
     floor for continued auditing, not a clearance. The screens
     calibrated to a 78.3%-accurate model on a synthetic cohort
     cannot speak to production. The screens themselves are
     conservative thresholds; a borderline pass under the 80%
     rule is not the same as substantive equity.

08 / What the work commits to:
     The audit pipeline as ongoing infrastructure rather than a
     one-time clearance. Quarterly re-runs. Proxy-variable
     monitoring. Documentation of business necessity for any
     criterion that survives a future flag. The closing
     methodology callout: what the audit is and what the audit
     is not.
```

Eight sections, each one a distinct move. The page is structurally
parallel to clinical-validation; the moves differ because the
genre move differs (a clinical specimen owns its uncertainty; an
audit specimen owns its null finding).

---

## 6. The opening move

```
OPENING SENTENCE:
What follows is a methodology walkthrough for a fair-lending
audit modeled on Upstart's underwriting framework, run against a
100,000-applicant synthetic cohort under three regulatory-inspired
screens; the audit returned no fairness flags, and the page is
written to be honest about what a null finding under those
conditions does and does not earn.
```

Names the artifact (a fair-lending audit), the institutional
reference (Upstart), the data condition (synthetic), the screen
count (three), the result (no flags), and the framing (honest
about what the result earns). A reader who reads only the first
sentence cannot read past it thinking the audit cleared a
production system.

---

## 7. The closing move

```
CLOSING SENTENCE:
The audit as it stands commits to a synthetic cohort matched to
public distributional summaries, three regulatory-inspired screens
each tied to a named source, a logistic model trained without
protected-class features and audited with them, and a result
treated as the floor for continued auditing rather than as a
clearance; the four commitments together are what the audit is,
and what the audit is not is a license for the policy to skip its
next quarterly re-run.
```

The same closing shape as clinical-validation: four commitments
restated, the negative space restated, no CTA, no link out. The
sentence is constructed so the last image the reader carries is
the next quarterly re-run, not the no-flag result.

---

## 8. The refusals (page-specific)

```
THIS PAGE REFUSES:
- To present the no-flag result as evidence the production
  Upstart policy is fair. The audit is on a synthetic cohort
  built from public summaries.
- To claim the 80% rule, the 5-point default deviation, and the
  10% revenue deviation are sufficient screens for fair lending.
  They are conservative thresholds, jointly the floor.
- To use the SHAP analysis as inference. SHAP attribution is a
  local explanation of one model's predictions on one cohort,
  not a causal claim about real-world income or DTI.
- To recommend the test policy on the basis of the audit alone.
  The test policy passed three screens; it also dropped approval
  by 20.9 points, an outcome a real lender would have to weigh
  against access goals separately.
- To present the synthetic-bias-injection demo from
  source_reference/credit-fairness.html (Black +0.12, Latinx
  +0.10 log-odds modifiers, 32% vs 19% default spread) as the
  same study. That demo is a *separate* exercise validating the
  audit screens against a deliberately biased cohort. The
  Upstart-aligned audit is what this specimen documents.
```

The last refusal is load-bearing. The two artifacts in the source
material are different studies with different findings; the page
must not collapse them, because doing so would let the reader
mistake the bias-injection demo's dramatic numbers for the actual
audit's null finding, or vice versa.

---

## 9. The interactive contract

Not applicable. This page is a methodology essay. Figures are
static SVGs: the cohort distribution, the policy comparison
table, the three audit-screen results, the SHAP feature
importance bar chart, the per-group fairness panel.

If the page were a thinking tool, the audit-screen panel in
section 04 might become interactive, with sliders for the three
thresholds and a live recomputation of pass/fail. The page is
not a thinking tool, so the screens are static and the
thresholds are documented in prose.

---

## 10. The exit gate

After drafting, the page is checked against `voice/checklist.md`.
The four hardest items for this page are:

- *VII.27 (no fuzzy quantifiers).* The audit produces precise
  numbers (20.9 points, 78.3% accuracy, p=0.83, $20 spread).
  Any sentence that says `roughly` or `substantially` should be
  rewritten with the actual number.
- *VIII.30 (no concession-then-pivot).* The page is full of
  natural-feeling pivots (the screens didn't fire, *but* a null
  result on synthetic data isn't a clearance). Each pivot has
  to be checked: is it doing analytic work, or is it a rhetorical
  tic? The clinical-validation specimen has roughly four
  legitimate pivots; this page should be in the same range.
- *VIII.32 (no closing hortatory beat).* The closing must not
  read as `here's what we should do next`. It should restate
  what the audit is and what the audit is not, and stop.
- *Brief-specific.* The page must not let a reader mistake the
  no-flag result for production clearance. Every section that
  reports an audit metric must, somewhere in its prose, name
  the synthetic-cohort condition or the 78.3%-accuracy ceiling.

---

## How this brief generalizes

Any future audit-genre methodology essay should produce a brief
with this shape:

- A thesis that names the screens, the cohort, the result, and
  the question the page exists to answer.
- A negative-space declaration at least as substantial as the
  positive claim, because audit findings travel further than
  their conditions.
- A section spine where the result is named in section 06 and
  re-framed in section 07. The reader meets the number twice:
  first as the headline, second as the contextualized headline.
- An opening sentence that makes it impossible to skim the page
  into a clearance.
- A closing sentence that ends on what the audit does not buy
  rather than on what the audit accomplished.
