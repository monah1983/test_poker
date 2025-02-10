from data import environment
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self.host = environment.Environment()
        self.driver = driver
        self.base_url = f"{self.host.get_base_url()}"

    def open_base_page(self):
        self.driver.get(self.base_url)

    def open(self, url: str):
        self.driver.get(url)

    def click(self, locator: tuple):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()

    def input(self, locator: tuple, data: str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(data)

    def get_text(self, locator: tuple, index: int = 0) -> str:
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        return elements[index].text if elements else ""

    def wait_for_element(self, locator: tuple, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def is_element_present(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_not_present(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
            return False
        except TimeoutException:
            return True

    def click_first_element(self, locator: tuple):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        if elements:
            elements[0].click()
