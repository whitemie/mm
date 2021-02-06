import pytest
import yaml

from test_appium.homework2.page.app import App

"""
读取数据
"""


def get_contact():
    with open("../datas/contacts.yml", encoding='utf-8')  as f:
        datas = yaml.safe_load(f)
    return datas


class TestWexin:
    def setup(self):
        """
        启动APP
        :return:
        """
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,sex,phonenum", get_contact())
    def test_addcontact(self, name, sex, phonenum):
        addpage = self.main.goto_addresslist().add_member().addmember_menual()
        toast_text = addpage.edit_name(name).edit_sex(sex).edit_phonenum(phonenum).clich_save().get_toast()
        assert toast_text == "添加成功"
