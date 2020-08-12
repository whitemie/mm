class Bicycle:
    def run(self,km):
        print(f"一共用脚骑了{km}公里")

class EBicycle(Bicycle):
    #构造函数.类实例化的时候就会调用init函数
    def __init__(self,valume):
        self.valume = valume

    def fill_charge(self,vol):
        self.valume = self.valume+vol
        print(f"充了{vol}度电，现在的电量为{self.valume}")

    def run(self,km):
        # 目前电量所能骑行的最大里程数
        power_km = self.valume*10
        # 最大里程数>骑行里程数
        if power_km>=km:
            print(f"我使用电瓶电量骑了{km}km")
        else:
            print(f"我使用电瓶骑行了{power_km}km")
            # bike = Bicycle()
            # bike.run(km - power_km)
            super().run(km - power_km)

bike = Bicycle()
bike.run(10)
ebike = EBicycle(1)
ebike.fill_charge(3)
ebike.run(100)
