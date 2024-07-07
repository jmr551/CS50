from um import count

def test_count():
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("um aja um umm sum um") == 3
    assert count("Um loco, no se, um") == 2
