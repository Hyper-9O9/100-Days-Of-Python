import random
# splitting bill among  a group of people
test_seed = input("Create a seed number: ")
random.seed(test_seed)

nameAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = nameAsCSV.split(", ")

random_picker = random.randint(0,len(names)-1)

print(f"The person who has to pay the bill is {names[random_picker]} !!!!")
