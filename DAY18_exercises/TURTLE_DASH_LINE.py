from turtle import *

# defining the tools
turtle = Turtle()
screen = Screen()
# customizing the turtle
turtle.shape("turtle")
turtle.color("DarkTurquoise")

# creating a dashed line
for iteration in range(30):
    if iteration % 2 == 0:
        turtle.pendown()
        turtle.forward(10)
    else:
        turtle.penup() 
        turtle.forward(10)


# exiting the window on click
screen.exitonclick()
