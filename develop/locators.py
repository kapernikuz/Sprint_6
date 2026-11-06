from selenium.webdriver.common.by import By

class MainPageLocators:
    FAQ_QUESTION = (By.XPATH, "//div[contains(@id, 'accordion__heading-')]")
    FAQ_ANSWER = (By.XPATH, "//div[contains(@id, 'accordion__panel-')]")
    
    @staticmethod
    def faq_question_by_index(index):
        return (By.ID, f"accordion__heading-{index}")
    
    @staticmethod
    def faq_answer_by_index(index):
        return (By.ID, f"accordion__panel-{index}")

    ORDER_TOP_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.CSS_SELECTOR, ".select-search__option")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-arrow")
    RENTAL_OPTION = (By.XPATH, "//div[text()='сутки']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

class CookieLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    COOKIE_BANNER = (By.CLASS_NAME, "App_CookieConsent__1yUIN")