import os
import time

import pytest
from test_selenium import webdriver


class Test_window:
    def setup(self):
        browser = os.getenv("browser")
        print(browser)
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "edg":
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_switchwindow(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print("当前窗口为：", self.driver.current_window_handle)
        print("所有窗口为：", self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print("当前窗口为：", self.driver.current_window_handle)
        print("所有窗口为：", self.driver.window_handles)
        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        time.sleep(3)

    def test_switch_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        self.driver.find_element_by_id("draggable")
        print(self.driver.find_element_by_id("draggable").text)
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN")
        print(self.driver.find_element_by_id("submitBTN").text)
