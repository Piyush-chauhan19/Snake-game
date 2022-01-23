import turtle
position = [(0, 0), (-20, 0), (-40, 0)]
body = []


class Snake(turtle.Turtle):
    def __init__(self):
        for pos in range(3):
            body_part = turtle.Turtle()
            body_part.penup()
            body_part.shape("square")
            body_part.goto(position[pos])
            body.append(body_part)
        self.head = body[0]

    @staticmethod
    def increase():
        body_part = turtle.Turtle()
        body_part.penup()
        body_part.shape("square")
        x = body[-1].xcor()
        y = body[-1].ycor()
        body_part.goto(x, y)
        body.append(body_part)

    @staticmethod
    def move():
        for part in range(len(body) - 1, 0, -1):
            x = body[part - 1].xcor()
            y = body[part - 1].ycor()
            body[part].goto(x, y)
        body[0].forward(20)

    @staticmethod
    def up():
        if body[0].heading() != 270:
            body[0].setheading(90)
    
    @staticmethod
    def down():
        if body[0].heading() != 90:
            body[0].setheading(270)
    
    @staticmethod
    def right():
        if body[0].heading() != 180:
            body[0].setheading(0)
    
    @staticmethod
    def left():
        if body[0].heading() != 0:
            body[0].setheading(180)
    
