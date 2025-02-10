import allure
import pytest

from faker import Faker
from locators.login import LoginLocators
from locators.poker import PokerLocators
from locators.tables import TableLocators
from locators.tabs import TabLocators
from locators.casino import CasinoLocators
from locators.menu import MenuLocators


def test_login(browser, manager, host):
    with allure.step("Open main page"):
        manager.main_page.open_base_page()

    with allure.step("Click login button"):
        manager.main_page.open_login_window()

    with allure.step("Enter username"):
        manager.main_page.input(LoginLocators.USERNAME_FIELD, host.username)

    with allure.step("Enter password"):
        manager.main_page.input(LoginLocators.PASSWORD_FIELD, host.password)

    with allure.step("Click login button in popup"):
        manager.main_page.click(LoginLocators.LOGIN_BUTTON_POPUP)

    with allure.step("Open menu"):
        manager.main_page.click(MenuLocators.MENU_BUTTON)

    with allure.step("Open account section"):
        manager.main_page.click(MenuLocators.ACCOUNT)

    with allure.step("Get nickname from account info"):
        manager.main_page.click(MenuLocators.ACCOUNT_INFO)

    with allure.step("Check nickname matches username"):
        nickname = manager.main_page.get_text(MenuLocators.NICK_NAME)

    assert host.username == nickname, (
        f"Username mismatch: expected {host.username}, but found {nickname}"
    )


@pytest.mark.smoke
def test_registration(browser, manager, host):
    fake = Faker()
    nickname = fake.pystr(min_chars=3, max_chars=16)
    email = fake.email()
    password = fake.password(length=12)

    with allure.step("Open main page"):
        manager.main_page.open_base_page()

    with allure.step("Click sing up button"):
        manager.main_page.open_sing_up_window()

    with allure.step("Enter nickname"):
        manager.main_page.input(LoginLocators.NICKNAME_INPUT, nickname)

    with allure.step("Enter email"):
        manager.main_page.input(LoginLocators.EMAIL_INPUT, email)

    with allure.step("Enter password"):
        manager.main_page.input(LoginLocators.PASSWORD_INPUT, password)

    with allure.step("Enter confirm password"):
        manager.main_page.input(LoginLocators.CONFIRM_PASSWORD_INPUT, password)

    with allure.step("Click send button"):
        manager.main_page.click(LoginLocators.SEND_BUTTON)

    with allure.step("Open menu"):
        manager.main_page.click(MenuLocators.MENU_BUTTON)

    with allure.step("Open account section"):
        manager.main_page.click(MenuLocators.ACCOUNT)

    with allure.step("Get nickname from account info"):
        manager.main_page.click(MenuLocators.ACCOUNT_INFO)

    with allure.step("Check nickname matches the registered one"):
        user_nickname = manager.main_page.get_text(MenuLocators.NICK_NAME)

    assert user_nickname == nickname, (
        f"Nickname mismatch: expected {nickname}, but found {user_nickname}"
    )


@pytest.mark.smoke
def test_start_first_game_casino(browser, manager, host):
    with allure.step("Open main page"):
        manager.main_page.open_base_page()

    with allure.step("Click login button"):
        manager.main_page.open_login_window()

    with allure.step("Enter username"):
        manager.main_page.input(LoginLocators.USERNAME_FIELD, host.username)

    with allure.step("Enter password"):
        manager.main_page.input(LoginLocators.PASSWORD_FIELD, host.password)

    with allure.step("Click login button in popup"):
        manager.main_page.click(LoginLocators.LOGIN_BUTTON_POPUP)

    with allure.step("Click casino button"):
        manager.main_page.click(TabLocators.CASINO_BUTTON)

    with allure.step("Start game"):
        manager.main_page.click_first_element(CasinoLocators.GAME_CONTAINER)
        manager.main_page.click(CasinoLocators.PLAY_BUTTON)

    with allure.step("Wait for game to start"):
        is_game = manager.casino_page.wait_for_game_start()

    assert is_game, 'Game is not loaded'


@pytest.mark.smoke
def test_start_first_table_poker(browser, manager, host):
    with allure.step("Open main page"):
        manager.main_page.open_base_page()

    with allure.step("Click login button"):
        manager.main_page.open_login_window()

    with allure.step("Enter username"):
        manager.main_page.input(LoginLocators.USERNAME_FIELD, host.username)

    with allure.step("Enter password"):
        manager.main_page.input(LoginLocators.PASSWORD_FIELD, host.password)

    with allure.step("Click login button in popup"):
        manager.main_page.click(LoginLocators.LOGIN_BUTTON_POPUP)

    with allure.step("Click first row on the list"):
        manager.main_page.click_first_element(TableLocators.TABLE_ROW)

    with allure.step("Click play button"):
        manager.main_page.click(TableLocators.PLAY_BUTTON)

    with allure.step("Check if OK button is present"):
        element = manager.main_page.is_element_present(PokerLocators.OK_BUTTON)

    assert element, 'OK button not shown, game is not loaded'
