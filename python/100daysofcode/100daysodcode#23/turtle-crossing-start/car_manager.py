COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_car=[]

    def car(self):
        if random.randint(1,6)==1:
            new_car=Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setposition(300,random.randint(-260,260))
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            car.backward(STARTING_MOVE_DISTANCE)

    def level(self,num):
        for car in self.all_car:
            car.backward(STARTING_MOVE_DISTANCE+(num*MOVE_INCREMENT))
        

    
    
