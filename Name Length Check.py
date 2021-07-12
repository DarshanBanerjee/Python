a = input("Enter the first name - ")
b = input("Enter the second name - ")
c = input("Enter the third name - ")
d = input("Enter the fourth name - ")
e = input("Enter the fifth name - ")
names = [a, b, c, d, e]
if len(a)>7 or len(b)>7 or len(c)>7 or len(d)>7 or len(e)>7:
    for i in names:
        if len(i) > 7:
                print(i)
else:
    print("Not Found")