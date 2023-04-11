import pytest
from fuel import convert, gauge

def test_convert():
    assert convert('1/1') == 100
    assert convert('3/4') == 75
    assert convert('1/4') == 25

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('5/0')

def test_convert_x_greater():
    with pytest.raises(ValueError):
        convert('5/4')

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(80) == '80%'