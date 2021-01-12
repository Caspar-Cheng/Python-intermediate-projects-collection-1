from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# set black 800*600 "Pong" game screen without animation tracer
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create paddles and set control keys
left_pad = Paddle((-350, 0))
right_pad = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(left_pad.move_up, "w")
screen.onkeypress(left_pad.move_down, "s")
screen.onkeypress(right_pad.move_up, "Up")
screen.onkeypress(right_pad.move_down, "Down")

# game start
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with up and down wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(right_pad) < 50 and ball.xcor() > 320 or ball.distance(left_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# click to close the screen
screen.exitonclick()
