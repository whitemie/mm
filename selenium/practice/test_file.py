import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


class Test_File:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_uploadpicture(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id('stfile').send_keys('D:\\咩咩图片\\6c351711gy1g2gburr83uj22c02c07wj.jpg')
        time.sleep(13)

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        time.sleep(3)

        self.driver.switch_to.alert.accept()

        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        time.sleep(3)
