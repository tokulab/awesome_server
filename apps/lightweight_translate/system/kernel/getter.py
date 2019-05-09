import sys
from selenium import webdriver

from ..handler import error_handler as e_handler

class Crawler:

    def __init__(self):
        import chromedriver_binary
        try:
            self.driver = webdriver.Chrome('asdf')
        except Exception as e:
            message = e_handler.ERROR_OCCURRED_TEMPLATE.format(err=str(e).rstrip('\n'))
            print(message)
            e_handler.force_abort()


    def get_text(self):
        pass