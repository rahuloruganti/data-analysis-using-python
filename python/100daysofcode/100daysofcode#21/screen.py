
from turtle import Screen
from bats import paddle
from ball import Ball
from score import score
import time


screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)
r=paddle((350,0))
l=paddle((-350,0))
ball=Ball()
right_score=score((200,250))
left_score=score((-200,250))

scoreboard=score((0,250))
scoreboard.score="SCORE"
scoreboard.update_scoreboard()

right_score.update_scoreboard()
left_score.update_scoreboard()

screen.listen()
screen.onkey(r.forward,"Up")
screen.onkey(r.backward,"Down")

screen.onkey(l.forward_left,"w")
screen.onkey(l.backward_left,"s")


game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>270 or ball.ycor()<-270:
        ball.bounce_y()
    if ball.distance(r)<50 and ball.xcor()>320 or ball.distance(l)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>350:
        ball.reset_postion()
        left_score.increase_score()
        left_score.update_scoreboard()
    if ball.xcor()<-350:
        ball.reset_postion()
        right_score.increase_score()
        right_score.update_scoreboard()





screen.exitonclick()