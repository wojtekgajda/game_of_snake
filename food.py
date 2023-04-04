from turtle import Turtle
from snake import Snake
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("circle")
        super().color("blue")
        super().shapesize()
        super().penup()
        self.food = super()

    def appearance(self):
        food_pos_x = random.randrange(-280, 280, 20)
        food_pos_y = random.randrange(-280, 280, 20)
        self.food.goto(food_pos_x, food_pos_y)
