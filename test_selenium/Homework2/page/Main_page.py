from selenium.webdriver.common.by import By

from test_selenium.Homework2.page.Add_number import add_number
from test_selenium.Homework2.page.BasePage import BasePage
from test_selenium.Homework2.page.Input_phones import input_phones
from test_selenium.Homework2.page.PhoneList import phonelist


class main_page(BasePage):
    def goto_phonelist(self):
        self.find(By.ID, "menu_contacts").click()
        print(self._url)
        return phonelist(self.driver)

    def goto_addnumber(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        return add_number(self.driver)

    def goto_inputphones(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        return input_phones(self.driver)
