#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
full=[]
for n in range (0,nr_letters):
 letters_random = random.randint(0,len(letters)-1)
 full.append(letters[letters_random])

for n in range (0,nr_symbols):
 symbols_random = random.randint(0,len(symbols)-1)
 full.append(symbols[symbols_random])

for n in range (0,nr_numbers):
 numbers_random = random.randint(0,len(numbers)-1)
 full.append(numbers[numbers_random])
# password =[letters,numbers,symbols]
x = ""
for n in full :
  x += n
print(x)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(full)
print(full)
e = ''
for n in full :
  e += n
print(e)
# full_random = [0]*len(full)
# print(full_random)
# #print(full)
# for x in full:
#   print(x)
#   p =  random.randint(0,len(full)-1)
#   full_random[p] = x
# print(full_random)