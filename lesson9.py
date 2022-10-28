moshin = {
    "BMW":{
        "a":["BMW iX","9 580 000 ₽"],
        "a1":["BMW iX M60","12 930 000 ₽"],
        "a2":["BMW ix m50","13 220 009 ₽"]
    },
    "GMC":{
        "a":["Sierra 1500","62 800$"],
        "a1":["Sierra HD","69600$"],
        "a2":["Canyon","41200$"]
    },
    "Chevrolet":{
        "a":["Cobalt","25600$"],
        "a1":["Nexia","17900$"],
        "a2":["captiva","36600$"]
    }
}
b = input('''Qaysi moshina turini tanlaysiz
BMW
GMC
CHevrolet
''')
if b.lower() == "bmw":
    print("Siz BMW moshina turini tanladingiz")
    c = int(input('''Qaysi breandi kerak
    1: BMW iX
    2: BMW iX M60
    3: BMW ix m50
    '''))
    if c == 1:
        print("Siz BMW  kompaniyasi tomonidan breandi: ",moshin["BMW"]["a"][0]," narxi: ",moshin["BMW"]["a"][1]," bo'lgan moshina tanladingiz ")
    elif c == 2:
        print("Siz BMW kompaniyasi  tomonidan breandi: ",moshin["BMW"]["a1"][0]," narxi: ",moshin["BMW"]["a1"][1]," bo'lgan moshina tanladingiz ")
    elif c == 3:
        print("Siz BMW kompaniyasi  tomonidan breandi: ",moshin["BMW"]["a2"][0]," narxi: ",moshin["BMW"]["a2"][1]," bo'lgan moshina tanladingiz ") 
elif b.lower() == "gmc":
    print("Siz GMC moshina turini tanladingiz") 
    d = int(input('''Qaysi breand kerak
    1: Sierra 1500
    2: Sierra HD
    3: Canyon
    '''))             
    if d == 1:
        print("Siz GMC kompaniyasi tomonidan breandi: ",moshin["GMC"]["a"][0]," narxi: ", moshin["GMC"]["a"][1],"bo'lgan moshina oldingiz") 
    elif d == 2:
        print("Siz GMC kompaniyasi tomonidan breandi: ",moshin["GMC"]["a1"][0]," narxi: ", moshin["GMC"]["1"][1],"bo'lgan moshina oldingiz")
    elif d == 3:
        print("Siz GMC kompaniyasi tomonidan breandi: ",moshin["GMC"]["a2"][0]," narxi: ", moshin["GMC"]["a2"][1],"bo'lgan moshina oldingiz")
elif b.lower() == "chevrolet":
    g = int(input('''Qaysi breand kerak
    1: Cobalt
    2: Nexia
    3: captiva
    '''))
    if g == 1:
        print("Siz Chevrolet kompaniyasi tomonidan breandi: ",moshin["Chevrolet"]["a"][0]," narxi: ",moshin["Chevrolet"]["a"][1]," bo'gan moshina tanladingiz")  
    elif g == 2:
        print("Siz Chevrolet kompaniyasi tomonidan breandi: ",moshin["Chevrolet"]["a1"][0]," narxi: ",moshin["Chevrolet"]["a1"][1]," bo'gan moshina tanladingiz")        
    elif g == 3:
        print("Siz Chevrolet kompaniyasi tomonidan breandi: ",moshin["Chevrolet"]["a2"][0]," narxi: ",moshin["Chevrolet"]["a2"][1]," bo'gan moshina tanladingiz")        
      
