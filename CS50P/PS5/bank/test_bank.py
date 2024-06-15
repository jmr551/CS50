from bank import value


def test_hello():
    assert value("Hello, darling") == "$0"


def test_hi():
    assert value("Hi, darling") == "$20"


def test_hiya():
    assert value("Hey, there") == "$20"


def test_not_h():
    assert value("I'm your father") == "$100"
