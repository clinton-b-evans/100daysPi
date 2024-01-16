import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

frogger = Player(-280)
cars = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(frogger.go_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()

    # Create random cars (1 in 6 chance of creating a car)
    cars.create_car()
    cars.move_cars()

    # Detect collision with car
    for car in cars.all_cars:
        if car.distance(frogger) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing (reached top of screen)
    if frogger.is_at_finish_line():
        frogger.go_to_start()
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()