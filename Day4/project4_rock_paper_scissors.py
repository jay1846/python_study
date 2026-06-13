import random

print("Welcome to rock - paper - scissors game")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

users_choice = int(input("What is your choice? 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if users_choice < 0 or users_choice > 2:
    print("Invalid number. You lose by default!")
else:
    computer_choice = random.randint(0, 2)
    
    print("\n[You Chose]")
    print(game_images[users_choice])
    
    print("[Computer Chose]")
    print(game_images[computer_choice])

    if users_choice == computer_choice:
        print("Draw!\n")
    elif (users_choice == 0 and computer_choice == 2) or \
         (users_choice == 1 and computer_choice == 0) or \
         (users_choice == 2 and computer_choice == 1):
        print("You Win!\n")
    else:
        print("You Lose!\n")