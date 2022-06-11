import random
#didn't solve, unclear question
test_seed = int(input("Create a seed number: "))
#changing the value of random module seed
random.seed(test_seed)

random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")