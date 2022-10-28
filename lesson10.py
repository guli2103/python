import time

parol = int(input("Kodni kiriting: "))
a = 0
b = 60
if parol == 2103:
    print("Hurmatli foydalanuvchi kodni to'g'ri kiritdingiz")
elif parol != 2103:
    print("60 sekund kuting")
    while a < b:
        a += 1
        time.sleep(1)
        print(a)
    print("60 sekunt tugadi qaytadan urinib ko'ring")
       