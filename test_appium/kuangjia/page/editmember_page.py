from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium.homework2.page.basepage import BasePage


class Editmember_Page(BasePage):
    delete_text = "删除成员"
    btn_element = (MobileBy.XPATH, '//*[@text="确定"]')

    def delete_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
        #                                                        '.scrollable(true).instance(0))'
        #                                                        '.scrollIntoView('
        #                                                        'new UiSelector()'
        #                                                         f'.text("删除成员").instance(0));')
        self.find_by_scroll_and_click(self.delete_text)
        # self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        self.find_and_click(self.btn_element)
        sleep(5)
        from test_appium.homework2.page.search_page import Search_Page
        return Search_Page(self.driver)
