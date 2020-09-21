import time
import pytest
from test_selenium import webdriver
from test_selenium.webdriver import ActionChains, TouchActions
from test_selenium.webdriver.common.by import By
from test_selenium.webdriver.common.keys import Keys
from test_selenium.webdriver.support import expected_conditions
from test_selenium.webdriver.support.wait import WebDriverWait


class TestHogwards:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        # self.driver.get("http://www.testerhome.com")

        # 隐式等待
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
        # pass

    @pytest.mark.skip
    def test_hogwards(self):
        # self.driver.find_element(By.XPATH,'//*[@title="httprunner 的 java 实现，有没有感兴趣的朋友，一起维护一下"]').click()
        # # time.sleep(3)
        # self.driver.find_element(By.LINK_TEXT,"https://github.com/liuguanglei123/httprunnerforjava_public").click()
        # self.driver.find_element(By.LINK_TEXT,'/topics').click()
        # time.sleep(3)
        # def wait(a):
        #     return len(self.driver.find_element(By.LINK_TEXT,'/topics/last_reply'))>1
        # WebDriverWait(self.driver,10).until(wait,message="没有找到元素")
        # el = self.driver.find_element(By.LINK_TEXT,'/topics/last_reply')
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(el))
        # self.driver.find_element_by_id("kw").send_keys("杨洋")
        # e_click = self.driver.find_element_by_xpath('//input[@type="submit"]')
        # e_right_click = self.driver.find_element_by_xpath('//*[@id="result_logo"]//img[1]')
        self.driver.get("https://www.baidu.com/")
        e_right_click = self.driver.find_element_by_id('kw')
        action = ActionChains(self.driver)
        # action.click(e_click)
        action.context_click(e_right_click)
        action.perform()
        time.sleep(5)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        action = ActionChains(self.driver)
        e2 = self.driver.find_element_by_name('tj_briicon')
        action.move_to_element(e2)
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_dragfrop(self):
        self.driver.get("https://www.baidu.com/")
        drag_ele = self.driver.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]//a[1]')
        drop_ele = self.driver.find_element_by_id('kw')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_ele,drop_ele).perform()
        # action.click_and_hold(drag_ele).release(drop_ele).perform()
        action.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()
        action.double_click(drag_ele).move_to_element(drop_ele).release().perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_key(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_id('kw')
        action = ActionChains(self.driver)
        action.send_keys("杨洋").pause(3)
        action.send_keys(Keys.SPACE).pause(3)
        action.send_keys("图片啊").pause(3)
        action.send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)

    def test_touch_actions(self):
        self.driver.get("http://www.baidu.com")
        e1 = self.driver.find_element_by_id('kw')
        el_search = self.driver.find_element_by_id('su')

        e1.send_keys("杨洋")
        action = TouchActions(self.driver)
        action.tap(el_search).perform()

        action.scroll_from_element(e1, 0, 10000).perform()
        time.sleep(3)
