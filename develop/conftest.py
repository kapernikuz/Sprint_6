import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import BASE_URL
from pages.main_page import MainPage

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def main_page_with_accepted_cookies(driver):
    page = MainPage(driver)
    page.accept_cookies()
    return page