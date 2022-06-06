print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# declaring variables for counting the occurence of true and love
name1_value=0
name2_value=0
true_value=0
love_value=0

#finding the sum of the letters of true in both names
for letter in "true":
    name1_value += name1.lower().count(letter)
    name2_value += name2.lower().count(letter)
true_value = name1_value + name2_value

name1_value=0
name2_value=0
#finding the sum of the letters of love in both names
for letter in "love":
    name1_value += name1.lower().count(letter)
    name2_value += name2.lower().count(letter)
love_value = name1_value + name2_value


score = int(str(true_value)+str(love_value))
# printing out the score
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

print(true_value)
print(love_value)

