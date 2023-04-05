from jar import Jar
import pytest


def test_init():
    # test initialization of Jar class
    jar = Jar()


def test_str():
    # use test strings provided by CS50P (https://cs50.harvard.edu/python/2022/psets/8/jar/)
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    # initialize a Jar, deposit 5 and check if size matches
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    # try to deposit more than Jar size capacity (default = 12)
    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw():
    jar = Jar()

    # deposit 10 cookies and withdraw 8, check if size matches result
    jar.deposit(10)
    jar.withdraw(8)
    assert jar.size == 2

    # attemp to withdraw more cookies than there are in the jar
    with pytest.raises(ValueError):
        jar.withdraw(15)
