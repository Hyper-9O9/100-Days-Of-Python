# creating random password generator
import random

print("Welcome to the PyPassword Generator!")

password_letters = int(input("How many letters would you like in your password?\n"))
password_symbols = int(input("How many symbols would you like?\n"))
password_numbers = int(input("How many numbers would you like?\n"))
password_length = password_letters + password_symbols + password_numbers
letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols_list = ["!", "@", "#", "$", "%", "^", "&"]
numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

letters_counter = 0
numbers_counter = 0
symbols_counter = 0
password = ""
for i in range(password_length):
    picker = random.randint(0,2)

    if picker == 0:
        if letters_counter < password_letters:
            password += letters_list[random.randint(0,len(letters_list)-1)]
            letters_counter += 1
        else:
            if numbers_counter < password_numbers:
                password += numbers_list[random.randint(0, len(numbers_list) - 1)]
                numbers_counter += 1
            if symbols_counter < password_symbols:
                password += symbols_list[random.randint(0,len(symbols_list)-1)]
                symbols_counter += 1
    if picker == 1:
        if numbers_counter < password_numbers:
            password += numbers_list[random.randint(0, len(numbers_list) - 1)]
            numbers_counter += 1
        else:
            if symbols_counter < password_symbols:
                password += symbols_list[random.randint(0,len(symbols_list)-1)]
                symbols_counter += 1
            if letters_counter < password_letters:
                password += letters_list[random.randint(0, len(letters_list) - 1)]
                letters_counter += 1
    if picker == 2:
        if symbols_counter < password_symbols:
            password += symbols_list[random.randint(0, len(symbols_list) - 1)]
            symbols_counter += 1
        else:
            if letters_counter < password_letters:
                password += letters_list[random.randint(0, len(letters_list) - 1)]
                letters_counter += 1
            if numbers_counter < password_numbers:
                password += numbers_list[random.randint(0, len(numbers_list) - 1)]
                numbers_counter += 1






print(f"Here is your password: {password}")