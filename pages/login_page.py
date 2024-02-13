from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import allure

from pages.base_page import BasePage


class LoginCustomer(BasePage):
    CUSTOMER_LOGIN = (By.CSS_SELECTOR, "button[ng-click='customer()']")
    SELECT_NAME = (By.CSS_SELECTOR, '#userSelect')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    @allure.step("Авторизоваться")
    def authorize_user(self, name):
        self.element_is_clickable(self.CUSTOMER_LOGIN).click()
        select = Select(self.element_is_clickable(self.SELECT_NAME))
        select.select_by_visible_text(name)
        self.element_is_clickable(self.LOGIN_BUTTON).click()
