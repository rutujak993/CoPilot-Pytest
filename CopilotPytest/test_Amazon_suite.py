from AutoInfraAmazon import *
import pytest


@pytest.mark.parametrize(
    "username, password",
    [
        ('8999634754', 'Shriram@1693')
    ]

)
def test_login_to_amazon(username, password):
    TestLogin.test_login(username, password)

def test_connect_with_us_on_facebook():
    TestLogin.connect_with_us_on_facebook()


def test_connect_with_us_on_Twitter():
    TestLogin.connect_with_us_on_Twitter()
