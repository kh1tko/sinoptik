import pytest

from MainPage import MainPage


class TestMainPage:

    def test_search_field_city_and_check(self, chrome):
        page = MainPage(chrome)
        page.open()
        page.fill_search_city_field('Дніпро')
        page.click_search_city_button()
        city_name = page.get_result_search_city()
        assert city_name == 'у Дніпрі (Дніпропетровськ)'

    def test_change_weather_day_two(self, chrome):
        page = MainPage(chrome)
        page.open()

        page.click_change_weather_day_two()
        number_of_weather_day = page.get_result_change_weather_days()
        class_attribute_value = number_of_weather_day.get_attribute('class')
        assert class_attribute_value == 'bd2'

    def test_change_weather_day_three(self, chrome):
        page = MainPage(chrome)
        page.open()
        page.click_change_weather_day_three()
        number_of_weather_day = page.get_result_change_weather_days()
        class_attribute_value = number_of_weather_day.get_attribute('class')
        assert class_attribute_value == 'bd3'

    def test_change_weather_day_four(self, chrome):
        page = MainPage(chrome)
        page.open()
        page.click_change_weather_day_four()
        number_of_weather_day = page.get_result_change_weather_days()
        class_attribute_value = number_of_weather_day.get_attribute('class')
        assert class_attribute_value == 'bd4'

    def test_change_weather_day_five(self, chrome):
        page = MainPage(chrome)
        page.open()
        page.click_change_weather_day_five()
        number_of_weather_day = page.get_result_change_weather_days()
        class_attribute_value = number_of_weather_day.get_attribute('class')
        assert class_attribute_value == 'bd5'

    def test_change_weather_day_six(self, chrome):
        page = MainPage(chrome)
        page.open()
        page.click_change_weather_day_six()
        number_of_weather_day = page.get_result_change_weather_days()
        class_attribute_value = number_of_weather_day.get_attribute('class')
        assert class_attribute_value == 'bd6'

    def test_change_weather_day_seven(self, chrome):
        page = MainPage(chrome)
        page.open()
        page.click_change_weather_day_seven()
        number_of_weather_day = page.get_result_change_weather_days()
        class_attribute_value = number_of_weather_day.get_attribute('class')
        assert class_attribute_value == 'bd7'
