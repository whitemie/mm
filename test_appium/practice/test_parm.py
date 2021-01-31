import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestParam:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
        caps["noReset"] = True
        caps["skipDeviceInitialization"] = True
        caps["unicodeKeyBoard"] = "true"
        caps["resetBoard"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
        # self.driver.quit()

    @pytest.mark.parametrize('searchkey,type,expect_price', [('阿里巴巴', 'BABA', 260), ('小米', '01810', 21)])
    def test_param(self, searchkey, type, expect_price):
        """
        # 选择搜索框，点击
        # 在搜索框中输入搜索内容
        # 读取第一个搜索结果并判断

        """
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        current_ele = self.driver.find_element(MobileBy.XPATH,
                                               f'//*[@text="{type}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        current_price = float(current_ele.text)
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))
