#RPS game

import random
rps=["rock","paper","scissors"]
result={("rock","paper"):False,("rock","scissors"):True,
        ("paper","scissors"):False,("paper","rock"):True,
        ("scissors","rock"):False,("scissors","paper"):True}

while True:
    player=input("rock/paper/scissors : ")
    if player=="":
        break
    computer=random.choice(rps)

    print("player --->",player)
    print("computer --->",computer)

    #result
    if player==computer:
        print("It's a tie!")
    elif result[(player,computer)]:
        print("You won! :)")
    else:
        print("You lost! :(")

    print()
