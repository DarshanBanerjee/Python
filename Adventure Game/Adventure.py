# 1. Importing Modules :-
import time

# 2. Asking Name and Age :-
name = input("What is your Name : ")
age = int(input("What is your Age : "))

# 3. Defining Data :-
Playing = True
GameStatus = None

# 4. Defining Functions to make Task easier :-
def hm(x):
    global health
    health -= x
    time.sleep(1.0)
    print("You lost ", x, " Health.")
    time.sleep(1.0)
    print("You have ", health, " Health now.")
    time.sleep(1.0)

def hp(y):
    global health
    health += y
    time.sleep(1.0)
    print("You gained ", y, " Health.")
    time.sleep(1.0)
    print("You have ", health, " Health now.")
    time.sleep(1.0)

def error():
    time.sleep(1.0)
    print("Sorry, Not received Correct Input... (PS - Make sure to Turn-off your Caps-Lock.)")
    time.sleep(1.0)


# 5. Checking if the Player is Eligible to Play :-
if age > 10:
    # 6. Welcoming User :-
    print("Hey ", name, ", Welcome to this Adventure Game.")
    time.sleep(1.0)
    print("You are out in an expedition.")
    time.sleep(1.0)
    print("You will be Asked a Few Questions for your Moves. Your options will be given in brackets after Every Question.")
    time.sleep(1.0)
    print("You will be Having some 10 Health at the Starting.")
    time.sleep(1.0)
    print("If you make a Wrong move, You will lose Health.")
    time.sleep(1.0)
    print("If you lose all your Health, then you will lose the Game.")
    time.sleep(1.0)
    print("However, you can Replay if you want.")
    time.sleep(1.0)

    # 7. Main Game Loop :-
    while Playing:
        print()
        health = 10
        print("You are having 10 Health.")
        time.sleep(1.5)
        weapon = input("Choose a Weapon/Tool (sword/knife/net/shield/club/rope/gun) : ")
        if weapon != "sword" and weapon != "knife" and weapon != "net" and weapon != "shield" and weapon != "club" and weapon != "rope" and weapon != "gun":
            error()
            weapon = input("Choose a Weapon/Tool (sword/knife/net/shield/club/rope) : ")
        if weapon != "sword" and weapon != "knife" and weapon != "net" and weapon != "shield" and weapon != "club" and weapon != "rope" and weapon != "gun":
            error()
            break
        direction = input("Which Direction do you want to go? (left/right) : ")
        if direction == "left":
            print("You see a Lake.")
            time.sleep(1.0)
            print("But it's too Large...")
            time.sleep(1.0)
            lake = input("Do you want to Swim across it or go Around it? (swim/around) : ")
            time.sleep(1.0)
            if lake == "swim" and weapon == "net":
                print("Some Piranhas attacked you but you were saved as you used your Net to catch them...")
            elif lake == "swim" and weapon != "net":
                print("Oh! No! You were attacked by Piranhas...")
                hm(4)
                if health <= 0:
                    Playing = False
                    GameStatus = "Lose"
                    break
            elif lake == "around":
                pass
            else:
                error()
                break
            time.sleep(1.0)
            print("You walked around and saw a River and a House...")
            time.sleep(1.0)
            rh = input("Where do you want to go? (river/house) : ")
            time.sleep(1.0)
            if rh == "river":
                if weapon == "rope":
                    print("You were falling down the River... But you are saved because you threw the Rope at the other end of the river and were saved...")
                    time.sleep(1.0)
                    print("You walked along and saw a Forest...")
                    time.sleep(1.0)
                    print("You entered into the Forest.")
                    time.sleep(1.0)
                    print("Roaaarrrrr!")
                    time.sleep(1.0)
                    print("Oh! What's That!")
                    time.sleep(1.0)
                    print("Oh My God! You were attacked by a Tiger...")
                    time.sleep(1.0)
                    print("The Tiger killed you and you died...")
                    time.sleep(1.0)
                    GameStatus = "Lose"


                else:
                    print("You fell into the River and died...")
                    time.sleep(1.0)
                    GameStatus = "Lose"

            elif rh == "house":
                if weapon == "shield":
                    print("Oh! No! The House you went was of a Murderer... But Luckily, you were saved as you had the Shield...")
                    time.sleep(1.0)
                    print("Still,", end=' ')
                    hm(2)
                    if health <= 0:
                        Playing = False
                        GameStatus = "Lose"
                        break
                    print("You ran away from the House...")
                    time.sleep(1.0)

                elif weapon == "knife":
                    print("Oh! No! The House was of a Murderer... You killed him with your Knife, but before that, you were severely injured...")
                    hm(7)
                    if health <= 0:
                        Playing = False
                        GameStatus = "Lose"
                        break
                    house = input("Do you want to go further inside the House or run away from the house? (inside/away) : ")
                    if house == "inside":
                        time.sleep(1.0)
                        print("Oh! You walked inside the House and found lot's of Foods and Drinks. You ate and drank them...")
                        hp(4)
                    elif house == "away":
                        pass
                    else:
                        error()
                        break
                    time.sleep(1.0)
                    print("You now see a City and a Range of Mountains...")
                    time.sleep(1.0)
                    cm = input("Where do you want to go? (city/mountain) : ")
                    time.sleep(1.0)
                    if cm == "city":
                        print("You went to the City but were not Welcome by the people living there...")
                        time.sleep(1.0)
                        print("They thought you as an enemy and attacked you...")
                        time.sleep(1.0)
                        print("You tried to tell them that you are a friend but they didn't listen to you...")
                        hm(5)
                        if health <= 0:
                            Playing = False
                            GameStatus = "Lose"
                            break
                        print("But you managed to stay with them at last...")
                        time.sleep(1.0)
                        print("Though your expedition was unsuccessful, but you still WON!")
                        GameStatus = "Win"


                    elif cm == "mountain":
                        if weapon == "rope":
                            print(
                                "You are Lucky! You were about to fall down from the slope, but to managed to survive as you had the rope with you...")
                            time.sleep(1.0)
                            print("Still, ", end='')
                            hm(2)
                            if health <= 0:
                                Playing = False
                                GameStatus = "Lose"
                                break
                            print("You walked along and... Hey! What's that!")
                            time.sleep(1.0)
                            print("Oh God! I can't believe it!")
                            time.sleep(1.0)
                            print("It's the CITY OF GOLD!")
                            time.sleep(1.0)
                            print("Your expedition was successful...")
                            GameStatus = "Win"

                        else:
                            print("You fell down from the slope and died...")
                            GameStatus = "Lose"

                elif weapon == "sword":
                    time.sleep(1.0)
                    print("Oh! No! The House was of a Murderer... You killed him with your Sword, but before that, you were injured a little...")
                    hm(4)
                    if health <= 0:
                        Playing = False
                        GameStatus = "Lose"
                        break
                    house = input("Do you want to go further inside the House or run away from the house? (inside/away) : ")
                    if house == "inside":
                        time.sleep(1.0)
                        print("Oh! You walked inside the House and found lot's of Foods and Drinks. You ate and drank them...")
                        hp(4)
                    elif house == "away":
                        pass
                    else:
                        break
                    time.sleep(1.0)
                    print("You now see a City and a Range of Mountains...")
                    time.sleep(1.0)
                    cm = input("Where do you want to go? (city/mountain) : ")
                    time.sleep(1.0)
                    if cm == "city":
                        print("You went to the City but were not Welcome by the people living there...")
                        time.sleep(1.0)
                        print("They thought you as an enemy and attacked you...")
                        time.sleep(1.0)
                        print("You tried to tell them that you are a friend but they didn't listen to you...")
                        hm(5)
                        if health <= 0:
                            Playing = False
                            GameStatus = "Lose"
                            break
                        print("But you managed to stay with them at last...")
                        time.sleep(1.0)
                        print("Though your expedition was unsuccessful, but you still WON!")
                        GameStatus = "Win"


                    elif cm == "mountain":
                        if weapon == "rope":
                            print(
                                "You are Lucky! You were about to fall down from the slope, but to managed to survive as you had the rope with you...")
                            time.sleep(1.0)
                            print("Still, ", end='')
                            hm(2)
                            if health <= 0:
                                Playing = False
                                GameStatus = "Lose"
                                break
                            print("You walked along and... Hey! What's that!")
                            time.sleep(1.0)
                            print("Oh God! I can't believe it!")
                            time.sleep(1.0)
                            print("It's the CITY OF GOLD!")
                            time.sleep(1.0)
                            print("Your expedition was successful...")
                            GameStatus = "Win"

                        else:
                            print("You fell down from the slope and died...")
                            GameStatus = "Lose"

                else:
                    print("Oh! No! The House was of a Murderer... He killed you and you Died...")
                    GameStatus = "Lose"


            else:
                error()
                break


        elif direction == "right":
            print("You walk forward and see a Forest and Desert...")
            time.sleep(1.0)
            fd = input("Where do you want to go? (forest/desert) : ")
            time.sleep(1.0)
            if fd == "desert":
                print("You walked across the Desert...")
                time.sleep(1.0)
                print("It's now been hours and you haven't ate or drank something.")
                time.sleep(1.0)
                print("You are feeling very weak...")
                hm(3)
                if health <= 0:
                    Playing = False
                    GameStatus = "Lose"
                    break
                print("Oh! What's that?")
                time.sleep(1.0)
                print("Its a small airplane!")
                time.sleep(1.0)
                if weapon == "gun":
                    print("You fired with your gun in the air and the pilot saw you...")
                    time.sleep(1.0)
                    print("He took you home and cured you...")
                    time.sleep(1.0)
                    print("Though your Expedition was Unsuccessful, But you WON!")
                    time.sleep(1.0)
                    GameStatus = "Win"
                else:
                    print("But you have nothing to do...")
                    time.sleep(1.0)
                    print("The airplane didn't see you and went away...")
                    time.sleep(1.0)
                    print("You fainted and died...")
                    time.sleep(1.0)
                    GameStatus = "Lose"
                    time.sleep(1.0)

            elif fd == "forest":
                print("You entered into the Forest.")
                time.sleep(1.0)
                print("You are walking for hours...")
                time.sleep(1.0)
                print("Roaaarrrrr!")
                time.sleep(1.0)
                print("Oh! What's That!")
                time.sleep(1.0)
                print("Ooh! It was a Tiger!! But Thank God... It ran away... ")
                time.sleep(1.0)
                print("You again walked for a while...")
                time.sleep(1.0)
                print("Oh! The path is covered with Thorny bushes...")
                time.sleep(1.0)
                if weapon == "knife" or weapon == "sword":
                    print("But don't worry, you have your ", weapon, "...")
                    time.sleep(1.0)
                    print("You just cut the bushes and walked along...")
                    time.sleep(1.0)

                else:
                    print("You were hurt because of the bushes and ", end='')
                    hm(2)
                    if health <= 0:
                        Playing = False
                        GameStatus = "Lose"
                        break
                    print("It's Getting Dark...")
                    time.sleep(1.0)
                    print("You are very Hungry and also need shelter...")
                    time.sleep(1.0)
                hs = input("What do you want? (food/shelter) : ")
                if hs == "food":
                    time.sleep(1.0)
                    print("You walked forward and saw a Mango Tree...")
                    time.sleep(1.0)
                    print("You were about to eat the sweet Mangoes but a group of Orangutans came and attacked you...")
                    time.sleep(1.0)
                    print("You somehow managed to survive, but ", end='')
                    hm(5)
                    if health <= 0:
                        Playing = False
                        GameStatus = "Lose"
                        break

                elif hs == "shelter":
                    pass

                else:
                    error()
                    break

                print("You walked around and saw a Cave...")
                time.sleep(1.0)
                print("You entered into the Cave...")
                time.sleep(1.0)
                print("You saw a room!")
                time.sleep(1.0)
                print("You entered into the Room.")
                time.sleep(1.0)
                print("Oh! What's That!!")
                time.sleep(1.0)
                print("I can't believe it!!")
                time.sleep(1.0)
                print("It's a Treasure!!!!")
                time.sleep(1.0)
                print("Your Expedition is a Success...")
                GameStatus = "Win"

            else:
                error()
                break

        else:
            error()
            break

        if GameStatus == "Win":
            time.sleep(1.0)
            print("Hooray! You won the Game!")
            time.sleep(1.0)
            again = input("Do you want to Play Again? (yes/no) : ")
            if again == "yes":
                pass
            elif again == "no":
                Playing = False
                GameStatus = None
            else:
                time.sleep(1.0)
                print("Sorry, Something Wrong Happened...")
        elif GameStatus == "Lose":
            time.sleep(1.0)
            print("Oops! You Lost the Game!")
            time.sleep(1.0)
            again = input("Do you want to Play Again? (yes/no) : ")
            if again == "yes":
                pass
            elif again == "no":
                Playing = False
                GameStatus = None
            else:
                time.sleep(1.0)
                print("Sorry, Something Wrong Happened...")
                Playing = False
                break

    if GameStatus == "Win":
        time.sleep(1.0)
        print("Hooray! You won the Game!")
        Playing = False
        GameStatus = None

    elif GameStatus == "Lose":
        time.sleep(1.0)
        print("Oops! You Lost the Game!")
        Playing = False
        GameStatus = None

    else:
        pass

else:
    print("Sorry, You are not OLD enough to Play this Game...")

print("Thank You!")