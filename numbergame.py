import random
import sys
def checkwin(attempts):
  guess_is_right = False
  while not guess_is_right:
    guess = int(input("Make a guess: "))
    if attempts == 1:
      sys.exit(f"You lose! The number was {number}.")
    if guess < number:
      print("Too low.")
      print("Guess again.")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess > number:
      print("Too high.")
      print("Guess again.")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
    else:
      print("Correct! You win!")
      guess_is_right = True
      
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 101)
print(f"Psst! The number is {number}.")
game_on = True

while game_on:
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == 'easy':
        game_on = False
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")
        checkwin(attempts)
    elif difficulty_level == 'hard':
        game_on = False
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")
        checkwin(attempts)
    else:
        print("Please choose the appropriate option.")