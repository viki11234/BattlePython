import random

pintu = []
# pintugailv [90,10]
# diaoluo gailv = 30
shouci = 30

nage = 0
a = 1
cishu = 0
diaobudiao = 0
diaoziji = 0
diaoqita = 0
jilv = 0

for i in range(1,25):
    cishu = cishu +1
    diaoluo = False
    #决定掉不掉
    while not diaoluo:
        cishu = cishu + 1
        jilv = random.randint(0,100)
        if shouci > jilv:
            diaoluo = True
            break
        diaobudiao = diaobudiao + 1

    nage = random.randint(0,100)
    #决定掉哪个
    if nage <21 :
        #不能掉自己也不能掉已经掉落的
        while a != i and a in pintu :
            a = random.randint(1,25)
            cishu = cishu + 1
        diaoqita = diaoqita +1
        pintu.append(a)
    elif 21<=nage<100:
        #掉自己 加进列表
        diaoziji =diaoziji +1
        pintu.append(i)

print(pintu)
print(f"总次数={cishu}")
print(f"掉不掉={diaobudiao}")
print(f"掉自己={diaoziji}")
print(f"掉其他={diaoqita}")