import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста '{text}' в поле {locator}")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.execute_script("return arguments[0].textContent;", element)

    @allure.step("Ожидание появления непустого текста в {locator}")
    def wait_for_text(self, locator):
        self.wait.until(
            lambda d: d.find_element(*locator).get_attribute("textContent").strip() != ""
        )

    @allure.step("Ожидание открытия новой вкладки и переключение на неё")
    def switch_to_new_window(self, original_window):
        self.wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    @allure.step("Ожидание URL, содержащего '{text}'")
    def wait_for_url(self, text):
        self.wait.until(EC.url_contains(text))

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Закрытие текущей вкладки и возврат на предыдущую")
    def close_and_switch_back(self, original_window):
        self.driver.close()
        self.driver.switch_to.window(original_window)

    @allure.step("Получение ID текущего окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle