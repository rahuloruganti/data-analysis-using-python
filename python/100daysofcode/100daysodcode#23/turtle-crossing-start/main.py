import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
cars=CarManager()
player=Player()
score=Scoreboard()

screen.listen()
screen.onkey(player.move_forward,"Up")
leve=0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car()
    cars.move_car()
    if player.ycor()>280:
        score.increase_score()
        player.reset()
        leve+=0.3
        cars.level(leve)

    for car in cars.all_car:
        if abs(player.ycor()-car.ycor())<25 and abs(player.xcor()-car.xcor())<20:
            score.game_over()
            game_is_on=False


screen.exitonclick()

    
    
    