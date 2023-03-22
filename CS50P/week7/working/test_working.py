import pytest
from working import convert


def test_convert():
    assert convert("9:30 AM to 4:30 PM") == "09:30 to 16:30"
    assert convert("8:00 PM to 6:30 AM") == "20:00 to 06:30"
    with pytest.raises(ValueError):
        convert("9AM until 5PM")
    with pytest.raises(ValueError):
        convert("06:00 to 17:00")
    with pytest.raises(ValueError):
        convert("13 AM to 15:30 PM")
