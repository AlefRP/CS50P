from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.cookies == 0

    jar = Jar(5)
    assert jar.capacity == 5

    try:
        jar = Jar(-1)
    except ValueError as e:
        assert str(e) == "Capacity must be a non-negative integer."

    try:
        jar = Jar("invalid")
    except ValueError as e:
        assert str(e) == "Capacity must be a non-negative integer."

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.cookies == 3

    try:
        jar.deposit(3)
    except ValueError as e:
        assert str(e) == "Jar capacity is 5"

    try:
        jar.deposit(-1)
    except ValueError as e:
        assert str(e) == "Jar capacity is 5"

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.cookies == 2

    try:
        jar.withdraw(3)
    except ValueError as e:
        assert str(e) == "Jar has only 2 cookies"

    try:
        jar.withdraw(-1)
    except ValueError as e:
        assert str(e) == "Jar has only 2 cookies"

if __name__ == "__main__":
    test_init()
    test_str()
    test_deposit()
    test_withdraw()
    print("All tests passed.")