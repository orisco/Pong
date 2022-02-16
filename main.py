from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from dotted_line import DottedLine
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.title(titlestring="Pong Game")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
scoreboard = Scoreboard()
dotted_line = DottedLine()
speed = 0.1

r_paddle = Paddle(450)
l_paddle = Paddle(-450)
ball = Ball()
screen.update()
game_is_on = True

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "a")
screen.onkey(l_paddle.move_down, "z")


while game_is_on:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()

    #detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    #detect collision with left and right walls
    if ball.xcor() > 480:
        scoreboard.increase_score("r")
        ball.reset_position()

    elif ball.xcor() < -480:
        scoreboard.increase_score("l")
        ball.reset_position()
















screen.exitonclick()
