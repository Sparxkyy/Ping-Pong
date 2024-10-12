import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
scoreboard=Scoreboard()

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("ping pong")
screen.tracer(0)

ball=Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
       ball.bounce_y()
        #need to bounce
#collision with r_paddle
    if ball.distance(r_paddle)<60 and ball.xcor()>330:
        ball.bounce_x()
    if ball.distance(l_paddle)<60 and ball.xcor()<-330:
        ball.bounce_x()


#if ball misses the paddle
    if ball.xcor()>380:

        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:

        ball.reset_position()
        scoreboard.r_point()








screen.exitonclick()

