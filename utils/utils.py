import csv

import allure

@allure.step("Сформировать табличку")
def add_to_scv(*args):

    datas = [
            ['Дата-времяТранзакции', 'Сумма', 'ТипТранзакции'],
            [args[0], args[1], args[2]],
            [args[3], args[4], args[5]]
            ]

    with open("allure_report/transactions.csv", 'a', encoding='UTF=8', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(datas)

def fib(n):
    """ рассчет числа Фибоначчи """
    if n < 2:
        return n
    return fib(n-1)+fib(n-2)
