import shelve

from test_selenium import webdriver
from time import sleep


class Test_weixin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        # sleep(60)
        # cookie = self.driver.get_cookies()
        # db = shelve.open(r"mydb/mycookies")
        # db["cookies"] = cookie
        # db.close()

    def teardown(self):
        # self.driver.quit()
        pass

    def test_weixin(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        # # sleep(60)
        # # print(self.driver.get_cookies())
        # cookie = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853093850380'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'A3SshQ9DxzNcebFKsnF0X5wCCTLdeUts6JoDe7ZW98tujAD7C_SC3M5ikyIbGKcqT1lSR1GgC1zEbZFSxd87o7ZTaYQRPnnnB4cbD3R26_zm80xbAYHSW-yRH-GxofYqYbz50OBoCQJOrpABu3uxr-fMnbsY20yx9SxRgZpkl4e5YBzECSfJEFxDqfkBv7Nh6qBpSzKVKzjyteHvOp6HBufyH_kL-N5HXo0i-OAnvjgkvd2sPhgl093EdNZe7k2OqWriirFAXPD_Ab7cwWQ-Sw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853093850380'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324984155036'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5021265'}, {'domain': 'work.weixin.qq.com', 'expiry': 1600379754, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5kjggvr'}, {'domain': '.qq.com', 'expiry': 1600434643, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.659042946.1600348223'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '061812'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'UsE_vax6k-6XYbNpUuZSxhldEqm92GAJlC_Elx2KsLGe51A140_9p3QsEgYv64Pn'}, {'domain': '.qq.com', 'expiry': 1663420243, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.856380257.1600348223'}, {'domain': '.work.weixin.qq.com', 'expiry': 1631884218, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1602940246, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
        db = shelve.open("mydb/mycookies")
        # db["cookies"] = cookie
        cookies = db["cookies"]
        db.close()
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        print(self.driver.current_window_handle)
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//div[@class="ww_btnWithMenu ww_btnWithMenu_Open_Up js_btnWithMenu js_import_other_wrap"]/a').click()
        self.driver.find_element_by_xpath(
            '//div[@class="ww_btnWithMenu ww_btnWithMenu_Open_Up js_btnWithMenu js_import_other_wrap ww_btnWithMenu_Open"]/div//li[1]').click()
        input_a = self.driver.find_element_by_xpath(
            '//a[@class="qui_btn ww_btn ww_fileImporter_fileContainer_upload"]/input')
        input_a.send_keys(r"D:\实习\银联\13计科1-2015-2016.xls")
        assert "13计科1-2015-2016.xls" == self.driver.find_element_by_xpath(
            '//div[@class="ww_fileImporter_fileContainer_fileNames"]').text

        # self.driver.find_element_by_xpath('//div[@class="qui_dropdownMenu ww_dropdownMenu"][3]//li').click()
