import pytest
from fuel import convert, gauge


def test_convert_well():
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_convert_wrong():
    with pytest.raises(ValueError):
        convert("2/1")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(30) == "30%"
