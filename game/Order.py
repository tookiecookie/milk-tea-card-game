from select import select
import pandas as pd
import constants as C
import Deck

def setup(orders):
    orders_list = []
    orders_list.extend(Deck.drawCards(orders, C.opening_orders_count))
    return orders_list

def getPoints(order_name, params):
    order = params.loc[params['name'] == order_name]
    points = order['points']
    return points

def getRecipe(order_name, params):
    order = params.loc[params['name'] == order_name]
    recipe = order['recipe'].values
    return recipe[0]

# TODO: Improve check.
# Recipes that contain dup ingredients do not work with this logic.
# E.g. Taste the Rainbow doesn't pass this check
def checkCards(recipe, player_hand):
    checksum = 0
    for ingredient in recipe:
        if ingredient not in player_hand:
            checksum += 1
    
    if checksum == 0:
        return True
    else:
        return False

def spendCards(recipe, player_hand, discard_pile):
    for ingredient in recipe:
        player_hand.remove(ingredient)
        discard_pile.append(ingredient)

