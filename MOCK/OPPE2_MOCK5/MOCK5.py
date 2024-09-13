'''QUESTIONS'''

'''Q1- a)'''
def pair_elements(t1: tuple, t2: tuple) -> tuple:
    '''
    Given two tuples of equal length, create a new tuple where each element
    is a pair from the corresponding elements of the input tuples.

    Arguments:
    t1: tuple - the first tuple
    t2: tuple - the second tuple of the same length as t1

    Return:
    tuple - a new tuple where each element is a pair from the corresponding
            elements of the input tuples

    Example:
    >>> pair_elements((1, 2, 3), ('a', 'b', 'c'))
    ((1, 'a'), (2, 'b'), (3, 'c'))
    >>> pair_elements((4, 5), (6, 7))
    ((4, 6), (5, 7))
    '''
    return tuple((t1[i],t2[i]) for i in range(len(t1)))



'''b) '''
def unique_vowels(s: str) -> set:
    '''
    Given a string, return a set of unique vowels present in the string.

    Arguments:
    s: str - the input string

    Return:
    set - a set of unique vowels present in the string

    Example:
    >>> unique_vowels('aeiou')
    {'u', 'i', 'o', 'e', 'a'}
    '''
    return set(s) & set('aeiouAEIOU')



'''c) '''
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
    if(n == 0):
        return 1
    if(n > 0):
        fact = 1
        for i  in range(n,0,-1):
            fact *= i
        return fact
    else:
        n = str(n)[1:]
        fact = 1
        for i  in range(int(n),0,-1):
            fact *= i
        return -fact
    


'''Q2) '''
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
    for i in range(len(lst)):
        if((i + shift) >= len(lst)):
            lst[(i + shift) % len(lst)] = l_copy[i]
        else:
            lst[(i + shift)] = l_copy[i]
    
    return lst


'''Q3-'''
def sort_tuples_by_second_then_third(input_list):
    """
    Args:
        input_list (list): The list of tuples to sort.
    Returns:
        list: The sorted list of tuples.
    """
    return sorted(input_list ,key = lambda x : (x[1] , x[2] , x[0]))



'''Q4-'''
def calculate_total_spent(filename):
    '''
    Args:
        filename (str): The path to the file containing transaction data.

    Returns:
        dict: A dictionary where keys are customer names and values are the total amount spent.
    '''
    f = open(filename , 'r')
    
    d = {}
    for line in f.readlines():
        l = (line.strip()).split(",")
        Name , spent , date = l[0] , float(l[1]) , l[2]
        
        # print(l)
        if(Name in d):
            d[Name] += spent
        else:
            d[Name] = spent
    return d

    

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
    for i in range(len(lst)):
        if((i + shift) >= len(lst)):
            lst[(i + shift) % len(lst)] = l_copy[i]
        else:
            lst[(i + shift)] = l_copy[i]
    
    return lst


def sort_tuples_by_second_then_third(input_list):
    """
    Args:
        input_list (list): The list of tuples to sort.
    Returns:
        list: The sorted list of tuples.
    """
    return sorted(input_list ,key = lambda x : (x[1] , x[2] , x[0]))
    
