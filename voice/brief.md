# Brief

> The contract. Filled in before any prose is drafted.
> Prose that exceeds the brief or contradicts it is rejected before it is polished.

> One brief per page. Save as `voice/briefs/<slug>.md` alongside this template.

---

## 1. The single-sentence thesis

The one sentence this page exists to deliver. If you cannot write it
in one sentence, you do not yet know what the page is about and you
are not ready to write it.

```
THESIS:
```

Test: a reader who reads only the thesis sentence and the closing
paragraph should come away with the page's claim. If the thesis is
vague (`a discussion of`, `an exploration of`, `a look at`), rewrite
it until it commits.

---

## 2. The genre

Choose one. The genre determines person, tense, opening move, and
closing move. Mixed-genre pages do not work; the register collapses.

- [ ] **Executive profile** — third person, `Dr. Leffew`, bio register,
      no first-person `I`, opens with positioning, closes with current
      work. Reference: `specimens/profile/`.
- [ ] **Case study** — third person or system-as-subject, situated,
      quantified outcomes, opens with the problem and the constraint,
      closes with what was learned. Reference: `specimens/case-study/`.
- [ ] **Methodology essay / working note** — first person `I`, past
      tense for what was done, present tense for structural claims,
      synthetic data permitted with disclosure, opens with the setup,
      closes with what the work commits to. Reference:
      `specimens/methodology/clinical-validation.html`.
- [ ] **Thinking tool** — system-as-subject, present tense, the page
      includes an interactive element the reader is expected to use,
      opens with the model's intent, closes with what the model is and
      is not. Reference: `specimens/thinking-tool/ai-adoption.html`.
- [ ] **Research index card** — eyebrow, title, one-sentence body. No
      narrative arc. Used in lists and citation graphs.
- [ ] **Position piece / letter** — first person `I`, declarative,
      arrived at through doing the work, no hedging. Reference:
      `specimens/position/`.

```
GENRE:
```

---

## 3. The speaker

Who is writing this page, in what tense and person.

```
SPEAKER:        (e.g., Dr. Leffew, third person)
PRIMARY TENSE:  (past, present, present-perfect)
PERSON:         (first / third / system-as-subject)
PERSON SHIFTS:  (none, unless a quoted passage)
```

Test: write the first sentence of the page. Read it. Confirm it matches
the speaker, tense, and person declared above. If it does not, rewrite
the sentence, not the brief.

---

## 4. The negative space

A negative-space move preempts a specific plausible misreading of the
argument. It is one sentence, embedded mid-argument, that names the
misreading and closes it off. It is not a structured block at the top of
the page. It is not a ritual disclaimer. It appears only when a
reasonable reader could genuinely mistake the argument for something
the page is not recommending.

Ask: is there a specific misreading a reasonable reader would make from
the thesis? Name it here in one sentence. If there is no plausible
misreading, this section is blank — and that is fine. Not every page
needs one.

```
PLAUSIBLE MISREADING (if any):
WHERE IN THE ARGUMENT IT APPEARS:
```

**What this is not:** a NOT AN ESTIMATE OF / NOT A CLAIM ABOUT
inventory. That produces a structured disclaimer block at the top of
the page. Her actual usage is a single embedded sentence, often dry,
mid-argument. See generative-patterns.md §7 for the pattern and examples.

---

## 5. The structural argument

The section spine. One section per move; one move per section. Each
section gets one sentence describing what it does. If a section's
one-sentence description starts with `discusses` or `covers` or `walks
through`, the section is not yet a move; it is filler. Rewrite or cut.

Section count follows the argument. Three sections is a real article.
Four sections is a real article. Eight sections is a real article. The
canonical specimen happens to have eight; that is not the schema. A
two-section piece is fine if the argument has two moves.

```
01 / [eyebrow]:   [one sentence: what this section does]
02 / [eyebrow]:   [one sentence]
03 / [eyebrow]:   [one sentence]
04 / [eyebrow]:   [one sentence]
...
```

Test: read the section list aloud as a sequence. Does it tell a story
that makes the thesis arrive? If a section is in the wrong order, the
page will not recover from it in prose. Reorder now.

---

## 6. The opening move

How section 01 begins. The genre determines the opening move:

- Methodology essay: `What follows is...` or `The architecture below...`
- Case study: situate the constraint and the cohort.
- Profile: positioning sentence, third person, present tense.
- Thinking tool: declare what the page is teaching and what it is not.

```
OPENING SENTENCE:
```

The opening sentence is the page's contract with the reader. Write it
last, after the brief is complete; revise it first when the prose
deviates from the brief.

---

## 7. The closing move

How the final section ends. Closing claims are quiet. Not triumphant,
not summative, not a CTA. The reader is trusted to know what to do with
what they have read. The closing paragraph names what the page commits
to and stops.

```
CLOSING SENTENCE:
```

---

## 8. The refusals (page-specific)

The general refusals are in `style-card.md`. Page-specific refusals are
declared here. Examples:

- A pipeline page might refuse to report any AUC above 0.95 on synthetic
  data, because the synthesis does not support that separability.
- A model page might refuse to estimate any organization's actual ROI,
  because the model is stylized.
- A profile page might refuse to use the first name `Heather`, because
  the convention is `Dr. Heather Leffew` first reference and `Dr. Leffew`
  thereafter.

```
THIS PAGE REFUSES:
```

---

## 9. The interactive inventory

Every substantial page carries interactive elements. The question is not
whether to include them — it is which concepts warrant which type. For every
section in the brief, ask: can the reader experience this concept, or can
they only read about it? If they can experience it, build it.

For each interactive element the page will carry:

```
ELEMENT [n]:
  TYPE:             (parameter simulator / distribution visualizer / state toggle /
                     schema explorer / animated diagram / decision path tracer /
                     data quality explorer / comparison engine)
  CONCEPT:          what this element demonstrates
  READER CONTROLS:  what parameters or states the reader manipulates
  OUTPUT:           what the reader observes changing
  PLACEMENT:        which section, at what point in the argument
  WHAT IT TEACHES:
  WHAT IT DOES NOT TEACH:
```

Three elements is a floor for any substantial methodology or case study piece.
A piece with five distinct demonstrable concepts carries five elements.
Consult `design_system/VISUALIZATIONS.md` for type definitions and placement rules.

### 9.1 Carryover items

If the page is being rewritten from a prior draft, name every element
that must be preserved across the rewrite. Bespoke CSS, custom JS,
data structures the page depends on, asset paths. The rewrite must
explicitly carry these forward; cloning a different page's chrome
silently drops them.

```
CARRYOVER FROM PRIOR DRAFT:
- [element]: [where it lives in the prior file]
- [element]: [where it lives in the prior file]
```

---

## 10. The exit gate

After drafting, the page is checked against `voice/checklist.md`. The
checklist is the last-mile catch, not the method. A page that fails
the checklist goes back to the brief, not to the editor.

If the brief was right and the prose still failed the checklist, the
prose was not following the brief. Re-read the brief. Re-write the
prose.

If the brief itself was wrong, the failure was upstream. Revise the
brief first. The prose follows the brief, not the other way around.
