from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # Read data.txt to get previous highest number
        with open("data.txt", mode="r") as file:
            self.highest_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        # Write new highest number inside data.txt
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highest_score}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
