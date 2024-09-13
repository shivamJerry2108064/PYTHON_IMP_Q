'''Q1 IMPORTANT'''

def top_k_teams(batsmen: list, k: int) -> list:
    '''
    Given a list of dictionaries with batsman names, runs, and team names,
    Create a list with the top k teams in terms of total runs 
    starting from the highest to the lowest runs.

    Assume no two teams have the same number of runs.

    Arguments:
    batsmen: list of dict - list containing dictionaries with keys 'name', 'runs', and 'team'
    k: int - number of top teams to return

    Return:
    list - top k teams in terms of total runs
    '''
    temp_dict = {d['team'] : [] for d in batsmen}
    {temp_dict[d['team']].append(d['runs']) for d in batsmen}
    
    main_dict = {d['team'] : sum(temp_dict[d['team']]) for d in batsmen}
    value_list = sorted([main_dict[key] for key in main_dict] , reverse = True)
    # print(value_list)
    
    res = []
    for el in value_list[:k]:
        for key in main_dict:
            if(el == main_dict[key]):
                res.append(key)
                
    return res



'''Q2 -'''
'''
Given a m x n matrix, find the index of the row with the maximum number of zeros. Assume there will be only one row with the maximum number of zeros.

Example

[
    [1,0,1,4,1],
    [1,5,1,1,2],
    [2,0,2,0,3],
    [3,0,0,0,4],
]
The 4th row(index 3) has the maximum number of zeros, so the answer is 3.'''

#Sol-
def row_index_with_most_number_of_zeros(matrix:list)->int:
    '''
    Given a matrix, find the index of the row with the 
    maximum number of zeros in it.

    Arguments: matrix: list[list] 
    Rertun: int - index of the row with the maximum number of zeros.
    '''
    max_zero_idx = -1
    ans = 0
    for i in range(len(matrix)):
        count = matrix[i].count(0)
        if(count > max_zero_idx):
            max_zero_idx = count
            ans = i
            
    return ans



'''Q3'''
def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    '''
    Given a string, check if all the odd indices are alphabets and the even indices are digits.

    Note: indices starts from 0.

    Arguments:
    string: str - the input string

    Return:
    bool - True if all odd indices are alphabets and even indices are digits, else False
    '''
    flag = False
    for i in range(len(string)):
        if(((i % 2 != 0) and (string[i].isalpha())) or ((i % 2 == 0) and (string[i].isdigit()))):
            flag = True
        else:
            flag = False
            break
    
    return True if flag else False

print(is_odd_indices_alpha_and_even_indices_digits('1a2b3c'))



'''Q4 -'''
'''a) '''
def swap_even_and_odd_indices(l: list) -> None:
    '''
    Given a list of integers, swap the values at the even indices
    and the odd indices by modifying the same list.

    Arguments:
    l: list - the input list of integers

    Return:
    None - the input list is modified inside the function.
    '''
    for i in range(len(l)):
        if(i % 2 == 0):
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
    return l


'''b)'''
def unique_chars_present_in_first_not_in_second(s1: str, s2: str) -> set:
    '''
    Given two words as strings, find the unique 
    chars that are present in the first word but not in 
    the second word.

    Assume all characters in the input are in lowercase.

    The order of elements in the set doesn't matter while returning.

    Eg. water, watch -> {'e','r'}

    Arguments:
    s1: str - the first string
    s2: str - the second string

    Return:
    set - the unique characters present in the first string but not in the second string
    '''
    return set(s1) - set(s2)

unique_chars_present_in_first_not_in_second('abcdef' ,'def')



'''Q5 - '''
def repeat(t: tuple) -> tuple:
    '''
    Given a tuple of length two, say (a,b), create a tuple 
    with a repeated b number of times and b repeated a number of times.

    E.g., repeat((2, 3)) ->  (2, 2, 2, 3, 3)

    Arguments:
    t: tuple - a tuple of two integers (a, b)

    Return:
    tuple - a new tuple with a repeated b times followed by b repeated a times
    '''
    string = ",".join((str(t[0])*t[1]) + str(t[1])*t[0])[::2]    # '22233'
    t = tuple(int(string[i]) for i in range(len(string)))
    
    return t

print(repeat((2,3)))
