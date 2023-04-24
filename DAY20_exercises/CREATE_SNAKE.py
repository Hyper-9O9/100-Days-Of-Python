# creating the snake game using python
# the aim is just to create the snake on the screen
from turtle import Screen, Turtle
# setting up the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# creating the postion for the snake
start_x = 0
start_y = 0
reducer = 0
snake = []
# setting the snake on the map
for initialize in range(3):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(start_x - reducer, start_y)
    turtle.pendown()
    reducer = reducer + 20
    snake.append(turtle)

screen.exitonclick()