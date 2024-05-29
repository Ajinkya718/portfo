print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("\nTo play this game, you need to type your choices. Be careful with your responses as the treasure might disappear. Let's begin!")
option = input("\nThere are two ways to get to the treasure. A left or a right. Which way you want to choose?\n")
choice = option.lower()

if choice == "left":
  option1 = input("\nYou have taken a left and have come across a river. You can either wait for a boat or swim to reach to the other side. Wait or swim?\n")
  choice1 = option1.lower()
  if choice1 == "wait":
    option2 = input("\nYou decided to wait and now you're on a boat. You have reached the island where the treasure is present, but you see three doors with colors red, blue and yellow. Which color door you wish to choose?\n")
    choice2 = option2.lower()
    if choice2 == "red":
      print("\nYou've chosen the red door and have been consumed by the fire inside. Game Over!")
    elif choice2 == "blue":
      print("\nYou've chosen the blue door and it's full of monsters. Game Over!")
    elif choice2 == "yellow":
      print("\nYou've chosen the yellow door and have found the treasure! Congratulations you win!")
    else:
      print("\nUh oh! You tried to act smart by choosing the wrong option and now the treasure is gone. Game Over!")
  else:
    print("\nYou decided to swim and have been devoured by sharks. Game Over!")
else:
  print("\nYou took a right and fell in a ditch. Game Over!")


