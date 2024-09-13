
'''Question'''

'''You are given a list of dictionaries overs where each dictionary corresponds to a single over bowled by a bowler. Each over contains:

Bowler name as key.
Value associated with this key is a list of events for the over, where each event could be:
An integer value {1, 2, 3, 4, 6} indicating runs scored on that ball.
'W' indicating a wicket taken on that ball.
'Wd' indicating a wide ball, which incurs 1 extra run.
'Nb[i]' indicating a no-ball, where i represents runs scored on that ball, and incurs 1 extra run in addition to the runs from the no-ball itself.
Each over has 6 valid balls (ie. excluding extras like wide and no-balls).

One of the entry is given for your reference:

{'Ashwin': [1, 1, 0, 'W', 'Wd', 6, 'Nb[4]', 0]}'''

# overs = [
# {"Shaheen Afridi": [4, 0, 2, 'W', 6, 'Nb[2]', 1]},
# {"Hasan Ali": [6, 4, 1, 'W', 0, 2]},
# {"Haris Rauf": [1, 4, 0, 6, 2, 'W']},
# {"Shaheen Afridi": ['W', 'Wd', 'Wd', 6, 1, 4, 0, 2]},
# {"Hasan Ali": [4, 6, 'W', 'Wd', 'Nb[6]', 0, 2, 1]},
# {"Haris Rauf": [2, 1, 6, 4, 0, 'W']},
# {"Shaheen Afridi": [2, 1, 'W', 'Nb[0]', 4, 6, 'W']},
# {"Hasan Ali": [1, 2, 'W', 6, 4, 0]},
# {"Haris Rauf": [6, 0, 4, 1, 2, 'W']}
# ]

overs = [
{'Bumrah': [1, 2, 'W', 0, 2, 'Wd', 0]},
{'Shami': ['Nb[4]', 2, 1, 0, 'W', 'Wd', 'Wd', 4, 0]},
{'Ashwin': [1, 4, 0, 3, 2, 1]},
{'Shami': ['W', 2, 0, 0, 'Wd', 2, 6]},
{'Bumrah': ['W', 'W', 1, 1, 0, 0]}
]

def best_performers(overs: list) -> list:
    '''Given a list of dictionaries, generate a ranking board, based on wickets taken and economy of the bowler.
    The output should be list of tuples, sorted on the basis of ranking of bowler.

    Args:
        overs (list[dict]): list of dictionaries, where each dictionary represents the performance of a bowlers in a over. 

    Returns:
        list of tuples - where each entry has format: (bowler_name, wickets, economy_rate).
    '''
    names_list = list(set(key for dictionary in overs for key in dictionary))
    
    dict_update = {el : [] for el in names_list}
    {dict_update[key].append(over_dict[over_key]) for over_dict in overs for over_key in over_dict for key in dict_update if over_key == key}
    print(dict_update)
    
    
    def wicket_count(l:list):
        wickets = sum([l[i].count('W') for i in range(len(l))])
        return wickets

    def economy_rate(l:list):
        runs = 0
        for i in range(len(l)):
            for j in range(len(l[i])):
                if(l[i][j] == 'Wd'):
                    runs += 1
                elif((str(l[i][j]))[:2] == 'Nb'):
                    runs += 1
                    runs += int((str(l[i][j]))[-2])
                elif(l[i][j] == 'W'):
                    runs += 0
                else:
                    runs += int(l[i][j])
        return round(runs / len(l), 2)


    l = [(key , wicket_count(dict_update[key]) , economy_rate(dict_update[key])) for key in dict_update]
    return l

print(best_performers(overs))



