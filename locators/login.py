from locators.locator_types import TypeLocators


class LoginLocators:
    USERNAME_FIELD = (TypeLocators.NAME, "username")
    PASSWORD_FIELD = (TypeLocators.NAME, "password")
    LOGIN_BUTTON_MAIN = (TypeLocators.XPATH, "//div[contains(@class, 'MiniUserInfo__login_button')]")
    LOGIN_BUTTON_POPUP = (TypeLocators.XPATH, "//div[contains(@class, 'LoginContainer__sign_in_action')]")
    CANCEL_BUTTON = (TypeLocators.CLASS_NAME, "LoginContainer__close_action")
    ERROR_MESSAGE = (TypeLocators.CLASS_NAME, "error-message")
    STORAGE_KEY = 'evenbetpoker-evenbetpoker.userData'
    SING_UP_BUTTON = (TypeLocators.XPATH, "//div[contains(@class, 'MiniUserInfo__sign_up_button')]")

    NICKNAME_INPUT = (TypeLocators.CSS_SELECTOR, ".nick-field .Input")
    EMAIL_INPUT = (TypeLocators.CSS_SELECTOR, ".email-field .Input")
    PASSWORD_INPUT = (TypeLocators.CSS_SELECTOR, ".password-field .Input")
    CONFIRM_PASSWORD_INPUT = (TypeLocators.CSS_SELECTOR, ".password_confirm-field .Input")
    JOIN_CODE_INPUT = (TypeLocators.CSS_SELECTOR, ".joinCode-field .Input")
    SEND_BUTTON = (TypeLocators.XPATH, "//div[contains(@class, 'send-form')]")
