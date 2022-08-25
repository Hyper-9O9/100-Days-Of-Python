from turtle import *
# defining the tools
turtle = Turtle()
screen = Screen()
# customizing the turtle
turtle.shape("turtle")
turtle.color("DarkTurquoise")

  
# creating a square

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)




# exiting the window on click
screen.exitonclick()
