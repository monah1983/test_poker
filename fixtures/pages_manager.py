from pages.casino_page import CasinoPage
from pages.main_page import MainPage


class PageManager:
    __main_page = None
    __casino_page = None

    @property
    def main_page(self) -> MainPage:
        if not self.__main_page:
            self.__main_page = MainPage(self._driver)
        return self.__main_page

    @property
    def casino_page(self) -> CasinoPage:
        if not self.__casino_page:
            self.__casino_page = CasinoPage(self._driver)
        return self.__casino_page

    def __init__(self, driver):
        self._driver = driver
