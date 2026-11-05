from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderPage(BasePage):
    # Поля первой формы
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.CSS_SELECTOR, ".select-search__option")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Поля второй формы
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-arrow")
    RENTAL_OPTION = (By.XPATH, "//div[text()='сутки']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    def fill_first_form(self, name, surname, address, metro, phone):
        self.find(self.NAME_INPUT).send_keys(name)
        self.find(self.SURNAME_INPUT).send_keys(surname)
        self.find(self.ADDRESS_INPUT).send_keys(address)
        self.find(self.METRO_INPUT).send_keys(metro)
        self.click(self.METRO_OPTION)
        self.find(self.PHONE_INPUT).send_keys(phone)
        self.click(self.NEXT_BUTTON)

    def fill_second_form(self, date, comment):
        self.find(self.DATE_INPUT).send_keys(date)
        self.click(self.RENTAL_PERIOD)
        self.click(self.RENTAL_OPTION)
        self.find(self.COMMENT_INPUT).send_keys(comment)
        self.click(self.ORDER_BUTTON)
        self.click(self.CONFIRM_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)