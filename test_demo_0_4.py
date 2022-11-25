
import pytest

def testlogin():
    print("login function works")

@pytest.mark.sanity
def testlogout():
    print("logout function works")

@pytest.mark.sanity
def testadd_to_card():
    print("\nadd_to_card function works")


# pytest test_demo_0_4.py -m sanity -v  ====> ye only marker ko hi run karega.

# pytest test_demo_0_4.py -kvs log  ===> to ye log ko search karega and jitne bhi function me log keyword milega unko ye run kar dega.

