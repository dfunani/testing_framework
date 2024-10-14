import os
import subprocess
from cards import Card, cli


def test_field_access(card_data):
    c = Card(**card_data)
    assert c.summary == card_data["summary"]
    assert c.owner == card_data["owner"]
    assert c.state == card_data["state"]
    assert c.id == card_data["id"]


def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_equality(card_data):
    c1 = Card(**card_data)
    c2 = Card(**card_data)
    assert c1 == c2


def test_equality_with_diff_ids(card_data, alt_card_data):
    c1 = Card(**card_data)
    c2 = Card(**alt_card_data)
    assert c1 == c2


def test_inequality(card_data, alt_card_data_2):
    c1 = Card(**card_data)
    c2 = Card(**alt_card_data_2)
    assert c1 != c2


def test_from_dict(card_data):
    c1 = Card(**card_data)
    c2 = Card.from_dict(card_data)
    assert c1 == c2


def test_to_dict(card_data):
    c1 = Card(**card_data)
    c2 = c1.to_dict()
    c2_expected = card_data
    assert c2 == c2_expected


def test_builtins_tmp_path(tmp_path):
    file = tmp_path / "file.txt"
    file.write_text("Hello")
    assert file.read_text() == "Hello"


def test_builtins_tmp_path_factory(tmp_path_factory):
    path = tmp_path_factory.mktemp("sub")
    file = path / "file.txt"
    file.write_text("Hello")
    assert file.read_text() == "Hello"


def test_capsys(capsys):
    process = subprocess.run(["ls"], capture_output=True, text=True)
    print(f"Subprocess: {process.stdout.strip()}")
    cli.version()
    print(f"CapSys: {capsys.readouterr().out.strip()}")


def test_monkeypatching(monkeypatch):
    print(f"Pre-Patch: {os.getenv("test")}")
    monkeypatch.setenv("test", "test")
    print(f"Post-Patch: {os.getenv("test")}")

def test_monkeypatching_new():
    print(f"New-Patch: {os.getenv("test")}")
    