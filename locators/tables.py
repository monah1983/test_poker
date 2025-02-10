from locators.locator_types import TypeLocators


class TableLocators:
    TABLE_ROW = (TypeLocators.CLASS_NAME, "Table__body_row_wrapper")
    PLAY_BUTTON = (TypeLocators.XPATH, "//div[contains(@class, 'open SimpleButton_interactive')]")
