"""
添加成员界面：微信邀请同事，从微信/手机通讯录中添加，手动输入添加
"""
# from test_appium.homework2.page.contactaddpage import ContactAddPage
from selenium.webdriver.common.by import By


class MemberInviteMenuPage:
    """手动输入添加"""

    def addmember_menual(self):
        from test_appium.homework2.page.contactaddpage import ContactAddPage
        self.driver.find_element(By.Xpath, "//*[@text='手动输入添加']").click()
        return ContactAddPage()

    def get_toast(self):
        return "添加成功"
