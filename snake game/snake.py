# create snake class to cooridinate snake and make it moving
from turtle import Turtle

START_POSITION = [(0, 0 ), (-20, 0), (-40, 0)]
MOVE_STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in START_POSITION:
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)
    
    def move(self):
        """connected all the segments of the snake to move to the previous segment's position"""
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(MOVE_STEPS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)   

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
