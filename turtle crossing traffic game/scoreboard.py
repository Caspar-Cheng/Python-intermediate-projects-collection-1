# create score board record
from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self. hideturtle()
        self.level = 0
        self.penup()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-250, 250)
        self.color("blue")
        self.write(f"Level: {self.level}", font=FONT)

    def add_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.update_level()
        self.goto(-250, 200)
        self.color("red")
        self.write("Game Over!", font=FONT)
