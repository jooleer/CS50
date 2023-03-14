from twttr import shorten


def test_shorten():
    assert shorten("whats up dog") == "whts p dg"
    assert shorten("WHATS UP DOG") == "WHTS P DG"
    assert shorten("WHATS UP D0G") == "WHTS P D0G"
    assert shorten("WHATS UP, DOG?") == "WHTS P, DG?"
