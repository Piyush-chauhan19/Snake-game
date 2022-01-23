import turtle
import time
from food import Food
import snake
from score_board import ScoreBoard
from boundary import Boundary

turtle.tracer(0)

# setting up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# declaring the turtles
snaky = snake.Snake()
food = Food()
score = ScoreBoard()

# making the boundary
boundary = Boundary()

# game preparations
snaky_is_alive = True
screen.listen()
screen.onkey(snaky.up, "Up")
screen.onkey(snaky.down, "Down")
screen.onkey(snaky.right, "Right")
screen.onkey(snaky.left, "Left")

# starting the game
while snaky_is_alive:
    snaky.move()
    screen.update()
    time.sleep(0.1)

    # eating food
    if snaky.head.distance(food) < 20:
        food.refresh()
        score.update()
        snaky.increase()

    # hitting the wall
    if snaky.head.xcor() > 270 or snaky.head.ycor() > 270 or snaky.head.xcor() < -270 or snaky.head.ycor() < -270:
        snaky_is_alive = False
        score.game_over()

    # biting the tail
    for part in snake.body[1:]:
        if snaky.head.distance(part) < 10:
            snaky_is_alive = False
            score.game_over()

screen.exitonclick()
