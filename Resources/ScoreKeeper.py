# Passer Effectiveness Rating for the Premiere League 2018/2019 Season
# Made by Jayden Pereira
## This file calculates total PER

import pickle
import Database

PER_data = pickle.load(open("rawdata","rb"))

def PER_calculator(player):
    score = 0
    for key in PER_data:
        score += (PER_data[key][player]['assists'] * 20)
        score += (PER_data[key][player]['successful passes'] * 5)
        score += (PER_data[key][player]['unsuccessful passes'] * -5)
        score += (PER_data[key][player]['key passes'] * 5)
        score += (PER_data[key][player]['long balls'] * 3)
        score += (PER_data[key][player]['through balls'] * 3)
    print('Their total PER is ' + str(score))
