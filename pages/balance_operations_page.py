import datetime

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import utils


class BalanceOperations(BasePage):
    DEPOSIT = (By.CSS_SELECTOR, "button[ng-click='deposit()']")
    WITHDRAWl = (By.CSS_SELECTOR, "button[ng-click='withdrawl()']")
    AMOUNT_INPUT = (By.XPATH, "//input[@type='number']")
    DEPOSIT_BUTTON = (By.XPATH, "//form/button[text()='Deposit']")
    WITHDRAWl_BUTTON = (By.XPATH, "//form/button[text()='Withdraw']")
    WITHDRAWl_TEXT = (By.XPATH, "//label[text()='Amount to be Withdrawn :']")
    BALANCE = (By.XPATH, "//div/strong[@class='ng-binding' and text()='0']")

    @allure.step("Внести деньги на счет")
    def add_money(self):
        money = utils.fib(datetime.datetime.now().day + 1)
        self.element_is_clickable(self.DEPOSIT).click()
        self.element_is_visible(self.AMOUNT_INPUT).send_keys(money)
        self.element_is_clickable(self.DEPOSIT_BUTTON).click()
        date_str = datetime.datetime.now().strftime('%b %d, %Y %I:%M:%S %p')
        date = datetime.datetime.strptime(date_str, '%b %d, %Y %I:%M:%S %p')
        return date, money, "Credit"

    @allure.step("Списать деньги со счета")
    def withdrawl_money(self):
        money = utils.fib(datetime.datetime.now().day + 1)
        self.element_is_clickable(self.WITHDRAWl).click()
        self.element_is_visible(self.WITHDRAWl_TEXT)
        self.element_is_visible(self.AMOUNT_INPUT).send_keys(money)
        self.element_is_clickable(self.WITHDRAWl_BUTTON).click()
        date_str = datetime.datetime.now().strftime('%b %d, %Y %I:%M:%S %p')
        date = datetime.datetime.strptime(date_str, '%b %d, %Y %I:%M:%S %p')
        return date, money, "Debit"

