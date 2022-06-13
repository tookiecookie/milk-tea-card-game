import pandas as pd
import numpy as np
from game import constants as C
from game import Deck
from game import Order
from game.Player import Player
from game.Board import Board
from game.Stats import Stats

def initiateGame(stats):
    ingredients = Deck.createDeck(C.ingredients)
    orders = Deck.createDeck(C.orders)
    order_list = Order.setup(orders)
    discard = Deck.createDiscard()
    players = []
    for i in range(C.player_count):
        players.append(Player("Player_" + str(i+1),[],[],[],0))
    board = Board("Game " + str(stats.gameCount), ingredients, orders, order_list, discard, players)
    
    Board.print(board)
    Stats.addRowToTurnData(stats, board)
    return board

def runGame(board, stats):
    print("\n ----- START GAME -----\n\n")
    # Player turns
    while(len(board.orders) != 0):
        print("TURN: ", stats.turnCount)
        stats.turnCount += 1

        for i in range(C.player_count):
            player = board.players[i]
            Player.turn(player, board.ingredients, board.orders, board.order_list, board.discard)
            Player.calculateScore(player)
            Stats.addRowToPlayerData(stats, player)
        Stats.addRowToTurnData(stats, board)
    
    print("END GAME " + str(stats.gameCount))
    
    Board.print(board)
    stats.playerData = pd.pivot_table(stats.playerData, values=['player_hand','player_orders','player_score'], index=['game','turn'], columns=['player_name'], aggfunc=np.sum)
    # printBoardState(players, orders_list, ingredients, orders, discard_pile)
    Stats.exportData(stats.turnData,C.turn_data_path)
    Stats.exportData(stats.playerData,C.player_data_path)
