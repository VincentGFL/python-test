import pytest
from programs import factorial

def test_factorial_zero():
    assert factorial.fact(1) == 1 
def test_factorial_one():
    assert factorial.fact(5) == 120 

