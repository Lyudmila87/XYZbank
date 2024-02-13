import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Transactions(BasePage):

    TRANSACTIONS_BUTTON = (By.CSS_SELECTOR, "button[ng-click='transactions()']")
    ELEMENTS = (By.XPATH, "//td[@class ='ng-binding']")
    TABLE = (By.XPATH, "//tbody/tr")

    @allure.step("Перейти на страницу с транзакциями")
    def go_to_transactions(self):
        time.sleep(2)
        self.element_is_clickable(self.TRANSACTIONS_BUTTON).click()

    @allure.step("Проверить, появилась ли таблица с информацией о транзакциях")
    def is_table_present(self):
        try:
            self.element_is_visible(self.TABLE)
        except TimeoutException:
            raise Exception('Таблица с банковскими операциями не представлена')

    @allure.step("Получить сведения о транзакциях")
    def transactions_info(self):
        value_list = self.elements_are_visible(self.ELEMENTS)
        transaction_data = [item.text for item in value_list]
        return transaction_data





