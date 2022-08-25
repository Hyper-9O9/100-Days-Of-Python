from turtle import *
from random import choice
# defining the tools
turtle = Turtle()
screen = Screen()
# customizing the turtle
turtle.shape("turtle")
turtle.color("DarkTurquoise")

# creating multi shape art
colors = ['firebrick', 'DodgerBlue4']

def draw_shape(num_side):
    turtle.pencolor(choice(colors))
    angle = 360 / num_side
    for _ in range(num_side):
        turtle.forward(100)
        turtle.right(angle)

# drawing the shapes
for shape in range(3,10):
    draw_shape(shape)

# exiting the window on click
screen.exitonclick()
