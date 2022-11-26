import math

print("""
press -
1 - Addition(x, y)
2 - subtraction(x,y)
3-multiplication(x,y)
4 - division(x, y)
5- exponent(x, y)
6 - tan(x)
7 - sin(x)
8 - cos(x)
9 - factorial(x)
10 - log(x)
""")
o = input("")
if o == "1":
    x = int(input("1st number -"))
    y = int(input("2nd number -"))
    print(x + y)
elif o == "2":
    x = int(input())
    y = int(input())
    print(x - y)
elif o == "3":
    x = int(input())
    y = int(input())
    print(x * y)
elif o == "4":
    x = int(input())
    y = int(input())
    print(x / y)
elif o == "5":
    x = int(input())
    y = int(input())
    print(x ** y)
elif o == "6":
    x = int(input())
    print(math.tan(x))
elif o == "7":
    x = int(input())
    print(math.sin(x))
elif o == "8":
    x = int(input())
    print(math.cos(x))
elif o == "9":
    x = int(input())
    print(math.factorial(x))
elif o == "10":
    x = int(input())
    print(math.log(x))
else:
    print("Invalid")