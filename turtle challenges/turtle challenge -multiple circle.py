import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
def draw_gap_circle(size_gap):
  for i in range(int(360 / size_gap)):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + size_gap)

draw_gap_circle(10)
