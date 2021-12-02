import random

user_wins=0
computer_wins=0

options=["rock","paper","scissors"]

while True:
    user_input=input("Enter rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in  options:
        continue

    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("Computer picked",computer_pick)

    if user_input == "rock" and computer_pick=="scissors":
        print("user won !!")
        user_wins+=1
   

    elif user_input == "paper" and computer_pick=="rock":
        print("user won !!")
        user_wins+=1
   

    elif user_input == "scissors" and computer_pick=="paper":
        print("user won !!")
        user_wins+=1
    else:
        print("Computer wins !!")
        computer_wins+=1
    print("User won ",user_wins," times!!")
    print("Computer won ",computer_wins," times!!")
    print("See you again!!")