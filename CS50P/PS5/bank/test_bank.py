from bank import value

def test_hello():
    print("Test Hello")
    assert value("Hello, darling") == 0

def test_hi():
    print("Test Hi")
    assert value("Hi, darling") == 20

def test_hey():
    print("Test Hey")
    assert value("Hey, there") == 20

def test_not_h():
    print("Test Not H")
    assert value("I'm your father") == 100

# Ejecutar las pruebas
if __name__ == "__main__":
    test_hello()
    test_hi()
    test_hey()
    test_not_h()
