from time import sleep

import pytest
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_dw:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
        caps["noReset"] = "true"
        caps["dontStopAppOnReset"] = "true"
        caps["skipDeviceInitialization"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_dw(self):
        """
            # 打开雪球APP，
            # 点击搜索框
            # 向搜索框输入阿里巴巴
            # 在搜索结果里面选择“阿里巴巴” 然后进行点击
            # 获取这只上香港 阿里巴巴的股价，并判断 这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        # 获取当前屏幕的尺寸
        window_rec = self.driver.get_window_rect()
        width = window_rec['width']
        height = window_rec['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        # self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys(
            "阿里巴巴")

        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.xueqiu.android:id/listview"]/*[1]//*[@resource-id="com.xueqiu.android:id/name"]').click()
        # current_price = self.driver.find_element_by_xpath('//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        locator = (MobileBy.XPATH, '//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        current_price = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator)).text

        print(current_price)
        assert current_price > "200"


if __name__ == "__main__":
    pytest.main()
