from bank import value


def test_value():
    assert value("Hey") == 20
    assert value("Hello") == 0
    assert value("Sup") == 100
    assert value("What's up") == 100
