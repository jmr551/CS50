import pytest
from fuel import convert, gauge


def test_convert_well():
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("1/2") == 50

def test_convert_wrong():
    with pytest.raises(ValueError)
        convert(2/1)

