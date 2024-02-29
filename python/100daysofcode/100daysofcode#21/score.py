from turtle import Turtle

class score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.position=position
        self.score=0
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        

    def update_scoreboard(self):
        self.goto(self.position)
        self.write(f"{self.score}",align="center",font=("Arial",24,"bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",18,"bold"))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
        
