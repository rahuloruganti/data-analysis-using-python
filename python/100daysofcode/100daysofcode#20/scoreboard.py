from turtle import Turtle
data_txt="C:/Users/rorugan/data-analysis-using-python/python/100daysofcode/100daysofcode#20/data.txt"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        with open(data_txt) as hs:
            self.highscore = int(hs.read())
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score={self.score}  high score {self.highscore}",align="center",font=("Arial",8,"normal"))

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open(data_txt,mode="w") as highscore:
                highscore.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()


    def increase_score(self):
        self.score+=1
        self.update_scoreboard()


   