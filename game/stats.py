import pandas as pd
import constants as C

global shuffleCount
global turnCount


turnCount = 0
shuffleCount = 0

def resetStats():
    global turnCount
    global shuffleCount
    turnCount = 0
    shuffleCount = 0