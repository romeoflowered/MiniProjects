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
game = [rock, paper, scissors]

int_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You choice:\n", game[int_choice])

ii = random.randint(0, 2)
print("Computer's choice:\n", game[ii])

if int_choice >= 3 or int_choice < 0:
    print("You typed an invalid number, you lose!")
elif int_choice == 0 and ii == 2:
    print("You win!")
elif ii == 0 and int_choice == 2:
    print("You lose")
elif ii > int_choice:
    print("You lose")
elif int_choice > ii:
    print("You win!")
elif ii == int_choice:
    print("It's a draw")