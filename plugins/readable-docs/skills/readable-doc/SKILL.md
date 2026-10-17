---
name: readable-doc
description: >-
  Writes and rewrites documentation in ASD-STE100 Simplified Technical English:
  20-word procedures, 25-word descriptions, approved verb forms, and the
  dictionary pairs in the skill's STE sheet. Use when the user asks for a
  readable doc, a clearer explanation, Simplified Technical English,
  ASD-STE100, STE, a runbook, a how-to, or a rewrite of dense model output.
---

# Readable doc

Write or rewrite a document so the reader can act after one read. Follow the STE sheet below. It is the text of [assets/ste100-overview.png](assets/ste100-overview.png).

The sheet is a working summary of ASD-STE100 (Simplified Technical English). It is not the licensed dictionary. That dictionary has about 1100 approved words. Use the pairs in this sheet. Do not invent other substitutions. Keep a technical name from the subject when the sheet has no pair for it (an API name, a product name, a unit).

Write approved keywords in normal sentence case. Uppercase in the dictionary table only marks the approved word.

This skill returns a markdown document. Do not produce an HTML page or a video from this skill.

## Workflow

1. Name the reader and the job the document helps them finish.
2. Keep facts, names, numbers, commands, and constraints from the source. Delete repetition.
3. If two source statements disagree, keep both and mark the conflict. Do not choose one in silence.
4. Pick the shape:
   - Procedure: numbered steps, one instruction each.
   - Description: short sections, one topic each, at most 6 sentences in a paragraph.
   - Safety: a `WARNING` or `CAUTION` line before the step it affects.
   - Relationship, sequence, or state: one mermaid diagram, then the short prose that depends on it.
5. Apply the STE sheet. You may add one opening sentence that names the reader and the outcome.
6. Read [references/examples.md](references/examples.md) when the source is longer than a few steps, or when a draft fails the check.
7. Run the check. Fix every failure before you return the document.

## STE sheet

### Document structure

ASD-STE100, Simplified Technical English. Owner: ASD. Written first for aircraft maintenance. Also used in defence, rail, and industry. Source: [asd-ste100.org](https://www.asd-ste100.org/).

Part 1, Writing rules:

1. Words
2. Noun clusters
3. Verbs
4. Sentences
5. Procedures
6. Descriptive writing
7. Safety instructions
8. Punctuation and word counts
9. Writing practices

Part 2, Dictionary:

- Approved words. The keyword is shown in uppercase. One part of speech. One meaning.
- Unapproved words, each with an approved alternative.
- Technical names, in defined categories.
- Technical verbs, in defined categories.
- About 1100 approved words.

History: AECMA started work on controlled English for aircraft in 1979. The AECMA Simplified English Guide was published in 1986. It became ASD-STE100 in 2005, after AECMA joined ASD in 2004. Issue 9 is developed and owned by the ASD STEMG (Simplified Technical English Maintenance Group).

### Writing rule limits

| Rule | Limit |
| --- | --- |
| Procedural sentence | 20 words |
| Descriptive sentence | 25 words |
| Descriptive paragraph | 6 sentences |
| Noun cluster | 3 words |
| Instructions in one sentence | 1, except simultaneous actions |

- Use the same word for the same thing every time.
- Do not leave out words such as "the", "a", and "this".
- Use the active voice in procedures.
- Use a vertical list for complex text.
- Write one topic in each paragraph.

### Anatomy of STE sentences

Procedural sentence. Same instruction, rewritten. Limit: 20 words.

Not STE: "It is imperative that the operator ensures the hydraulic reservoir is replenished prior to commencing operation."

STE: "Make sure that the hydraulic reservoir is full before you start the operation."

- Command form of an approved verb.
- "hydraulic reservoir" is a noun cluster of two words. The limit is three.
- Not "replenished". Not "prior to". Not "commencing".
- Active voice. "you" is allowed.

Safety instruction. Limit: 20 words. Put a clear command, then the risk.

`WARNING`: risk of injury. `CAUTION`: risk of damage.

STE: "WARNING: Do not touch the brake unit until it is cool. Hot parts can cause injury."

Descriptive sentence. Simple present. Limit: 25 words. At most 6 sentences in a paragraph. One topic in that paragraph.

STE: "The pump supplies fuel to the engine when the switch is on." (12 words)

### Verb forms

| Verb form | Example | Status |
| --- | --- | --- |
| Command (imperative) | Close the valve. | Approved |
| Simple present | The valve closes. | Approved |
| Simple past | The valve closed. | Approved |
| Simple future | The valve will close. | Approved |
| Infinitive | Turn the knob to close it. | Approved |
| Past participle as adjective | The closed valve. | Approved |
| Progressive (-ing) | The valve is closing. | Not approved |
| Perfect | The valve has closed. | Not approved |
| Passive, in procedures | The valve must be closed. | Not approved |

Use an `-ing` form only inside a technical name, for example "landing gear".

### Dictionary entries

An approved word keeps only its listed meaning and part of speech. "Close" is a verb here. It is not an adjective that means "near".

| Word | Status | Meaning or alternative | Approved example | Not approved |
| --- | --- | --- | --- | --- |
| CLOSE (v) | Approved | To move together; to stop flow | Close the valve. | |
| close (adj) | Not approved | NEAR | | Put the tool close to the panel. |
| commence (v) | Not approved | START | START the pump. | Commence pumping. |
| ensure (v) | Not approved | MAKE SURE | MAKE SURE that the switch is off. | Ensure the switch is off. |
| prior to (prep) | Not approved | BEFORE | BEFORE you start the engine. | Prior to starting the engine. |
| replenish (v) | Not approved | FILL | FILL the reservoir. | Replenish the reservoir. |
| utilize (v) | Not approved | USE | USE a torque wrench. | Utilize a torque wrench. |
| approximately (adv) | Not approved | ABOUT | Wait ABOUT 10 minutes. | Wait approximately 10 minutes. |
| in order to | Not approved | TO | Remove the panel TO get access. | Remove the panel in order to get access. |
| TEST (v) | Approved | To find if it operates correctly | TEST the circuit. | |

In the document, write the approved word in sentence case: "Make sure that the switch is off." "Start the pump." "Before you start the engine." "Fill the reservoir." "Use a torque wrench." "Wait about 10 minutes." "Remove the panel to get access."

## Diagram

Add one mermaid diagram when the reader must see order, ownership, or state changes. Title it with the question it answers. Do not add a diagram for a linear procedure the steps already show.

## Check

When you write the document to a file, run this from the `readable-doc` skill directory:

```bash
python3 scripts/check_doc.py path/to/doc.md
```

The script flags sentences over the limit (20 words on a numbered step, 25 words elsewhere), a descriptive paragraph over 6 sentences, filler, and the unapproved words in the dictionary table. It does not judge voice or missing facts. Check those yourself:

- The opening sentence, when you include one, names the reader and the outcome.
- Each step has one instruction, unless the actions are simultaneous.
- Verb forms are in the approved list. Procedures are active, not passive.
- A `WARNING` is injury. A `CAUTION` is damage. The command comes before the risk.
- The same thing has the same name throughout.
- Noun clusters have at most 3 words.
- Source claims are still present, or listed under `Removed`.
- Commands and identifiers match the source.

Return the document with no preamble. After it, add a `Removed` list only when you dropped a source claim. One line per claim.
