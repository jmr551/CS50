from numb3rs import validate

def test_valid():
    assert validate("192.168.1.1") == True

def test_invalid():

