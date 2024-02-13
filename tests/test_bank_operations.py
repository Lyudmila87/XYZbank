import datetime

import allure

from pages.balance_operations_page import BalanceOperations
from pages.transactions_page import Transactions
from pages.login_page import LoginCustomer
from utils import utils


@allure.story("TestSmoke")
class TestSmoke:
    @allure.title("Проведение пользовательских банковских операций")
    def test_bank_operations(self, driver):
        login_customer = LoginCustomer(driver)
        login_customer.open()
        login_customer.authorize_user("Harry Potter")

        customer_bank_operations = BalanceOperations(driver)
        time_to_balance, money_to, name_operation_to = customer_bank_operations.add_money()
        time_out_balance, money_out, name_operation_out = customer_bank_operations.withdrawl_money()
        assert customer_bank_operations.element_is_visible(BalanceOperations.BALANCE).text == '0', 'Баланс не равен нулю'

        look_transactions = Transactions(driver)
        look_transactions.go_to_transactions()
        look_transactions.is_table_present()


        transaction_data = look_transactions.transactions_info()
        assert time_to_balance == datetime.datetime.strptime(transaction_data[0], '%b %d, %Y %I:%M:%S %p'),"Дата внесения на счет не соответствует"
        assert money_to == int(transaction_data[1]), "Сумма внесения на счет не соответствует"
        assert name_operation_to == transaction_data[2], "Название операции не соответствует"
        assert time_out_balance == datetime.datetime.strptime(transaction_data[3], '%b %d, %Y %I:%M:%S %p'), "Дата списания со счета не соответствует"
        assert money_out == int(transaction_data[4]), "Сумма списания со счета не соответствует"
        assert name_operation_out == transaction_data[5], "Название операции не соответствует"

        utils.add_to_scv(time_to_balance.strftime('%b %d, %Y %I:%M:%S %p'), money_to, name_operation_to, time_out_balance.strftime('%b %d, %Y %I:%M:%S %p'), money_out, name_operation_out)








