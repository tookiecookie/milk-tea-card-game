import random
import constants as C


def createDeck(deck_params):
    deck = []

    for i in deck_params.index:
        l = [deck_params['name'][i] for x in range(deck_params['number_of'][i])]
        deck.extend(l)
    
    shuffleDeck(deck)
    return deck

def createDiscard():
    return []

def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

def drawCards(deck, size):
    draw = []
    for i in range(size):
        card = deck.pop()
        draw.append(card)
    return draw

def reshuffleDeck(ingredients, discard_pile):
    print("Reshuffling ingredients pile")
    for i in range(len(ingredients)):
        ingredient = ingredients.pop()
        discard_pile.append(ingredient)
    ingredients.extend(shuffleDeck(discard_pile))
    discard_pile = createDiscard()
    return ingredients