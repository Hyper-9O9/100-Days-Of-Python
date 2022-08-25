from turtle import *
from random import choice
# defining the tools
turtle = Turtle()
screen = Screen()
# customizing the turtle

# setting the speed of the brush
turtle.speed(15)
# list of colors
colors = ['pink', 'gold', 'turquoise']

def draw_spirograph(size_gap):
    # drawing spirograph
    for _ in range(int(360/size_gap)):
        turtle.color(choice(colors))
        turtle.circle(radius=100)
        turtle.right(5)

draw_spirograph(5)
# exiting the window on click
screen.exitonclick()
