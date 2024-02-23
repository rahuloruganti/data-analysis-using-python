import colorgram
import turtle
import random
from turtle import Turtle

rgb_color=[(204, 163, 110),
            (120, 91, 65),
            (55, 39, 28),
            (76, 108, 92),
            (32, 51, 46),
            (225, 198, 135),
            (147, 134, 93),
            (26, 41, 44),
            (47, 73, 66),
            (90, 54, 41),
            (114, 138, 108),
            (76, 64, 46),
            (242, 203, 163),
            (72, 81, 84),
            (178, 114, 81),
            (37, 30, 32),
            (125, 145, 117),
            (84, 75, 77),
            (54, 67, 69),
            (231, 180, 155),
            (73, 58, 60),
            (59, 63, 69),
            (149, 156, 157),
            (154, 140, 142)]

t=Turtle()
turtle.colormode(255)
def hirst_painting(num,count):
    t.penup()
    t.setposition(-200.0,-100.0)
    for i in range(1,num+1):
        t.dot(10,random.choice(rgb_color))
        t.forward(25)
        if i%count==0:
            t.setposition(-200.0,-100+(25*(i//count)))

hirst_painting(200,20)


screen=turtle.Screen()
screen.exitonclick()