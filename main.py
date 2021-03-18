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

map = [rock, paper, scissors]

choice = int(input("Which do you choose? Type 0 for rock, 1 for Paper and 2 for Scissors: "))
#print(map[choice])

# computer choice
comp_choice = random.randint(0,2)
#print(comp_choice)

rock_c = int(0)
paper_c = int(1)
scissors_c = int(2) 

#rock wins against scissors
#scissors wins agains paper
#paper wins against rock

if choice == rock_c:
    if comp_choice == paper_c:
        print(f"You choose \n{map[choice]} \n\n Computer choose \n{map[comp_choice]} \n\n Computer Wins")
    elif comp_choice == scissors_c:
        print(f"You choose \n{map[choice]} \n\n Computer choose \n{map[comp_choice]} \n\n You win")
    else:
        print(f"You choose \n{map[choice]} \n\n Computer choose \n{map[comp_choice]} \n\n Its a draw Replay")
elif choice == paper_c:
    if comp_choice == rock_c:
        print(f"You choose \n{map[choice]} \n\n Computer choose \n{map[comp_choice]} \n\n You win")
    elif comp_choice == scissors_c:
        print(f"You choose \n{map[choice]} \n\n Computer choose \n{map[comp_choice]} \n\n Computer Wins")
    else:
        print(f"You choose \n{map[choice]} \n\n Computer choose \n{map[comp_choice]} \n\n Its a draw Replay")
elif choice == scissors_c:
    if comp_choice == paper_c:
        print(f"You choose \n{map[choice]} \n\n Computer choose \n{map[comp_choice]} \n\n You win")
    elif comp_choice == rock_c:
        print(f"You choose \n{map[choice]} \n\n Computer choose \n{map[comp_choice]} \n\n Computer Wins")
    else:
        print(f"You choose \n{map[choice]} \n\n Computer choose \n{map[comp_choice]} \n\n Its a draw Replay")
else:
    print(f"You choose an invalid number, You lose!")

