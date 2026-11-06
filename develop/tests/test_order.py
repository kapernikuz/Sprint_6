import pytest
import allure
from data import ORDER_DATA_1, ORDER_DATA_2, BASE_URL
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Позитивный сценарий заказа через верхнюю кнопку")
    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
    def test_order_top_button(self, main_page_with_accepted_cookies, order_data):
        main_page = main_page_with_accepted_cookies
        main_page.click_order_top()
        
        order_page = OrderPage(main_page.driver)
        order_page.fill_first_form(order_data["name"], order_data["surname"], order_data["address"], order_data["metro"], order_data["phone"])
        order_page.fill_second_form(order_data["date"], order_data["comment"])
        
        assert "Заказ оформлен" in order_page.get_success_message()

    @allure.title("Позитивный сценарий заказа через нижнюю кнопку")
    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
    def test_order_bottom_button(self, main_page_with_accepted_cookies, order_data):
        main_page = main_page_with_accepted_cookies
        main_page.click_order_bottom()
        
        order_page = OrderPage(main_page.driver)
        order_page.fill_first_form(order_data["name"], order_data["surname"], order_data["address"], order_data["metro"], order_data["phone"])
        order_page.fill_second_form(order_data["date"], order_data["comment"])
        
        assert "Заказ оформлен" in order_page.get_success_message()