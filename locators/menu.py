from locators.locator_types import TypeLocators


class MenuLocators:
    MENU_BUTTON = (TypeLocators.CLASS_NAME, "menu_button")
    ACCOUNT = (TypeLocators.XPATH, "//div[contains(@class, 'account')]")
    ACCOUNT_INFO = (TypeLocators.XPATH, "//div[contains(@class, 'account_info')]")
    NICK_NAME = (TypeLocators.XPATH, "//div[contains(@class, 'AccountInformationContainer__form_field')]//div[@class='FormField__control']")


