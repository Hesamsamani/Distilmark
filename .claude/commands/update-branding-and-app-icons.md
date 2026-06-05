---
name: update-branding-and-app-icons
description: Workflow command scaffold for update-branding-and-app-icons in Distilmark.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /update-branding-and-app-icons

Use this workflow when working on **update-branding-and-app-icons** in `Distilmark`.

## Goal

Refreshes the application's branding by updating icons, sidebar/logo layout, and ensuring correct icon usage in the app and bundled executables.

## Common Files

- `icon.png`
- `icon.ico`
- `distilmark/app.py`
- `distilmark/styles.py`
- `.github/workflows/release.yml`
- `screenshots/convert-dark.png`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create or update icon.png and icon.ico with new branding assets.
- Update sidebar or header layout in styles and app code to use the new branding.
- Ensure the app and bundled executables load the updated icons (including fallback logic).
- Update release workflow to bundle the new icons with the executable.
- Refresh screenshots in the README or docs to reflect the new branding.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.