#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

li = []
for num in range(0, nr_letters):
  li.append(random.choice(letters))
#print(li)
l = ''.join(li)
#print(l)

li1 = []
for num in range(0, nr_symbols):
  li1.append(random.choice(symbols))
#print(li1)
s = ''.join(li1)
#print(s)

li2 = []
for num in range(0, nr_numbers):
  li2.append(random.choice(numbers))
#print(li2)
n = ''.join(li2)
#print(n)

password = l + s + n
password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)
print(f"Your password can be {final_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P