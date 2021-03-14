from selenium.webdriver.common.by import By

from test_appium.homework2.page.basepage import BasePage
from test_appium.homework2.page.editmember_page import Editmember_Page


class Detailinfo_Page(BasePage):
    editbtn_element = (By.XPATH, '//*[@text="编辑成员"]')

    def edit_member(self):
        # self.driver.find_element_by_xpath('//*[@text="编辑成员"]').click()
        self.find_and_click(self.editbtn_element)
        return Editmember_Page(self.driver)
