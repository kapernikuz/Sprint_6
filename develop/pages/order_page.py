import allure
from locators import OrderPageLocators
from .base_page import BasePage

class OrderPage(BasePage):
    @allure.step("Заполнение первой формы заказа")
    def fill_first_form(self, name, surname, address, metro, phone):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.send_keys(OrderPageLocators.METRO_INPUT, metro)
        self.click(OrderPageLocators.METRO_OPTION)
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение второй формы заказа")
    def fill_second_form(self, date, comment):
        self.send_keys(OrderPageLocators.DATE_INPUT, date)
        self.click(OrderPageLocators.RENTAL_PERIOD)
        self.click(OrderPageLocators.RENTAL_OPTION)
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получение текста сообщения об успешном заказе")
    def get_success_message(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)