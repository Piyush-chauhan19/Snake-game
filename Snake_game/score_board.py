import turtle


class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 290)
        self.write(f"Score: {self.score}", align="center", font=('Arial', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 20, 'normal'))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 14, 'normal'))
