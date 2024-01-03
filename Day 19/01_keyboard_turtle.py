from turtle import Turtle, Screen


donatello = Turtle()
screen = Screen()


def move_forward():
    donatello.forward(10)


def move_backward():
    donatello.backward(10)


def turn_left():
    donatello.setheading(donatello.heading() + 5)


def turn_right():
    donatello.setheading(donatello.heading() - 5)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)

screen.exitonclick()