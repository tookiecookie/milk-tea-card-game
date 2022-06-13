import pandas as pd


opening_hand_size   = 6
hand_limit          = 8
opening_orders_count = 6
draw_size           = 2
order_draw_size     = 1
player_count        = 3

ingredients = pd.DataFrame([
    ("milk", 16),
    ("fruit", 16),
    ("pearl", 11),
    ("taro", 9),
    ("pudding", 9),
    ("jelly", 9),
    ("sugar", 9),
    ("magic", 3)
])
ingredients.columns = ["name", "number_of"]

orders = pd.DataFrame([
    ("Milk Tea", 4, ["milk", "sugar"], 1),
    ("Taro Milk Tea", 4, ["pearl", "taro"], 1),
    ("Strawberry Milk Tea", 4, ["milk", "fruit"], 1),
    ("Mango Pudding Tea", 4, ["fruit", "pudding"], 1),
    ("Jelly Fruit Tea", 4, ["fruit", "jelly"], 1),
    ("Classic PMT", 3, ["milk", "pearl", "sugar"], 3),
    ("Taro-fic Tea", 3, ["milk", "pearl", "taro"], 3),
    ("Strawberry Shortcake", 3, ["milk", "fruit", "pudding"], 3),
    ("Acquried Taste", 3, ["fruit", "jelly", "taro"], 3),
    ("Giga Pudding", 3, ["milk", "pudding", "sugar"], 3),
    ("QQ Passion Frenzy", 2, ["fruit", "pearl", "jelly", "sugar"], 5),
    ("My Neighbour Totaro", 2, ["milk", "pearl", "taro", "magic"], 5),
    ("Sweetie Pearlie", 1, ["pearl", "jelly", "pudding", "sugar", "magic"], 10),
    # ("Taste the Rainbow", 1, ["fruit", "fruit", "jelly", "jelly", "magic"], 10),
])
orders.columns = ["name","number_of", "recipe", "points"]

player1 = {
    "name": "Player 1",
    "hand": [],
    "pile": [],
    "points": [],
    "score": 0
}
player2 = {
    "name": "Player 2",
    "hand": [],
    "pile": [],
    "points": [],
    "score": 0
}
player3 = {
    "name": "Player 3",
    "hand": [],
    "pile": [],
    "points": [],
    "score": 0
}
player4 = {
    "name": "Player 4",
    "hand": [],
    "pile": [],
    "points": [],
    "score": 0
}
players = [player1, player2, player3, player4]
# players = [player1, player2, player3]
# players = [player1, player2]

turn_data_path = 'turn_data.csv'
player_data_path = 'player_data.csv'