############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from blackjack_art import logo
# import only system from os
from os import system, name


def clear():
    # define our clear function: https://www.geeksforgeeks.org/clear-screen-python/

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():

    cardDrawn = cards[random.randint(0, 12)]

    return cardDrawn


def hit(currentCards):

    newCard = draw_card()
    if sum(currentCards) + newCard > 21:
        roundOver = True
    else:
        roundOver = False

    return [roundOver, newCard]


continuePlaying = 'y'

while continuePlaying == 'y':

    clear()
    print(logo)
    roundOver = False

    initialPlayerCards = [draw_card(), draw_card()]
    initialDealerCards = [draw_card(), draw_card()]

    dealerCards = initialDealerCards
    playerCards = initialPlayerCards

    while roundOver == False:
        if sum(playerCards) == 21 or sum(dealerCards) == 21:
            print(
                f"Your cards: {playerCards}, current score: {sum(playerCards)}"
            )
            print(
                f"Dealer's cards: {dealerCards}, current score: {sum(dealerCards)}"
            )
            if sum(playerCards) == 21:
                print("BLACKJACK, you win!")
            else:
                print("BLACKJACK, dealer wins!")
            roundOver = True
        else:
            print(
                f"Your cards: {playerCards}, current score: {sum(playerCards)}"
            )
            print(f"Computer's first card: {initialDealerCards[0]}")
            if sum(playerCards) > 21:
                if 11 not in playerCards:
                    print("Dealer wins")
                    roundOver = True
                elif 11 in playerCards:  # if Ace is in the hand when sum > 21, count it as 1
                    if sum(playerCards) - 10 > 21:
                        print("Dealer wins")
                        roundTrue = True
            else:
                nextAction = input(
                    "Type 'y' to get another card, type 'n' to pass: ").lower(
                    )

                if nextAction == 'y':
                    roundOver, newCard = hit(playerCards)
                    playerCards.append(newCard)
                    print(
                        f"Your cards: {playerCards}, current score: {sum(playerCards)}"
                    )

                    if roundOver == True:
                        print(
                            f"Dealer's cards: {dealerCards}, current score: {sum(dealerCards)}"
                        )
                        print("Dealer wins!")

                elif nextAction == 'n':
                    while sum(dealerCards) < 17:
                        roundOver, newCard = hit(dealerCards)
                        dealerCards.append(newCard)
                        print(
                            f"Dealer's cards: {dealerCards}, current score: {sum(dealerCards)}"
                        )
                        if roundOver == True:
                            print("You win")

                    if roundOver == False:
                        print(
                            f"Your cards: {playerCards}, current score: {sum(playerCards)}"
                        )
                        print(
                            f"Dealer's cards: {dealerCards}, current score: {sum(dealerCards)}"
                        )

                        if 21 - sum(dealerCards) < 21 - sum(playerCards):
                            print("Dealer wins")
                        elif 21 - sum(playerCards) < 21 - sum(dealerCards):
                            print("You win")
                        else:
                            print("It's a draw")

                        roundOver = True

    continuePlaying = input(
        "Type 'y' to continue playing, type 'n' to leave the game: ").lower()

