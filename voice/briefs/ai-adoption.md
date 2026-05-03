# Brief: ai-adoption.html

> Retroactive brief, written after the page exists. Used as a structural
> audit instrument: deltas between this brief and the actual page become
> a revision list. Also used as the worked example for the thinking-tool
> genre.

**File:** `design_system/ui_kits/case-study/ai-adoption.html`
**Genre:** Thinking tool

---

## 1. The single-sentence thesis

```
THESIS:
The depth of the early-month trough in the AI-adoption J-curve is the
variable that decides whether the curve compounds at all, and the
trough's depth is set almost entirely by the ratio of legacy debt to
talent density.
```

The page exists to deliver this one sentence. Every section either sets
it up, demonstrates it, or restates it. A reader who reads only the
thesis and the closing paragraph should arrive at the same claim.

---

## 2. The genre

- [ ] Executive profile
- [ ] Case study
- [ ] Methodology essay / working note
- [x] **Thinking tool**
- [ ] Research index card
- [ ] Position piece / letter

```
GENRE: Thinking tool.
```

The page is not a methodology essay. The methodology specimen at
`clinical-validation.html` walks through a built system; the AI-adoption
page walks through a stylized model the reader is expected to interact
with. The genres share publication chrome and refuse the same things,
but the section spine is different and the speaker is different.

---

## 3. The speaker

```
SPEAKER:        The system, as the grammatical subject. The page is the
                voice; the author is not the agent.
PRIMARY TENSE:  Present tense for structural claims; past tense only
                for the choice of exponents (the exponents were chosen).
PERSON:         System-as-subject throughout. First person `I` does not
                appear. The page is not documenting the author's
                methodology; it is documenting a structural intuition.
PERSON SHIFTS:  None.
```

The methodology specimen uses `I` heavily because the methodology was
the author's. This page does not, because the J-curve is not the
author's; it is a structural feature of general-purpose technology
adoption, well-established in the literature. The author is the
expositor, not the agent.

---

## 4. The negative space

```
NOT AN ESTIMATE OF: any organization's actual ROI on AI adoption.
NOT A CLAIM ABOUT:  the specific exponents being correct; they are
                    stylized, chosen for shape, not estimated from data.
NOT A RECOMMENDATION TO: push integration scope up or down. The model is
                    symmetric about that choice; the right answer
                    depends on coefficients the model does not know.
NOT A FORECAST OF:  any specific organization's breakeven horizon. The
                    sandbox produces qualitative structure, not
                    quantitative prediction.
```

The page must declare the negative space at least twice: once in
section 01 (the *teaching tool, not an estimate* framing) and once in a
closing methodology callout (the *what this page is not* block). The
existing page does both.

---

## 5. The structural argument

```
01 / Setup:
     Establish that the page is a thinking tool, not an estimate.
     Name the two-function model. Name the negative space.

02 / The two functions:
     Specify Cost(t) and Gain(t). Show the math. Show the resulting
     net curve as a static figure, with breakeven and trough markers.

03 / The sandbox:
     The interactive element. Three sliders, three KPIs, the live
     curve. The reader cannot read this section passively.

04 / What the trough teaches:
     The thesis, restated as a structural claim. Three corollaries
     follow. The closing methodology callout: what this page is not.
```

Four sections. Not eight. The clinical-validation specimen has eight
sections because it has eight moves; this page has four moves and four
sections. Forcing eight would produce ceremony. The brief commits the
page to four; the page must not exceed it.

---

## 6. The opening move

```
OPENING SENTENCE:
What follows is a thinking tool for one structural intuition about
enterprise AI adoption: the early-month trough is not a side effect of
the curve, the trough is the variable that decides whether the curve
compounds at all.
```

The opening sentence is the page's contract. It names the genre
(*thinking tool*), the subject (*enterprise AI adoption*), and the
thesis (*the trough is the variable*). The reader knows by sentence one
what the page is and what it is not.

---

## 7. The closing move

```
CLOSING SENTENCE:
The page is a thinking tool, in the same sense Olah's circuits writeups
are thinking tools: the math is the medium, the interaction is the
lesson, and the reader is expected to come away with a sharper
intuition about a tradeoff they already had to make.
```

The closing names what the page commits to (a thinking tool, not an
estimate) and stops. No CTA, no link out, no summary list of what was
covered.

---

## 8. The refusals (page-specific)

```
THIS PAGE REFUSES:
- To estimate any specific organization's coefficients. The sliders
  are coefficients, not estimates.
- To report any specific J-curve as the J-curve. The sandbox produces
  a curve at the reader's chosen coefficients; the curve is the
  reader's, not the page's.
- To use the subjunctive. The model exists; the math is written down;
  the sandbox runs. The page is not about a model that would be built;
  it is about a model that is built.
- To use the eight-section publication structure of the methodology
  specimen. Section count follows the argument.
- To dress the math in poetic analogy. Cost peaks and decays; gain
  compounds. No tapestries, no symphonies, no engines.
```

---

## 9. The interactive contract

```
INTERACTIVE ELEMENT: A three-slider sandbox driving an SVG plot and
                    three KPI readouts (max drawdown, breakeven horizon,
                    M24 net).

WHAT IT TEACHES:    The qualitative shape of the J-curve under three
                    coefficients. That the trough deepens when talent
                    is pulled down and scope is pushed up. That low-
                    talent + high-scope produces a curve that may
                    never recover.

WHAT IT DOES NOT TEACH: Any specific organization's actual breakeven.
                    The sandbox does not know the reader's
                    organization. It knows the structural shape.
```

---

## 10. The exit gate

After drafting, the page is checked against `voice/checklist.md`. The
checklist caught three real defects on the first verifier pass (missing
sandbox CSS, missing sandbox JS, stale PREVIEWS object) and would not
have caught the structural voice problems if any remained, because the
checklist is a surface gate.

---

## Audit: deltas between this brief and the page as written

After writing the brief, read the page section by section and list any
place the prose deviates from the contract above.

### Setup (§01)
- The opening sentence in the page matches the brief's opening sentence
  exactly. **Pass.**
- The negative-space declaration is present in the methodology callout
  (*"What the model is for"*). **Pass.**
- The dropcap convention is preserved on the first paragraph. **Pass.**

### The two functions (§02)
- The math strip carries the equations in canonical mono register. The
  brief did not specify whether the math should appear as a strip or
  inline; the strip works because the equations carry weight. **Pass.**
- The methodology callout (*"Why these specific exponents"*) discloses
  the stylization and refuses to claim the exponents were estimated.
  **Pass.**
- The figure (Fig. 1) shows Cost(t), Gain(t), and Net(t) with breakeven
  and trough markers. Static. **Pass.**

### The sandbox (§03)
- The sandbox is the centerpiece of the section. The CSS and JS were
  patched in after the verifier flagged them missing; the brief should
  have committed to them being present from the first draft, and the
  failure to do so is a process failure, not a brief failure. **Note.**
- The closing paragraph of §03 names what the sandbox is not. **Pass.**

### What the trough teaches (§04)
- The thesis is restated as the section's opening sentence. **Pass.**
- Three corollaries follow, each one declarative, each one tied to the
  thesis. **Pass.**
- The closing methodology callout *"What this page is not"* is present
  and explicit. **Pass.**

### Voice gates the brief commits to
- No subjunctive: the page does not say `I would build` or `if I were
  designing`. **Pass.**
- No first-person `I`: confirmed; the system is the subject throughout.
  **Pass.**
- No em or en dashes inside sentences: confirmed on a final scan.
  **Pass.**
- No banned vocabulary: confirmed; no `transform`, `leverage`,
  `seamless`, `robust`, `empower`, `journey`, `ecosystem`,
  `revolutionary`. **Pass.**
- No bare-demonstrative openers: confirmed; the previous audit caught
  these in the methodology specimen, and the AI-adoption rewrite did
  not introduce new ones. **Pass.**

### Where the brief was right and the prose followed it

The four-section structure is the place the brief did the most work.
Without the brief, the methodology-specimen template would have produced
eight sections and the page would have carried four sections of
ceremony. The brief's §5 *structural argument* test (*"if a section's
description starts with `discusses` or `walks through`, the section is
filler"*) would have rejected at least three of the would-be sections
on the first read.

### Where the brief would have caught the original failure

The original page (before this turn's rewrite) was a clone of the
clinical-validation specimen with the wrong content: ADOS-2 ensemble
prose at a URL named ai-adoption. The brief would have caught this in
§1 (the thesis sentence is about an AI-adoption J-curve, not about an
ADOS-2 pipeline) and again in §2 (the genre is thinking tool, not
methodology essay). Either gate would have rejected the page before
draft. The checklist did not catch it because the checklist tests the
surface, and the surface was clean clinical-validation chrome.

The brief is the instrument that catches this class of failure. The
checklist is the instrument that catches em dashes.
