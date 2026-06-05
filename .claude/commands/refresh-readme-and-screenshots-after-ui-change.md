---
name: refresh-readme-and-screenshots-after-ui-change
description: Workflow command scaffold for refresh-readme-and-screenshots-after-ui-change in Distilmark.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /refresh-readme-and-screenshots-after-ui-change

Use this workflow when working on **refresh-readme-and-screenshots-after-ui-change** in `Distilmark`.

## Goal

Updates README and screenshot assets to reflect UI or branding changes.

## Common Files

- `screenshots/convert-dark.png`
- `screenshots/convert-light.png`
- `screenshots/courses-dark.png`
- `screenshots/engines-dark.png`
- `README.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Take new screenshots of the updated UI.
- Replace outdated screenshot files in the screenshots/ directory.
- Update README.md to reference the new screenshots.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.