from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:

    def __init__(self, driver: WebDriver):
        self.url = 'https://ua.sinoptik.ua/'
        self.driver = driver
        self.search_city_field = (By.ID, 'search_city')
        self.search_city_button = (By.CLASS_NAME, 'search_city-submit')
        self.change_language_page = (By.CSS_SELECTOR, 'a[rel="alternate"]')
        self.result_city_name = (By.CSS_SELECTOR, '#header .cityNameShort strong')
        self.change_weather_day_two = (By.ID, 'bd2')
        self.change_weather_day_three = (By.CSS_SELECTOR, '#bd3 > p:nth-child(1) > a')
        self.change_weather_day_four = (By.CSS_SELECTOR, '#bd4 > p:nth-child(1) > a')
        self.change_weather_day_five = (By.CSS_SELECTOR, '#bd5 > p:nth-child(1) > a')
        self.change_weather_day_six = (By.CSS_SELECTOR, '#bd6 > p:nth-child(1) > a')
        self.change_weather_day_seven = (By.CSS_SELECTOR, '#bd7 > p:nth-child(1) > a')
        self.result_change_weather_days = (By.CSS_SELECTOR, 'div#blockDays')
        self.show_weather_linkblock = (By.CSS_SELECTOR, 'h2.show-weather-linkblock > a')
        self.result_show_weather_linkblock = (By.CSS_SELECTOR, '#weatherLinks')

    def open(self) -> 'MainPage':
        self.driver.get(self.url)
        return self

    def clear_search_city_field(self) -> None:
        self.driver.find_element(*self.search_city_field).clear()

    def fill_search_city_field(self, text) -> None:
        self.driver.find_element(*self.search_city_field).send_keys(text)

    def click_search_city_button(self) -> None:
        self.driver.find_element(*self.search_city_button).click()

    def scroll_down(self) -> None:
        self.driver.execute_script('window.scrollBy(0, 500);')

    def click_show_weather_linkblock(self):
        self.driver.find_element(*self.show_weather_linkblock).click()

    def get_result_show_weather_linkblock(self):
        return self.driver.find_element(*self.result_show_weather_linkblock)

    def get_result_search_city(self):
        return self.driver.find_element(*self.result_city_name).text

    def click_change_weather_day_two(self):
        self.driver.find_element(*self.change_weather_day_two).click()

    def click_change_weather_day_three(self):
        self.driver.find_element(*self.change_weather_day_three).click()

    def click_change_weather_day_four(self):
        self.driver.find_element(*self.change_weather_day_four).click()

    def click_change_weather_day_five(self):
        self.driver.find_element(*self.change_weather_day_five).click()

    def click_change_weather_day_six(self):
        self.driver.find_element(*self.change_weather_day_six).click()

    def click_change_weather_day_seven(self):
        self.driver.find_element(*self.change_weather_day_seven).click()

    def get_result_change_weather_days(self):
        return self.driver.find_element(*self.result_change_weather_days)
