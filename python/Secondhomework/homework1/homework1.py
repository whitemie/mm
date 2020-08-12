class Energyforest:
    def __init__(self,name):
        self.name=name

    def introduce(self):
        print("元气森林，元气满满")

class SparklingWater(Energyforest):
    def __init__(self,name,price):
        super().__init__(name)
        self.price=price

    def introduce(self):
        print(self.name+"是一款苏打气泡水，价格为每瓶"+self.price+"元")

    def zl(self):
        print("元气森林气泡水有五种口味：橘味、白桃味、青瓜味、桃香乌龙茶、醇香乌龙茶")

class RC(Energyforest):
    def __init__(self,name):
        super().__init__(name)

    def introduce(self):
        print("元气森林乳茶口感醇厚 口味高度还原奶茶!")


ef = Energyforest("元气森林")
ef.introduce()
sw = SparklingWater("元气森林气泡水","6.5")
sw.introduce()
sw.zl()
rc = RC("元气森林")
rc.introduce()