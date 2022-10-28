try: 
    import time

    from lesson11 import *
    if login == "guli" and parol == 2103:
        print("Siz  tizimga muvaffaqiyatli kirdingiz")
    elif login == "guli" and parol != 2103:
        print("Siz parolni xato kiritdingiz va 10 sekund kuting")
        a = 0
        while a < 10:
            a += 1
            time.sleep(1)
            print(a)
    elif login != "guli" and parol == 2103:
        print("Siz loginni xato kiritdingiz va 5 soniya kuting")
        b = 0
        while b < 5:
            b += 1 
            time.sleep(1)
            print(b)
    else:
        print("Siz login va parolni xato kiritdingiz shu sababli 60 soniya kuting")
        c = 0 
        while c < 60:
            c += 1
            time.sleep(1)
            print(c)
except ValueError:
    print("Siz harf kiritdingiz")
except:
    print("xatolik bor")                                      