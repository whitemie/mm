from time import sleep

from appium import webdriver


class Testbrowser:
    def setup(self):
        caps = {
            'platformName': 'android',
            'platformVerion': '6.0.1',
            'browserName': 'Browser',
            'deviceName': '127.0.0.1:7555',
            'noReset': True,
            'chromedriverExecuteable': 'D:\\software\\软件安装包\\81chromedriver_win32\\chromedriver.exe'
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://www.baidu.com")
        sleep(5)
