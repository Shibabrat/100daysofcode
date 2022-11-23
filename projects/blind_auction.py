# Day 9: Blind auction

from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bidders = {
    "name": [],
    "bidAmount": [],
}

continueOrNot = "yes"

bidAmountOld = 0

while continueOrNot == "yes":
    name = input("What is your name?: ")
    bidAmount = int(input("What's your bid?: "))

    if bidAmount > bidAmountOld:
        winner = name
        bidAmountOld = bidAmount
    
    bidders["name"] = name
    bidders["bidAmount"] = bidAmount
    
    continueOrNot = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    clear()
    
    

print(f"The winner is {winner} with a bid of ${bidAmountOld}")

