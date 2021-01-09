from turtle import Turtle, Screen
import random

is_race_start = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Guess who will win the game?", prompt="Please enter a color: ")
colors = ["red", "yellow", "orange", "green", "blue", "purple"]
Y_position = [-100, -60, -20, 20, 60, 100]
all_turtle = []

for turtle_number in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_number])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=Y_position[turtle_number])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_start = True

while is_race_start:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_start = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} is the winner~")
            else:
                print(f"You've lost... The {winner_color} is the winner~")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
