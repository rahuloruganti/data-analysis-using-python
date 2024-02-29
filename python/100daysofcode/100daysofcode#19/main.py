import turtle
from turtle import Turtle,Screen

screen=Screen()
t=Turtle()

def movefoward():
    t.forward(10)
def movebackward():
    t.backward(10)
def anticlockwise():
    t.left(10)
def clockwise():
    t.right(10)

screen.listen()

screen.onkey(movefoward,"w")
screen.onkey(anticlockwise,"a")
screen.onkey(clockwise,"d")
screen.onkey(movebackward,"s")
screen.onkey(t.clear,"c")


screen.exitonclick()
