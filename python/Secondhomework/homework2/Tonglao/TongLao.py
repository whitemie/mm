class TongLao:
    '''属性有血量，武力值（通过传入的参数得到'''
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power

    '''see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，
    打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”'''
    def see_people(self,name):
        if name=="WYZ":
            print("师弟！！！！")
        elif name=="李秋水":
            print("呸，贱人")
        elif name =="丁春秋":
            print("叛徒！我杀了你")
        else:
            print("无名之辈，恐污我耳！")

    '''调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，
    进行一回合制对打，打完之后，比较双方血量。血多的一方获胜'''
    def fight_zms(self,enemy_hp,enemy_power):
        my_hp=self.hp/3
        my_power=self.power*10
        enemy_hp=enemy_hp-my_power
        my_hp = enemy_hp-my_power
        if my_hp <enemy_hp:
            print("哈哈哈，小子，想赢我回去再修炼几百年吧！")
        elif my_hp >enemy_hp:
            print("承让承让~~")
        else:
            print("阿弥陀佛，")

