import turtle as t
import random
tim = t.Turtle()


colors = ["deep sky blue", "green yellow", "orange red", "medium slate blue", "yellow", "aquamarine"]

def draw_shape(num_side):
  angle = 360 / num_side
  for i in range(num_side):
    tim.forward(100)
    tim.right(angle)

for num_side in range(3,11):
  tim.color(random.choice(colors))
  draw_shape(num_side)