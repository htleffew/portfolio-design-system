# Specimens

> The exemplars per genre. What to copy. What not to copy.

The brief at `voice/brief.md` asks the writer to choose a genre. Each
genre points here. This document tells the writer which file in the
project is the canonical exemplar for that genre, what the file
demonstrates well, and what the file does NOT generalize.

The lesson the AI-adoption rewrite taught: templates are dangerous when
not annotated. Cloning the eight-section structure of the clinical
specimen produced ceremony for an argument that needed four sections.
**Clone the chrome, not the section count.** The writer copies the
publication shell (band system, sidenote pattern, eyebrow style,
methodology callouts, back matter chrome) and then writes the section
spine the argument actually requires.

---

## 1. Methodology essay / working note

**Canonical exemplar:** `ui_kits/case-study/clinical-validation.html`

**What to copy:**
- The publication shell (atmosphere, top nav, side spine, status strip,
  footer) and the dark/paper band alternation.
- The front-matter pattern: meta-row, single declarative title, italic
  abstract, three-cell byline grid (cohort / architecture / output, or
  the genre-appropriate equivalents).
- The drop-cap convention on the first paragraph of section 01 only.
- The `.gloss` inline glossary for jargon the reader is expected not to
  know yet, with a tooltip body that defines without condescending.
- The `.sn` sidenote pattern for caveats, citations, and deployment
  notes the main column should not carry.
- The methodology callout (`.method`) for asides that earn their own
  block: hard guardrails, design decisions, what-this-is-not
  declarations.
- The `.figure` + `.cap` figure pattern with the `Fig. N , ` numbering.
- The `.stats` strip for four-number summaries; never more than four.
- The bibliography + citation graph + related-cards back matter.

**What NOT to copy:**
- **The section count.** This page has eight sections because it has
  eight moves. Most methodology essays do not have eight moves. Copy
  the band-alternation pattern (paper / dark / paper / dark) and let
  the section spine follow the argument.
- The specific SVG figures. The gaze-overlap density chart, the
  ensemble-bar plot, the calibration curve, the recommendation grid
  are bespoke to the ADOS-2 argument and do not generalize.
- The bibliography entries. The literature on a methodology essay is
  the literature of that methodology, not this one.
- The first-person frequency. This page uses `I` heavily because the
  methodology was the author's. A methodology essay where the
  methodology is borrowed should use `I` more sparingly.

**Genre signals the page demonstrates:**
- Past tense indicative for what was done, present tense for structural
  claims.
- Synthetic data with disclosure: the page declares the cohort is
  synthetic in section 01 and reiterates the limitation in the
  methodology callout.
- Negative-space declaration: *"There is no clinical claim and no
  deployment."*
- Section 03 closing paragraph: rhetorical questions used to organize
  the next section, not as marketing hooks.

---

## 2. Thinking tool

**Canonical exemplar:** `ui_kits/case-study/ai-adoption.html`

**What to copy:**
- The four-section structure (setup, the math, the sandbox, what the
  model teaches). This is the right number of moves for a thinking-tool
  argument; it is not the right number for a methodology essay.
- The interactive sandbox pattern: three sliders, three KPIs, an SVG
  plot, and inline JS. The sliders control coefficients, not estimates.
  The KPIs derive from the curve, not from a database.
- The math strip (`.math-strip` + `.math-block`) for the equations
  expressed in the canonical mono register.
- The closing methodology callout titled *"What this page is not"*.
  Every thinking-tool page should have this callout. It is the page's
  honesty.

**What NOT to copy:**
- The specific exponents. `t^1.85` and `e^(-t/4.5)` are stylized
  choices for the J-curve argument; another thinking-tool page should
  pick exponents that produce the qualitative shape its argument
  requires, and should disclose the choice in a methodology callout.
- The system-as-subject register if the page is documenting a personal
  methodology. Thinking tools where the author is the agent should use
  first person `I`; thinking tools that are about a structural
  intuition should use system-as-subject.

**Genre signals the page demonstrates:**
- Present tense throughout for structural claims.
- The page is honest about being stylized: *"The exponents were chosen
  for shape, not estimated from data."*
- The closing names what the page commits to: the qualitative shape,
  not the specific values.
- The interactive element is the lesson, not a decoration.

---

## 3. Executive profile

**Canonical exemplar:** `ui_kits/profile/profile.html`
(forward brief at `voice/briefs/profile.md`).

**What to copy:**
- The paper-only band system. The profile is the one genre that
  refuses the dark/paper alternation; the page is read in one
  register, top to bottom, and switching backgrounds at it would
  make a five-section page feel like a long one.
- The simplified chrome: top nav and footer carried from the
  methodology specimen, *no* spine, *no* status strip, *no*
  reading-progress bar, *no* hover-preview portal. A profile is
  too short to warrant any of them; the chrome the methodology
  page uses to keep a reader oriented across twenty-two minutes
  is exactly the chrome a profile does not need.
- The five-section spine (`Positioning / Current work / Trajectory
  / Selected work / Contact`) as a *floor*, not a ceiling. A profile
  with four sections is fine; a profile with eight sections is a CV.
- The opening move: a single declarative sentence that names the
  person, the field, and the kind of work, in that order, before any
  italic abstract or affiliation strip. The reader should know within
  the first sentence whether the page is for them.
- The affiliation strip pattern (`Field / Register / Posture` in
  this exemplar) as the profile's analog of the case-study byline.
  Three short labels, one declarative phrase under each, in italic.
  Names the work's genre and discipline, not the author's titles.
- The selected-work grid as the same `.r-card` pattern the
  case-study back matter uses. Three to five cards. Eyebrow,
  title, one-sentence description, `Read &rarr;`. The cards link
  out to the full pieces; the profile is the index, not the prose.
- The closing line: a single italic sentence, declarative, that
  hands the reader to the work, followed by one line of contact
  links. No form, no calendar embed, no newsletter signup, no
  call-to-action language.

**What NOT to copy:**
- The hero photograph, hero illustration, or any centered portrait
  treatment. The profile carries a single quiet calibration arc as
  ambient background, the same primitive the methodology specimen
  uses; the *person* the profile is about is named in the prose,
  not depicted in the chrome.
- The methodology specimen's drop-cap on section 01. The profile's
  positioning section is a register declaration, not the opening of
  a long argument; a drop-cap there reads as ceremonial.
- The methodology and case-study chrome's reading-progress bar,
  side spine, and status strip. A five-section paper-only page is
  navigated by scrolling; supplying readout chrome for a page that
  doesn't need it is the kind of thing a profile rejects on purpose.
- The case-study back-matter pattern (bibliography, citation graph,
  next chapter). The profile is itself the index of the back matter;
  there is no further reading after a profile, only further pieces.

**Genre signals the page demonstrates:**
- Third person throughout. `Dr. Heather Leffew` on first reference,
  `Dr. Leffew` thereafter, `Heather` never. The page does not
  contain `I`, `we`, or `you`; the discipline is in the prose, not
  in a lint rule.
- Present tense for current work and ongoing affiliations, past
  tense for completed positions and degrees, present-perfect for
  the arc statements. Each section commits to one tense and stays
  there.
- The trajectory section names institutions (`TikTok USDS`,
  `Spokeo`, `Fielding Graduate University`) and not job titles.
  The profile is positioning the *register* of the work, not the
  rank of the author.
- The closing is one declarative sentence and a one-line contact
  block. No `Reach out`, no `Get in touch`, no `Available for`.
  The work is the offer; the writing is how to read it.
- No skill bullets, no stack lists, no `Tools I use` blocks. The
  reader is reading a portfolio, not hiring a stack; the technical
  vocabulary surfaces in the methodology essays where it earns its
  place against an argument.

---

## 4. Case study

**Canonical exemplar:** `ui_kits/case-study/entity-resolution.html`
(forward brief at `voice/briefs/entity-resolution.md`).

**What to copy:**
- The publication shell (atmosphere, top nav, side spine, status strip,
  footer) and the dark/paper band alternation. The case-study page
  borrows it from the methodology specimen on purpose; the chrome is
  the genre's chrome, not the methodology's.
- The seven-section spine (`Setup / Architecture / Stability / Defect /
  Repair / ML benchmark / Verdict`) as a *shape*, not a count. Every
  case-study section title is a finding, not a phase number; the phase
  numbers belong in the artifacts the back matter cites, not in the
  display titles.
- The front-matter byline strip rewritten for case-study material:
  `Domain / Surface area / Cadence` instead of the methodology page's
  `Cohort / Architecture / Output`. The grid is the same; the labels
  are genre-appropriate.
- The "Calibration" abstract pattern: a two- or three-sentence
  italic block under the title that names the situation, the
  measurement, and the verdict. The reader who reads only the abstract
  should leave with the case study's actual finding, not with a hook.
- The methodology callout (`.method`) used here for *evidence
  retention* and *what was learned* — the two most genre-specific
  callouts. Every case study should have a "what was learned"
  callout in the closing section, in plain language.
- The number-grid pattern (`.stats` + `.figure` strips). For a case
  study the numbers are the operational outcomes, not the model
  metrics: hours per iteration, records repaired, defect count,
  squads consuming. Four numbers, no more.
- The bibliography of *internal artifacts* (memos, gates, validation
  packets) plus a citation graph. A case study cites the work that
  produced it, not the academic literature behind the technique.
- The closing posture: quiet, not triumphant. The verdict section
  ends on what the program *taught* (production lore is data, the
  data was wrong, the rebuild instinct is the default), not on an
  architecture hero shot.

**What NOT to copy:**
- **The first-person frequency from the methodology specimen.** The
  case-study voice is third-person or system-as-subject. `I` appears
  rarely and only where the first-person admission is doing real
  work — the team's bias toward rebuilding, the assumption the author
  had to give up. The methodology specimen's drop-cap "I noticed
  early" opening is the wrong opener for a case study.
- The specific seven-section spine. This page has seven moves because
  it has seven moves: situation, undocumented architecture, stability
  measurement, located defect, surgical repair, ML benchmark, verdict.
  A case study with a different shape (a recalibration with no repair,
  a rebuild that succeeded, a measurement that vindicated lore) should
  follow its own argument.
- The specific numbers and SVGs. The 0.004% churn figure, the
  17-rule cascade diagram, the 11-gate review, the calibration arc in
  the front matter, the `.cite-graph` topology — all are bespoke to
  the Spokeo program. The patterns generalize; the values do not.
- The internal-artifact bibliography format. Another case study may
  cite external papers, regulatory documents, or trial registrations;
  the format adapts. What does not adapt is the discipline of citing
  *something* — a case study with no bibliography is a press release.
- The architectural-review table treatment from section 07. That table
  is shaped by an eleven-gate bar and a Mixture-of-Experts proposal;
  another case study's verdict will be shaped by a different
  acceptance bar.

**Genre signals the page demonstrates:**
- Past tense indicative for the work, present tense for the structural
  claims (`The architecture is`, `The defect is local`, `The bounded
  posture stands`).
- The uncomfortable findings stated on the page, not buried in
  back-matter. The folk estimate was wrong by three orders of
  magnitude. The model learned to be the heuristic. The verdict was
  *not to rebuild*. Each is in the prose, in plain language, in the
  section it belongs to.
- Outcomes stated as numbers, then explained. `150+ hours → 24-36
  hours per iteration` stands as a sentence; the next paragraph says
  why, against what architecture, retained how.
- Mechanism over metaphor: `transitive closure`, `partial-null
  bridging`, `abstain surface`, `shadow mode`. Glossed inline via
  `.gloss` tooltips, not paraphrased into vagueness.
- The work is quantified, contextualized, and bounded. `0.004%` is
  given against the population it was measured on (96M records, the
  v14 retained set), the regime it holds in (steady-state churn, not
  bootstrap), and the evidence it survives (the conservative label
  packet from Wave 14).
- No softening verbs. The page does not say `we discovered`, `we
  uncovered`, `we found that`. It says `the heuristic was, on the
  evidence retrieved, mostly correct`.
- No claim of novelty in the techniques. Union-find, isotonic
  calibration, gradient-boosted trees, shadow deployment are all
  named without adornment. The contribution is the program's
  discipline, not the toolkit.

---

## 5. Research index card

**Canonical exemplar:** the related-cards in the back matter of the
methodology and thinking-tool specimens. See the `.r-card` pattern.

**What to copy:**
- Eyebrow (one or two words), title (a sentence), description (one
  sentence, declarative), reading-time / venue footer.
- No narrative arc. No opening or closing moves. The card is dense and
  finished.

---

## 6. Position piece / letter

**Canonical exemplar:** *to be written.*

Until this specimen exists, the brief should default to:

- First person `I`.
- Declarative throughout. The position is arrived at through doing the
  work, not through reading other people's work.
- No hedging language (`I think maybe`, `it seems possible that`).
- Opens with the position, not the buildup. Closes with the position
  restated as a commitment.

---

## How to use this document

1. Open `voice/brief.md`. Pick a genre.
2. Open the file at the genre's canonical exemplar path.
3. Read the *What to copy* and *What NOT to copy* sections above for
   that genre.
4. Read the exemplar end to end before drafting your own.
5. Fill in the brief.
6. Draft the page using the brief, not the exemplar, as the contract.
   The exemplar is the chrome reference, not the content reference.
7. Run the checklist as the exit gate.

If a genre's exemplar is *to be written*, the writer is allowed to
draft the page anyway, but the page becomes a candidate exemplar and
must be reviewed against the genre signals listed above before it is
shipped. The first page in a genre is held to a higher bar because it
sets the chrome reference for everything that follows.
