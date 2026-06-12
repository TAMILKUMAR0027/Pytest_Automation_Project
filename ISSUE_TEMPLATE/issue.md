---
name: 
about: 
title: ""
labels: bug, pytest, selenium, framework, jenkins, high-priority
assignees: ''
---

# Fix Circular Import Issue Between `<page_module>.py` and `<action_module>.py` Causing Pytest Collection Failure

## Problem
Pytest test collection fails due to a circular import between the Page Object and Action classes.

## Issue Creator
@<your-username>

## Error
```text
ImportError: cannot import name '<ClassName>' from partially initialized module '<module.path>'
(most likely due to a circular import)
```

## Stack Trace
```text

# example 
tests/<test_file>.py
    ↓
pages/<page_module>.py
    ↓
actions/<action_module>.py
    ↓
pages/<page_module>.py
```

## Root Cause

`pages/<page_module>.py` imports `<ActionClassName>`:
```python
# example 
from actions.<action_module> import <ActionClassName>
```

and `actions/<action_module>.py` imports `<PageClassName>`:
```python
from pages.<page_module> import <PageClassName>
```

This creates a circular dependency during module initialization.

## Expected Behavior
- Pytest should successfully collect and execute tests.
- Page classes should not depend on Action classes.
- Action classes can depend on Page classes following the Page Object Model design.

## Suggested Fix
- Remove the import of `<ActionClassName>` from `pages/<page_module>.py`.
- Keep dependencies one-directional:
```text
# example 
Pages   → No Action imports
Actions → Can import Pages
Tests   → Can import Actions
```

## Impact
- Jenkins build fails during test collection.
- `<test_file>.py` is not executed.
- Test pipeline is blocked.

## Priority
**High**

## Labels
`bug` `pytest` `selenium` `framework` `jenkins` `high-priority`
