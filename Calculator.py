def Input_Number():
    p = ""
    while True:  
        p = input(">>>")
        try:
            p = int(p)
            break
        except:
            print("Please try again and enter a number")
    return p

def Calculating():
    if z == "+":
        a = x + y
        print(a)
    else:
        if z == "-":
            b = x - y
            print(b)
        else:
            if z == "*":
                c = x * y
                print(c)
            else:
                if z == "/":
                    d = x / y
                    print(d)
                else:
                    pass

print("Hello")

print("Type first number")
x = Input_Number()

print("Type second number")
y = Input_Number()

opts = {"+", "-", "*", "/"}
print("Type an Action: + - * /")

while True:
    z = input(">>>")
    if z in opts:
        break
    else:
        print("Please try again and enter an operator")

Calculating()