import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    _url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver
        if self._url != "":
            self.driver.get(self._url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)

    def getcookie(self, file_path, key_name):
        db = shelve.open(file_path)
        if key_name not in db.keys():
            cookies = None
        else:
            cookies = db["cookie"]
        db.close()
        return cookies

    def setcookie(self, file_path, key_name):
        db = shelve.open(file_path)
        sleep(15)
        db[key_name] = self.driver.get_cookies()
        db.close()

    def base_quit(self):
        self.driver.quit()
