import pandas as pd
from game import constants as C

global gameCount
global shuffleCount
global turnCount
global turnData 


gameCount = 0
turnCount = 0
shuffleCount = 0
turnData = pd.DataFrame()

def resetStats():
    global gameCount
    global turnCount
    global shuffleCount
    global turnData
    global playerData
    gameCount = 0
    turnCount = 0
    shuffleCount = 0
    turnData = pd.DataFrame()
    playerData = pd.DataFrame()
    # turnData.to_csv(path, mode='a', header=False)

def addRowToPlayerData(gameCount, turn, player_name, player_hand, player_orders, player_score):
    global playerData
    row = pd.DataFrame(
        [[gameCount, turn, player_name, len(player_hand), len(player_orders), player_score]],
        columns=['game','turn','player_name','player_hand','player_orders','player_score'] 
        )
    playerData = pd.concat([playerData, row])

def addRowToTurnData(gameCount, turnCount, ingredients, discard_pile, orders, orders_list):
    global turnData
    row = pd.DataFrame(
            [[gameCount, turnCount, len(ingredients), len(discard_pile), len(orders), orders_list, len(orders_list)]],
            columns=['game','turn','ingredient_deck_count','discard_count','order_deck_count','orders_list', "orders_list_count"]  
            )        
    turnData = pd.concat([turnData, row], ignore_index=True)

def exportData(df, path):
    df.to_csv(path)#, mode='a', header=False)