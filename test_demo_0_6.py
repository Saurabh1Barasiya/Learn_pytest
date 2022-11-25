import pytest

def test_first_case():
    assert 10 == 10

def test_second_case():
    assert 2+2 == 4

@pytest.mark.xfail
def test_third_case():
    assert 20 == 2



