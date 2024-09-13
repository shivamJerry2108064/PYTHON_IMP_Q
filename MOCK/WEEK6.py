'''Q1'''
'''a) '''
# dict with list as values
def get_all_batsman_runs():
    '''
    Given the batsman name and the comma separated runs 
    where both are seperted by a hypen in multiple lines, 
    create a dictionary with batsman name and list of runs as value.
    The number of lines is given in the first line

    Input format:
    3
    batsman1-1,2,1,4,6,2,2,1
    batsman2-2,2,6,4,1
    batsman3-6,1,2,4,4,2

    Return: dict[str,list[int]] - with batsman name as key and list of runs as values
    '''
#     n = int(input())
#     d = {}
#     for i in range(n):
#         data = input().split("-")
#         subdata_int = [int(el) for el in data[1].split(",")]
#         d[data[0]] = subdata_int
#     return d

# print(get_all_batsman_runs())


'''b) ''' # VIEW
def get_student_marks():
    '''
    Given the student rollno, city, age,
    course1_marks, course2_marks and course3_marks 
    as comma separated values over multiple lines,
    create a list of dict with the above attributes as keys 
    and the corresponding value as values.
    The number of lines is given in the first line

    Input Format:
    n
    1,citya,23,86,69,86
    2,cityb,19,78,65,89
    ...
    n,cityx,35,89,57,76

    Return: 
    student_data - list[dict]: where each dict would be 

    {'rollno':int, 'city':str,'age':int, 
    'course1':int, 'course2':int, 'course3':int}
    '''
    # attribute_list = ['rollno','city','age','course1','course2','course3']

    # n = int(input())

    # l = []
    # for i in range(n):
    #     data_str = input().split(",")
    #     data = []
    #     for el in data_str:
    #         if(data_str.index(el) == 1):
    #             data.append(el)
    #         else:
    #             data.append(int(el))

    #     d = {attribute_list[j] : data[j] for j in range(len(attribute_list))} 
    #     l.append(d)
    # return l
# print(get_student_marks())


'''c'''
# list of dicts    # VIEW
def get_student_data_over_multiple_lines():
    '''
    Given each attribute as described above in given over multiple lines 
    and multiple entries are given create a dictionary as described above.

    Input format:
    n
    1
    citya
    23
    86
    69
    86
    2
    cityb
    19
    78
    65
    89
    ...
    n
    cityx
    35
    89
    57
    76
    '''
    key_list = ['rollno','city','age','course1','course2','course3']
    n = int(input('n'))

    data_list = []
    for i in range(n):
        inner_list = []
        for j in range(len(key_list)):
            data = input()
            inner_list.append(data)
        data_list.append(inner_list)
    
    l = []
    for p in range(len(data_list)):
        d = {}
        for q in range(len(key_list)):
            if(q == 1):
                d[key_list[q]] = data_list[p][q]
            else:
                d[key_list[q]] = int(data_list[p][q])
        l.append(d)
    return l
        
# print(get_student_data_over_multiple_lines())



'''Q4 -'''
# a)
def display_float_nums_over_multiple_lines(nums:list):
    '''
    Given a list of floating point nums print them 
    over multiple lines with 3 digits after the decimal point.
    For example, if nums = [1.2, 3.4,5.6,7.8]

    Output format:
    1.200
    3.400
    5.600
    7.800
    '''
    for el in nums:
        print(f"{el:.3f}")

display_float_nums_over_multiple_lines([1.2, 3.4, 5.6, 7.8])


# b)
def get_election_winner(votes:dict)->str:
    '''
    Given a dictionary with candidate name as key and number of votes as values,
    Find the winner of the election who has the maximum votes

    Arguments: votes - dict[str, int]
    Return: winner - str'''
    return max(votes , key = votes.get)

print(get_election_winner({'Anish': 1234, 'Aswhin': 2314, 'Aditi': 3145, 'Afnan': 3000}))


'''Q5 ''' #IMPORTANT 
import random
def display_random_ints(seed:int):
    '''
    Given a random seed, set the random seed and 
    generate multiple random integers within the range [0,100] 
    (using randint(0,100)), until 0 is encountered and 
    print it with max 10 comma seperated ints per line over multiple lines

    Output format
    34,26,73,82,35,36,7,4,27,46
    6,33,62,78,0
    '''
    random.seed(seed)

    while True:
        line = []
        for i in range(10):
            n = random.randint(0,100)
            line.append(n)
            if(n == 0):
                break
        
        line_str = list(map(lambda x: str(x), line))
        print(",".join(line_str))

        if(n == 0):
            break
        
display_random_ints(1)


'''Q6 -'''
# IMPORTANT : lhs , rhs and sorted
def sorted_num_count(nums:list) -> int:
    '''
    Given a list of nums(int) find the count of sorted numbers in the list.

    Arguments: nums - list[int]
    Return: count - int
    '''
    count = 0
    for el in nums:
        lhs = str(el)
        rhs = "".join(sorted(lhs))

        if(lhs == rhs):
            count += 1
    return count

print(sorted_num_count([123,456,765,32,23,1]))


'''Q7 ''' # IMPORTANT
def common_substring(words:list)->str:
    '''
    Given a list of words check whether there is a word in words 
    that is a substring of all other words.
    If there is a word return that word else return None

    Hint: only the smallest word can be a substring of all other words.

    Arguments: words - list[str]
    Return: common_substr_word - str
    '''
    smallest_word = min(words , key = len)    # important line
    
    flag = False
    for el in words:
        if(smallest_word in el):
            flag = True
        else:
            flag = False

    return smallest_word if flag else None


print(common_substring(['mantle', 'man', 'mango', 'raman', 'manager', 'manage']))



'''Q8'''
def validate_phone_numbers(phone_nos:list)->dict:
    '''
    Given a list of phone numbers, create a dict with 
    phone numbers as keys and the string "VALID" or "INVALID"
    depending on the validity of the phone number as described by the above funtion.

    Arguments: phone_nos - list
    Return: validity_dict - dict[int,str]'''
    def is_valid_phone_number2(el):
        def check_repeat(el):
            l = [0,1,2,3,4,5,6,7,8,9]

            for x in l:
                if(el.count(str(x)) > 5):
                    return False
            return True
        return ((len(el) == 10) and (el.startswith('98123')) and (check_repeat(el)))

    d = {str(el) : 'VALID' if is_valid_phone_number2(str(el)) else 'INVALID' for el in phone_nos}
    return d

print(validate_phone_numbers([9812301234, 9812378321, 9812333333, 9123456789, 98123456789]))




'''Q9'''
def misspelt_words(vocab:str, sentence:str)->list:
    '''
    Given a comma separated string of vocabulary, and a space separated string sentence,
    return a list of misspelt words in the order they occur in the sentence.

    The words which are not in the vocabulary are considered misspelt.

    Arguments: 
        vocab - str: comma separated string with vocabulary
        sentence - str: space separated string of sentence
    Return:
        misspelt_words - list'''
    sentence_list = sentence.split(" ")
    vocab_list = vocab.split(",")

    return [sentence_list[i] for i in range(len(sentence_list)) if sentence_list[i] not in vocab_list]
    
vocab="a,good,faith,time,here,are,coming,you"
sentence="aree you comin here"

print(misspelt_words(vocab , sentence))
    



'''Q10 - '''
def count_sock_pairs(sock_colors:list)->int:
    '''
    Given a list of sock colors representing the color of each sock, 
    find the number of sock pair (both having same color) is there.
    Eg. ["red","blue","green","green","red","green","red","red","blue","black"] 
    2 red+ 1 green+ 1 blue = 5 pairs

    Arguments: sock_colors - list: of sock colors
    Return: number of pairs of sock - int
    '''
    unique_colors = sorted(set(sock_colors))
    
    pairs = 0
    for el in unique_colors:
        count = sock_colors.count(el)

        pairs += (count // 2)
    return pairs

print(count_sock_pairs( [
'green', 'black', 'blue', 'black', 'green',
'red', 'white', 'blue', 'white', 'blue', 'green'
]))



'''Q11''' # VERY IMPORTANT
def vowely_count(words:list)->int:
    ''' Given a list of words find the number of vowely words from the list. 
    A word is vowely if 
    - it has all the vowels in it.
    - the vowels occur in ascending order. 

    Arguments: words :list[str]   Return: int - number of vowely words'''

    vowels = ['a','e','i','o','u']
    count = 0

    for word in words:
        result = []
        for i in range(len(word)):
            if(word[i] in vowels):
                result.append(word[i])
        if(result == vowels):           # if true : means words has all words in it and ordered in ascending order
            count += 1
    return count

print(vowely_count(['abecidofu', 'tripe', 'abxyepiforu', 'uredfzxn', 'aqetiol', 'eviaoqu']
))



'''Q12'''
def double_palindromes(n:int)->list:
    '''
    Given a number n, find all the positive integers till n (including)
    that are double_palindrome. A number is double palindrome if 
    it is a palindrome and its square is a palindrome.

    Eg. 
    8 - palindrome, not double palindrome
    11 - palindrome and double palindrome
    12 - not palindrome and not double palindrome

    Arguments: n - int: range of numbers to search
    Return: list of integers which are double palindrome in the ascending order
    '''
    num_list = [x for x in range(1,n+1)]
    single_palindrome = [x for x in num_list if(x == int(str(x)[::-1]))]
    return [x for x in single_palindrome if(x**2 == int(str(x**2)[::-1]))]

print(double_palindromes(15))

    

'''Q14 '''  # USE OF ZIP
def scores_spx(k:list, g:list):
    '''
    Given the series of moves played by Kakashi and Guy in a Stone-Paper-Scissor game,
    find the scores of Kakashi and guy respectively.
    Rules - Stone beats Scissor, Scissor beats Paper and Paper beats Stone
    Score - Number of times won
    Symbols - Stone - S, Paper - P, Scissor - X

    Arguments: 
    kakashi_moves and guy_moves - list of moves where each move 
        is a string corresponding to the symbol

    Return: kakashi_score:int , guy_score:int
    '''
    k_score , g_score = 0 , 0
    rules = {'S':'X' , 'X':'P' , 'P':'S'}

    for k_move , g_move in zip(k,g):
        if(k_move == g_move):
            continue      # skip the same moves(data) 
        if(rules[k_move] == g_move):
            k_score += 1
        else:
            g_score += 1

    return k_score , g_score


k_moves = ['S', 'X', 'P', 'X', 'P', 'P', 'S', 'P', 'X']
g_moves = ['P', 'X', 'X', 'S', 'X', 'P', 'S', 'S', 'X']
print(scores_spx(k_moves , g_moves))



'''Q15 a) '''
def swap_first_and_last_chars(s):
    '''Swap the first and last characters of a string.

    Args:
    s (str): The input string.

    Returns:
    str: The string with first and last characters swapped.

    Examples:
    >>> swap_first_and_last_chars("hello")
    'oellh'   '''
    
    return s[-1] + s[1:-1] + s[0]
    
print(swap_first_and_last_chars('hello'))


'''b) '''
def are_alternate_positions_equal(t):
    """Check if the elements at alternate positions in the tuple are equal.
    Assume even number of elements in the tuple.

    Args:
    t (tuple): The input tuple.

    Returns:
    bool: result as True or False"""

    for i in range(0,len(t)-1,2):
        if(t[i] != t[i+1]):
            return False
    return True

print(are_alternate_positions_equal((1,1,2,0,3,3)))


'''c) '''
def has_all_values(l, s):
    '''Check if all numbers from a list are present in a set.

    Args:
    l (list): The input list of numbers.
    s (set): The input set of numbers.

    Returns:
    bool: result as True or False

    Examples:
    >>> has_all_values([1, 2, 3, 4, 4, 3, 2, 1], {1, 2, 3, 4})
    True'''
    sorted_set_l = sorted(set(l))
    sorted_s = sorted(s)

    return sorted_s == sorted_set_l

print(has_all_values([1, 2, 3, 4, 4, 3, 2, 1],{1,2,3,4}))


'''d) '''
"""Swap the key and value for a given key in a dictionary.
    Modify the dictionary inplace do not return a new dictionary.

    Args:
    d (dict): The input dictionary.
    k: The key to swap.

    Returns:
    dict: The dictionary with the key and value swapped.

    Examples:
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> swap_key_and_value(d,'b')
    >>> d
    {2: 'b', 'a': 1, 'c': 3}    """

def swap_key_and_value(d , key):
    d[d[key]] = key
    del d[key]

    return d

d = {'a': 1, 'b': 2, 'c': 3}
print(swap_key_and_value(d , 'b'))




# IMPORTANT
'''Q16  a) '''
def n_hostile_pairs(L:list)->int:
    '''Given a list of integers, find the number of 
    `hostile_pairs` in the given list.

    Two positive integers are called hostile 
    if they have no common digits. 

    Args:
        L: list[int] - numbers to check

    Return:
        int - number of hostile pairs
    '''
    def hostile(x,y):
        return True if len(set(str(x)) & set(str(y))) == 0 else False
        
    count_pair = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if(hostile(L[i] , L[j])):
                count_pair += 1
    print(count_pair)

n_hostile_pairs([1234, 38706, 567, 89])


'''b) '''
def are_anagrams(words:list)->bool:
    '''
    Check if all the given words are anagrams.

    Args: words - list[str]: list of lowercase words

    Return: bool - True if all the words are anagrams, else False.
    '''
    l = ["".join(sorted(el)) for el in words]
    res = [True if(l[i] == l[i+1]) else False for i in range(len(l)-1)]
    return(all(res))

print(are_anagrams(['listen', 'silent', 'hello']))


n = input()

for i in range(int(n)):
    data_list = input().split(" ")

    sum = 0
    for i in range(len(data_list)-1):
        sum += abs(int(data_list[i]) - int(data_list[i+1]))
    
    perimeter_bar_graph = int(data_list[0]) + sum + int(data_list[-1]) + 2*(len(data_list))
    print(perimeter_bar_graph)