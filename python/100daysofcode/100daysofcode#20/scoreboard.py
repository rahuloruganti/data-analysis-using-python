from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
        
       
    def update_scoreboard(self):
        self.write(f"score={self.score}",align="center",font=("Arial",8,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",12,"normal"))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()


   