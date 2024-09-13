'''Q'''
def swap_adjacent_elements(t):
    '''Swap every pair of adjacent elements in the tuple.

    Args:
        t (tuple): A tuple of even length.

    Returns:
        tuple: A new tuple with adjacent elements swapped.

    Examples:
    >>> swap_adjacent_elements((1, 2, 3, 4, 5, 6))
    (2, 1, 4, 3, 6, 5)
    >>> swap_adjacent_elements(('a', 'b', 'c', 'd'))
    ('b', 'a', 'd', 'c')
    '''
    l = list(t)
    for i in range(len(t)):
        if(i % 2 == 0):
            temp = l[i+1]
            l[i+1] = l[i]
            l[i] = temp
    return tuple(l)

print(swap_adjacent_elements((1,2,3,4,5,6)))


'''Q'''  # VIEW
def longest_common_prefix(sentence: str) -> str:
    '''Find the longest common prefix among the given words of the sentence. 

    Args:
        sentence (str): A string of space sepearated words.
    Returns: 
        str: longest prefix. 
    '''
    l = sentence.split(' ')

    res = []
    for i in range(len(l)-1):
        temp = []
        for j in range(min(len(l[i]) , len(l[i+1]))):
            if(l[i][j] == l[i+1][j]):
                temp.append(l[i][j])
        res.append("".join(temp))
        print(res)
    
    return min(res , key = len)

print(longest_common_prefix('flower flow flight'))        


'''IMPORTANT'''  # VIEW
def is_heterogram(sentence: str) -> bool:
    '''Check if a given sentence is a heterogram or not. 

    A heterogram is a word, phrase, or sentence in which no letter of the alphabet occurs more than once.

    Ignore the multiple occurences of space.

    Args:
        s (str): The input sentence. 

    Returns:
        bool: True if the sentence is heterogram, False otherwise.

    Examples:
    >>> is_heterogram('The big dwarf only jumps')
    True
    >>> is_heterogram('Blue bat')
    False
    >>> is_heterogram('Hello World')
    False
    '''
    word = sentence.split(" ")
    
    flag = False
    for i in range(len(word)):
        for j in range(len(word[i])):
            if((sentence.lower()).count((word[i][j]).lower()) <= 1):
                flag = True
            else:
                flag = False 
                break

    return True if flag else False

print(is_heterogram('blue Bat'))



def kth_longest_word(words: list, k: int) -> str:
    '''Find the k-th longest word in a list of words where each word has a unique length.

    Args:
        words (list): The list of words.
        k (int): The position (1-based) of the longest word to find.

    Returns:
        str: The k-th longest word in the list.

    Examples:
    >>> kth_longest_word(['apple', 'banana', 'cherry', 'date'], 2)
    'apple'
    >>> kth_longest_word(['elephant', 'dog', 'cat', 'hippopotamus'], 1)
    'hippopotamus'
    >>> kth_longest_word(['a', 'abc', 'abcd', 'ab'], 3)
    'ab'
    '''
    return sorted(words , key = len , reverse = True)[k-1]
print(kth_longest_word(['a','abc','abcd', 'ab'] , 3))   # if k = 2 then words[2] == 3rd longest word 

def digit_product(n: int) -> int:
    '''Calculate the product of the digits of an integer.

    Args:
        n (int): The integer whose digits are to be multiplied.

    Returns:
        int: The product of the digits.

    Examples:
    >>> digit_product(123)
    6
    >>> digit_product(101)
    0
    '''
    ans = 1
    while(n > 1):
        rem = n % 10
        ans *= rem
        n = n // 10
    return ans
print(digit_product(123))


def unique_vowels(s: str) -> set:
    '''
    Given a string, return a set of unique vowels present in the string.

    Arguments:
    s: str - the input string

    Return:
    set - a set of unique vowels present in the string

    Example:
    >>> unique_vowels('aeiou')
    {'u', 'i', 'o', 'e', 'a'}'''

    return set(s) & set('aeiouAEIOU')
print(unique_vowels('abeicouAbEiorhwIOU'))



# VIEW
def factorial(n: int) -> float:
    '''
    Find the factorial of the given number
    Note: Factorial of 0 is 1

    Arguments:
    n: integer 

    Return:
    int - factorial of the given number

    Example:
    >>> factorial(5)
    120
    >>> factorial(-5)
    -120
    '''
    if(n ==1):
        return 1
    
    if(n > 0):
        fact = 1
        for x in range(n,0,-1):
            fact *= x
        return fact
    
    if(n < 0):
        n_str = str(n)[1:]
        fact = 1
        for i in range(int(n_str) , 0 , -1):
            fact *= i
        return -fact
print(factorial(-5))

def sort_tuples_by_second_then_third(input_list):
    """
    Args:
        input_list (list): The list of tuples to sort.
    Returns:
        list: The sorted list of tuples.
    """
    return sorted(input_list , key = lambda x : (x[1] , x[2], x[0]))





'''level 2'''
def rotate_list(lst: list, k: int) -> list:
    '''
    Given a list of items and an integer k, rotate the list to the right by k steps.

    Arguments:
    lst: list - a list of items
    k: int - the number of steps to rotate the list to the right

    Return:
    list - the rotated list
    '''
    shift = k % len(lst)
    l_copy = lst.copy()

    for i in range(len(l_copy)-1):
        if((i+ shift) >= len(l_copy)):
            lst[(i+shift) % len(l_copy)] = l_copy[i]
        else:
            lst[(i+shift)] = l_copy[i]
    return lst

print(rotate_list([1,2,3,4,5] , 2))


def most_frequent_alpha_character(filename: str) -> str:
    '''
    Arguments:
    filename: str - name of the file

    Return:
    list - the most frequent alphabetic characters (case-sensitive)
    '''
    f = open(filename, 'r')
    
    res = []   # list of el of most occurence in each line
    for line in f.readlines():
        temp = []
        word_list = (line.strip()).split(' ')
        for i in range(len(word_list)):
            for j in range(len(word_list[i])):
                temp.append(word_list[i][j])
        
        temp_d = {el : temp.count(el) for el in temp}
        val_temp_d = [temp_d[key] for key in temp_d]
        for key in temp_d:
            if(temp_d[key] == max(val_temp_d)):
                res.append(key)
        # print(temp)
        # print(res)
    res_d = {el : res.count(el) for el in res}
    val_res_d = [res_d[key] for key in res_d]
    # print(res_d)
    output = []
    for key in res_d:
        if(res_d[key] == max(val_res_d)):
            output.append(key)
    
    return output

print(most_frequent_alpha_character('test.csv'))





def most_frequent_element(lst: list) -> int:
    '''
    Arguments:
    lst: list - a list of integers

    Return:
    int - the integer that occurs most frequently, or the largest one
          if there are multiple with the same frequency

    Example:
    >>> most_frequent_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    4
    '''



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


'''Question''' # VERY IMPORTANT
'''A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of square of its digits.
Repeat the process until the number equals 1(where it will stay), or it loops endlessly in a cycle that doesn't include 1.
Those numbers for which the process ends in 1 are happy.
Example1:

19 is a happy number.

Explanation:

$1^{2} + 9^{2} = 82$

$8^{2} + 2^{2} = 68$

$6^{2} + 8^{2} = 100$

$1^{2} + 0^{2} + 0^{2} = 1$

Example2:

4 is not a happy number.
The cycle for 4 is as follows:

# Important line
$4 \rightarrow 16 \rightarrow 37 \rightarrow 58 \rightarrow 89 \rightarrow 145 \rightarrow 42 \rightarrow 20 \rightarrow 4$ (and same seq repeats)
if any of above repeats then 4 is not a happy number , here 4 itself repeats and then from 4 onwards 16 , 37... again

Define a function n_happy_numbers that accepts a list of positive integers and returns the count of happy numbers in the given list.'''


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