# !/usr/bin/env python
# -*- coding: utf-8 -*-
import decimal
import os


class Calculator:
    def test_decimal(self, a):
        a = decimal.Decimal(str(a))
        return a

    def add(self, a, b):
        if type(a) == float or type(b) == float:
            return float(self.test_decimal(a) + self.test_decimal(b))
        return a + b

    def sub(self, a, b):
        if type(a) == float or type(b) == float:
            return self.test_decimal(a) - self.test_decimal(b)
        return a - b

    def mul(self, a, b):
        if type(a) == float or type(b) == float:
            return self.test_decimal(a) * self.test_decimal(b)
        return a * b

    def div(self, a, b):
        if b == 0:
            return "除数不能为0"
        return a / b

# cal = Calculator()
# print(cal.add(1.3, 20.70))
