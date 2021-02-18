"""
添加成员界面：微信邀请同事，从微信/手机通讯录中添加，手动输入添加
"""
# from test_appium.homework2.page.contactaddpage import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.homework2.page.basepage import BasePage


class MemberInviteMenuPage(BasePage):
    """手动输入添加"""
    # def __init__(self,driver):
    #     self.driver = driver
    addmember_menual_element = (By.XPATH, "//*[@text='手动输入添加']")

    def addmember_menual(self):
        from test_appium.homework2.page.contactaddpage import ContactAddPage
        # self.driver.find_element(By.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(self.addmember_menual_element)
        return ContactAddPage(self.driver)

    def get_toast(self):
        # toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        toasttext = self.get_toast_text()
        return toasttext
