'''QUESTIONS'''

'''Q'''
'''You are given a list of dictionaries matches where each element of the list would correspond to a match result. 
Each match result contains the team involved, the winner and the goals scored by the winner team. 
One of the entry is given below for your reference:

{'team1': 'Brazil', 'team2': 'Argentina', 'goals1': 2, 'goals2': 1}
Define a function named get_leaderboard, that takes matches as input and returns the leaderboard.'''
#Sol-
def get_leaderboard(matches:list)->list: 
    '''Given a list of dictionaries, generate a leaderboard based on points and goal scored.
    The output should be a list of tuples starting from the top team to bottom one.

    Args:
        matches : list[dict]

    Returns: 
        list of tuples - where each entry should be in format: (TeamName, Points, GoalScored)
                         sorted from top team to bottom. 
    '''
    countries_list = sorted(set([d[key] for d in matches for key in d if(type(d[key]) == str)]))
    # print(countries_list)
    
    temp_dict = {}   # goals_dict
    for d in matches:
        for key in d:
            if(key == 'team1'):
                if(d[key] in temp_dict):
                    temp_dict[d[key]] += d['goals1']
                else:
                    temp_dict[d[key]] = d['goals1']
                
            if(key == 'team2'):
                if(d[key] in temp_dict):
                    temp_dict[d[key]] += d['goals2']
                else:
                    temp_dict[d[key]] = d['goals2']
    
    
    points_dict = {el : [] for el in countries_list}
    
    for d in matches:
        if(d['goals1'] > d['goals2']):
            points_dict[d['team1']].append(2)
        elif(d['goals1'] == d['goals2']):
            points_dict[d['team1']].append(1)
            points_dict[d['team2']].append(1)
        else:
            points_dict[d['team2']].append(2)
    
    points_dict = {key : sum(points_dict[key]) for key in points_dict}
    
    res_l = []
    for key1 in temp_dict:
        temp_l = []
        for key2 in points_dict:
            if(key1 == key2):
                temp_l.append(key1)
                temp_l.append(points_dict[key2])
                temp_l.append(temp_dict[key1])
        res_l.append(tuple(temp_l))
        
    # Sort the res_l first by points (desc), then by goals scored (desc)
    res_l.sort(key=lambda x: (x[1], x[2]), reverse = True)
    
    return res_l
                
            
                
    
                
            
'''Q'''
'''You are given a CSV file with following columns:

ID,Name,Gender,Region,Q1,Q2,Q3,Q4
Each row in the file (except header) represents the record of sales representatives, 
which includes their ID, Name, Gender, Region where they operate, and their sales figure of each quarter.

The variable filename represents the name of the file. 
Define a function named consistent_sales_increase that takes filename as argument and that returns the name of the region 
with the highest count of representatives whose sales figures are consistently increasing across quarters, i.e. Q1 < Q2 < Q3 < Q4.'''
#Sol

def consistent_sales_increase(filename):
    '''Return the name of the region with the highest count of representatives, 
    who have shown consistent sales growth across the quarters.

    Args:
        filename (str): path of the file. 

    Return:
        str: Name of the region with highest count of such representatives. 
    '''
    f = open(filename , 'r')
    f.readline()
    
    d = {}
    for line in f.readlines():
        ID , Name , Gender , Region , Q1, Q2, Q3, Q4 = (line.strip()).split(",")
        if((Q1 < Q2) and (Q2 < Q3) and (Q3 < Q4)):
            if(Region in d):
                d[Region] += 1
            else:
                d[Region] = 1
                
    return max(d , key = d.get)
