from game import constants as C
from game import Order
from game import Deck
from game.Player import Player

class Board:
    def __init__(self, name, ingredients, orders, order_list, discard, players):
        self.name = name
        self.ingredients = ingredients
        self.orders = orders
        self.order_list = order_list
        self.discard = discard
        self.players = players

    def setup(player, ingredients):
        cards = Deck.drawCards(ingredients, C.opening_hand_size)
        player.hand.extend(cards)
        return player
    
    def print(board):
        print("Orders on the board: ", board.order_list)
        for i in range(C.player_count):
            print("Player State: \n", Player.print(board.players[i])) 
        print("\nNumber of cards in Ingredients Deck = ", len(board.ingredients))
        print("\nNumber of cards in Orders Deck = ", len(board.orders))
        print("---------------------------------------")
        print("\nNumber of cards in Discard Deck = ", len(board.discard))
        print("---------------------------------------")

    def calculateScore(player):
        for point in player.points:
            player.score += point
        return player.score
        
    def turn(player, ingredients, orders, orders_list, discard_pile):
        player_hand = player['hand']

        # Check if there are any order cards left to flip
        if len(orders) == 0:
            return
        else:
            orders_list.extend(Deck.drawCards(orders, C.order_draw_size))

        # Reshuffle if there are not enough ingredients card to draw
        if len(ingredients) <= C.draw_size: 
            ingredients = Deck.reshuffleDeck(ingredients, discard_pile)
        
        player_hand.extend(Deck.drawCards(ingredients, C.draw_size))
        fulfill(orders_list, player, discard_pile)

def fulfill(orders_list, player, discard_pile):
    Order.getRecipe(orders_list[1], C.orders)
    for order in orders_list:
        recipe = Order.getRecipe(order, C.orders)
        check = Order.checkCards(recipe, player['hand'])
        
        if check == True:
            Order.spendCards(recipe, player['hand'], discard_pile)
            points = Order.getPoints(order, C.orders)
            player['points'].extend(points)
            player['pile'].append(order)
            orders_list.remove(order)

            print("Order fulfilled by ", player['name'], ": ", order)




