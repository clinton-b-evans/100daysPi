from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        self.all_cars = []

        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.color(COLORS[random.randint(0,5)])
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.goto(300,0)
        self.movement_speed = 0.1
        self.showturtle()
    
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance != 1:
            return
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.penup()
        new_car.color(COLORS[random.randint(0,5)])
        random_y = random.randint(-25, 25)
        random_y *= 10
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
