import random
import time

class Forest:
    def __init__(self, count: int, *monster):
        forest_count = []
        for i in range(count):
            forest_count.append(random.choice(monster))
        self.forest_count = forest_count


# 只有名字的怪物类
class wolf:
    monster_name = '狼妖'


class hawk:
    monster_name = '鹰妖'




class Soldier:
    soldier_name = '普通人'
    soldier_price = 100
    soldier_hp_max = 100
    enemy_god = '狼妖'
    enemy_bad = '鹰妖'


    def __init__(self):
        self.soldier_hp_now = 100


    def treat(self, money_count):
        if self.soldier_hp_now == self.soldier_hp_max:
            print('当前生命是满的，治疗无效')
        else:
            self.soldier_hp_now += money_count
        if self.soldier_hp_now > self.soldier_hp_max:
            self.soldier_hp_now = self.soldier_hp_max
        print(self.soldier_hp_now)


    def fight(self, enemy_name):
        if enemy_name == self.enemy_god:
            self.soldier_hp_now -= 20
        elif enemy_name == self.enemy_bad:
            self.soldier_hp_now -= 80
        else:
            print('怪物类型不对劲，血量不变')


class Axe(Soldier):
    soldier_type = '斧头兵'
    soldier_price = 120
    soldier_hp_max = 120
    enemy_god = '狼妖'
    enemy_bad = '鹰妖'

    def __init__(self, soldier_name):
        self.soldier_hp_now = 120
        self.soldier_name = soldier_name


# 弓箭类
class Arch(Soldier):
    soldier_name = '弓箭兵'
    soldier_price = 100
    soldier_hp_max = 100
    enemy_god = '狼妖'
    enemy_bad = '鹰妖'

    def __init__(self, soldier_name):
        self.soldier_hp_now = 100
        self.soldier_name = soldier_name



class Player:
    def __init__(self):
        self.money = 1000
        self.army = {}
    def hire(self, soldier):
        banlance = self.money - soldier.soldier_price
        if soldier.soldier_name in self.army:
            print('名字重复，雇佣失败')
        elif banlance >= 0:
            self.money -= soldier.soldier_price
            self.army[soldier.soldier_name] = soldier
            print(f'雇佣成功,余额{self.money}')
        else:
            print('余额不足，雇佣失败')



print('==========================游戏开始============================\n')
forest_list = Forest(7, wolf, hawk)
print(f'共7个关卡，怪物分别为:\n')
for i in forest_list.forest_count:
    print(i.monster_name)
print('注意：十秒后内容消失\n')
# time.sleep(10)
for i in range(10):
    print('\n')


player1 = Player()
print(f'你有{player1.money},准备开始雇佣士兵\n')
while True:
    fighter_type = input('请输入需要雇佣的士兵类型序号\n1.斧头兵\n2.弓箭兵\n3.退出雇佣环节\n4.可查看雇佣队列\n5.退出雇佣模式')
    if fighter_type.isdigit():
        fighter_type = int(fighter_type)
        if fighter_type == 1:
            name = input('给斧头兵取名字\n')
            player1.hire(foutou(name))
        elif fighter_type == 2:
            name = input('给弓箭兵取名字\n')
            player1.hire(gongjian(name))
        elif fighter_type == 3:
            print(f'你当前余额{player1.money}')
        elif fighter_type == 4:
            for i in player1.army.keys():
                print(i)
        elif fighter_type == 5:
            break
        else:
            print('打错了，重来\n')
    else:
        print(f'{type(fighter_type)}输入错误，重新输入\n')



print(f'===========开始闯关==========\n')
game_end = 1
for i in range(len(forest_list.forest_count)):
    if game_end == 0:
        break
    print(f'欢迎来到第{i + 1}关\n')
    while True:
        if len(player1.army) == 0:
            print('您的士兵数量为0.闯关失败\n')
            game_end = 0
            break
        else:
            fighter = input(f'--请从您的雇佣列表内选择出击的士兵，输入（army）可查看雇佣列表--\n')
            if fighter == 'army':
                for k in player1.army.keys():
                    print(k)
            else:
                if fighter in player1.army:
                    player1.army[fighter].fight(not forest_list.forest_count[i].monstr_name)
                    fighter_hp = player1.army[fighter].soldier_hp_now
                    print(fighter_hp)
                    if fighter_type > 0:
                        while True:
                            treat_count = input(f'闯关成功，准备进入下一关，输入数字可恢复{fighter}对应数额的血量\n')
                            if treat_count.isdigit():
                                if player1.money > int(treat_count):

                                    player1.army[fighter].treat(int(treat_count))
                                    break
                            else:
                                print('余额不足')
                    else:
                            print('输入错误，重新输入\n')
                    break
                elif fighter_hp < 0:
                    del player1.army[fighter]
                    print(f'{fighter}战斗后的血量为{fighter_hp}，阵亡，闯关失败,重新开始\n')
                    continue
                else:
                    print('输入的士兵名称有误\n')

if game_end == 1:
    print('666666666666\n')
    print(f'你还剩下{player1.money}')
elif game_end == 0:

    print('完蛋，森林都过不去')