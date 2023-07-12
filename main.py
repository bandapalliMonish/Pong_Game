from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from divider import Divider
import time

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_score = Scoreboard((-100, 200))
r_score = Scoreboard((100, 200))
# divider = Divider()

screen.title("PONG")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
sleep = 0.1
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(sleep)

    # Detect collision with upper and lower wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with left and right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep /= 1.1

    # Detect collision with left and right wall
    if ball.xcor() > 380:
        l_score.increase_score()
        ball.reset_position()
        sleep = 0.1

    if ball.xcor() < -380:
        r_score.increase_score()
        ball.reset_position()
        sleep = 0.1

    if l_score.score == 3:
        l_score.game_over("left")
        game_is_on = False
    elif r_score.score == 3:
        r_score.game_over("right")
        game_is_on = False

screen.exitonclick()
