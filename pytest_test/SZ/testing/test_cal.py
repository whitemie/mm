# -*-coding:utf-8 -*-

"""
文件名：以test_开头
类名：以Test开头
方法名：以test_开头
"""
# from pytest_test.SZ.pythoncode.calculator import Calculator
import pytest
import yaml

from pytest_test.SZ.pythoncode.calculator import Calculator


def get_datas():
    with open('./data/calc.yaml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas, myids]


print(get_datas())


class TestCalc:

    def setup_class(self):
        print("----开始计算------")
        self.calc = Calculator()

    def teardown(self):
        print("结束计算")

    @pytest.mark.add
    # @pytest.mark.parametrize("a,b,expect",[
    #     (1,1,2),
    #     (0.3,0.4,0.7),
    #     (100,10.5,111.5),
    #     (-1,-2,-3)
    # ],ids=["int","小数","混合","负数"])
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert expect == result

    @pytest.mark.sub
    def tes_sub(self):
        result = self.calc.sub(100, 1)
        assert 99 == result

    @pytest.mark.mul
    def test_mul(self):
        result = self.calc.mul(2, 3)
        assert 6 == result

    @pytest.mark.div
    def test_div(self):
        result = self.calc.div(6, 2)
        assert 3 == result
