from Tonglao import TongLao
from XuZhu import XuZhu


if __name__ == '__main__':
    tonglao = TongLao.TongLao(500,20)
    xz=XuZhu.XuZhu(1000,300)
    tonglao.fight_zms(300,10)
    tonglao.see_people("")
    xz.read()
    xz.fight()
