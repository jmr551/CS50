from twttr import shorten


def test_minusculas():
    assert shorten("aeiou") == ""
    assert shorten("murcielago") == "mrclg"


def test_mayusculas():
    assert shorten("AEIOU") == ""
    assert shorten("MURCIELAGO") == "MRCLG"
