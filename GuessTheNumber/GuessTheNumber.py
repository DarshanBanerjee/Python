
try:
    # 1. Importing Modules :-
    import random
    import time

    # 2. Defining Data :-
    Playing = True

    # 3. Welcoming User :-
    print("Welcome to Guess the Number Game!\n")
    time.sleep(1.0)
    print("First, you have to choose between which numbers you want to play the Game.\n")
    time.sleep(1.0)
    rang1 = int(input("What is the Start Range of Number you want to play : "))
    time.sleep(1.0)
    rang = int(input("What is the End Range of Number you want to play : "))
    time.sleep(1.0)
    chances = (rang-rang1)//40
    no = random.randrange(1, rang)  # Generating a Random Number...
    print("\nLet's Start the Game!")
    time.sleep(1.0)
    print('''
The Computer will generate a Random number between the range of the numbers you have given earlier.
You have to guess any number and enter it.
If the number is greater than the original number, computer will ask you to decrease it.
If it's lesser, it will ask you to increase it.\n
    ''')
    time.sleep(3.0)
    print("You have only ", chances, " chances.\n")
    time.sleep(1.0)
    print("So, Let's Begin!")
    time.sleep(1.0)

    # 4. Main Game Loop :-
    while chances > 0 and Playing:
        guess = int(input("Guess and Enter a Number : "))
        if guess == no:
            Playing = False
            print("Yay! You Guessed it correctly! You won the Game! :)")
            time.sleep(1.0)
            print("You won the Game at ", chances, " chances.")
            time.sleep(1.0)
            break
        elif guess > no:
            if chances != 0:
                print("Decrease the Number please...")
                time.sleep(1.0)
            chances -= 1
            print("You have ", chances, " chances.")
            time.sleep(1.0)
        elif guess < no:
            if chances != 0:
                print("Increase the Number please...")
                time.sleep(1.0)
            chances -= 1
            print("You have ", chances, " chances.")
            time.sleep(1.0)
        else:
            print("Sorry, an Error occurred...")

    if Playing:
        print("Sorry, all your chances are over... You lost the Game... :(")
        time.sleep(1.0)
        print("The number was - ", no)
        time.sleep(1.0)

    print("Thank You For Playing the Game...")
    time.sleep(1.0)

except Exception as e:
    print("Sorry, an Error occurred...")
    time.sleep(1.0)
    print("Error Type :-", e)



