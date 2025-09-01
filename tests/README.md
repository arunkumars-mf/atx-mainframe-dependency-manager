# Tests

This directory contains tests for the ATX Mainframe Dependency Manager package.

## Running tests

```bash
# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=atx_mainframe_dependency_manager
```

## Writing tests

Place test files in this directory, using file names that start with `test_`.

## Current tests

- `tools/test_source_code_tools.py` - Tests for source code access functionality
