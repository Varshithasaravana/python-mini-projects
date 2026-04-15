import random
print("Welcome To Rock Paper Scissors Game")
options=["rock","paper","scissors"]
user_wins=0
computer_wins=0
while True:
    user_pick=input("Type rock/paper/scissors or q to quit:").lower()
    if user_pick=="q":
        break
    if user_pick not in options:
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("computer has picked",computer_pick)
    if user_pick==computer_pick:
        print("Same choice no result")
    if user_pick=="rock" and computer_pick=="scissors":
        print("You won!")
        user_wins += 1
    elif user_pick=="paper" and computer_pick=="rock":
        print("You won!")
        user_wins += 1
    elif user_pick=="scissors" and computer_pick=="paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost")
        computer_wins += 1
print("You won",user_wins,"times")
print("computer won",computer_wins,"times")
if user_wins>computer_wins:
    print("You won the game")
elif user_wins==computer_wins:
    print("The result is draw")
else:
    print("computer won the game")
print("Thank you !")
