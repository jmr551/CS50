from numb3rs import validate

def test_valid():
    assert validate("192.168.1.1") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True

def test_invalid():
    assert validate("275.3.6.28") == False
    assert validate("27.256.6.28") == False
    assert validate("275.3.256.28") == False
    assert validate("275.3.6.256") == False
    assert validate("cat") == False
    assert validate("255.255.0") == False
