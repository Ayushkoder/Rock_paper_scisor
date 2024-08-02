import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True: 
    # print("pass")  This is to code is run properly or not 
    user_input = input("Type rock/paper/scissors and q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Please write a valid input.") 
        continue

    random_number = random.randint(0, 2)  
    computer_input = options[random_number]    
    print(f"Computer picked: {computer_input}")     

    if user_input == computer_input:
        print("Match has been drawn")
    elif user_input == "rock" and computer_input == "scissors":
        print("You Won")
        user_wins += 1
    elif user_input == "scissors" and computer_input == "paper":     
        print("You Won") 
        user_wins += 1
    elif user_input == "paper" and computer_input == "rock":     
        print("You Won") 
        user_wins += 1     
    else:
        print("Computer won")
        computer_wins += 1

print(f"Final Score - You: {user_wins}, Computer: {computer_wins}")
 
         
         
         
         
         
         