# Create Etch a Sketch game
# here are the commands:
# w: move forward
# S: move backward
# D: move clockwise
# A: move counter-clockwise
# C: clear sketch

from turtle import Turtle, Screen

# creating turtle and screen
tim = Turtle()
screen = Screen()

# setting the movement for the turtle

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def move_clockwise():
    tim.right(10)

def move_counter_clockwise():
    tim.left(10)

# clearing the screen
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# listening to the movements
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clear)
# exit the program when clicked
screen.exitonclick()
