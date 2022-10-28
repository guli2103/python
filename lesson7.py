a = int(input('''Quyidagilardan birini tanlang:
1:string
2:intejer
3:float
4:boolen
5:list
'''))
if a == 1:
    print("Siz string turini tanladingiz")
    b = int(input('''Sizga qaysi biri kerak:
    1:O'zimiz haqimizda ma'lumot
    2:Registratsiya
    '''))
    if b == 1:
        print("Men Ergasheva Gulbahor yoshim 19 da. Hozirda  2- D guruh talabasiman")
    elif b == 2:
        print("Siz registratsityadan  o'tyapsiz")
        ism = input("Ismingiznni kiriting: ") 
        fam = input("Familiyangizni kiriting: ")   
        parol = input("Parolingizni kiriting: ")
        login = input("Loginingizni kkiriting: ")
        email = input("emailingizni kiriting: ")
if a == 2:
    print("Siz intejer turini tanladingiz")
    c = int(input('''Sizga qaysi biri kerak:
    1:Kalkulyator
    2:Toq sonlar
    3:Juft sonlar
    4:2 ta nol bilan tugaydigan sonlar
    '''))        
    if c == 1:
        qiymat1 = int(input("1-sonni kiriting: "))
        qiymat2 = int(input("2-sonni kiriting: "))
        amal = input("amalni tanlang: ")
        def calc(qiymat1,qiymat2):
            if amal == "+":
                print("Natija: ", qiymat1 + qiymat2)
            elif amal == "-":
                print("Natija: ",qiymat1 + qiymat2) 
            elif amal == "*":
                print("Natija: ", qiymat1 * qiymat2)
            elif amal == "/":
                print("Natija: ", qiymat1 / qiymat2)
            else:
                print("Siz xato amal kiritdingiz")
        calc(qiymat1,qiymat2) 
    elif c == 2:
        for x in range(-1,1000,2):
            print(x) 
    elif c == 3:
        d = 0:
        while d < 1000:
            d += 2:
            print(d)                     

