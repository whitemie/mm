"""
通讯录界面：展示通讯录成员，添加成员功能
"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium.homework2.page.memberinvitemenu import MemberInviteMenuPage


class AddressListPage:
    """
    添加成员
    """

    def add_member(self):
        """跳到添加成员的界面"""
        # 用scrollable(true)找到对象，.instance(0) 再获取子元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollableIntoView('
                                                               'new UiSelector().text("添加成员").instance(0));').click()
        return MemberInviteMenuPage()
