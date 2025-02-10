from locators.locator_types import TypeLocators


class TabLocators:
    POKER_BUTTON = (TypeLocators.XPATH, "//div[contains(@class, 'lpg-lobby-poker-games-global-page_button')]")
    CLUBS_BUTTON = (TypeLocators.XPATH, "//div[contains(@class, 'lpg-lobby-clubs-global-page_button')]")
    CASINO_BUTTON = (TypeLocators.XPATH, "//div[contains(@class, 'lpg-lobby-casino-global-page_button')]")
    PROMO_BUTTON = (TypeLocators.XPATH, "//div[contains(@class, 'lpg-lobby-promo-global-page_button')]")
    SPORTS_BUTTON = (TypeLocators.XPATH, "//div[contains(@class, 'lpg-lobby-sports-global-page_button')]")
    MYGAMES_BUTTON = (TypeLocators.XPATH, "//div[contains(@class, 'lpg-lobby-my-games-global-page_button')]")
    STORE_BUTTON = (TypeLocators.XPATH, "//div[contains(@class, 'lpg-lobby-internal-store-global-page_button')]")
