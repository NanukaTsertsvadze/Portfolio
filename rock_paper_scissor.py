import random

#Choosing random word 
words = ["rock","paper","scissor"]
random_word = random.choice(words)


print("Welcome to Rock, Paper, Scissor Game")
person_points = 0
computer_points = 0

def game():
    global person_points
    global computer_points
    person_choice = input("Please enter your choice(rock,paper,scissor)").lower()
    if person_choice == random_word:
        print("ITS A TIE!")
        print(f"Player :{person_choice}")
        print(f"Computer : {random_word}")
    elif person_choice == "rock" and random_word == "scissor":
        person_points +=1
        print("You win!")
        print(f"Player :{person_choice}")
        print(f"Computer : {random_word}")
        print(f"Player's Score :{person_points}")
        print(f"Computer's Score :{computer_points}")
    elif person_choice =="scissor" and random_word =="paper":
        person_points +=1
        print("You win!")
        print(f"Player :{person_choice}")
        print(f"Computer : {random_word}")
        print(f"Player's Score :{person_points}")
        print(f"Computer's Score :{computer_points}")
    elif person_choice =="paper" and random_word == "rock":
        person_points +=1
        print("You win!")
        print(f"Player :{person_choice}")
        print(f"Computer : {random_word}")
        print(f"Player's Score :{person_points}")
        print(f"Computer's Score :{computer_points}")
    else:
        computer_points+=1
        print("Sorry, You lost")
        print(f"Player :{person_choice}")
        print(f"Computer : {random_word}")
        print(f"Player's Score :{person_points}")
        print(f"Computer's Score :{computer_points}")


#Starting Game
start = input("Do you want to strat Playing ? y for yes, n for no: ").lower()
while True:
    random_word = random.choice(words)
    if start == "y":
        game()
    elif start == "n":
        print("It is totally fine. have a nice day.")
        break
    else:
        print("Please write y or n.")
