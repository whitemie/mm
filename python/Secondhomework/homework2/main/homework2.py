import sys

from XuZhu.XuZhu import XuZhu

sys.path.append('..')

from Tonglao.TongLao import TongLao


if __name__ == '__main__':
    tonglao = TongLao(500, 20)
    xz = XuZhu(1000, 300)
    tonglao.fight_zms(300,10)
    tonglao.see_people("")
    xz.read()
    xz.fight()
