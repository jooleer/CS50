from seasons import convert
import pytest


def test_convert():
    assert convert(
        "1990-10-10") == "Seventeen million, seventy-six thousand, nine hundred sixty minutes"
    assert convert(
        "2000-01-01") == "Twelve million, two hundred twenty-four thousand, one hundred sixty minutes"
    with pytest.raises(SystemExit):
        assert convert("bark bark") == SystemExit
