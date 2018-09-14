# Passer Effectiveness Rating for the Premiere League 2018/2019 Season
# Made by Jayden Pereira
## This file is the non-serialized database for players and passes

import pickle
import ScoreKeeper

def databaseappender():
    player_append = int(input('what player would you like to append?'))
    week_append = int(input('in what week are you appending?'))
    data_selector = str(input('Please type what stat you would like to change:\n\nAssists = 1\n\nSuccessful Passes = 2\n\nUnsuccessful Passes = 3\n\nKey Passes = 4\n\nLong Balls = 5\n\nThrough Balls = 6\n\n'))
    while True:
        if data_selector == '1':
            data_append = int(input('Input new data\n'))
            Data[week_append][player_append]["assists"] = data_append
            pickle.dump(Data,open("rawdata","wb"))
            print('Assists are now at ' + str(data_append) + "!")
            break
        elif data_selector == '2':
            data_append = int(input('Input new data\n'))
            Data[week_append][player_append]["successful passes"] = data_append
            pickle.dump(Data,open("rawdata","wb"))
            print('Successful Passes are now at ' + str(data_append) + "!")
            break
        elif data_selector == '3':
            data_append = int(input('Input new data\n'))
            Data[week_append][player_append]["unsuccessful passes"] = data_append
            pickle.dump(Data,open("rawdata","wb"))
            print('Unsuccessful Passes are now at ' + str(data_append) + "!")
            break
        elif data_selector == '4':
            data_append = int(input('Input new data\n'))
            Data[week_append][player_append]["key passes"] = data_append
            pickle.dump(Data,open("rawdata","wb"))
            print('Key Passes are now at ' + str(data_append) + "!")
            break
        elif data_selector == '5':
            data_append = int(input('Input new data\n'))
            Data[week_append][player_append]["long balls"] = data_append
            pickle.dump(Data,open("rawdata","wb"))
            print('Long Balls are now at ' + str(data_append) + "!")
            break
        elif data_selector == '6':
            data_append = int(input('Input new data\n'))
            Data[week_append][player_append]["through balls"] = data_append
            pickle.dump(Data,open("rawdata","wb"))
            print('Through Balls are now at ' + str(data_append) + "!")
            break

def PlayerList():
    pickle.dump(PlayerKey,open("PlayerList","wb"))
    list = pickle.load(open("PlayerList","rb"))
    teamselector = int(input('\nPlease input a the club\'s ID to see it\'s players:\nArsenal = 1  Bournemouth = 2  Brighton = 3\nBurnley = 4  Cardiff = 5  Chelsea = 6\nCrystal Palace = 7  Everton = 8  Fulham = 9\nHuddersfield = 10  Leicester = 11  Liverpool = 12\nMan City = 13  Man United = 14  Newcastle = 15\nSouthampton = 16  Tottenham = 17  Watford = 18\nWest Ham = 19  Wolves = 20\n\n'))
    print(list[teamselector])

PlayerKey = {
    1: {
        101: 'Ozil',
        102: 'Mkhitaryan',
        103: 'Torreira',
    },
    2: {
        201: 'Ibe',
        202: 'Pugh',
        203: 'Arter',
    },
    3: {
        301: 'Knockaert',
        302: 'Gross',
        303: 'Propper',
    },
    4: {
        401: 'Defour',
        402: 'Lennon',
        403: 'Gudmundosson',
    },
    5: {
        501: 'Harris',
        502: 'Pilkington',
        503: 'Gunnarsson',
    },
    6: {
        601: 'Hazard',
        602: 'Kante',
        603: 'Jorginho',
    },
    7: {
        701: 'Meyer',
        702: 'Townsend',
        703: 'Kouyate',
    },
    8: {
        801: 'Gueye',
        802: 'Sigurdsson',
        803: 'Davies',
    },
    9: {
        901: 'Seri',
        902: 'Cairney',
        903: 'Johensen',
    },
    10: {
        1001: 'Mooy',
        1002: 'Williams',
        1003: 'Bucana',
    },
    11: {
        1101: 'A. Silva',
        1102: 'Ndidi',
        1103: 'Albrighton',
    },
    12: {
        1201: 'Henderson',
        1202: 'Fabinho',
        1203: 'Keita',
    },
    13: {
        1301: 'De Bruyne',
        1302: 'D. Silva',
        1303: 'Gundogan',
    },
    14: {
        1401: 'Pogba',
        1402: 'Fred',
        1403: 'Mata',
    },
    15: {
        1501: 'Shelvey',
        1502: 'Ritchie',
        1503: 'Diame',
    },
    16: {
        1601: 'Ward-Prowse',
        1602: 'Romeu',
        1603: 'Lemina',
    },
    17: {
        1701: 'Lucas',
        1702: 'Eriksen',
        1703: 'Dembele',
    },
    18: {
        1801: 'Pereyra',
        1802: 'Cleverley',
        1803: 'Chalobah',
    },
    19: {
        1901: 'Wilshere',
        1902: 'Noble',
        1903: 'Lanzini',
    },
    20: {
        2001: 'Moutinho',
        2002: 'Neves',
        2003: 'Jota'
    }
}

Data = {
    1: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    2: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    3: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    4: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    5: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    6: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    7: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    8: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    9: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    10: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    11: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    12: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    13: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    14: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    15: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    16: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    17: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    18: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    19: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    20: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    21: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    22: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    23: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    24: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    25: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    26: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    27: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    28: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    29: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    30: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    31: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    32: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    33: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    34: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    35: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    36: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    37: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    },
    38: {
        101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1101: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1102: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1103: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1201: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1202: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1203: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1301: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1302: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1303: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1401: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1402: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1403: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1501: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1502: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1503: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1601: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1602: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1603: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1701: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1702: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1703: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1801: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1802: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1803: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1901: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1902: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        1903: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2001: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2002: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
        2003: {
            "assists": 0,
            "successful passes": 0,
            "unsuccessful passes": 0,
            "key passes": 0,
            "long balls": 0,
            "through balls": 0
        },
    }
}
