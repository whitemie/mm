import shelve
from time import sleep

from selenium import webdriver

from test_selenium.Homework2.page.BasePage import BasePage
from test_selenium.Homework2.page.Login import login


class Test_case:
    def setup(self):
        self.login = login()

    def teardown(self):
        BasePage().base_quit()

    def test_(self):
        self.login.goto_main()