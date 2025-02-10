from locators.casino import CasinoLocators
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CasinoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_game_start(self) -> bool:
        try:

            iframe = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(CasinoLocators.IFRAME))

            self.driver.switch_to.frame(iframe)
            wait = WebDriverWait(self.driver, 40)
            is_visible = wait.until(
                EC.presence_of_element_located(CasinoLocators.SPAN_LOAD))

            if is_visible:
                return True
            else:
                return False

        except:
            return False
