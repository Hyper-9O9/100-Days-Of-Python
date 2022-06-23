import random
# a simple guessing game
# i haven't made it dynamic, at least for now
print(r''''                                                                                                                                                               
  ,ad8888ba,                                                  88                                  ,ad8888ba,                                               88  
 d8"'    `"8b                                                 ""                                 d8"'    `"8b                                              88  
d8'                                                                                             d8'                                                        88  
88             88       88   ,adPPYba,  ,adPPYba,  ,adPPYba,  88  8b,dPPYba,    ,adPPYb,d8      88             ,adPPYYba,  88,dPYba,,adPYba,    ,adPPYba,  88  
88      88888  88       88  a8P_____88  I8[    ""  I8[    ""  88  88P'   `"8a  a8"    `Y88      88      88888  ""     `Y8  88P'   "88"    "8a  a8P_____88  88  
Y8,        88  88       88  8PP"""""""   `"Y8ba,    `"Y8ba,   88  88       88  8b       88      Y8,        88  ,adPPPPP88  88      88      88  8PP"""""""  ""  
 Y8a.    .a88  "8a,   ,a88  "8b,   ,aa  aa    ]8I  aa    ]8I  88  88       88  "8a,   ,d88       Y8a.    .a88  88,    ,88  88      88      88  "8b,   ,aa  aa  
  `"Y88888P"    `"YbbdP'Y8   `"Ybbd8"'  `"YbbdP"'  `"YbbdP"'  88  88       88   `"YbbdP"Y8        `"Y88888P"   `"8bbdP"Y8  88      88      88   `"Ybbd8"'  88  
                                                                                aa,    ,88                                                                     
                                                                                 "Y8bbdP"                                                                      ''')
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty/ Type 'easy' or 'hard': ").lower()
chosen_number = random.randint(1,100)

def guessing_game(game_difficulty, answer):
    """"function to start the game"""
    if game_difficulty == "easy":
        attempts = 10
        in_game = False
        while not in_game:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))

            if guess < answer:
                print("Too low.")
                attempts -= 1
            elif guess > answer:
                print("Too high.")
                attempts -= 1
            else:
                print(f"Congratulations your guess is correct!! answer = {answer}. ")
                in_game = True
            if attempts == 0:
                print(f"Unfortunately you have reached the limit you lose :(\n",
                      f"Correct answer = {answer}")
                in_game = True

    elif game_difficulty == "hard":
        attempts = 5
        in_game = False
        while not in_game:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))

            if guess < answer:
                print("Too low.")
                attempts -= 1
            elif guess > answer:
                print("Too high.")
                attempts -= 1
            else:
                print(f"Congratulations your guess is correct!! answer = {answer}. ")
                in_game = True
            if attempts == 0:
                print(f"Unfortunately you have reached the limit you lose :(\n"+
                      f"Correct answer = {answer}")
                in_game = True
    else:
        print("Sorry you chose an option that is not in the game")


guessing_game(game_difficulty= difficulty, answer= chosen_number)