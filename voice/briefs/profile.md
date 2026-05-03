# Brief: profile.html

> The canonical exemplar for the executive-profile genre.
> Brief written before the page is drafted.

**File:** `design_system/ui_kits/profile/profile.html` (to be created)
**Genre:** Executive profile

---

## 1. The single-sentence thesis

```
THESIS:
Dr. Heather Leffew is a clinical AI researcher and practitioner whose
work sits at the intersection of computational psychology, applied
machine learning, and the architecture of high-stakes prediction
systems, and the page exists so that a technical reader who lands on
it can place her work and her register in under a minute.
```

The page is not a CV. The page is not a portfolio index. The page is
the positioning statement that establishes who the reader is reading,
so that everything else in the portfolio reads in the right voice.

---

## 2. The genre

- [x] **Executive profile**
- [ ] Case study
- [ ] Methodology essay / working note
- [ ] Thinking tool
- [ ] Research index card
- [ ] Position piece / letter

---

## 3. The speaker

```
SPEAKER:        Third person. The portfolio refers to the author. The
                author does not speak for herself on the profile page;
                that voice is reserved for methodology essays and
                position pieces.
PRIMARY TENSE:  Present tense for current work and ongoing
                affiliations. Past tense for completed positions and
                degrees. Present-perfect for arc statements.
PERSON:         Third person throughout. First person `I` does not
                appear. `Dr. Heather Leffew` first reference;
                `Dr. Leffew` thereafter; `Heather` never.
PERSON SHIFTS:  None.
```

---

## 4. The negative space

```
NOT A CV:        the page is not a chronological list of positions.
NOT A PITCH:     the page does not solicit work, name rates, or list
                 services.
NOT A SUMMARY OF: every project. The page names a small number of
                 representative pieces and links to the full portfolio.
NOT A BIO:       in the Wikipedia sense. The page is positioning, not
                 biography. Birthplace, schooling chronology, family
                 information do not appear.
```

---

## 5. The structural argument

```
01 / Positioning:
     One paragraph. Names the field, the register, the kind of work.
     The reader leaves this paragraph knowing what register the rest
     of the portfolio will be in.

02 / Current work:
     One paragraph or one tight section. What the author is doing
     right now. Present tense. Specific.

03 / Trajectory:
     One paragraph. The arc that produced the current work. Past
     tense and present-perfect. Concrete: TikTok USDS, Spokeo,
     clinical neurotherapy, doctoral research. Names the
     institutions, not the titles.

04 / Selected work:
     Three to five cards. Each card links to a portfolio page.
     Eyebrow + title + one-sentence description.

05 / Contact:
     One line. Email or LinkedIn. No form, no calendar embed, no
     newsletter signup.
```

Five sections. The page is short by design. A profile that runs to
eight sections is a CV pretending to be a profile.

---

## 6. The opening move

```
OPENING SENTENCE:
Dr. Heather Leffew is a clinical AI researcher and practitioner whose
work sits at the intersection of computational psychology, applied
machine learning, and the architecture of high-stakes prediction
systems.
```

Names her, names the field, names the kind of work. The reader knows
within the first sentence whether the page is for them.

---

## 7. The closing move

```
CLOSING SENTENCE:
The portfolio collects writing on systems she has built, methodologies
she has committed to, and structural intuitions about applied machine
learning that she has arrived at through doing the work.
```

Quiet. Names what the portfolio is. Hands the reader to the work.

---

## 8. The refusals (page-specific)

```
THIS PAGE REFUSES:
- The first name `Heather`. First reference is `Dr. Heather Leffew`,
  every subsequent reference is `Dr. Leffew`.
- The pitch register. No `transform`, no `partner with`, no `let's
  build something together`, no `available for consulting`.
- Skill bullets. The reader is not hiring a stack; the reader is
  reading a portfolio.
- A photo placement that competes with the prose. If a photo appears
  it is small, monochrome, and below the fold.
- A CTA at the close. The closing paragraph hands the reader to the
  work; the work itself is the CTA.
- Marketing language about the author's `passion` or `mission`. The
  work is the mission; the work speaks for the mission.
```

---

## 9. The interactive contract

Not applicable. The profile is read, not interacted with.

### 9.1 Carryover items

The publication chrome (atmosphere, top nav, footer, type system) is
carried from the methodology specimen at `clinical-validation.html`.
The band system is simplified: no dark/paper alternation, paper-only.
No spine, no status strip, no progress bar; the page is too short to
warrant them.

```
CARRYOVER FROM clinical-validation.html:
- :root token block (full)
- @font-face declarations
- .atmosphere
- .topnav (with the same nav items)
- .site-foot
- The publication body type rules
- The .gloss inline glossary pattern (in case a single term needs it)
```

---

## 10. The exit gate

After drafting, the page is checked against `voice/checklist.md`. The
profile genre has no genre-specific gates beyond the universal ones,
because the profile's discipline is in the brief, not in the surface.
A profile that passes the checklist but violates §3 (third person,
no `I`) or §8 (refuses pitch register, refuses skill bullets) is not
the brief's profile and goes back to the brief.
