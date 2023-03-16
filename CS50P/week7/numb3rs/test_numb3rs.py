# numb3rs or numb3rs_alternative 
from numb3rs import validate


def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("10.10.10") == False
    assert validate("10.10.100.300") == False
