import pytest
from programs import list_of_squares

def test_list_of_squares_one():
    assert list_of_squares.list_of_squares(1)
def test_list_of_squares_five():
    assert list_of_squares.list_of_squares(5)