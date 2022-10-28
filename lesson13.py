import time

b = int(input('''Quyidagiardan birinni tanlang
1: Registratsiya
2: Kalkulyator
3: Dictonaries(telefon)
4: Dictonaries(moshina)
5: Import
'''))

if b == 1:
    from lesson import *
elif b == 2:
    from lesson5 import *
elif b == 3:
    from lesson8 import *
elif b == 4:
    from lesson9 import *
elif b == 5:
    from lesson12 import *
else:
    print("Siz xato sonni kiritdingiz 15 soniya kuting")
    for x in range(15):
        time.sleep(1)
        print(x)    



