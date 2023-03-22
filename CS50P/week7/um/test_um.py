from um import count


def test_count():
    assert count("alumni") == 0
    assert count("Yummy in the TUMMY") == 0
    assert count("um?") == 1
    assert count("Um, thanks bro, um...") == 2
    assert count("Hehe, um, no m'lady, um, I, um, hehe.. Um..") == 4
