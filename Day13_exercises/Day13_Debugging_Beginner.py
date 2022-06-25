#  ___    ___       _____  _   _  ___       ___    _   _  ___
# (  _`\ (  _`\    (_   _)( ) ( )(  _`\    (  _`\ ( ) ( )(  _`\
# | | ) || (_(_)     | |  | |_| || (_(_)   | (_) )| | | || ( (_)
# | | | )|  _)_      | |  |  _  ||  _)_    |  _ <'| | | || |___
# | |_) || (_( )     | |  | | | || (_( )   | (_) )| (_) || (_, )
# (____/'(____/'     (_)  (_) (_)(____/'   (____/'(_____)(____/'
#
############################ DEBUGGING ############################

# 1. Describe the problem
def my_function():
    for i in range(1,20):
        if i == 20:
            print("You got it!")
my_function()
# Description
# our function does not have parameters so we do not need to pass arguments, no error there
# the for loop assigns the values between 1-20 to i
# if i equals 20 then we print a message
# the error is in the range, first number is included while the last number is excluded
# solution: change range to range(1,21) or range(21)

print("Solution for 1st problem ↓")

solution = '''def my_function():
    for i in range(21):
        if i == 20:
            print("You got it!")
my_function()'''
print(solution)


print("\n\n\n")

#-----------------------------------------------------------------------------------------------------------------------

# 2. Reproduce the Bug ↓
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1,6)
# print(dice_imgs[dice_num])

problem = '''from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1,6)
print(dice_imgs[dice_num])'''
print(problem+"\n")

# in this example we need to recreate this error in a way that it always happens
# the error we have is in dice_num which sometimes create out of boundary num
# to recreate it → make the random number range out of dice_img len
solution = '''to reproduce the error ↓
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(6,10)
print(dice_imgs[dice_num])'''
print(solution+"\n\n\n")

# to fix the error ↓
solution = '''to fix the error ↓
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0,len(dice_imgs)-1)
print(dice_imgs[dice_num])'''
print(solution+"\n\n\n")

#-----------------------------------------------------------------------------------------------------------------------

# 3. Play Computer
problem = '''year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")'''

print(problem+"\n\n\n")

# think as a computer

# first we get the year from the user, after that we compare the year inside if blocks
# if year is between 1980 and 1994 the person is a millenial
# if they are boren after 1994 they are gen z
# we have an error if the person is born on 1994, because 1994 is not bigger or smaller than 1994
# so the year will not be classified in any of the categories
# in order not to skip 1994 we need to make one of them either greater or equal, or smaller or equal

solution = '''this way 1994 is not skipped ↓
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")'''

print(solution+"\n\n\n")
#-----------------------------------------------------------------------------------------------------------------------

# 4. Fix the Errors
problem = ''' problem ↓
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}")'''
print(problem+"\n\n")

solution = ''' solution ↓
age = int(input("How old are you?"))
if age >= 18:
    print(f"You can drive at age {age}")
'''
print(solution+"\n\n\n")
#-----------------------------------------------------------------------------------------------------------------------

# 5. Print is Your Friend
problem = '''The problem is what number we give we get 0 ↓
pages = 0
word_per_page = 0
pages = int(input("Number of pages:"))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
'''
print(problem+"\n\n\n")

debugging = ''' use print to debug the code ↓
pages = 0
word_per_page = 0
pages = int(input("Number of pages:"))
print(f"Pages = {pages}")
word_per_page == int(input("Number of words per page: "))
print(f"Words per page = {word_per_page}")
total_words = pages * word_per_page
print(total_words)
'''
print(debugging+"\n\n\n")


debugging = ''' the proble is in line 142 we used '==' instead of '=' ↓
pages = 0
word_per_page = 0
pages = int(input("Number of pages:"))
print(f"Pages = {pages}")
word_per_page = int(input("Number of words per page: "))
print(f"Words per page = {word_per_page}")
total_words = pages * word_per_page
print(total_words)
'''
print(solution+"\n\n\n")
#-----------------------------------------------------------------------------------------------------------------------

# 6. Use a Debugger

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)
mutate([1,2,3,5,8,13])