import json
import time

from locators.login import LoginLocators
from pages.base_page import BasePage
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_window(self):
        self.click(LoginLocators.LOGIN_BUTTON_MAIN)

    def open_sing_up_window(self):
        self.click(LoginLocators.SING_UP_BUTTON)

    def is_class_present(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def check_guest_login(self, storage_key=LoginLocators.STORAGE_KEY):

        time.sleep(5)

        user_data = self.driver.execute_script(f"return localStorage.getItem('{storage_key}');")

        if user_data:
            try:
                user_data_json = json.loads(user_data)
                guest_login = user_data_json.get("guestLogin", None)

                if guest_login is False:
                    return True
                else:
                    return False
            except json.JSONDecodeError:
                return False
        else:
            return False
