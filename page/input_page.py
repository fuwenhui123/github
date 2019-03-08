from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class InputPage(BaseAction):


    input_button = By.ID,"android.widget.EditText"

    def input_keyword(self,text):

        self.input(self.input_keyword,text)

    def input_phone(self, text):

        self.input(self.input_phone, text)