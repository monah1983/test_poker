import pytest
import allure

from allure_commons.types import AttachmentType
from data import environment
from fixtures.pages_manager import PageManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--bn', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--h', action='store', type=bool, default=False, help='Choose headless mode: True or False')
    parser.addoption('--s', action='store', default='1920,1080', help='Size window: width,height')
    parser.addoption('--t', action='store', type=int, default=60000, help='Choose timeout (ms)')
    parser.addoption("--env", action="store", default="prod", help="Environment to run tests in: dev or prod")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("bn")
    headless = request.config.getoption("h")
    window_size = request.config.getoption("s")

    options = None
    driver = None

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument(f"--window-size={window_size}")
        options.add_argument("--start-maximized")
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        width, height = map(int, window_size.split(","))
        options.add_argument(f"--width={width}")
        options.add_argument(f"--height={height}")
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(request.config.getoption("t") / 1000)

    yield driver

    driver.quit()


@pytest.fixture()
def manager(browser):
    manager = PageManager(browser)
    return manager


@pytest.fixture()
def host():
    return environment.Environment()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'setup' and rep.failed:
        print(f"Set up has failed: {rep.nodeid}")
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs['browser']
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
        allure.attach(rep.longreprtext, name='Log', attachment_type=AttachmentType.TEXT)
        allure.attach(rep.capstderr, name='Stderr', attachment_type=AttachmentType.TEXT)
        allure.attach(rep.capstdout, name='Stdout', attachment_type=AttachmentType.TEXT)
        print(f"Test failed: {rep.nodeid}")
