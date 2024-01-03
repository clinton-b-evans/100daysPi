from turtle import Turtle, Screen
import random


#SETTING UP VARIABLES AND SCREEN 
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bets!", prompt="Type the color of your winning turtle.")
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []
is_race_on = False

#CREATING TURTLES AND SETTING UP THEIR COLOR + POSITIONS
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=-100 + i*40)
    all_turtles.append(new_turtle)

#TAKE USER INPUT AS BET AND START THE RACE
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"Congratulations! Your {turtle.pencolor()} won!")
            else:
                print(f"Unlucky! The {turtle.pencolor()} turtle won and your {user_bet} turtle lost!")
            is_race_on = False
        turtle.forward(random.randint(0,10))

screen.exitonclick()