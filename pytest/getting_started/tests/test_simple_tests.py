def test_pass():
    assert 1 == 1
    assert "string" == "string"
    assert (1, 2, 3) == (1, 2, 3)
    
def test_fail():
    assert 1 == 2
    assert "string" == "strings"
    assert (1, 2, 3) == (1, 2, 3, 4)