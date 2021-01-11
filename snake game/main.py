from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# create 600*600 black screen with screen title

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# set control directions keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# start game here
game_is_on = True

while game_is_on:
    # use update to update screen after each time of move to get better animation effect
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_socre()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        # the snake head segment is not mean to be inside for loop here
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
