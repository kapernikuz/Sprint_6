import pytest
from pages.main_page import MainPage

class TestFAQ:
    @pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_faq_question(self, driver, index):
        page = MainPage(driver)
        page.click_faq_question(index)
        answer = page.get_faq_answer(index)
        assert answer != "", f"Ответ на вопрос {index} пустой"