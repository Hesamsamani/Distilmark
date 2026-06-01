```markdown
# pymupdfgui Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the `pymupdfgui` repository, a Python project built on the Flask framework. You'll learn about its file organization, code style, commit message practices, and how to write and run tests. This guide is ideal for contributors aiming for consistency and maintainability in this codebase.

## Coding Conventions

### File Naming
- Use **camelCase** for file names.
  - Example: `pdfViewer.py`, `documentHandler.py`

### Import Style
- Use **relative imports** within the package.
  - Example:
    ```python
    from .utils import parseDocument
    from .models import PDFPage
    ```

### Export Style
- Use **named exports** (explicitly define what is exported).
  - Example:
    ```python
    __all__ = ['parseDocument', 'PDFPage']
    ```

### Commit Messages
- Commit messages are **freeform** (no strict prefixes), but concise (~60 characters).
  - Example:  
    ```
    Add zoom functionality to PDF viewer
    Fix bug in page navigation logic
    ```

## Workflows

### Adding a New Feature
**Trigger:** When implementing a new functionality.
**Command:** `/add-feature`

1. Create a new file using camelCase naming.
2. Write code using relative imports for internal modules.
3. Export new functions/classes using named exports.
4. Add or update tests in a corresponding `*.test.*` file.
5. Commit changes with a clear, concise message.

### Fixing a Bug
**Trigger:** When resolving a reported or discovered bug.
**Command:** `/fix-bug`

1. Locate the relevant module using camelCase file names.
2. Apply the fix, maintaining code style and import conventions.
3. Update or add tests in the related `*.test.*` file.
4. Commit with a descriptive message about the fix.

### Writing and Running Tests
**Trigger:** When verifying new or existing functionality.
**Command:** `/run-tests`

1. Create or update test files using the `*.test.*` naming pattern.
2. Follow the code style and import conventions in test files.
3. Use the project's (unknown) test runner to execute tests.
4. Review test output and address any failures.

## Testing Patterns

- Test files are named using the pattern `*.test.*` (e.g., `pdfViewer.test.py`).
- The specific testing framework is **unknown**, so check existing tests for structure.
- Tests should follow the same import and export conventions as the main codebase.
- Example test file structure:
  ```python
  from .pdfViewer import PDFViewer

  def test_pdf_viewer_loads_document():
      viewer = PDFViewer('sample.pdf')
      assert viewer.pageCount == 10
  ```

## Commands
| Command      | Purpose                                    |
|--------------|--------------------------------------------|
| /add-feature | Start the workflow for adding a new feature|
| /fix-bug     | Begin the bug fixing workflow              |
| /run-tests   | Run all tests in the repository            |
```