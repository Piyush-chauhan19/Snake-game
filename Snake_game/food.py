from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.refresh()

    def refresh(self):
        xpos = random.randint(-280, 280)
        ypos = random.randint(-280, 280)
        self.goto(xpos, ypos)

