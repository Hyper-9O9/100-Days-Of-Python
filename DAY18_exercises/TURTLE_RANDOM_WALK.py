from turtle import *
from random import choice
# defining the tools
turtle = Turtle()
screen = Screen()
# customizing the turtle
turtle.shape("turtle")
turtle.color("DarkTurquoise")

# creating a random walk
colors = ['#37AB65', '#3DF735', '#AD6D70', '#EC2504', '#8C0B90', '#C0E4FF', '#27B502', '#7C60A8', '#CF95D7']

def random_walk(num_steps):
    turtle.pensize(7)
    angle = [90, 180, 270, 360]
    paces = [10, 20, 30, 40, 50]
    for _ in range(num_steps):
        print(_)
        turtle.pencolor(choice(colors))
        turtle.forward(choice(paces))
        turtle.setheading(choice(angle))

# drawing the steps
random_walk(500)

# exiting the window on click
screen.exitonclick()
