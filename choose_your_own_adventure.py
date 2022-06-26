name = input("Type your username: ")
print("Welcome", name, "to this adventure. Have fun!!")

answer = input("You are now in the Summoners Rift! Which lane do you want to go? " 
"Type TOP or JUNGLE or MID or ADC or SUPPORT: ").lower()

if answer == "top":
    answer = input("You are now in the top lane. Do you want to play ORNN or KENNEN? ").lower()

    if answer == "ornn":
        print("As you probably know top tanks are broken. In this game you dealt twice more damage " 
        "and you tanked twice more than you would have with Kennen. Anyways, you won!!")
    elif answer == "kennen":
        print("You picked a bad champion with which you dealt no damage and got reported. " 
        "Of course you lost;")
    else:
        print("Not a valid option. Try again...")

elif answer == "jungle":
    answer = input("You are now in the jungle playing with Master Yi. " 
    "What do you want to do FARM or GANK? ").lower()

    if answer == "farm":
        print("Even though your teammates blamed you during the early and mid game, you "
        "hit your powerspike by having 3 items and got a Penta kill at 35 minutes. You won!!")
    elif answer == "gank":
        print("You chose to gank but even though your teammates didn't blame you in the early mid "
        "game you did't get much with the ganks and got weak. Unlucky, you lost.")
    else:
        print("Not a valid option. Try again...")

elif answer == "mid":
    answer = input("You are now in the mid lane. Do you want to play ASSASSIN or NO? ").lower()

    if answer == "assassin":
        print("You really didn't do much this game but you got fed anyways because assassin " 
        "is broken. You won!!")
    elif answer == "no":
        answer = input("Do you want to ROAM or FARM? ").lower()
        if answer == "farm":
            print("You aren't playing assassin plus you are not roaming, I mean even though "
            "mid is that broken, if you keep on playing like that you are going to lose "
            "all your games. You lost.")
        elif answer == "roam":
            print("Even though you chose to not play assassin, you made the right call to roam "
            "because you got yourself, your top laner and jungler ahead. You won!!")
        else:
            print("Not a valid option. Try again...")
    else:
        print("Not a valid option. Try again...")

elif answer == "adc":
    print("You really chose adc?! Of course, no need to go further, you lost.")

elif answer == "support":
    answer = input("You are now playing support. Do you want to ROAM or NO? ").lower()

    if answer == "roam":
        print("You chose to roam, which means you let your adc by his own (he inted) and played for "
        "the other lanes. Honestly you did the right thing because even if the enemy adc is 8/0 he "
        "can't do much againt your 1/0 mid laner. You won!!")
    elif answer == "no":
        print("You chose to play with your adc he got fed with 6 kills in the early game but once " 
        "the enemy mid laner roamed bot, he killed your adc getting a huge bounty and got " 
        "fed. You lost.")
    else:
        print("Not a valid option. Try again...")

else:
    print("Not a valid option. Try again...")

print("Thank you", name ,"for giving LoL a shot even though it is a bad game!")