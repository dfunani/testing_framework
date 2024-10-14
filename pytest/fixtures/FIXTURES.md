# Fixtures

## Definition:

Fixtures are functions that are run by pytest before (and sometimes after) the actual test
functions. The code in the fixture can do whatever you want it to. You can
use fixtures to get a data set for the tests to work on. You can use fixtures to
get a system into a known state before running a test. Fixtures are also used
to get data ready for multiple tests.

## Usage:

Fixtures or Fixture functions are functions decorated with **PyTest's** fixture decorator.

```python
import pytest

@pytest.fixture
def some_data():
    return "data"

def test_some_test(some_data):
    test = some_data
    assert test == "data
```

## Detailed Reports:

Using flags to the pytest command, you can review the the order of operations of tests and fixtures, including the setup and
teardown phases of the fixtures.

```zsh
pytest --setup-show tests/
```

You can also use `--fixtures` to discover the fixtures in the project's location. pytest shows us a list of all available fixtures our test can use

```zsh
pytest --fixtures -v
```

## Scoping:

Each fixture has a specific scope, which defines the order of when the setup
and teardown run relative to running of all the test function using the fixture.
The scope dictates how often the setup and teardown get run when it’s used
by multiple test functions.
The default scope for fixtures is function scope. That means the setup portion
of the fixture will run before each test that needs it runs. Likewise, the teardown portion runs after the test is done, for each test.

Here’s a rundown of each scope value:

- scope='function'
  Run once per test function. The setup portion is run before each test using
  the fixture. The teardown portion is run after each test using the fixture.
  This is the default scope used when no scope parameter is specified.
- scope='class'
  Run once per test class, regardless of how many test methods are in the class.
  scope='module'
  Run once per module, regardless of how many test functions or methods
  or other fixtures in the module use it.
- scope='package'
  Run once per package, or test directory, regardless of how many test
  functions or methods or other fixtures in the package use it.
- scope='session'
  Run once per session. All test methods and functions using a fixture of
  session scope share one setup and teardown call.

**Please Note:** You can put fixtures into individual test files, but to share fixtures among
multiple test files, you need to use a conftest.py file either in the same directory
as the test file that’s using it or in some parent directory. The conftest.py file is
also optional. It is considered by pytest as a “local plugin” and can contain
hook functions and fixtures.

## Auto Run:

You can use `autouse=True` to get a fixture to run all of the time. This works well for code you want to
run at certain times, but tests don’t really depend on any system state or
data from the fixture.

## Rename:

The name of a fixture, listed in the parameter list of tests and other fixtures
using it, is usually the same as the function name of the fixture. However,
pytest allows you to rename fixtures with a `name` parameter to @pytest.fixture().

## Built-Ins:

1. tmp_path - for temporary directories
2. tmp_path_factory - for temporary directories
3. capsys—for capturing output
4. monkeypatch—for changing the environment or application code, like a
   lightweight form of mocking
5. capfd, capfdbinary, capsysbinary—Variants of capsys that work with file descriptors
   and/or binary output
6. caplog—Similar to capsys and the like; used for messages created with
   Python’s logging system
7. cache—Used to store and retrieve values across pytest runs. The most
   useful part of this fixture is that it allows for --last-failed, --failed-first, and
   similar flags.
8. doctest_namespace—Useful if you like to use pytest to run doctest-style tests
9. pytestconfig—Used to get access to configuration values, pluginmanager, and
   plugin hooks
10. record_property, record_testsuite_property—Used to add extra properties to the
    test or test suite. Especially useful for adding data to an XML report to
    be used by continuous integration tools
11. recwarn—Used to test warning messages
12. request—Used to provide information on the executing test function. Most
    commonly used during fixture parametrization
13. pytester, testdir—Used to provide a temporary test directory to aid in running
    and testing pytest plugins. pytester is the pathlib based replacement for
    the py.path based testdir.
14. tmpdir, tmpdir_factory—Similar to tmp_path and tmp_path_factory; used to return
    a py.path.local object instead of a pathlib.Path object
