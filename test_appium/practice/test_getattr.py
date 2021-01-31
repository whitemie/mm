import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
from selenium.webdriver.support.wait import WebDriverWait


class Testcase1:
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
        self.driver.quit()

    @pytest.mark.skip
    def test_attribute(self):
        test_a = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(test_a.get_attribute("clickable"))
        print(test_a.get_attribute("content-desc"))
        print(test_a.get_attribute("resource-id"))
        print(test_a.get_attribute("enabled"))

    def test_hamcrest(self):
        # self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        # # self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys(
        #     "阿里巴巴")
        locator = (MobileBy.XPATH, '//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        current_price = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator)).text

        print(current_price)
        # assert_that(current_price,equal_to(200),"这是一个提示")
        assert_that("contains string some", contains_string("string"))
        # assert_that(290,close_to(300,10))
        assert_that(current_price, close_to(300, 300 * 0.1))
