from appium.webdriver.common.mobileby import MobileBy

from test_appium.homework2.page.basepage import BasePage
from test_appium.homework2.page.detailinfo_page import Detailinfo_Page


class Personinfo_Page(BasePage):
    detailbtn_element = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/iga"]')

    def detail_info(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/ie0"]').click()
        self.find_and_click(self.detailbtn_element)
        return Detailinfo_Page(self.driver)
