from selenium.webdriver.common.by import By

from test_selenium.Homework2.page.Add_department import add_department
from test_selenium.Homework2.page.Add_number import add_number
from test_selenium.Homework2.page.BasePage import BasePage
from test_selenium.Homework2.page.Input_phones import input_phones


class phonelist(BasePage):
    def goto_addnumber(self):
        return add_number(self.driver)

    def goto_adddepartment(self):
        # 点击加号按钮
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        # 点击添加部门
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return add_department(self.driver)

    def goto_inputphones(self):
        return input_phones(self.driver)
