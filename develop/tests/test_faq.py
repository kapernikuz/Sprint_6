import pytest
import allure
from data import BASE_URL, FAQ_EXPECTED_ANSWERS
from pages.main_page import MainPage

@allure.feature("FAQ")
class TestFAQ:
    @allure.title("Проверка ответа на вопрос FAQ: {index}")
    @pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_faq_question(self, main_page_with_accepted_cookies, index):
        page = main_page_with_accepted_cookies
        page.click_faq_question(index)
        answer = page.get_faq_answer(index)
        
        # Проверяем конкретный ожидаемый текст
        assert answer.strip() == FAQ_EXPECTED_ANSWERS[index].strip(), \
            f"Неверный ответ на вопрос {index}"