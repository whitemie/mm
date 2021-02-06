"""
首页：有消息页面，通讯录页面，工作台，我的界面
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.homework2.page.addresslist import AddressListPage


class MainPage:
    """
        通信录界面
        """

    def goto_addresslist(self):
        tx_locator = (By.XPATH, '//*[@text="通讯录"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(tx_locator))
        self.driver.find_element(By.XPATH, '//*[@text="通讯录"]').click()
        return AddressListPage()
