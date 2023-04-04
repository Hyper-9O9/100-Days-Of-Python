from turtle import Turtle, Screen

#creating turtle and screen
tim = Turtle()
screen = Screen()

#creating function for moving the turtle up
def move_forward():
    tim.forward(10)

#listening to inputs
screen.listen()
# for functions as an argument, if you add () at the end, the func will run automatically
# we don't want that, instead remove () so the func runs when a key is pressed
# below is a higher order function which takes a func as an input and works with it inside the body of the func
#moving the turtle when space is pressed
screen.onkey(key="space", fun=move_forward)
#exiting the program when it is clicked
screen.exitonclick()
