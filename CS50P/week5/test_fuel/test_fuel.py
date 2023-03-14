from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
