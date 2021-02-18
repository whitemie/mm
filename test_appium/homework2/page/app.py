"""
App类：APP常用的方法，例如启动应用，关闭应用，重启应用，进入首页等
"""
from appium import webdriver

from test_appium.homework2.page.basepage import BasePage
from test_appium.homework2.page.mainpage import MainPage

import sys

sys.setrecursionlimit(100000)


class App(BasePage):


    def start(self):
        """
        如果driver为None，则重新赋值
        如果不为None，则直接打开APP
        :return:
        """
        if self.driver == None:
            caps = {
                "platformName": "android",
                "deviceName": "AUNZINUOMZYLIFEI",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": True
            }

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            # 启动 caps 里面设置的appPackage appActivity
            self.driver.launch_app()
            # 启动 任何一个包和activity
            # self.driver.start_activity()  这个启动需要传入包名和activity名  对跨应用启动的
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    # 进入到首页
    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
