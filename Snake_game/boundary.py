from turtle import Turtle


class Boundary(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(-290, 290)
        self.pendown()
        self.goto(290, 290)
        self.goto(290, -290)
        self.goto(-290, -290)
        self.goto(-290, 290)

