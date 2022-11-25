import pytest 

@pytest.fixture
def tc_setup():
    print("connecting to server...")
    print("login..")
    yield
    print("Logout..")
    print("Connection close")


