# Content Generation Workflow

> The sequence for generating any substantial prose from a project folder.
> Run in order. Do not skip to writing before the earlier steps are complete.

---

## Step 1 — Read everything in the folder

Read all files in the project folder. Where the folder contains a Jupyter notebook
or Python script, use the notebook stripping tool to extract a clean version:
preserve Python source, markdown cells, code comments, and text-based outputs;
strip JSON output cells and image outputs. The comments inside the code often
carry the design reasoning and are as important as the code itself.

Also read any README, PDF technical reports, sample outputs, or other documentation
in the folder. The full picture of what was built and why is rarely in one file.

Make notes under these headings:
- **What it does:** The system or analysis in one or two sentences.
- **Why the design choices were made:** Which architectural or methodological decisions
  were deliberate, what was considered and rejected, and what the choices commit to.
- **What is distinctive:** What this work does that a default approach would not.
- **What it does not claim:** Limits that are named explicitly or implied by the
  synthetic/demo context.
- **The argument:** What case the work is making, stated as a thesis sentence.

If the thesis sentence cannot be written after reading everything, the argument is not
yet clear. Do not proceed to writing until it can be written.

---

## Step 2 — Write the 60-minute presentation

Before drafting any publication prose, write a 60-minute live-delivered presentation
on the content. This step is not the deliverable; it is how the argument is internalized
before the deliverable is written.

The presentation audience: intelligent, capable, intellectually curious people who do
not share identical expertise. This means:
- Use the right technical and clinical terminology.
- Pair every term with its definition or rationale the first time it appears.
- Show the decision-making: "I used gradient boosted trees because this part of the
  problem demands... I considered X but found that Y because..."
- Do not gloss over technical or mathematical content. Do not substitute plain-language
  approximations for precise terms.
- The audience can follow the argument. They cannot be assumed to know your specific
  domain vocabulary without introduction.

The presentation forces the argument structure to become visible. It reveals whether
the content has a coherent arc, what the thesis is, and what the most important points
are — before any voice-specific writing begins.

---

## Step 3 — Ask one question

If there is any ambiguity about what the author considers most important, ask:

> "What do you want people to take away from this work?"

This question surfaces authorial priority that may not be prominent in the material
itself. It identifies the thesis the piece should be organized around.

A second question is permitted only if genuine ambiguity remains after the first answer:

> "What about this work is not obvious from the material itself?"

This surfaces the naming move — the connection or mechanism that requires the author's
perspective to see.

Do not ask about the field, about what others are doing wrong, or about how this work
compares to alternatives. Those questions produce manufactured tension. These two
questions produce the argument.

---

## Step 4 — Embody the position and write

Before drafting, establish the intellectual position:
- What does the author already believe about this argument?
- Who is the reader — specifically, what is their relationship to this material?
- What will the reader leave with that they did not have before?

Write from that position. The argument was formed before the first sentence. The prose
builds the case for it.

Read `voice/style-card.md` and `voice/generative-patterns.md` before drafting.
Fill in `voice/brief.md` for the specific piece.

---

## Step 5 — Apply mechanistic checks

After a complete draft exists, run `voice/checklist.md`. The checklist is a gate,
not a method. It catches surface failures in a completed draft; it cannot generate
authentic prose from scratch. A draft that fails the checklist goes back to the brief,
not to the editor.

The order matters: embodiment produces the draft; the checklist validates it.
Running the checklist before writing is how you get prose that passes all 36 items
and sounds like no one.

---

## Revision protocol — applies to every edit, not just initial drafts

When revising or adding prose in response to feedback, the full workflow does not
need to repeat. The punctuation gate does. Before submitting any new or revised
prose — even a single paragraph, even a single sentence — run this minimal check:

1. **Grep for em dashes (`—`).** Any match in prose is a failure. Replace using the
   substitution rules in `voice/style-card.md`: colon, semicolon, parentheses, or
   comma depending on the logical relationship.
2. **Read the new prose against the brief.** The revision should not introduce a
   register shift, a person shift, or a structural move the brief does not authorize.
3. **Confirm the closing sentence still lands.** Additions before the closing paragraph
   can dilute or contradict it. Re-read the final paragraph after any revision.

The checklist catches failures in completed drafts. The revision protocol catches
failures introduced after the checklist has already run. Both are required.
