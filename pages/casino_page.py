from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CasinoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_game_start(self, timeout=40):
        try:

            iframe = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='staging.the-rgs.com']")))

            self.driver.switch_to.frame(iframe)

            game_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, "game"))
            )
            wait = WebDriverWait(self.driver, 20)  # Таймаут 20 секунд

            is_visible = wait.until(lambda driver: driver.execute_script(
                "return arguments[0].style.display === 'block' && arguments[0].style.visibility === 'visible';",
                game_element
            ))

            if is_visible:
                return True
            else:
                return False

        except:
            return False
