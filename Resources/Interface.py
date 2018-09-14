# Passer Effectiveness Rating for the Premiere League 2018/2019 Season
# Made by Jayden Pereira
## This file is the main, front-end interface for the program

print("Welcome to the PER database!\n")

import ScoreKeeper
import Database

def Menu():
    print('\nPlease type 1 for looking at previous PER scores, 2 for inputing new data, or 3 for the list of Player IDs')
    selector = str(input())
    if selector == '1':
        player_request = int(input('\nPlease input a Player ID\n'))
        ScoreKeeper.PER_calculator(player_request)
        print('\n\nPress 1 to restart or 2 to exit\n')
        selector = str(input())
        if selector == '1':
            Menu()
        if selector == '2':
            exit()
    elif selector == '2':
        Database.databaseappender()
        print('\n\nPress 1 to restart or 2 to exit\n')
        selector = str(input())
        if selector == '1':
            Menu()
        if selector == '2':
            exit()
    elif selector == '3':
        Database.PlayerList()
        print('\n\nPress 1 to restart or 2 to exit\n')
        selector = str(input())
        if selector == '1':
            Menu()
        if selector == '2':
            exit()
    elif selector != '1' or selector != '2' or selector != '3':
        print('Invalid input, try again!\n')

Menu()
