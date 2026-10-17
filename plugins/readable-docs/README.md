# Readable docs

An [Agent Plugin](https://agent-plugins.org/plugin-authors/manifest) that exposes the `readable-doc` skill.

The skill writes or rewrites documentation a reader can understand on the first pass. The style follows the writing idea in [Andrej Karpathy's note on understanding model output](https://x.com/karpathy/status/2105819303471976479): ask for [ASD-STE100](https://www.asd-ste100.org/) (Simplified Technical English). The skill contains that sheet: sentence limits, approved verb forms, safety lines, and the sample dictionary pairs.

## Skill

`readable-doc` applies when you ask for a readable doc, a clearer explanation, Simplified Technical English, a runbook, a how-to, or a rewrite of dense model output.

```text
Rewrite this design note as a readable doc.
Write a how-to for rotating the API key.
Explain the cache invalidation path in strict STE.
```

The sheet is in the skill. A procedure stays at 20 words. A description stays at 25 words. A descriptive paragraph stays at 6 sentences.

## Layout

```text
plugins/readable-docs/
├── plugin.json
├── .cursor-plugin/plugin.json
└── skills/readable-doc/
    ├── SKILL.md
    ├── assets/ste100-overview.png
    ├── references/examples.md
    └── scripts/check_doc.py
```

`plugin.json` is the Agent Plugins manifest. `.cursor-plugin/plugin.json` is the Cursor manifest for marketplace install. Both point at the same skill.

## Install

This repository is a Cursor marketplace. In Cursor, add the marketplace from `jean-kunz/my-agent-plugins`, then install **Readable docs**.

To load it only on this machine, copy `plugins/readable-docs` to `~/.cursor/plugins/local/readable-docs` and reload the window.

## Check a draft

```bash
python3 skills/readable-doc/scripts/check_doc.py path/to/doc.md
```

Run the command from the plugin root. Numbered steps are limited to 20 words. Other sentences are limited to 25. The script also reports a descriptive paragraph over 6 sentences, filler, and the unapproved words from the sheet.
