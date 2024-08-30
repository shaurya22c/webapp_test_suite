import pytest
from selenium.webdriver.common.by import By

def test_valid_login(browser):
    browser.get('http://127.0.0.1:8000')

    username_input = browser.find_element(By.ID, 'username')
    password_input = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login')

    username_input.send_keys('validUser')
    password_input.send_keys('validPass')

    login_button.click()

    assert "Login successful" in browser.page_source


def test_invalid_login(browser):
    browser.get('http://127.0.0.1:8000')

    username_input = browser.find_element(By.ID, 'username')
    password_input = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login')

    username_input.send_keys('invalidUser')
    password_input.send_keys('invalidPass')

    login_button.click()

    assert "Login failed" in browser.page_source