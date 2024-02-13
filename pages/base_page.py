import allure
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Включает в себя необходимые методы для работы с webdriver"""

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @allure.step("Открыть ссылку")
    def open(self):
        self._driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')

    def element_is_visible(self, locator: tuple, timeout=5):
        """Возвращает элемент, если он видим"""

        return wait(self._driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: tuple, timeout=5):
        """Возвращает список элементов, если они видимы"""

        return wait(self._driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator: tuple, timeout=5):
        """Возвращает элемент, если он кликабелен"""

        return wait(self._driver, timeout).until(EC.element_to_be_clickable(locator))







