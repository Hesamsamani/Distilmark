```markdown
# Distilmark Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the Distilmark Python codebase. You'll learn how to structure files, write imports and exports, follow commit message conventions, and understand the project's approach to testing. This guide is ideal for contributors looking to quickly align with Distilmark's established practices.

## Coding Conventions

### File Naming
- Use **camelCase** for file names.
  - **Example:** `dataLoader.py`, `utilsHelper.py`

### Import Style
- Use **relative imports** within the codebase.
  - **Example:**
    ```python
    from .utilsHelper import processData
    ```

### Export Style
- Use **named exports** (explicitly listing what is exported).
  - **Example:**
    ```python
    def processData(data):
        # processing logic
        return result

    __all__ = ['processData']
    ```

### Commit Messages
- Follow **conventional commit** patterns.
- Use the `fix` prefix for bug fixes.
- Keep commit messages concise (average ~39 characters).
  - **Example:**  
    ```
    fix: correct data parsing in loader
    ```

## Workflows

### Code Contribution
**Trigger:** When adding new features or fixing bugs  
**Command:** `/contribute`

1. Create a new branch for your changes.
2. Implement changes following coding conventions.
3. Use relative imports and named exports.
4. Write or update tests in files matching `*.test.*`.
5. Commit changes with a conventional message (e.g., `fix: ...`).
6. Open a pull request for review.

### Testing
**Trigger:** When verifying code correctness  
**Command:** `/test`

1. Identify or create test files matching the `*.test.*` pattern.
2. Write tests for new or modified code.
3. Run tests using the project's preferred method (testing framework is currently unknown).
4. Ensure all tests pass before committing.

## Testing Patterns

- Test files are named using the `*.test.*` pattern (e.g., `dataLoader.test.py`).
- The specific testing framework is not detected; check existing tests for style.
- Place tests alongside the code they validate or in a dedicated `tests` directory if present.

**Example Test File:**
```python
# dataLoader.test.py

from .dataLoader import processData

def test_processData():
    sample = {"input": 42}
    result = processData(sample)
    assert result == expected_output
```

## Commands
| Command      | Purpose                                 |
|--------------|-----------------------------------------|
| /contribute  | Start the code contribution workflow    |
| /test        | Run or write tests for the codebase     |
```
