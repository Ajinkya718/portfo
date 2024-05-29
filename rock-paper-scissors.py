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

#Write your code below this line 👇
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print("\nYou chose", end = " ")
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("the wrong number. Whereas,\n")

print("Computer chose")
choice1 = random.randint(0,2)
if choice1 == 0:
  print(rock)
elif choice1 == 1:
  print(paper)
elif choice1 == 2:
  print(scissors)

if choice == 0 and choice1 == 1 or choice == 1 and choice1 == 2 or choice == 2 and choice1 == 0:
  print("You lose :(")
elif choice == 1 and choice1 == 0 or choice == 2 and choice1 == 1 or choice == 0 and choice1 == 2:
  print("You win :)")
elif choice == 1 and choice1 == 1 or choice == 2 and choice1 == 2 or choice == 0 and choice1 == 0:
  print("It\'s a draw :|")
else:
  print("You lose anyways :(")