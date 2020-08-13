# !/usr/bin/env python
# -*- coding: utf-8 -*-
import decimal


class Calculator:
    def add(self, a, b):
        if type(a) == float or type(b) == float:
            a = decimal.Decimal(str(a))
            b = decimal.Decimal(str(b))
            return float(a + b)
        return a + b

    def sub(self, a, b):
        if type(a) == float or type(b) == float:
            a = decimal.Decimal(str(a))
            b = decimal.Decimal(str(b))
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


cal = Calculator()
print(cal.add(1.3, 20.4))
