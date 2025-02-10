from locators.locator_types import TypeLocators


class CasinoLocators:
    GAME_CONTAINER = (TypeLocators.CLASS_NAME, "viewable-monitor")
    PLAY_BUTTON = (TypeLocators.XPATH, "//div[contains(@class, 'WidgetCasinoGameListItemContainer__play')]")
    GAME_START = (TypeLocators.XPATH, "//div[@id='game' and contains(@style, 'display: block')]")
    iIFRAME = (TypeLocators.CSS_SELECTOR, "iframe[src*='staging.the-rgs.com']")
