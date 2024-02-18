import random
from game_data import data
from arthigherlower import logo,vs
import os

def celeb():
    return random.choice(data)
a=celeb()
b=celeb()
def score(var):
    if var=="a":
        return a["follower_count"]>b["follower_count"]
    else:
        return b["follower_count"]>a["follower_count"]
    
def game():
    a=celeb()
    b=celeb()
    high_score=True
    current_score=0
    while high_score:
        print(logo)
        print("compare A:",a["name"],",a",a["description"],",from",a["country"])
        print(vs)
        print("compare B:",b["name"],",a",b["description"],",from",b["country"])
        v=input("who has more followers? type 'a' or 'b':")
        if score(v):
            current_score+=1
            os.system("cls")
            a=b
            b=celeb()
            print("you're correct!,current score :",current_score)
        else:
            os.system("cls")
            high_score=False
            print("awe you lose :( , final score:",current_score)

while input("want to play a game? enter 'y' or 'n' to exit ")=='y':
    os.system("cls")
    game()

