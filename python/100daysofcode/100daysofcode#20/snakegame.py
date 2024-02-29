from food import Food
from turtle import Screen
import time
from snake import Snake
from scoreboard import Score

screen=Screen()
screen.title("snake game")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
snake_position=[(0,0),(-20,0),(-40,0)]

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


on=True
while on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.extend_snake()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.xcor()<-280:
        on=False
        score.game_over()
    for i in snake.segments[1:]: 
        if snake.head.distance(i)<10:
            on=False
            score.game_over()


screen.exitonclick()