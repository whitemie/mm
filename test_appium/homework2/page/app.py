"""
App类：APP常用的方法，例如启动应用，关闭应用，重启应用，进入首页等
"""
from appium.webdriver import webdriver

from test_appium.homework2.page.mainpage import MainPage


class App:

    def start(self):
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
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    # 进入到首页
    def goto_main(self) -> MainPage:
        return MainPage()
