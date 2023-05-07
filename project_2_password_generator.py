import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

print('Welcome to Password Generator')

letter_length = int(input("How many letters you want in your password?\n:"))
symbols_length = int(input("How many letters you want in your password?\n:"))
numbers_length = int(input("How many letters you want in your password?\n:"))

password_list = []

for i in range(1, letter_length+1):
    char = random.choice(letters)
    password_list += char

for i in range(1, symbols_length+1):
    char = random.choice(symbol)
    password_list += char

for i in range(1, numbers_length+1):
    char = random.choice(numbers)
    password_list += char

password = random.shuffle(password_list)
password = ''

for i in password_list:
    password += i
print(password)