from page.input_page import InputPage
from page.seting_page import SetingPage


class Page:

    def __init__(self,driver):
        self.driver = driver

    @property
    def seting(slef):
        return SetingPage(slef.driver)

    @property
    def search(self):
        return InputPage(self.driver)


