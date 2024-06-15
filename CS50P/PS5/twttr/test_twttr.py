import pytest
from twttr import shorten


def minusculas():
    assert shorten("aeiou") == ""
    assert shorten("murcielago") == "mrclg"


def mayusculas():
    assert shorten("AEIOU") == ""
    assert shorten("MURCIELAGO") == "MRCLG"
