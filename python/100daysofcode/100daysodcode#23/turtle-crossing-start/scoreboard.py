FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # self.color("white")
        self.score=0
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update_scoreboard()
        
       
    def update_scoreboard(self):
        self.write(f"score={self.score}",align="center",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()


