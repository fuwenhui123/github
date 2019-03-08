from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SetingPage(BaseAction):

    search_button = By.ID, "com.android.contacts:id/floating_action_button"
    click_button = By.ID,"//*[@text='本地保存']"

    def click_search(self):
        self.click(self.search_button)

    def ya_search(self):
        self.click(self.click_button)
