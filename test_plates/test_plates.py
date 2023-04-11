from plates import is_valid


def test_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False

    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False


def test_number_end():
    assert is_valid("CS05") == False


def test_number_middle():
    assert is_valid("CS50P") == False


def test_special_charact():
    assert is_valid("PI3.14") == False


def test_two_charact():
    assert is_valid("HH") == True


def test_six_charact():
    assert is_valid("OUTATIME") == False
