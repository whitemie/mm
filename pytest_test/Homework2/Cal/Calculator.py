# !/usr/bin/env python
# -*- coding: utf-8 -*-
import decimal


def dedata(a):
    a = decimal.Decimal(str(a))
    return a


class Calculator:
    def add(self, a, b):
        if type(a) == float or type(b) == float:
            return float(dedata(a) + dedata(b))
        return a + b

    def sub(self, a, b):
        if type(a) == float or type(b) == float:
            return float(dedata(a) - dedata(b))
        return a - b

    def mul(self, a, b):
        if type(a) == float or type(b) == float:
            return float(dedata(a) * dedata(b))
        return a * b

    def div(self, a, b):
        if b == 0:
            return "除数不能为0"
        return a / b
