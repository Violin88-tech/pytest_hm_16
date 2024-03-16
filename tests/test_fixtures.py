import pytest
from selene import browser, have

@pytest.mark.desktop
def test_github_desktop():
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()