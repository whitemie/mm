import shelve
from time import sleep

from test_selenium.Homework2.page.BasePage import BasePage
from test_selenium.Homework2.page.Main_page import main_page
from test_selenium.Homework2.page.Reister import register


class login(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu"

    def goto_register(self):

        return register(self.driver)

    def goto_main(self):
        cookies = self.getcookie(r"../page/mydb/logincookie", "cookie")
        if cookies is None:
            self.setcookie(r"../page/mydb/logincookie", "cookie")
            cookies = self.getcookie(r"../page/mydb/logincookie", "cookie")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get(self._url)
        return main_page(self.driver)
