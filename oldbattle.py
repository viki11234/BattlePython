import random


class people:

    def __init__(self, name):
        self.NAME = name
        self.ATK = random.randint(10, 40)
        self.DEF = random.randint(0, 30)
        self.HP = random.randint(60, 100)
        print(f'{self.NAME}的攻击力为{self.ATK}, 防御力为{self.DEF}, 生命值为{self.HP} ')

    def hurt(self, dam):
        self.HP = self.HP - dam
        if self.dead():
            print(f"{self.NAME} 死了")

    def dead(self):
        return self.HP <= 0
    def critical(self,dam):
        if random.randint(0,100)>40:
            dam = 1.5*dam
            return dam
        else:
            return dam
class battle:

    def damage(self,A,B):
        dam = A.ATK - B.DEF
        dam1 = B.ATK - A.DEF
        if dam <= 0:
            dam = 1
        else:
            dam = dam
        if dam1 <= 0:
            dam1 = 1
        else:
            dam1 = dam1
        return dam , dam1

    def fight(self, A, B,turns):
        firsthit = random.randint(0, 100)
        dam,dam1 = self.damage(A,B)
        if firsthit > 50:

            while not A.dead() and not B.dead():
                enddam2 = B.critical(dam)
                B.hurt(enddam2)
                print(f'{B.NAME}对{A.NAME}造成了{enddam2}点伤害，{A.NAME}还剩{A.HP}点生命值')
                if A.dead() or B.dead():
                    break
                enddam1 = A.critical(dam1)
                A.hurt(enddam1)
                print(f'{A.NAME}对{B.NAME}造成了{enddam1}点伤害，{B.NAME}还剩{B.HP}点生命值')

        else:

            while not A.dead() and not B.dead():
                enddam1 = A.critical(dam1)
                A.hurt(enddam1)
                print(f'{A.NAME}对{B.NAME}造成了{enddam1}点伤害，{B.NAME}还剩{B.HP}点生命值')
                if A.dead() or B.dead():
                    break
                enddam2 = B.critical(dam)
                B.hurt(enddam2)
                print(f'{B.NAME}对{A.NAME}造成了{enddam2}点伤害，{A.NAME}还剩{A.HP}点生命值')
    def times(self):
        turns = turns +1
        return turns
    viki = people("viki")
hiker = people("Hiker")

battle().fight(viki, hiker,0)
