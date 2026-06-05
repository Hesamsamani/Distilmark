---
name: release-workflow-icon-bundling
description: Workflow command scaffold for release-workflow-icon-bundling in Distilmark.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /release-workflow-icon-bundling

Use this workflow when working on **release-workflow-icon-bundling** in `Distilmark`.

## Goal

Ensures that the correct icon assets are built and bundled into the executable during the release process.

## Common Files

- `scripts/build_icon.py`
- `.github/workflows/release.yml`
- `icon.png`
- `icon.ico`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Run a script to generate icon.ico from icon.png with all required sizes.
- Update the release workflow to run the icon build script before packaging.
- Bundle the new icon assets into the executable using PyInstaller --add-data.
- Verify that the bundled app displays the correct icons in the window and taskbar.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.