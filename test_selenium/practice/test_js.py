import time
import pytest

from selenium import webdriver


class TestJS:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        # for code in [
        #     'return document.title',
        #     'return JSON.stringify(performence.timing)'
        # ]:
        #     print(self.driver.execute_script(code))

    def test_datettime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script(
            "a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
