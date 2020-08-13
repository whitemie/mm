# from Tonglao import TongLao

'''
XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。
所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
'''
from Tonglao.TongLao import TongLao


class XuZhu(TongLao):
    def __init__(self,hp,power):
        super().__init__(hp,power)

    def read(self):
        print("罪过罪过")

    def fight(self):
        print("出家人慈悲为怀，不宜动武~")