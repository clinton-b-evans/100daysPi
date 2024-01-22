import turtle
import pandas

data = pandas.read_csv("Day 25/us-states-game-start/50_states.csv")
remaining_states = data.state.to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
counter = 0

while len(remaining_states) > 0:
    answer_state = screen.textinput(title=f"{counter}/50 || Guess the State", prompt="What's another state's name?").title()
    found_state = data[data.state == answer_state]
    if len(found_state) > 0:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(found_state.x.values[0], found_state.y.values[0])
        t.write(answer_state)
        # data = data.drop(answer_state)
        remaining_states.remove(answer_state)
        counter += 1
screen.exitonclick()