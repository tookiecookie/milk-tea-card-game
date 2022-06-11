import pandas as pd
import constants as C
import stats as S
import Deck
import Order
import Player



def printBoardState(players, orders_list, ingredients, orders, discard_pile):
    print("Orders on the board: ", orders_list)
    print("Player State: \n", players) 
    print("\nNumber of cards in Ingredients Deck = ", len(ingredients))
    print("\nNumber of cards in Orders Deck = ", len(orders))
    print("---------------------------------------")
    print("\nNumber of cards in Discard Deck = ", len(discard_pile))
    print("---------------------------------------")

def initiateGame():
    global ingredients
    global orders
    global discard_pile
    global players
    global orders_list

    ingredients = Deck.createDeck(C.ingredients)
    orders = Deck.createDeck(C.orders)
    discard_pile = Deck.createDiscard()
    players = Player.setup(C.players, ingredients)
    orders_list = Order.setup(orders)
    S.resetStats()

def runGame():
    print("\n ----- START GAME -----\n\n")

    # Initiate board, players and decks
    initiateGame()
    printBoardState(players, orders_list, ingredients, orders, discard_pile)
     
    # Player turns
    while(len(orders) != 10):
        print("TURN: ", S.turnCount)
        S.turnCount += 1
        for i in range(len(players)):
            player = players[i]
            Player.turn(player, ingredients, orders, orders_list, discard_pile)
            player['score'] = Player.calculateScore(player)
            printBoardState(players, orders_list, ingredients, orders, discard_pile)

    printBoardState(players, orders_list, ingredients, orders, discard_pile)
runGame()
