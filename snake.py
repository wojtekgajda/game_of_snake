from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP_LENGTH = 10


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def create_single_segment(self):
        new_single_segment = Turtle()
        new_single_segment.penup()
        new_single_segment.color("white")
        new_single_segment.shape("square")
        new_single_segment_x = self.segments[-1].xcor()
        new_single_segment_y = self.segments[-1].ycor()
        new_single_segment.goto(new_single_segment_x, new_single_segment_y)
        self.segments.append(new_single_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[i - 1].xcor()
            y_pos = self.segments[i - 1].ycor()
            self.segments[i].goto(x_pos, y_pos)
        self.snake_head.forward(STEP_LENGTH)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def snake_reset(self):
        for s in self.segments:
            s.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]
