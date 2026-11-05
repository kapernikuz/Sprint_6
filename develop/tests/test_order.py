import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA_1, ORDER_DATA_2

class TestOrder:
    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
    def test_order_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.click_order_top()
        order_page = OrderPage(driver)
        order_page.fill_first_form(
            order_data["name"], order_data["surname"],
            order_data["address"], order_data["metro"], order_data["phone"]
        )
        order_page.fill_second_form(order_data["date"], order_data["comment"])
        assert "Заказ оформлен" in order_page.get_success_message()

    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
    def test_order_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.click_order_bottom()
        order_page = OrderPage(driver)
        order_page.fill_first_form(
            order_data["name"], order_data["surname"],
            order_data["address"], order_data["metro"], order_data["phone"]
        )
        order_page.fill_second_form(order_data["date"], order_data["comment"])
        assert "Заказ оформлен" in order_page.get_success_message()