import os

from dotenv import load_dotenv

load_dotenv()


class Environment:
    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: 'https://example.ru/',
        PROD: 'https://poker.evenbetpoker.com/html5'
    }

    def __init__(self):
        self.env = os.getenv('ENV', self.PROD)

        self.username = os.getenv('USER_NAME')
        self.password = os.getenv('PASSWORD')

        if not self.username or not self.password:
            raise ValueError("Environment variables USERNAME and PASSWORD are not set!")

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable: {self.env}")

    def get_credentials(self):
        return self.username, self.password


host = Environment()
