from turtle import Turtle, Screen
raphael = Turtle()
raphael.shape("arrow")
raphael.color("green")
count = 0
for _ in range(30):
    count += 1
    if count % 2 == 0:
        raphael.penup()
    else:
        raphael.pendown()
    raphael.forward(10)

screen = Screen()
screen.exitonclick()