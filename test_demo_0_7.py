import pytest

@pytest.fixture
def setup():
    print("Open the browser...")
    print("Login...")
    yield
    print("Log off ...")
    print("Close the browser...")

def test_add_to_card(setup):
    print("Card added successfully!")

def test_remove_to_card(setup):
    print("Card removed successfully!")

