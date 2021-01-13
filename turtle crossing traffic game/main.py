import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing Busy Road!")

# generate game objects
turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(turtle.move_forward, "Up")

# game start
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_left()

    # detect the turtle has reached the top edge of the screen successfully
    if turtle.at_finish_line():
        turtle.to_start()
        scoreboard.add_level()
        cars.speed_up()

    # detect if the turtle collision with cars
    for car in cars.all_cars:
        if car.distance(turtle) < 25:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
