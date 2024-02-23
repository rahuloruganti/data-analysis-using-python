from turtle import Turtle
import random
import turtle
"""t=Turtle()
for i in range(4):
    t.forward(100)
    t.left(90)

t.screen()
t.onclick()

t=Turtle()
for i in range(10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    
for side in range(3,11):
    t.color(random.choice(color_list))
    for i in range(side): 
        t.forward(90)
        t.left(360/side)

directions=[0,90,180,270,360]
t=Turtle() 
def random_walk(dis):
    for i in range(dis):
        t.color(random.choice(color_list))
        t.pensize(7)
        t.speed(2)
        t.forward(25)
        t.setheading(random.choice(directions))

random_walk(60)
color_list = [
    "coral", 
    "deepskyblue",
    "mediumseagreen",
    "orchid",
    "hotpink",
    "khaki",
    "wheat",
    "palevioletred",
    "teal",
    "plum"
]"""

turtle.colormode(255)
def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    color=(r,g,b)
    return color

t=Turtle()
t.speed(15)
def spiral(degree):
    for i in range(360//degree):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + degree)

spiral(5)

screen=turtle.Screen()
screen.exitonclick()