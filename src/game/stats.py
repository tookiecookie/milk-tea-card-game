import pandas as pd
from game import constants as C

class Stats:
    def __init__(self):
        self.gameCount = 0
        self.shuffleCount = 0
        self.turnCount = 0
        self.turnData = pd.DataFrame()
        self.playerData = pd.DataFrame()

    def resetStats(stats):
        stats.turnCount = 0
        stats.shuffleCount = 0
        stats.turnData = pd.DataFrame()
        stats.playerData = pd.DataFrame()

    def addRowToPlayerData(stats, player):
        row = pd.DataFrame(
            [[stats.gameCount, stats.turnCount, player.name, len(player.hand), len(player.pile), player.score]],
            columns=['game','turn','player_name','player_hand','player_orders','player_score'] 
            )
        stats.playerData = pd.concat([stats.playerData, row], ignore_index=True)

    def addRowToTurnData(stats, board):
        row = pd.DataFrame(
                [[stats.gameCount, stats.turnCount, len(board.ingredients), len(board.discard), len(board.orders), board.order_list, len(board.order_list)]],
                columns=['game','turn','ingredient_deck_count','discard_count','order_deck_count','orders_list', "orders_list_count"]  
                )        
        stats.turnData = pd.concat([stats.turnData, row], ignore_index=True)

    def exportData(df, path):
        df.to_csv(path, mode='a', header=False)

    def resetExports():
        df_player = pd.DataFrame(columns=['game','turn','player_name','player_hand','player_orders','player_score'])
        df_turn = pd.DataFrame(columns=['game','turn','ingredient_deck_count','discard_count','order_deck_count','orders_list', "orders_list_count"])
        df_player.to_csv(C.player_data_path, index=False)
        df_turn.to_csv(C.turn_data_path, index=False)
