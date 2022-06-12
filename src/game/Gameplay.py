import pandas as pd
import numpy as np
from game import constants as C
from . import stats as S
from game import Deck
from game import Order
from game import Player

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

    # turnStats = pd.DataFrame()

    # Initiate board, players and decks
    initiateGame()
    printBoardState(players, orders_list, ingredients, orders, discard_pile)
    S.addRowToTurnData(S.gameCount, S.turnCount, ingredients, discard_pile, orders, orders_list)

    # Player turns
    while(len(orders) != 10):
        print("TURN: ", S.turnCount)
        S.turnCount += 1

        for i in range(len(players)):
            player = players[i]
            Player.turn(player, ingredients, orders, orders_list, discard_pile)
            player['score'] = Player.calculateScore(player)
            S.addRowToPlayerData(S.gameCount, S.turnCount, player['name'], player['hand'], player['pile'], player['score'])
            
        S.addRowToTurnData(S.gameCount, S.turnCount, ingredients, discard_pile, orders, orders_list)
    
    S.playerData = pd.pivot_table(S.playerData, values=['player_hand','player_orders','player_score'], index=['game','turn'], columns=['player_name'], aggfunc=np.sum)
    printBoardState(players, orders_list, ingredients, orders, discard_pile)
    S.exportData(S.turnData,C.turn_data_path)
    S.exportData(S.playerData,C.player_data_path)
