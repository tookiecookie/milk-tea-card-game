from game import constants as C
from game import Order
from game import Deck


def setup(players, ingredients):
    for i in range(len(players)):
        cards = Deck.drawCards(ingredients, C.opening_hand_size)
        players[i]['hand'].extend(cards)
    return players



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


def calculateScore(player):
    player_score = 0
    player_points = player['points']
    for point in player_points:
        player_score += point
    return player_score


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

