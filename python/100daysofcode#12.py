#number guessing game
import random
import os



def game():
    guess_number=random.randint(1,100)
    difficulty=input("select your difficulty 'easy ' or 'hard' ")
    level={"easy":10,"hard":5}
    for i in range(level[difficulty],0,-1):
        print(f"you have {i} attempts remaining to guess the number ")
        user_num=int(input("make a guess "))
        if guess_number==user_num:
            print(f"you got it! the answer was {user_num}.")
            break   
        elif user_num>guess_number:
            print("too high")
        else:
            print("too low")
        
        if i==1:
            print("you've run out of guess:(")
        else:
            print("guess again")
        


while input("want to guess a number? enter 'y' to start 'n' to exit ")=='y':
    os.system("cls")
    game()




