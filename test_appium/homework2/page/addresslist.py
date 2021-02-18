"""
通讯录界面：展示通讯录成员，添加成员功能
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.homework2.page.basepage import BasePage
from test_appium.homework2.page.memberinvitemenu import MemberInviteMenuPage
from test_appium.homework2.page.search_page import Search_Page


class AddressListPage(BasePage):
    """
    添加成员
    """
    # def __init__(self,driver):
    #     self.driver = driver
    add_member_element = "添加成员"
    search_element = (By.XPATH, '//*[@resource-id="com.tencent.wework:id/igk"]')

    def add_member(self):
        """跳到添加成员的界面"""
        # 用scrollable(true)找到对象，.instance(0) 再获取子元素
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
        #                                                        '.scrollable(true).instance(0))'
        #                                                        '.scrollIntoView('
        #                                                        'new UiSelector().text("添加成员").instance(0));').click()
        self.find_by_scroll_and_click(self.add_member_element)
        return MemberInviteMenuPage(self.driver)

    # """ 搜索界面 """

    def goto_search(self):
        # self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/ie_"]').click()
        self.find_and_click(self.search_element)
        return Search_Page(self.driver)
