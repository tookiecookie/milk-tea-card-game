from game import Gameplay
from game.Stats import Stats

stats = Stats()
Stats.resetExports()
    
for i in range(100):
    board = Gameplay.initiateGame(stats)
    Gameplay.runGame(board, stats)
    Stats.resetStats(stats)
    stats.gameCount += 1
