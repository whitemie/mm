from time import sleep
from selenium.webdriver.common.by import By

from test_appium.homework2.page.basepage import BasePage
from test_appium.homework2.page.personinfo_page import Personinfo_Page


class Search_Page(BasePage):
    searchbutton_element = (By.XPATH, '//*[@text="搜索"]')

    def searchwords(self, name):
        # self.driver.find_element_by_xpath('//*[@text="搜索"]').send_keys(name)
        self.find_and_sendkeys(self.searchbutton_element, name)
        sleep(2)
        # eles = self.driver.find_elements_by_xpath(f"//*[@text='{name}']")
        search_elements = (By.XPATH, f"//*[@text='{name}']")
        eles = self.find_elements(search_elements)
        beforenum = len(eles)
        if beforenum < 2:
            assert "没有可删除的结果"
            return
        eles[1].click()
        return Personinfo_Page(self.driver), beforenum

    def after_delete(self, name):
        search_elements = (By.XPATH, f"//*[@text='{name}']")
        eles1 = self.find_elements(search_elements)
        afternum = len(eles1)

        return afternum
