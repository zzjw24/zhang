from random import randint
import time,sys

class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber
        self.warriors = {}


class Warrior:


    def __init__(self, strength):
        self.strength = strength


    def healing(self, stoneCount):

        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount


        if self.strength > self.maxStrength:
            self.strength = self.maxStrength



class Archer(Warrior):

    typeName = '弓箭兵'
    price = 100
    maxStrength = 100



    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name


    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('不知名的妖怪')




class Axeman(Warrior):

    typeName = '斧头兵'
    price = 120
    maxStrength = 120



    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name


    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')


class Eagle():
    typeName = '鹰妖'


class Wolf():
    typeName = '狼妖'


class Forest():
    def __init__(self,monster):

        self.monster = monster

print('''
***************************************
****           游戏开始             ****
***************************************

'''
)


forest_num = 7

forestList = []


notification = '出现的妖怪：'
for j in range(forest_num):
    typeName = randint(1,2)
    if typeName == 1:
        forestList.append( Forest(Wolf()) )
    else:
        forestList.append( Forest(Eagle()) )

    notification += \
        f'第{j+1}座森林里面是 {forestList[j].monster.typeName}  '

print(notification,end='')
print('\n')
for j in range(10):
    print('\n')


player0 = Player(1000)
print(f'你有1000,开始雇佣士兵\n')
while True:
    fighter_type = input('请输入雇佣的士兵类型序号\n0.斧头兵\n1.弓箭兵\n2.可以看现在的余额\n3.可查看雇佣队列\n4.退出雇佣环节')
    if fighter_type.isdigit():
        fighter_type = int(fighter_type)
        if fighter_type == 0:
            name = input('给斧头兵取一个名\n')
            player0.hire(foutou(name))
        elif fighter_type == 1:
            name = input('给弓箭兵取一个名\n')
            player0.hire(gongjian(name))
        elif fighter_type == 2:
            print(f'你现在的余额{player0.money}')
        elif fighter_type == 3:
            for j in player0.army.keys():
                print(j)
        elif fighter_type == 4:
            break
        else:
            print('重新\n')
    else:
        print(f'{type(fighter_type)}有错\n')



print(f'===========开始闯关==========\n')
game_end = 1
for j in range(len(forest_list.forest_count)):
    if game_end == 0:
        break
    print(f'欢迎来到第{j + 1}关\n')
    while True:
        if len(player1.army) == 0:
            print('您的士兵数量为0.闯关失败\n')
            game_end = 0
            break
        else:
            fighter = input(f'选择士兵，输入（army）可看雇佣列表--\n')
            if fighter == 'army':
                for h in player0.army.keys():
                    print(h)
            else:
                if fighter in player0.army:
                    player0.army[fighter].fight(not forest_list.forest_count[j].monstr_name)
                    fighter_hp = player0.army[fighter].soldier_hp_now
                    print(fighter_hp)
                    if fighter_type > 0:
                        while True:
                            treat_count = input(f'闯关成功，{fighter}相应数额的血量\n')
                            if treat_count.isdigit():
                                if player0.money > int(treat_count):

                                    player0.army[fighter].treat(int(treat_count))
                                    break
                            else:
                                print('余额不狗')
                    else:
                            print('输入有误，重新输入\n')
                    break
                elif fighter_hp < 0:
                    del player0.army[fighter]
                    print(f'{fighter}血量剩余{fighter_hp}失败,重新开始\n')
                    continue
                else:
                    print('该士兵名不对\n')

if game_end == 0:
    print('6666666\n')
    print(f'你还剩下{player0.money}')
elif game_end == 1:

    print('结束')