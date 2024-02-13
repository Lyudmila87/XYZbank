# Проект по автоматизации тестирования
На языке Python создан проект UI-автотестов для проверки банковских операций на основе следующих критериев:

- Применяется Selenium Grid и Pytest;
- Используется паттерн проектирования Page Object;
- Реализовано формирование отчетов о пройденных тестах через Allure;
- По завершении прогона автотестов формируется csv-файл;
- Возможность прогона тестов через Docker-контейнер.
____

Версия Python 3.11.5

Чтобы запустить тест с применением Selenium Grid, необходимо:
1. запустить командную строку 
2. из директории со скачанным файлом selenium-server-4.17.0.jar запустить команду `java -jar selenium-server-4.17.0.jar standalone` 
3. в терминале запустить тест командой `pytest --alluredir=allure_report -v tests\test_bank_operations.py`

Запустить тест через Docker:
1. В терминале запустить команду `java -jar selenium-server-4.17.0.jar standalone`
2. Запустить образ `docker run --mount type=bind,source="%cd%"\allure_report,target=/app/allure_report autotests`

Посмотреть отчет о тестах: `allure serve allure_report `