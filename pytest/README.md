# Testing with PyTest

## Introduction

**PyTest** is a software testing framework, which means **PyTest** is a command-line tool that automatically finds tests you’ve written,
runs the tests, and reports the results. It has a library of goodies that you can use in your tests to help you test more effectively.
It can be extended by writing plugins or installing third-party plugins. And it integrates easily with other tools like continuous integration and web automation.

Here are a few of the reasons **PyTest** stands out above many other testing frameworks:

- Simple tests are simple to write in **PyTest**.
- Complex tests are still simple to write.
- Tests are easy to read.
- Tests are easy to read. (So important it’s listed twice.)
- You can get started in seconds.
- You use assert in tests for verifications, not things like `self.assertEqual()` or `self.assertLessThan()`. Just assert.
- You can use **PyTest** to run tests written for unittest or nose.

**PyTest** is being actively developed and maintained by a passionate and growing community.
It’s so extensible and flexible that it will easily fit into your work flow.
And because it’s installed separately from your Python version, you can use the same version of **PyTest** on multiple versions of Python.

## Installation

```sh
python3 -m pip install venv # or virtualenv
python3 -m venv .venv
source .venv/bin/activate
pip install pytest

pytest --version # output pytest x.x.x
```

## Running

Running tests is straightforward. Execute the command:

```sh
pytest tests/
```

Here, **PyTest** is the executable command, and `tests/` is the path to the folder containing your test files.

Note: You can enhance the `pytest` command with flags like `-v`, `--tb`, and `-h` for more detailed output.
Run `pytest -h` for a help page listing all available flags.

## Discovery

_PyTest_ automatically searches through the specified folder (e.g., tests/) for files following the naming pattern test*.py or *test.py.
It then executes functions starting with test and classes starting with Test. Additionally,
PyTest handles functionalities like _fixtures_ and _parameterization_.

## Outcome

Running PyTest leads to various test results:

PASSED (.) - The test ran successfully.
FAILED (F) - The test encountered an error and did not pass.
SKIPPED (s) - The test was intentionally skipped.
XFAIL (x) - The test was expected to fail, and it did.
XPASS (X) - The test was marked xfail but unexpectedly passed.
ERROR (E) - An exception occurred during the execution of a fixture or hook function.

## Assertions:

### Built-Ins:

**PyTest** by default makes use of **Python's** built-in assert keyword, to test a statement or 'evaluate' the assertion.

```python
assert something assertTrue(something)
assert not something assertFalse(something)
assert a == b assertEqual(a, b)
assert a != b assertNotEqual(a, b)
assert a is None assertIsNone(a)
assert a is not None assertIsNotNone(a)
assert a <= b assertLessEqual(a, b)
```

### Custom Assertions:

Users can create custom assertions by creating functions that raise `pytest.Fail(message)`.

```python
import pytest
def assert_valid(lhs):
    if lhs['id'] != 1:
        pytest.Fail("Invalid ID, Must be 1.")

def test_id():
    data = {"id": "1"}
    assert_valid(data)
```

## [Getting Started](getting_started/GETTINGSTARTED.md)

## [Fixtures](fixtures/FIXTURES.md)
