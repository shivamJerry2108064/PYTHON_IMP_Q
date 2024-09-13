
'''IMPORTANT'''

'''Q1 a)'''
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
    for i in range(len(l)):
        if(i % 2 == 0):
            temp = l[i+1]
            l[i+1] = l[i]
            l[i] = temp
    return tuple(l)


'''b) '''
def count_values_occurrences(d):
    '''Count the number of occurrences of each value in the dictionary.

    Args:
        d (dict): The input dictionary.

    Returns:
        dict: A dictionary where the keys are the values from the input dictionary, 
        and the values are their occurrence counts.

    Examples:
    >>> count_values_occurrences({'a': 1, 'b': 2, 'c': 1})
    {1: 2, 2: 1}
    >>> count_values_occurrences({1: 'x', 2: 'y', 3: 'x'})
    {'x': 2, 'y': 1}
    '''
    value_list = [d[key] for key in d.keys()]
    return {el: value_list.count(el) for el in value_list}



'''Q2 -'''
'''Define a function longest_common_prefix, that accepts a sentence of space seperated words as an input, 
and returns the longest common prefix among all the words of the sentence. If there's no common prefix, then you should return an empty string.'''
#Sol-
def longest_common_prefix(sentence: str) -> str:
    '''Find the longest common prefix among the given words of the sentence. 

    Args:
        sentence (str): A string of space sepearated words.
    Returns: 
        str: longest prefix. 
    '''
    l = sentence.split(" ")
    
    output = []
    for i in range(len(l)-1):
        res = []
        for k in range(min(len(l[i]),len(l[i+1]))):
            if(l[i][k] == l[i+1][k]):
                res.append(l[i][k])
        output.append("".join(res))
    
    return min(output , key = len)

print(longest_common_prefix('flower flow flight'))




