import pandas as pd
from game import constants as C

global gameCount
global shuffleCount
global turnCount
global turnStats 


gameCount = 0
turnCount = 0
shuffleCount = 0
turnData = pd.DataFrame()

def resetStats():
    global gameCount
    global turnCount
    global shuffleCount
    global turnData
    gameCount = 0
    turnCount = 0
    shuffleCount = 0
    turnData = pd.DataFrame()