import random

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
res = [rock, paper, scissors]
ur_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print(f"You chose {res[ur_choice]}")
comp_choice = random.randint(0, (len(res)-1))
print(f"Computer chose {res[comp_choice]}")
if ur_choice < 0 or ur_choice > 2:
    print("You typed an invalid number. You lose!")
elif ur_choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and ur_choice == 2:
    print("You lose!")
elif comp_choice > ur_choice:
    print("You lose!")
elif ur_choice > comp_choice:
    print("You win!")
elif comp_choice == ur_choice:
    print("It's a draw!")

