import random
rock='''  
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)

         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("what do you chose? type 0 for rock,1 for paper,2 for scissors"))
if user_choice >=0 and user_choice <=2:
    print("your choice:")
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("computer_choice:")
print(game_images[computer_choice])
if user_choice >=3 and user_choice < 0:
    print("you have entered invalid number")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif user_choice ==1 and computer_choice == 0:
    print("you lose")
elif user_choice ==2 and computer_choice == 1:
    print("you lose")
elif user_choice ==1 and computer_choice == 2:
    print("you win")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice == computer_choice:
    print("Its a tie")



