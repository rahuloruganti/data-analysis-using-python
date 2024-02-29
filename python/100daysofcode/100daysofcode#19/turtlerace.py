import turtle
from turtle import Turtle,Screen
import random
colors=["red","blue","green","black","yellow","orange","purple"]
screen=Screen()
user_color=screen.textinput(title="place you bet",prompt="which turtle will win the race? enter color:")
screen.setup(500,400)
on=True
all=[]
result=''

for i in range(len(colors)):
    t=Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.setposition(-230.0,200+(-50*(i+1)))
    all.append(t)
while on:
    for i in all:
        i.forward(random.randint(1,10))
        if int(i.position()[0])>=230:
            result=i.pencolor()     
            if result==user_color:
                print(f"you won! {result} turtle won the race.")
            else:
                print(f"you lose! {result} turtle won the race.")
            on=False
    
screen.exitonclick()
