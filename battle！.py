import random


class people:

    def __init__(self, name):
        # 初始化属性，随机攻防，HP
        self.NAME = name
        self.ATK = random.randint(10, 40)
        self.DEF = random.randint(20, 30)
        self.HP = random.randint(60, 100)
        self.max_HP = self.HP

        self.buff_round = 2
        print(f'{self.NAME}的攻击力为{self.ATK}, 防御力为{self.DEF}, 生命值为{self.HP} ')

    def hurt(self, dam):
        # 新生命值 = 老生命值 - 受到的伤害
        self.HP = self.HP - dam

    def is_dead(self):
        # 生命值小于0时，死了
        return self.HP <= 0

    def buff_test(self, dam):
        # buff效果，当defender的生命值低于最大生命值的40%，dam*2，持续2回合
        if self.buff_round > 0:
            if self.HP < 0.4 * self.max_HP:
                dam = 2 * dam
            return dam
        else:
            return dam


class battle:
    # 默认从第1回合开始
    turns = 1

    actors = []

    def go_first(self, attacker, defender):

        actors = [attacker, defender]
        # 随机数 决定先后手
        firsthit = random.randint(0, 100)
        if firsthit > 50:
            self.go_round(attacker, defender)
        else:
            self.go_round(defender, attacker)

    def go_round(self, attacker, defender):
        # 直到有人死为止，反复互相造成伤害
        while True:

            if self.apply_damage(attacker, defender):
                break
            if self.apply_damage(defender, attacker):
                break
            self.times()

    def apply_damage(self, attacker, defender):
        # 判断有没有人死，死了返回True
        if not attacker.is_dead() and not defender.is_dead():
            # damage有两个返回值，dam的值和是不是暴击
            dam, is_critical = self.damage(attacker, defender)
            defender.hurt(dam)
            if is_critical:
                print(
                    f'第{self.turns}回合，{attacker.NAME}对{defender.NAME}造成了{dam}点伤害,暴击了!，{defender.NAME}还剩{defender.HP}点生命值')
            else:
                print(f'第{self.turns}回合，{attacker.NAME}对{defender.NAME}造成了{dam}点伤害,{defender.NAME}还剩{defender.HP}点生命值')
            if attacker.is_dead() or defender.is_dead():
                print(f"{defender.NAME} 死了")
                return True

        return False

    def critical(self, dam):
        if random.randint(0, 100) < 40:
            dam = 1.5 * dam
            return dam, True
        else:
            return dam, False

    def damage(self, attacker, defender):
        dam = attacker.ATK - defender.DEF
        if dam <= 5:
            dam = 5
        else:
            dam = dam
        dam, is_critical = self.critical(dam)
        dam = defender.buff_test(dam)
        return dam, is_critical

    def times(self):
        self.turns = self.turns + 1

        for i in self.actors:
            i.buff_round = i.buff_round - 1;


viki = people("viki")
hiker = people("Hiker")

battle().go_first(viki, hiker)
