import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import BASE_URL
from locators import CookieLocators
from pages.base_page import BasePage

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
    # Закрываем куки через методы BasePage (без прямого обращения к driver в тестах)
    page = BasePage(driver)
    try:
        page.click(CookieLocators.COOKIE_BUTTON)
    except:
        pass # Если баннера нет
    
    from pages.main_page import MainPage
    return MainPage(driver)