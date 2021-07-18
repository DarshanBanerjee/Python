# 1. Importing Modules :-
import time
import math

# 2. Defining Data :-



# 3. Defining Functions for Different Operations :-

class Operations():
    class Add():
        def Add2(self):
            num1 = float(input("Enter the First Number : "))
            num2 = float(input("Enter the Second Number : "))
            print("The Sum of ", num1, " and ", num2, " is - ", (num1 + num2))
        def Add3(self):
            num1 = float(input("Enter the First Number : "))
            num2 = float(input("Enter the Second Number : "))
            num3 = float(input("Enter the Third Number : "))
            print("The Sum of ", num1, ", ", num2, " and ", num3, " is - ", (num1 + num2 + num3))
        def Add4(self):
            num1 = float(input("Enter the First Number : "))
            num2 = float(input("Enter the Second Number : "))
            num3 = float(input("Enter the Third Number : "))
            num4 = float(input("Enter the Fourth Number : "))
            print("The Sum of ", num1, ", ", num2, ", ", num3, " and ", num4, " is - ", (num1 + num2 + num3 + num4))

    def Sub(self):
        num1 = float(input("Enter the First Number : "))
        num2 = float(input("Enter the Second Number : "))
        print("The Difference of ", num1, " and ", num2, " is - ", (num1 - num2))

    def Mul(self):
        num1 = float(input("Enter the First Number : "))
        num2 = float(input("Enter the Second Number : "))
        print("The Product of ", num1, " and ", num2, " is - ", (num1 * num2))

    def Div(self):
        num1 = float(input("Enter the First Number (Dividend) : "))
        num2 = float(input("Enter the Second Number (Divisor) : "))
        print("The Quotient of ", num1, " and ", num2, " is - ", (num1 / num2))

    def Per(self):
        num1 = float(input("Enter the First Number (Percentage) : "))
        num2 = float(input("Enter the Second Number (Total) : "))
        num3 = num1/100
        num4 = num3 * num2
        print(num1, "% of ", num2, " is - ", num4)

    def Fac(self):
        num = int(input("Enter a Number : "))
        print("The Answer is - ", math.factorial(num))

# 4. Main Game Loop :-
print("Welcome!")
time.sleep(1.0)
print('''
We have the Following Operations :-\n
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Percentage
6. Sine
7. Cosine
8. Tangent
9. ArcSine
10. ArcCosine
11. ArcTangent
12. Factorial
13. Log
14. Power
15. Root
''')
time.sleep(1.0)
oper = int(input("Which Operation do you want to use? (1 - 15) : "))
if oper == 1:
    add = int(input("How many Numbers do you want to add? (2 - 4) : "))
    if add == 2:
        root = Operations()
        add_Root = root.Add()
        add_Root.Add2()
    elif add == 3:
        root = Operations()
        add_Root = root.Add()
        add_Root.Add3()
    elif add == 4:
        root = Operations()
        add_Root = root.Add()
        add_Root.Add4()
    elif add > 4:
        print("Sorry, We Do NOT have the Feature of Adding more than 4 Numbers as of now.\nPlease Come back later.")
    else:
        print("Sorry, Not received correct Input")
elif oper == 2:
    root = Operations()
    root.Sub()
elif oper == 3:
    root = Operations()
    root.Mul()
elif oper == 4:
    root = Operations()
    root.Div()
elif oper == 5:
    root = Operations()
    root.Per()
elif oper == 6:
    num = float(input("Enter a Number : "))
    print("The Answer is - ", math.sin(num))
elif oper == 7:
    num1 = float(input("Enter a Number : "))
    print("The Answer is - ", math.cos(num1))
elif oper == 8:
    num2 = float(input("Enter a Number : "))
    print("The Answer is - ", math.tan(num2))
elif oper == 9:
    num = float(input("Enter a Number : "))
    print("The Answer is - ", math.asin(num))
elif oper == 10:
    num = float(input("Enter a Number : "))
    print("The Answer is - ", math.acos(num))
elif oper == 11:
    num = float(input("Enter a Number : "))
    print("The Answer is - ", math.atan(num))
elif oper == 12:
    root = Operations()
    root.Fac()
elif oper == 13:
    num = float(input("Enter the First Number : "))
    num1 = float(input("Enter the Second Number (Base) : "))
    print("The Answer is - ", math.log(num, num1))
elif oper == 14:
    num = float(input("Enter the First Number (Base) : "))
    num1 = float(input("Enter the Second Number (Power) : "))
    print("The Answer is - ", math.pow(num, num1))
elif oper == 15:
    num = float(input("Enter the First Number (Base) : "))
    num1 = float(input("Enter the Second Number (Power) : "))
    print("The Answer is - ", (num**num1))
else:
    print("Sorry, Not Received Correct Input...")
print("Thank You!")

