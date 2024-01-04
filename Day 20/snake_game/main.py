from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game / Nokia Throwback")
snake_body = []
snake_body_length = 3

for i in range(0, snake_body_length):
    snake = Turtle(visible=False)
    snake.penup()
    snake.shape("square")
    snake.size = 20
    snake.color("white")
    snake.goto(i*-20,0)
    snake.pendown()
    snake_body.append(snake)
    print(snake.position())

for i in range(0, snake_body_length):
    snake = snake_body[i].showturtle()
 


screen.exitonclick()