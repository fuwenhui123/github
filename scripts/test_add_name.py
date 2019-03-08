from base.base_driver import init_driver

from page.page import Page


class TestAddName:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.page.seting.click_search()
        self.page.seting. ya_search()
        self.page.search.input_keyword("zhangsan")
        self.page.search.input_phone("13588888888")
