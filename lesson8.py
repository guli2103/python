lugat = {
    "Apple": {
        "a": ["13 Pro Max","1250$"],
        "a1":["MackBook Pro 2022 M2","18000$"],
        "a2": ["Apple iPhone SE (2020)","5 386 000$" ]
    },
    "Samsung": {
        "b": ["Samsung Galaxy S10","22989$"],
        "b1": ["Samsung Galaxy S10e","49848$"],
        "b2": ["Samsung Galaxy S22","22006$"]
    },
    "Huawei": {
        "c": ["huawei p40","22333$"],
        "c1": ["huawei p30","34342$"],
        "c2": ["Huawei P50 Pro","12234$"]
    }
}
d = input('''Qaysi birini tanlaysiz:
Apple
Samsung
Huawei
''')
if d.lower() == "apple":
    g = int(input('''Siz Apple kompaniyasi tomonidan qaysi brendni tanlaysiz:
    1:
    2:
    3:
    '''))
    if g == 1:
        print("Siz tanlagan brend va shuni narxi",lugat["Apple"]["a"])
    elif g == 2:
        print(("Siz tanlagan brend va shuni narxi",lugat["Apple"]["a1"]))
    elif g == 3:
        print("Siz tanlagan brend va shuni narxi", lugat["Apple"],["a3"])        
elif d.lower() == "samsung":
    
    print(lugat["Samsung"]) 
elif d.lower() == "huawei":
    print(lugat["Huawei"]) 
else:
    print("siz xato nom kiritdingiz")    


