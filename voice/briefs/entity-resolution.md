# Brief — case study: Entity resolution at Spokeo

> **Genre:** Case study. **Surface:** `ui_kits/case-study/entity-resolution.html`.
> **Reference exemplar:** `ui_kits/case-study/clinical-validation.html` (chrome, type, sections, sidenotes, methodology callouts, back matter).
> **Status:** forward brief — the contract the prose must keep. The current `source_reference/entity-resolution-pipeline.html` is **not** the model: it has the right numbers and the wrong voice (`glass-panel` chrome, Three.js monolith, `Phase 12 Verdict` headline tone, Lenis/GSAP boot sequence). The new file uses the canonical `clinical-validation.html` chrome and rewrites the prose against the voice system.

---

## 1. The situation, in one paragraph

A consumer-identity graph at Spokeo (≈49TB, 59 vendor partitions, ~8B person rows) was running on an undocumented 17-rule heuristic in a 60-day batch cadence. Internal lore held that ~1 in 11 person identifiers shifted per iteration (≈9.09% churn) — a number nobody had measured, only inferred. The team's first instinct was to replace the heuristic with ML. The brief was the opposite: measure the system that already exists, find out what's actually broken, then decide whether to replace anything.

## 2. The finding the case study is about

The heuristic was, on the evidence the team retrieved, mostly correct. The folk 9.09% churn estimate was off by three orders of magnitude — actual substantive churn measured at 0.004% across 96M records. The real defect was narrower than the mythology: a single transitive-closure failure (Partial-Null Bridging) producing 35,097 bad clusters. A surgical repair (Variant B) eliminated the defect with zero record orphaning. A supervised model trained against the same evidence reproduced the heuristic's decisions exactly (AUC 0.9996 vs 0.9996, ΔAUC = 0.0000) and could not resolve the heuristic's abstain surface (137,698 cases → 81 resolved at p ≥ 0.90). The Phase 12 architectural review then asked whether a Mixture-of-Experts rearchitecture should displace the bounded-repair posture; against an 11-gate bar, no alternative cleared all eleven. The verdict was that the bounded posture stands.

The case study is about **what was learned by measuring before rebuilding** — not the elegance of any one repair.

## 3. Voice posture

Voice family: `voice/specimens.md §4` (case study) — third-person or system-as-subject, opens with situation+constraint, closes with what was learned. Not the writeup-voice of the methodology family.

- **Subject of sentences.** Mostly the system or the work, occasionally the team. Never "I" except in one or two places where the first-person admission is doing real work (the bias toward rebuilding, the assumption Heather had to give up). Compare: clinical-validation uses "I" for the build but the entity-resolution work was a team program — third-person is more honest here.
- **Outcomes are stated, then explained.** "Reduced core processing time from 150+ hours to 24–36 hours" stands on its own; the architecture explains *why* in the next paragraph, not the next clause.
- **Mechanism over metaphor.** "A 17-rule waterfall whose first eight rules anchor on SSN and account for 66.93% of all edges" — not "a sophisticated cascade." When precise terms are needed (transitive closure, hash-aligned sampling, abstain surface), use them; gloss them as `<span class="gloss">` tooltips, not in-line.
- **Acknowledge what was uncomfortable.** Three places, on the page, in plain language:
  1. The folk estimate (9.09%) was wrong by three orders of magnitude. Somebody had been using it. The case study names that.
  2. The instinct to replace the heuristic with ML was the team's instinct, including Heather's. The model recapitulated the heuristic. That is written down.
  3. The Phase 12 verdict was *not to rebuild*. The page does not pretend that conclusion was easy or universally welcomed; it explains the 11-gate bar that produced it.
- **Closing posture is quiet, not triumphant.** The page ends on what the work taught, not on a hero shot of the architecture diagram.

## 4. Anti-voice — what this case study does not do

- No `glass-panel` cards, no Three.js monolith, no Lenis smooth-scroll boot sequence, no cursor halo. The chrome is `band--paper` / `band--ink` / `band--dark` from `clinical-validation.html`.
- No "Phase 12 Verdict" as a section title. The phase number is a working artifact; the section title is the *finding*.
- No `cutting-edge`, `transformative`, `revolutionize`, `paradigm`. (System rule.) No "we're excited to" or "thrilled to share."
- No em dashes in prose. Hyphens for ranges (`24–36 hours` is the one allowed range glyph; everywhere else, comma/semicolon/parenthetical).
- No oxford-comma exceptions.
- No claim of novelty in the techniques. The techniques (union-find, isotonic, weak supervision, shadow-mode ML) are all known. The contribution is in the discipline of measuring before rebuilding, in public, with the numbers retained.
- No softening of the uncomfortable findings. If the section reads like it could appear in a Spokeo recruiting brochure, rewrite it.

## 5. Section spine, with what each section is for

| #  | Band       | Spine label    | Section title                                         | Job                                                                                                  |
|----|------------|----------------|-------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| 01 | paper      | Setup          | Measure first. Rebuild only if the measurements ask. | The brief. The folk estimate. The constraint that produced the program.                              |
| 02 | ink        | Architecture   | The architecture nobody had written down.             | Forensic recovery of the 17-rule waterfall. SSN backbone at 66.93%.                                  |
| 03 | paper      | Stability      | A folk estimate, off by three orders of magnitude.    | 1% hash-aligned protocol. 99.64% retention. The 0.004% finding.                                       |
| 04 | ink        | Defect         | The one place the graph really did fail.              | Partial-Null Bridging mechanism. 35,097 defective clusters. Source 33_01_01.                          |
| 05 | paper      | Repair         | Variant B, surgical, zero orphans.                    | The repair, why split-by-anchor, what alternative was rejected, why zero orphaning was the bar.       |
| 06 | ink        | ML benchmark   | The model learned to be the heuristic.                | AUC 0.9996 vs 0.9996. Abstain surface 137,698 → 81. `ml_recapitulates_heuristic`.                     |
| 07 | paper      | Verdict        | The bounded posture stands.                           | Phase 12 11-gate bar. Why MoE didn't clear it. What the program taught about when *not* to rebuild.   |

Plus front matter (dark, hero) and back matter (dark, bibliography + cite-graph + related cases + next chapter).

## 6. Numbers that must appear, with their stake

- **49TB** multi-vendor data, **59** vendor partitions, **~8B** person-graph rows, **20** research notebooks. *(Stake: the scale is the constraint on every method choice that follows.)*
- **17 rules**, **75GB** edge data, **49.5GB** SSN-anchored (**66.93%**), **17.8GB** DOB+phone, **6.0GB** DOB+email, **1.9GB** DOB+address. *(Stake: any architecture change that displaces SSN linking without a validated replacement dissolves two-thirds of the graph's identity associations.)*
- **96M** records sampled, **1%** deterministic hash-aligned protocol, **99.64%** retention, **0.36%** changed of which **98.2%** cosmetic, **0.004%** substantive churn. *(Stake: this is the number the folk estimate of 9.09% was wrong about. Three orders of magnitude.)*
- **35,097** defective clusters from Partial-Null Bridging, source **33_01_01** (Court Records), **100%** eliminated by Variant B, **zero** record orphaning. *(Stake: the only real defect, surgically repairable.)*
- **AUC 0.9996** ML, **0.9996** heuristic, **ΔAUC = 0.0000**; abstain surface **137,698** → **81** resolved at p ≥ 0.90. *(Stake: the model was a re-encoding of the rules, not a discovery of new signal.)*
- **11-gate** acceptance bar, Phase 12. *(Stake: the bar that prevented a wholesale rearchitecture.)*
- **150+ → 24–36 hours** core processing time, **~80 engineers**, **8+ squads**. *(Stake: the operational outcome that justified the whole program. Stated once, in front matter or sec 07.)*

## 7. Diagrams

Mirror the SVG-figure pattern from `clinical-validation.html` exactly: `.figure > .frame.parallax > svg`, with `.cap` underneath. Hand-drawn SVG, no library. Use the case-study diagram palette (`--phthalo`, `--alizarin`, `--hookers`, `--hansa`) — the same monochrome rules apply.

- **Fig. 1** — Edge-volume by rule category. Horizontal bars. Phthalo for SSN (49.5GB), Hansa for DOB+phone (17.8GB), Hookers for DOB+email (6.0GB), Alizarin for DOB+address (1.9GB). Caption ends on the **66.93%** number.
- **Fig. 2** — The 9.09% / 99.64% pair. Two side-by-side reliability-style indicators. The point of the figure is the *gap*; the gap is what gets the visual emphasis.
- **Fig. 3** — Partial-Null Bridging mechanism. Three-node SVG: A(SSN_1) — C(NULL) — B(SSN_2), with the invalid transitive merge drawn as a dashed alizarin arc above. Toggle to Variant B state where C is reassigned to A, B isolated. Two static states side-by-side, no JS toggle (the canonical chrome doesn't use them).
- **Fig. 4** — Abstain-surface waterfall. Two columns, `137,698` left, `81` right, alizarin delta label `−137,617 unresolved`. Mirror the Fig. 2 layout from clinical-validation, but as a mass-balance instead of an ensemble breakdown.

## 8. Methodology callouts (the `.method` block)

Two, mirroring the clinical-validation cadence:

1. After §03 **Stability**: *"How the 1% sample was constructed."* Explains why deterministic hash-alignment (not random sampling) — random sampling would have fractured cluster integrity by dropping neighbors, making the retention number meaningless. This is the kind of methodological discipline the voice system rewards. Plain language, no boast.
2. After §06 **ML benchmark**: *"What `ml_recapitulates_heuristic` means, and what it doesn't."* The model is not bad. The data was not bad. The decision surface the heuristic produced was already the decision surface available; ML on the same evidence retrieved the same surface. This is what the formal label is for.

## 9. Sidenotes

Three, no more. They sit in the right gutter on wide viewports (≥1080px), inline footnotes on narrow. Use `<span class="sn"><span class="sn-num">N</span><span class="sn-body">…</span></span>` exactly as in clinical-validation.

1. *On the folk estimate.* "9.09% was 1/11. Nobody had measured 1/11; somebody had said 'about one in ten or eleven' once and the number had hardened. This is how production lore works."
2. *On hash-alignment.* "Random 1% sampling would have dropped neighbors of every sampled person and inflated the apparent churn. The hash alignment is the difference between measuring stability and measuring sampling artifact."
3. *On the Phase 12 11-gate bar.* "The gates aren't trivia: contradiction behavior under conflicting evidence, PID stability across versions, deployment posture (shadow / canary / general), and ML safety (calibration, abstention, drift). A Mixture-of-Experts proposal cleared eight."

## 10. Glossary terms (`.gloss` tooltips)

- **Entity resolution** — a single sentence on what the layer does and why it sits upstream of every product.
- **Union-find** — the algorithmic primitive whose transitive closure produced the Partial-Null Bridging defect.
- **Hash-aligned sampling** — the protocol that makes the 99.64% number defensible.
- **Abstain surface** — the cases the heuristic deliberately did not decide on. Test set for whether a model adds anything.
- **Shadow mode** — ML running in production but not affecting decisions, used as the holding posture after the recapitulation finding.
- **Mixture of Experts** — the rearchitecture proposal that did not clear the Phase 12 bar.

## 11. Closing note

The last paragraph is one sentence about what the work taught the team. The candidate sentence: *"The most valuable artifact the program produced was a number — 0.004% — and a willingness to let that number determine whether the rest of the proposal still made sense."* Adjust phrasing in writing; do not weaken the structure (a number; a willingness).

## 12. Exit gate

The page ships when:
- Every number in §6 appears with its stake nearby.
- The three uncomfortable findings in §3 are present, in plain language, not buried in subordinate clauses.
- The chrome diff against `clinical-validation.html` is purely content — no new layout primitives, no new band classes, no new components.
- The 36-item editorial checklist (`voice/checklist.md`) passes.
