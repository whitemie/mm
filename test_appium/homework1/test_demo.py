from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testdemo:
    def setup(self):
        caps = {
            "platformName": "android",
            # "platformVersion": "6.0.1",
            "deviceName": "AUNZINUOMZYLIFEI",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True,
            "dontStopAppOnReset": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_addmember(self):
        sex = "女"
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView('
                                                               'new UiSelector().text("添加成员").instance(0));').click()
        self.driver.find_element(By.XPATH, "//*[@text='手动输入添加']").click()
        input_path = self.driver.find_element(By.XPATH,
                                              "//*[@resource-id='com.tencent.wework:id/igz']/android.widget.LinearLayout[2]"
                                              "//android.widget.TextView")
        path_text = input_path.text
        if path_text == "完整输入":
            input_path.click()

        self.driver.find_element(By.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys("测试测试")
        self.driver.find_element(By.XPATH, '//*[contains(@text,"男")]').click()
        self.driver.find_element(By.XPATH, f'//*[contains(@text,"{sex}")]').click()
        self.driver.find_element(By.XPATH, '//*[contains(@text,"手机号")]').send_keys("13756882378")
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView('
                                                               'new UiSelector().text("保存").instance(0));').click()




    def teardown(self):
        pass
        # self.driver.quit()

    def test_delete(self):
        # 切换到通讯录tab
        name = "测试"
        tx_locator = (By.XPATH, '//*[@text="通讯录"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(tx_locator))
        self.driver.find_element(By.XPATH, '//*[@text="通讯录"]').click()
        # 搜索账号
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/ie_"]').click()
        # 输入要删除的账号
        self.driver.find_element_by_xpath('//*[@text="搜索"]').send_keys(name)
        sleep(2)
        # 找出搜索结果和搜索名相同的结果的长度
        eles = self.driver.find_elements_by_xpath(f"//*[@text='{name}']")
        num = len(eles)
        if num < 2:
            assert "没有可删除的结果"
            return
        eles[1].click()
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.tencent.wework:id/ie0"]').click()
        self.driver.find_element_by_xpath('//*[@text="编辑成员"]').click()
        action = TouchAction(self.driver)
        windows_rec = self.driver.get_window_rect()
        width = windows_rec['width']
        height = windows_rec['height']
        x1 = int(width / 2)
        y_start = int(height * 3 / 4)
        y_end = int(height * 1 / 2)
        action.press(x=x1, y=y_start).wait(5).move_to(x=x1, y=y_end).release().perform()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@text="删除成员"]').click()
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        assert "删除成功"

