from numb3rs import validate

def test_valid_ip():
    assert validate("192.168.1.1") == True
    assert validate("10.0.0.1") == True
    assert validate("172.16.0.1") == True
    assert validate("127.0.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid_ip():
    assert validate("256.0.0.1") == False
    assert validate("10.0.0") == False
    assert validate("172.16.0.1.1") == False
    assert validate("256.0.0.1") == False
    assert validate("1000.0.0.1") == False
    assert validate("abc.0.0.1") == False
    # Test for incorrect IPv4 format
    assert validate("75.456.76.65") == False

def test_invalid_ip_first_byte():
    assert validate("256.277.277.277") == False
