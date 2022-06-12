from game import Gameplay
from game import stats as S
from game import constants as C

S.resetExports(S.playerData, S.turnData)

for i in range(5):
    Gameplay.initiateGame()
    Gameplay.runGame()
    S.resetStats
    S.gameCount += 1


S.exportData(S.turnData,C.turn_data_path)
S.exportData(S.playerData,C.player_data_path)