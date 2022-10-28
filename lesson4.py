a = int(input("1-son: "))
b = int(input("2-son: "))
c = 0 

if a % 2 == 0:
    print(str(a), "Juft son")
elif a % 2 != 0:
    print(str(a), "Toq son")
else:
    print("xatolik bor")

for x in range(a,b):
    c += x

for x in range(b,a):
    c += x
print("yig'indi", str(c), "ga teng")
if c % 2 == 0:
    print(str(c), "Juft son")
elif c % 2 == 1:
    print(str(c), "Toq son")


a = [["gulxayo"],["shahnoza"]]
b = int(input("sonni kiriting: "))

def son(b):
    if b % 2 != 0:
 0       print(a[0])
    elif b % 2 == 0:
        print(a[1])
    else:
        for x in range(60):
            print(x)        
son(b)




