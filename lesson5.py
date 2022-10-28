a = int(input("1-son: "))
b = int(input("2-son: "))
c = 0
amal = input("amalni kiriting: ")

def son(a,b):
    if amal == "+":
        print("natija: ", a + b)
    elif amal == "*":
        print("natija: ", a + b)
    elif amal == "-":
        print("natija: ", a - b)
    elif amal == "/":
        print("natija: ", a / b) 
    else:
       print("amalda xatolik bor")                             
son(a,b) 


while a < b:
    print(a)
    a += 1 

    
while a > b:
    print(b)
    b += 1   
          
