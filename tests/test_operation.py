from src.math_operations import add, sub, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(4, 3) == 1
    assert sub(3, 3) == 0
    assert sub(2, 3) == -1

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 9) == 0