from plates import is_valid


def test_CS50():
    assert is_valid("CS50") == "Valid"

def test_CS05():
    assert is_valid("CS05") == "Invalid"

def test_CS50P():
    assert is_valid("CS50P") == "Invalid"

def test_PI314():
    assert is_valid("PI3.14") == "Invalid"

def test_H():
    assert is_valid("H") == "Invalid"

def test_OUTATIME():
    assert is_valid("OUTATIME") == "Invalid"
