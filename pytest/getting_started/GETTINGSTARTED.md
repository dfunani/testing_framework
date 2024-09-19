# Getting Started

## _PyTest - Simple Passing Tests_

```python
# /tests/test_simple_tests.py
def test_pass():
    assert 1 == 1
    assert "string" == "string"
    assert (1, 2, 3) == (1, 2, 3)
```

```sh
pytest /tests/test_simple_tests.py

=================================================================== test session starts ===================================================================
platform linux -- Python x.x.x, pytest-x.x.x, pluggy-x.x.x
rootdir: ~/testing_design/pytest
collected 1 item
tests/test_simple_tests.py .                                                                                                                              [100%]

==================================================================== 1 passed in 0.01s ====================================================================
```

## _PyTest - Simple Failing Tests_

```python
# /tests/test_simple_tests.py
def test_fail():
    assert 1 == 2
    assert "string" == "strings"
    assert (1, 2, 3) == (1, 2, 3, 4)
```

```sh
pytest /tests/test_simple_tests.py

=================================================================== test session starts ===================================================================
platform linux -- Python x.x.x, pytest-x.x.x, pluggy-x.x.x
rootdir: ~/testing_design/pytest
collected 1 item
tests/test_simple_tests.py F                                                                                                                       [100%]

======================================================================== FAILURES =========================================================================
________________________________________________________________________ test_fail ________________________________________________________________________

    def test_fail():
>       assert 1 == 2
E       assert 1 == 2

tests/test_simple_tests.py:7: AssertionError
================================================================= short test summary info =================================================================
FAILED tests/test_simple_tests.py::test_fail - assert 1 == 2
=============================================================== 1 failed in 0.02s ===============================================================
```

## Summary

This looks very simple. It is. The functions test*pass() and test_fail() will be discovered by pytest as a test function because it starts
with test* and are in a file that starts with test\_. And when the test is run, the assert statement will determine if the test passes or fails. `assert` is a keyword built into Python and has the behavior of raising a AssertionError exception if the expression after assert is false.

**Please Note**: Any uncaught exception raised within a test will cause the test to fail. Although any type of uncaught exception can
cause a test to fail, traditionally we stick with AssertionError from assert to determine pass/fail for tests.
