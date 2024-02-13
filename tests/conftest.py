import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# #локальный запуск автотестов
# @allure.step("Открыть и закрыть браузер")
# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     yield driver
#     driver.quit()

@allure.step("Открыть и закрыть браузер")
@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Remote(
        command_executor='http://192.168.88.254:4444/wd/hub',  # localhost
        options=options
    )

    yield driver
    driver.quit()