import random
rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """
scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
game_images = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(game_images[user_input])
pc_input = random.randint(0,2)
print("Computer chose:\n"+game_images[pc_input])

if user_input == 0 and pc_input == 0:
    print("It's a draw!")
elif user_input == 0 and pc_input == 1:
    print("Computer wins!")
elif user_input == 0 and pc_input == 2:
    print("You win!")
elif user_input == 1 and pc_input == 1:
    print("It's a draw!")
elif user_input == 1 and pc_input == 2:
    print("Computer wins!")
elif user_input == 1 and pc_input == 0:
    print("You win!")
elif user_input == 2 and pc_input == 2:
    print("It's a draw!")
elif user_input == 2 and pc_input == 0:
    print("Computer wins!")
elif user_input == 2 and pc_input == 1:
    print("You win!")