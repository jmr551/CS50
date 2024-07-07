import pytest
from working import convert

def test_right():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_wrong():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("13:00 AM to 3:00 PM")
    with pytest.raises(ValueError):
        convert("11:60 AM to 4:00 PM")
    with pytest.raises(ValueError):
        convert("11:50 FM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("11:50 AM TO 6:00 PM")
    with pytest.raises(ValueError):
        convert("11:50 AM TO 13:00 PM")
    with pytest.raises(ValueError):
        convert("11:50 AM TO 11:60 PM")
    with pytest.raises(ValueError):
        convert("11:50 AM TO 11:50 EM")

