import pytest
import sys
import os

sys.path.append("..")
from pytest_test.Homework.Cal.Calculator import Calculator
from pytest_test.Homework.testdata.test_data import get_data

print(os.getcwd())
fnpath = r'..\testdata\data.yaml'


class TestCase:
    def setup_class(self):
        self.calc = Calculator()
        # self.mydatas = get_data()[0]
        # self.myids = get_data()[1]

    def setup(self):
        print("**********开始计算**********")

    def teardown(self):
        print("**********计算结束**********")

    @pytest.mark.parametrize("a,b,expect", get_data(fnpath)[0], ids=get_data(fnpath)[1])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b", get_data(fnpath)[2])
    def test_addexcept(self, a, b):
        try:
            result = self.calc.add(a, b)
        except Exception as e:
            print(e.args)
            assert e.args

    @pytest.mark.parametrize("a,b,expect", get_data(fnpath)[3])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b", get_data(fnpath)[4])
    def test_divexcept(self, a, b):
        try:
            result = self.calc.div(a, b)
        except Exception as e:
            print(e.args)
            assert e.args
