
'''Questions'''

'''Q1 a)'''
def second_largest(lst: list) -> int:
    '''
    Given a list of integers, return the second largest number in the list.
    Consider that list contains at least two integers.

    Arguments:
    lst: list - the input list of integers

    Return:
    int - the second largest number in the list

    Example:
    >>> second_largest([1, 2, 3, 4, 5])
    4
    '''
    return sorted(lst , reverse = True)[1]



'''b) '''
def not_present_in_both(lst1: list, lst2: list) -> list:
    '''
    Given two lists, return a list containing the items 
    that are present in either list 1 or list 2 but not in both.

    Arguments:
    lst1: list - the first list 
    lst2: list - the second list 

    Return:
    set - a set containing the items present in either list 1 or list 2 but not in both

    Example:
    >>> symmetric_difference([1, 2, 3], [3, 4, 5])
    {1, 2, 4, 5}
    '''
    return (set(lst1) | set(lst2)) - (set(lst1) & set(lst2))



'''c) '''
def modify_string_1(s: str) -> str:
    '''
    Given a string, Seperate the characters present in odd and even indices
    and return the merged string with even indices first and odd indices second in reverse order.

    Arguments:
    s: str - the input string

    Return:
    str - modified string

    Example:
    >>> modify_string_1('abcde')
    'acedb'
    >>> modify_string_1('python')
    'ptonhy'
    '''
    return s[::2] + s[1::2][::-1]



'''d) '''
def average_of_numbers(lst: list) -> float:
    '''
    Given a list containing integers, floats, and strings, return the average 
    of the integers and floats, rounded to two decimal points. If neither 
    integers nor floats are present, return -1.

    Arguments:
    lst: list - a list containing integers, floats, and strings

    Return:
    float - the average of the integers and floats rounded to two decimal points,
            or -1 if no integers or floats are present

    Example:
    >>> average_of_numbers([1, 2.5, 'a', 3, 'b'])
    2.17
    >>> average_of_numbers(['a', 'b', 'c'])
    -1
    '''
    l = []
    for el in lst:
        if((type(el) == int) or (type(el) == float)):
            l.append(el)
            
    if(len(l) == 0):
        return -1
    else:
        return round((sum(l)/len(l)),2)
    


'''Q2 -'''
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
    d = {el : lst.count(el) for el in lst}
    max_val_l = max([d[key] for key in d])
    
    res = []
    for key_i in d:
        for key_j in d:
            if((key_i != key_j) and (d[key_i] == d[key_j]) and (d[key_i] == max_val_l)):
                res.append(max(key_i , key_j))
        
    return max(res) if res else max(d , key = d.get)



'''Q3 -'''
def most_frequent_alpha_character(filename: str) -> str:
    '''
    Arguments:
    filename: str - name of the file

    Return:
    list - the most frequent alphabetic characters (case-sensitive)
    '''
    f = open(filename , 'r')
    
    res = []
    for line in f.readlines():
        l = (line.strip()).split(" ")

        temp_l = []
        for i in range(len(l)):
            for j in range(len(l[i])):
                if((l[i][j]).isalpha()):
                    temp_l.append(l[i][j])
        
        d = {x : temp_l.count(x) for x in temp_l}
        val_l = [d[key] for key in d]
        
        for key in d:
            if(d[key] == max(val_l)):
                res.append(key)
                
    res_d = {k : res.count(k) for k in res}
    val_res_d = [res_d[key] for key in res_d]
    
    output = []
    for key in res_d:
        if(res_d[key] == max(val_res_d)):
            output.append(key)
    
    return output


def valid_substring(s: str, word_list: list) -> bool:
    '''
    Arguments:
    s: str - the string to be checked
    word_list: list - a list of valid words

    Return:
    bool - True if the string can be split into two valid words, False otherwise
    '''
    mid = len(s) // 2
    part1 = s[:mid]
    part2 = s[mid:]
    
    return True if((part1 in word_list) and (part2 in word_list)) else False