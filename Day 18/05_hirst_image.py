import turtle as t
import colorgram
import random


# Variable creation
t.colormode(255)
color_skip = 0
rbg_colors = []
colors = colorgram.extract('image.jpg', 30)

# Turtle variables 
leonardo = t.Turtle()
leonardo.color("white")
leonardo.hideturtle()
leonardo.penup()
leonardo.speed(0)
num_of_dots = 100

# Function creation
def starting_position():
    leonardo.setheading(225)
    leonardo.forward(300)
    leonardo.setheading(0)


# Loop through the colors and add them to a list but skip first 5 colors
for color in colors:
    if color_skip < 5:
        color_skip += 1
    else:
        new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
        rbg_colors.append(new_color)


starting_position()


for dot_count in range(1, num_of_dots + 1):
    leonardo.dot(20, random.choice(rbg_colors))
    leonardo.forward(50)

    if dot_count % 10 == 0:
        leonardo.setheading(90)
        leonardo.forward(50)
        leonardo.setheading(180)
        leonardo.forward(500)
        leonardo.setheading(0)

t.exitonclick()