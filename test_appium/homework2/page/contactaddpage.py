"""
手动添加页面
"""
# from test_appium.homework2.page.memberinvitemenu import MemberInviteMenuPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.homework2.page.basepage import BasePage


class ContactAddPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    name_element = (By.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText')
    male_element = (By.XPATH, '//*[contains(@text,"男")]')
    phonenum_element = (By.XPATH, '//*[contains(@text,"手机号")]')
    save_element = "保存"

    def edit_name(self, name):
        # self.driver.find_element(By.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(name)
        self.find_and_sendkeys(self.name_element, name)
        return self

    def edit_sex(self, sex):
        # self.driver.find_element(By.XPATH, '//*[contains(@text,"男")]').click()
        self.find_and_click(self.male_element)
        self.driver.find_element(By.XPATH, f'//*[contains(@text,"{sex}")]').click()
        return self

    def edit_phonenum(self, phonenum):
        # self.driver.find_element(By.XPATH, '//*[contains(@text,"手机号")]').send_keys(phonenum)
        self.find_and_sendkeys(self.phonenum_element, phonenum)
        return self

    def clich_save(self):
        from test_appium.homework2.page.memberinvitemenu import MemberInviteMenuPage
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
        #                                                        '.scrollable(true).instance(0))'
        #                                                        '.scrollIntoView('
        #                                                        'new UiSelector().text("保存").instance(0));').click()
        self.find_by_scroll_and_click(self.save_element)
        return MemberInviteMenuPage(self.driver)
