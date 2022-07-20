from turtle import Turtle
import random as rm


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = rm.randint(-280, 280)
        rand_y = rm.randint(-280, 280)
        self.goto(rand_x, rand_y)