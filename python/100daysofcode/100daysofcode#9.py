import os
import art
print(art.logo)
def acution():
  i=True
  highest_bid=0
  while i is True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids={}
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if more_bidders =="yes":
        os.system('cls')
    else:
      i=False
      os.system('cls')
  highest_bid = max(zip(bids.keys(),bids.values()))[0]
  print(f"highest bidder is",highest_bid)
  
    
acution()
#HINT: You can call clear() to clear the output in the console.