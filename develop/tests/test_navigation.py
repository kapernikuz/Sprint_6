import allure
from pages.main_page import MainPage

@allure.feature("Навигация")
class TestNavigation:
    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo(self, main_page_with_accepted_cookies):
        page = main_page_with_accepted_cookies
        page.click_scooter_logo()
        assert "qa-scooter.education-services.ru" in page.get_url()

    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_yandex_logo(self, main_page_with_accepted_cookies):
        page = main_page_with_accepted_cookies
        
        original_window = page.get_current_window_handle()
        page.click_yandex_logo()
        page.switch_to_new_window(original_window)
        page.wait_for_url("ya.ru")
        
        assert "ya.ru" in page.get_url()
        
        page.close_and_switch_back(original_window)