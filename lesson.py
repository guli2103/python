a = input(''' Quyidagilardan birini tanlang
1: Registratsiya
2: Login
''')

if  a == "1":
     print("siz registratsiyaga muvaffaqiyatli kirdingiz")
     ism = input("Ismingizni kiriting: ")
     fam = input("Familiyangizni kiriting: ")
     email = input("emailingizni kiriting: ")
     parol =input("parolingizni kiriting: ")
     print( ism + "siz registratsiyaga kirdingiz")
elif a == "2":
    print("login va parolingizni kiriting")
    login = input("loginingizni kiriting: ")
    parol = input("parolingizni kiriting: ")
    if  login == "guli" and parol == "2103":
        print("guli siz muvaffaqiyatli kirdingiz")
    elif login != "guli" and parol =="2103":
        print("login xato")
    elif login == "guli" and parol != "2103":
        print("parol xato")
    else:
        print("login va parol xato")
else:
    for x in range(60):
        print(x)
        print("siz dasturga kirolmadiz")                         