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

Using flags to the pytest command, you can review the  the order of operations of tests and fixtures, including the setup and
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
pytest allows you to rename fixtures with a `name` parameter to @pytest.fixture():