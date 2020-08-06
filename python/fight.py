def fight():
    my_power = 200
    enemy_power = 200
    my_hp = 1000
    enemy_hp = 1000
    while True:
        my_hp=my_hp - enemy_hp
        enemy_hp = enemy_hp - my_power
        if my_hp <=0:
            print("我输了")
            break
        elif enemy_hp <=0 :
            print("敌人输了")
            break
