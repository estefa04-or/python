from calculator import add, multiply, is_adult


def test_add():
    assert add(2, 3) == 5
    assert add(0, 5) == 5
    assert add(-2, 3) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_is_adult():
    assert is_adult(20) == True


def test_is_not_adult():
    assert is_adult(17) == False