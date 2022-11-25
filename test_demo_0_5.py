import pytest

def test_demo_0_1():
    assert 4+5 == 9

@pytest.mark.skip
def test_demo_0_2():
    assert 4+6 == 10

@pytest.mark.skip
def test_demo_0_3():
    assert 'apple' == 'apple'

