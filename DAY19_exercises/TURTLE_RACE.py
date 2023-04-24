# the goal is to make a turtle racing game, you get prompted on whom you will bet on
# the turtles will race in random sequence and who ever reaches the end of the screen wins
# if you chose the correct color, the system will print that you chose the correct answer
import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
# creating the input screen + capturing user bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["blue","purple", "red", "orange", "pink", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
racers = []
game_over = False
winner = ''
# creating and setting the turtles in their positions

for turtle_index in range(0,6):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[turtle_index])
    turtle.pendown()
    racers.append(turtle)

while not game_over:
    for turtle_index in range(0,6):
        racers[turtle_index].forward(random.randint(0,10))
        if racers[turtle_index].xcor() >= 235:
            game_over = True
            winner = colors[turtle_index]
            break

# Compare the user's bet to the winner
if user_bet == winner:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")


screen.exitonclick()