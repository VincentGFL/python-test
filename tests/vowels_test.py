import pytest
from programs import vowels

def test_vowels():
    assert vowels.vowels("testing") == 2