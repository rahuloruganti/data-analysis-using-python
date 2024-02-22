from turtle import Turtle
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
    t.pendown()"""
t=Turtle()
for side in range(3,11):
    for i in range(side):
        t.forward(100)
        t.left(360/side)
    
    