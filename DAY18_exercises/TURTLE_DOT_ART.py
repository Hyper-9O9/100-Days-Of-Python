# this project is incomplete for now
from turtle import *
from random import choice

turtle = Turtle()
screen = Screen()

screen.colormode(255)

color_pallet = [(36, 10, 28), (16, 21, 40), (97, 163, 242), (56, 87, 157), (151, 53, 122), (125, 27, 94)]
turtle.right(140)
for _ in range(30):

    # turtle.dot(20, choice(color_pallet))
    turtle.forward(20)

turtle.setheading(0)
turtle.forward(920)
turtle.setheading(90)
turtle.forward(10)
turtle.setheading(180)
turtle.forward(920)

screen.exitonclick()