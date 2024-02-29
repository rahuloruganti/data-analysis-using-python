SNAKE_POSTION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


import turtle
from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for i in SNAKE_POSTION:
            self.set_segment(i)
            
    
    def set_segment(self,i):
        new_turtle=Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(i)
        self.segments.append(new_turtle)

    def extend_snake(self):
        self.set_segment(self.segments[-1].position())


    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            x=self.segments[i-1].xcor()
            y=self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        self.head.forward(20)  

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
         if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)


    
