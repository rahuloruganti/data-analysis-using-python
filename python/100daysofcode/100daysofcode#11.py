#building a blackjack project
import random
import os
card=[2,3,4,5,6,7,8,9,10,10,10,10,11]
def rand_card():
    return random.choice(card)

def calculate(value):
    if sum(value)==21 and len(value)==2:
        return 0
    if 11 in value and sum(value)>21:
        value.remove(11)
        value.append(1)
        return sum(value)
    else:
        return sum(value)
def blackjack(pla,com):
    if calculate(pla)==calculate(com):
        return "draw"
    elif calculate(pla)==0 or calculate(pla)>calculate(com) and  calculate(pla)<21 or calculate(com)>21:
        return"you win!!"
    elif calculate(com)==0 or calculate(com)>calculate(pla) and calculate(com)<21 or calculate(pla)>21:
        return "you lose :("
    

def game():
    game_over=True
    computer =[]
    player=[]
    for i in range(2):
        computer.append(rand_card())
        player.append(rand_card())
    while game_over:
        total_player=calculate(player)
        total_computer=calculate(computer)
        
        print(f"your card {player} current total {calculate(player)}")
        print(f"computer's first card {computer[0]}")
        if total_computer==0 or total_player==0 or total_computer>21 or total_player>21:
            game_over = False
            
        else:
            y=input("enter 'y' to pick another card 'n' to end ")
            if y =="y":
                player.append(rand_card())
                total_player=calculate(player)
            else:
                game_over=False
    while calculate(computer)<=17 and calculate(computer)!=0:
            computer.append(rand_card())
            total_computer=calculate(computer)

    print(f"your cards {player} final total{total_player}")
    print(f"computer cards{computer} final total {total_computer}")
    print(blackjack(player,computer))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':")=='y':
    os.system("cls")
    game()
   
    
        ############### Blackjack Project #####################
