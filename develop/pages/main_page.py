import allure
from locators import MainPageLocators, CookieLocators
from .base_page import BasePage
from .order_page import OrderPage


class MainPage(BasePage):
    @allure.step("Принятие куки")
    def accept_cookies(self):
        # Используем BasePage.click для обработки перекрытий
        self.click(CookieLocators.COOKIE_BUTTON)

    @allure.step("Клик по вопросу FAQ с индексом {index}")
    def click_faq_question(self, index):
        locator = MainPageLocators.faq_question_by_index(index)
        self.click(locator)

    @allure.step("Получение ответа на вопрос FAQ с индексом {index}")
    def get_faq_answer(self, index):
        locator = MainPageLocators.faq_answer_by_index(index)
        self.wait_for_text(locator)
        return self.get_text(locator)

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_order_top(self):
        self.click(MainPageLocators.ORDER_TOP_BUTTON)
        return OrderPage(self.driver)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_order_bottom(self):
        self.click(MainPageLocators.ORDER_BOTTOM_BUTTON)
        return OrderPage(self.driver)

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Получение текущего URL")
    def get_url(self):
        return self.get_current_url()