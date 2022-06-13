from game import constants as C
from game import Order
from game import Deck

class Player:
    def __init__(self, name, hand, pile, points, score):
        self.name = name
        self.hand = hand
        self.pile = pile
        self.points = points
        self.score = score

    def setup(player, ingredients):
        cards = Deck.drawCards(ingredients, C.opening_hand_size)
        player.hand.extend(cards)
        return player
    
    def print(player):
        print("Player Name: " + player.name)
        print(player.hand)
        print(player.pile)
        print(player.score)

    def calculateScore(player):
        for point in player.points:
            player.score += point
        return player.score
        
    def turn(player, ingredients, orders, orders_list, discard_pile):

        # Check if there are any order cards left to flip
        if len(orders) == 0:
            return
        else:
            orders_list.extend(Deck.drawCards(orders, C.order_draw_size))

        # Reshuffle if there are not enough ingredients card to draw
        if len(ingredients) <= C.draw_size: 
            ingredients = Deck.reshuffleDeck(ingredients, discard_pile)
        
        player.hand.extend(Deck.drawCards(ingredients, C.draw_size))
        Player.fulfill(orders_list, player, discard_pile)

    def fulfill(orders_list, player, discard_pile):
        Order.getRecipe(orders_list[1], C.orders)
        for order in orders_list:
            recipe = Order.getRecipe(order, C.orders)
            check = Order.checkCards(recipe, player.hand)
            
            if check == True:
                Order.spendCards(recipe, player.hand, discard_pile)
                points = Order.getPoints(order, C.orders)
                player.points.extend(points)
                player.pile.append(order)
                orders_list.remove(order)

                print("Order fulfilled by ", player.name, ": ", order)




