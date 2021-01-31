from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["ensureWebviewsHavePages"] = True
        # caps["noReset"] = "true"
        # caps["dontStopAppOnReset"] = "true"
        # caps["skipDeviceInitialization"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    # 解锁
    def test_touchaction_unlock(self):
        print("解锁屏幕")
        # self.driver.find_element_by_xpath(
        #     "//android.widget.LinearLayout[@content-desc=\"文件夹：系统应用\"]/android.widget.ImageView").click()
        # self.driver.find_element_by_xpath('//*[@text="设置"]').click()
        action = TouchAction(self.driver)
        # windows_rec = self.driver.get_window_rect()
        # print(windows_rec)
        # width = windows_rec['width']
        #         # height = windows_rec['height']
        #         # x1 =int(width /2)
        #         # y_start = int(height * 4/5)
        #         # y_end = int(height *3/5)
        # action.press(x=x1, y=y_start).wait(100).move_to(x=x1, y=y_end).release().perform()
        self.driver.find_element_by_xpath('//*[@text="安全"]').click()
        self.driver.find_element_by_xpath('//*[@text="屏幕锁定方式"]').click()
        action.press(x=233, y=544).wait(2).move_to(x=403, y=544).wait(2).move_to(x=577, y=544).move_to(x=403, y=718). \
            move_to(x=233, y=895).move_to(x=403, y=895).move_to(x=577, y=895).release().perform()
