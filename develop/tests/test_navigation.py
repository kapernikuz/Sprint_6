from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNavigation:
    def test_scooter_logo(self, driver):
        driver.find_element(By.CLASS_NAME, "Header_LogoScooter__3lsAR").click()
        assert "qa-scooter.education-services.ru" in driver.current_url

    def test_yandex_logo(self, driver):
        original_window = driver.current_window_handle
        driver.find_element(By.CLASS_NAME, "Header_LogoYandex__3TSOI").click()

        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # Логотип Яндекса на учебном стенде ведёт на ya.ru
        WebDriverWait(driver, 10).until(EC.url_contains("ya.ru"))

        assert "ya.ru" in driver.current_url

        driver.close()
        driver.switch_to.window(original_window)