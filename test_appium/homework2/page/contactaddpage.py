"""
手动添加页面
"""
# from test_appium.homework2.page.memberinvitemenu import MemberInviteMenuPage
from selenium.webdriver.common.by import By


class ContactAddPage:
    def edit_name(self, name):
        self.driver.find_element(By.Xpath, '//*[contains(@text, "姓名")]/../android.widget.EditText').senfkeys(name)
        return self

    def edit_sex(self, sex):
        self.driver.find_element(By.XPATH, '//*[contains(@text,"男")]').click()
        self.driver.find_element(By.XPATH, f'//*[contains(@text,"{sex}")]').click()
        return self

    def edit_phonenum(self, phonenum):
        self.driver.find_element(By.XPATH, '//*[contains(@text,"手机号")]').send_keys("13756882378")
        return self

    def clich_save(self):
        from test_appium.homework2.page.memberinvitemenu import MemberInviteMenuPage
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView('
                                                               'new UiSelector().text("保存").instance(0));').click()
        return MemberInviteMenuPage()
