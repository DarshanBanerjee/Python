# Importing Modules :-
import time
import random

# Asking for 1 Game :-
time.sleep(0.5)
print("Hey, Let's play a Game!")
time.sleep(0.5)
print("But what to play?")
time.sleep(0.5)
print("Let it be your choice...")
time.sleep(0.5)
print("Type 1, If you want to play Snake-Water-Gun.")
time.sleep(0.2)
print("Type 2, If you want to play Rock-Paper-Scissor.")
time.sleep(0.2)
print("Type 3, If you want to play Lady-Hunter-Tiger.")
time.sleep(0.5)
t = int(input("Type 1, 2 or 3 - "))

# Playing a Game according to conditions based on input taken :-
if t == 1:

    # Defining Data:-
    SWG = ["Snake", "Water", "Gun"]
    i = True
    disclaimer = "[Disclaimer -      "
    disclaimer2 = "              This Game don't do any sort of cheating."
    disclaimer3 = "              Please do not think that it does the process according to your input."
    disclaimer4 = "              Everything is pre-defined and it generate a random value only. "
    disclaimer5 = "THANK YOU!]"


    def s(g):
        time.sleep(g)


    score = 0
    miss = 0


    def show():
        print("                                                        Score - ", score, "  Miss - ", miss)


    def miss1():
        time.sleep(0.5)
        print("Oops! You missed it...", end='')
        global miss
        miss += 1
        show()


    def win():
        time.sleep(0.5)
        print("Yeah! You got it...   ", end='')
        global score
        score += 1
        show()


    # Welcome User :-
    time.sleep(1)
    print("Hey, Let's play a Snake-Water-Gun Game!")
    time.sleep(0.5)
    print(disclaimer)
    print(disclaimer2)
    print(disclaimer3)
    print(disclaimer4)
    print(disclaimer5)
    time.sleep(1.0)
    print("Please turn your Caps-Lock on!")

    # Main Game Logic :-
    while i == True:
        Comp = random.choice(SWG)
        s(0.5)
        try:
            x = input('''Type 'S' for "Snake", 'W' for "Water" and 'G' for "Gun" - ''')
            if x == 'S':
                y = "Snake"
            if x == 'W':
                y = "Water"
            if x == 'G':
                y = "Gun"
            time.sleep(0.5)

            # Working according to Conditions :-
            if y == Comp:
                print("Computer - ", Comp, "    ", end='')
                show()
            else:
                if y == "Snake" and Comp == "Water":
                    print("Computer - ", Comp)
                    win()
                if y == "Snake" and Comp == "Gun":
                    print("Computer - ", Comp)
                    miss1()
                if y == "Water" and Comp == "Snake":
                    print("Computer - ", Comp)
                    miss1()
                if y == "Water" and Comp == "Gun":
                    print("Computer - ", Comp)
                    win()
                if y == "Gun" and Comp == "Snake":
                    print("Computer - ", Comp)
                    win()
                if y == "Gun" and Comp == "Water":
                    print("Computer - ", Comp)
                    miss1()
                if y == "Null":
                    pass


        except Exception as e:
            time.sleep(0.5)
            print("Sorry, Something wrong happened.")
            s(0.5)
            print("[Error Type :- ")
            print(e)

        finally:
            if score == 10:
                print()
                print("Yay! You won the Game!")
                i = False
            else:
                if miss == 10:
                    print()
                    print("Oops! You lost the Game...")
                    i = False

    print("Thank You!")

if t == 2:

    # Defining Data:-
    RPS = ["Rock", "Paper", "Scissor"]
    i = True
    disclaimer = "[Disclaimer -      "
    disclaimer2 = "              This Game don't do any sort of cheating."
    disclaimer3 = "              Please do not think that it does the process according to your input."
    disclaimer4 = "              Everything is pre-defined and it generate a random value only. "
    disclaimer5 = "THANK YOU!]"


    def s(g):
        time.sleep(g)


    score = 0
    miss = 0


    def show():
        print("                                                        Score - ", score, "  Miss - ", miss)


    def miss1():
        time.sleep(0.5)
        print("Oops! You missed it...", end='')
        global miss
        miss += 1
        show()


    def win():
        time.sleep(0.5)
        print("Yeah! You got it...   ", end='')
        global score
        score += 1
        show()


    # Welcome User :-
    time.sleep(1)
    print("Hey, Let's play a Rock-Paper-Scissor Game!")
    time.sleep(0.5)
    print(disclaimer)
    print(disclaimer2)
    print(disclaimer3)
    print(disclaimer4)
    print(disclaimer5)
    time.sleep(1.0)
    print("Please turn your Caps-Lock on!")

    # Main Game Logic :-
    while i == True:
        Comp = random.choice(RPS)
        s(0.5)
        try:
            x = input('''Type 'R' for "Rock", 'P' for "Paper" and 'S' for "Scissor" - ''')
            if x == 'R':
                y = "Rock"
            if x == 'P':
                y = "Paper"
            if x == 'S':
                y = "Scissor"
            time.sleep(0.5)

            # Working according to Conditions :-
            if y == Comp:
                print("Computer - ", Comp, "   ", end='')
                show()
            else:
                if y == "Rock" and Comp == "Paper":
                    print("Computer - ", Comp)
                    miss1()
                if y == "Rock" and Comp == "Scissor":
                    print("Computer - ", Comp)
                    win()
                if y == "Paper" and Comp == "Rock":
                    print("Computer - ", Comp)
                    win()
                if y == "Paper" and Comp == "Scissor":
                    print("Computer - ", Comp)
                    miss1()
                if y == "Scissor" and Comp == "Rock":
                    print("Computer - ", Comp)
                    miss1()
                if y == "Scissor" and Comp == "Paper":
                    print("Computer - ", Comp)
                    win()
                if y == "Null":
                    pass

        except Exception as e:
            time.sleep(0.5)
            print("Sorry, Something wrong happened.")
            s(0.5)
            print("[Error Type :- ")
            print(e)

        finally:
            if score == 10:
                print()
                print("Yay! You won the Game!")
                i = False
            else:
                if miss == 10:
                    print()
                    print("Oops! You lost the Game...")
                    i = False

    print("Thank You!")

if t == 3:

    # Defining Data:-
    LHT = ["Lady", "Hunter", "Tiger"]
    i = True
    disclaimer = "[Disclaimer -      "
    disclaimer2 = "              This Game don't do any sort of cheating."
    disclaimer3 = "              Please do not think that it does the process according to your input."
    disclaimer4 = "              Everything is pre-defined and it generate a random value only. "
    disclaimer5 = "THANK YOU!]"


    def s(g):
        time.sleep(g)


    score = 0
    miss = 0


    def show():
        print("                                                        Score - ", score, "  Miss - ", miss)


    def miss1():
        time.sleep(0.5)
        print("Oops! You missed it...", end='')
        global miss
        miss += 1
        show()


    def win():
        time.sleep(0.5)
        print("Yeah! You got it...   ", end='')
        global score
        score += 1
        show()


    # Welcome User :-
    time.sleep(1)
    print("Hey, Let's play a Lady-Hunter-Tiger Game!")
    time.sleep(0.5)
    print(disclaimer)
    print(disclaimer2)
    print(disclaimer3)
    print(disclaimer4)
    print(disclaimer5)
    time.sleep(1.0)
    print("Please turn your Caps-Lock on!")

    # Main Game Logic :-
    while i == True:
        Comp = random.choice(LHT)
        s(0.5)
        try:
            x = input('''Type 'L' for "Lady", 'H' for "Hunter" and 'T' for "Tiger" - ''')
            if x == 'L':
                y = "Lady"
            if x == 'H':
                y = "Hunter"
            if x == 'T':
                y = "Tiger"
            time.sleep(0.5)

            # Working according to Conditions :-
            if y == Comp:
                print("Computer - ", Comp, "    ", end='')
                show()
            else:
                if y == "Lady" and Comp == "Hunter":
                    print("Computer - ", Comp)
                    win()
                if y == "Lady" and Comp == "Tiger":
                    print("Computer - ", Comp)
                    miss1()
                if y == "Hunter" and Comp == "Lady":
                    print("Computer - ", Comp)
                    miss1()
                if y == "Hunter" and Comp == "Tiger":
                    print("Computer - ", Comp)
                    win()
                if y == "Tiger" and Comp == "Lady":
                    print("Computer - ", Comp)
                    win()
                if y == "Tiger" and Comp == "Hunter":
                    print("Computer - ", Comp)
                    miss1()
                if y == "Null":
                    pass

        except Exception as e:
            time.sleep(0.5)
            print("Sorry, Something wrong happened.")
            s(0.5)
            print("[Error Type :- ")
            print(e)
            print("]")

        finally:
            if score == 10:
                print()
                print("Yay! You won the Game!")
                i = False
            else:
                if miss == 10:
                    print()
                    print("Oops! You lost the Game...")
                    i = False

    print("Thank You!")

else:
    print("Sorry, Not received correct input...")