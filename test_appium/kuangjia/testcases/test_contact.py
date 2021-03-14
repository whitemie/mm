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


def get_deletecontact():
    with open("../datas/delete_contact.yml", encoding='utf-8') as f:
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
        add_page = self.main.goto_addresslist().add_member().addmember_menual()
        my_page = add_page.edit_name(name).edit_sex(sex).edit_phonenum(phonenum).clich_save()
        toast_text = my_page.get_toast()

        assert toast_text == "添加成功"

    @pytest.mark.parametrize("name", get_deletecontact())
    def test_deletecontact(self, name):
        search_page = self.main.goto_addresslist().goto_search()
        edit_page = search_page.searchwords(name)
        beforenum = edit_page[1]
        afternum = edit_page[0].detail_info().edit_member().delete_member().after_delete(name)
        print(afternum)
        print("be:", beforenum)
        assert afternum == beforenum - 1
