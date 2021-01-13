import random
choices=["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player=False
cpu_score=0
player_score=0
while True:
    player=input("rock paper  scissor").capitalize()
    if player==computer:
        print('tie')
    elif player == 'Rock':
        if computer == 'Paper':
            print("u lose ", computer, 'covers',player)
            cpu_score+=1
        else:
            print("u win ", player, 'smashes', computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("u lose", computer, "cut", player)
            cpu_score+=1
        else:
            print("u win", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("u lose", computer, "smashes", player)
            cpu_score+=1
        else:
            print("u win", player, "cut", computer)
            player_score+=1
    elif player=='E':
        print("---------------------------")
        print("final scores")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break
    else:
        print("that's not a valid play. check ur spelling")
    computer= random.choice(choices)