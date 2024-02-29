import turtle
from turtle import Turtle
MOVE=30
class paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.setposition(position)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        

    def forward(self):
        up=self.ycor()+MOVE
        self.goto(350,up)
    def backward(self):
        down=self.ycor()-MOVE
        self.goto(350,down)

    def forward_left(self):
        up=self.ycor()+MOVE
        self.goto(-350,up)
    def backward_left(self):
        down=self.ycor()-MOVE
        self.goto(-350,down)







