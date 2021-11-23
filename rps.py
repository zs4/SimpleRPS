from random import randint

user_choice = input("Enter your choice: ")

computer_choice = randint(1, 3)

if computer_choice == 1:
    computer_choice = "rock"
    if user_choice == "rock":
        print("Tie, Computer got: " + computer_choice)
    elif user_choice == "paper":
        print("You win, Computer got: " + computer_choice)
    elif user_choice == "scissors":
        print("You lose, Computer got: " + computer_choice)

elif computer_choice == 2:
    computer_choice = "paper"
    if user_choice == "rock":
        print("You lose, Computer got: " + computer_choice)
    elif user_choice == "paper":
        print("Tie, Computer got: " + computer_choice)
    elif user_choice == "scissors":
        print("You win, Computer got: " + computer_choice)

else:
    computer_choice = "scissors"
    if user_choice == "rock":
        print("You win, Computer got: " + computer_choice)
    elif user_choice == "paper":
        print("You lose, Computer got: " + computer_choice)
    elif user_choice == "scissors":
        print("Tie, Computer got: " + computer_choice)
