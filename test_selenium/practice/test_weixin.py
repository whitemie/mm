import shelve
import time

import pytest
from test_selenium import webdriver


class Test_weixin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_session(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        # 获取cookies可以先等待几秒扫完登陆之后获取
        # time.sleep(10)
        # print(self.driver.get_cookies())
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853093850380'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'vi9pOAmmyK_zH2shEZgckdaJr4JFONXSJZou1tA4g1mvrt3GBsZPMO03NiN-vBjRoXhqyRzefaq6wSab2nvq_CSOk9dLU5f2VfvhSycfjPmDDeTmfsgxA8tI1OIGKbo2JJhQ8ZlKJEv97LxvM5vzIKYAOVoCXfztIJqcePrVQo1A1r9GKRSFsqx62z8RrRgxmNz_qZGL9_DvCgQTZDTicVvRquX5bFvGZ9lWq9MB6auxy6SIRpXW_seAqqPhz_1dH_siYqGutUx6Rlwr4Gkrlw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853093850380'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324984155036'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a1572113'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1600297857, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '3fv3nd1'},
            {'domain': '.qq.com', 'expiry': 1600352729, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1871975881.1600266323'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '01523977'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'UsE_vax6k-6XYbNpUuZSxqYXaf1T9LKT9KMic_B1VUCaoSw9Q9cNMk2hiAjOsQAg'},
            {'domain': '.qq.com', 'expiry': 1600266382, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1663338329, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1391205836.1600266323'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1631802321, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1602858332, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'}]
        for cookie in cookies:
            # expiry这个参数有没有都可以成功，但是为小数的时候就会报错
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        time.sleep(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_contacts").click()
        time.sleep(3)

    def test_cookie1(self):
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853093850380'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'vi9pOAmmyK_zH2shEZgckdaJr4JFONXSJZou1tA4g1mvrt3GBsZPMO03NiN-vBjRoXhqyRzefaq6wSab2nvq_CSOk9dLU5f2VfvhSycfjPmDDeTmfsgxA8tI1OIGKbo2JJhQ8ZlKJEv97LxvM5vzIKYAOVoCXfztIJqcePrVQo1A1r9GKRSFsqx62z8RrRgxmNz_qZGL9_DvCgQTZDTicVvRquX5bFvGZ9lWq9MB6auxy6SIRpXW_seAqqPhz_1dH_siYqGutUx6Rlwr4Gkrlw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853093850380'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324984155036'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1572113'}, {'domain': 'work.weixin.qq.com', 'expiry': 1600297857, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '3fv3nd1'}, {'domain': '.qq.com', 'expiry': 1600352729, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1871975881.1600266323'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '01523977'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'UsE_vax6k-6XYbNpUuZSxqYXaf1T9LKT9KMic_B1VUCaoSw9Q9cNMk2hiAjOsQAg'}, {'domain': '.qq.com', 'expiry': 1600266382, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1663338329, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1391205836.1600266323'}, {'domain': '.work.weixin.qq.com', 'expiry': 1631802321, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1602858332, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
        #
        # db = shelve.open("mydb/logincookie")
        # db["cookie"]=cookies
        # db.close()
        db = shelve.open("mydb/logincookie")
        cookies = db["cookie"]
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            # expiry这个参数有没有都可以成功，但是为小数的时候就会报错
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        time.sleep(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_contacts").click()
        time.sleep(3)
