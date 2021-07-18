# 1. Importing Modules :-
import time
import NormalDice

# 2. Main Game Loop :-
print("Welcome to The Game of Dice!")
time.sleep(1.0)
print("You have to give the percentage of each value (1, 2, 3, 4, 5, 6).\nBut Make Sure that they add up to 100.")
percentage1 = int(input("Enter the Percentage of 1 : "))
percentage2 = int(input("Enter the Percentage of 2 : "))
percentage3 = int(input("Enter the Percentage of 3 : "))
percentage4 = int(input("Enter the Percentage of 4 : "))
percentage5 = int(input("Enter the Percentage of 5 : "))
percentage6 = int(input("Enter the Percentage of 6 : "))

if (percentage1 + percentage2 + percentage3 + percentage4 + percentage5 + percentage6) != 100:
    print("Sorry, The Values do NOT add up to 100.")
    time.sleep(1.0)
    print("Quiting...")
    time.sleep(1.0)
    print("Quited.")
    quit()
real1 = percentage1// 10
real2 = percentage2//10
real3 = percentage3//10
real4 = percentage4//10
real5 = percentage5//10
real6 = percentage6//10

toGive = []
for i in range(real1):
    toGive.append(1)
for i in range(real2):
    toGive.append(2)
for i in range(real3):
    toGive.append(3)
for i in range(real4):
    toGive.append(4)
for i in range(real5):
    toGive.append(5)
for i in range(real6):
    toGive.append(6)

NormalDice.Dice(toGive)
