from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы вопросов
    FAQ_QUESTION_1 = (By.ID, "accordion__heading-0")
    FAQ_ANSWER_1 = (By.ID, "accordion__panel-0")

    # Кнопки «Заказать»
    ORDER_TOP_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")

    def click_faq_question(self, index):
        locator = (By.ID, f"accordion__heading-{index}")
        self.click(locator)

    def get_faq_answer(self, index):
        locator = (By.ID, f"accordion__panel-{index}")
        # Ждём, пока в панели появится непустой текст
        self.wait.until(
            lambda d: d.find_element(*locator).get_attribute("textContent").strip() != ""
        )
        element = self.find(locator)
        # Читаем текст через JS (обход проблемы с getText в Firefox)
        return self.driver.execute_script("return arguments[0].textContent;", element)

    def click_order_top(self):
        self.click(self.ORDER_TOP_BUTTON)

    def click_order_bottom(self):
        self.click(self.ORDER_BOTTOM_BUTTON)