import pytest


@pytest.fixture
def card_data():
    return {"summary": "something", "owner": "brian", "state": "todo", "id": 123}

@pytest.fixture
def alt_card_data():
    return {"summary": "something", "owner": "brian", "state": "todo", "id": 4567}

@pytest.fixture
def alt_card_data_2():
    return {"summary": "something", "owner": "okken", "state": "todo", "id": 4567}

@pytest.fixture
def done_card_data():
    return {"summary": "completely different", "owner": "okken", "state": "done", "id": 123}

