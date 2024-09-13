'''Q1'''

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
    # product = 1
    # for i in range(len(str(n))):
    #     product *= int(str(n)[i])
    # print(product)

    product = 1

    while(n > 0):
        remainder = n % 10
        product *= remainder 
        n = n // 10
    print(product)

digit_product(123)


'''Q2'''
def capitalize_first_and_last(sentence: str) -> str:
    '''Capitalize the first and last characters of each word of the sentence.

    Args:
        sentence (str): Input string sentence of space seperated words. 

    Returns:
        str: The string with the first and last characters of each word capitalized.

    Examples:
    >>> capitalize_first_and_last("hello world")
    'HellO WorlD'
    >>> capitalize_first_and_last("python programming")
    'PythoN ProgramminG'  '''
    
    res = []
    for el in sentence.split(" "):
        word = el[0].capitalize() + el[1:-1] + el[-1].capitalize()
        res.append(word)

    return " ".join(res)

print(capitalize_first_and_last('hello world'))


'''Q3-'''  # IMPORTANT
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
    count = 0
    words_sorted = sorted(words , key = len , reverse= True)

    for i in range(len(words)):
        count += 1
        if(count == k):
            return words_sorted[i]

print(kth_longest_word(['a', 'abc', 'abcd', 'ab'] , 4))   # 3rd longest word 



'''Q4 - '''
def unflatten(t: tuple, m: int, n: int) -> tuple:
    '''Given a flat tuple of length m*n, convert it into a tuple of tuples 
    with dimensions m x n.

    Args:
        t (tuple): Flat tuple of length m*n.
        m (int): Number of rows in resulting tuple of tuples.
        n (int): Number of columns in resulting tuple of tuples. 

    Returns:
        tuple: A tuple of tuples with dimension m x n. 

    Examples:
    >>> unflatten((1, 2, 3, 4, 5, 6), 2, 3)
    ((1, 2, 3), (4, 5, 6))
    >>> unflatten((1, 2, 3, 4), 2, 2)
    ((1, 2), (3, 4))  '''
    
    res = []
    for i in range(m):
        temp_l = []
        for j in range(n):
            temp_l.append(t[j])
        res.append(tuple(temp_l))
        t = t[j+1:]
    
    return tuple(res)

print(unflatten((1,2,3,4,5,6),2,3))



'''Q5 -'''
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
    word_list_lower = [el.lower() for el in sentence.split(" ")]
    
    flag = False
    for i in range(len(word_list_lower)):
        for j in range(len(word_list_lower[i])):
            if((sentence.lower()).count((word_list_lower[i][j]).lower()) == 1):
                flag = True
            else:
                flag = False
                break

    return True if flag else False

print(is_heterogram('The big dwarf only jumps'))


'''Q6 -'''
def filter_keys_by_value(d: dict, threshold: int) -> None:
    '''Filter the dictionary keys where the value is greater than the given threshold.
    Modify the dictionary in place, do not return a new dictionary.

    Args:
        d (dict): The input dictionary.
        threshold (int): The threshold value.

    Returns:
        None
    >>> d = {'a': 1, 'b': 5, 'c': 3}
    >>> filter_keys_by_value(d, 3)
    >>> d
    {'b': 5}   '''

    for key in d.copy():
        if(d[key] <= threshold):
            del d[key]
    print(d)

filter_keys_by_value({'a':1 , 'b': 5, 'c': 3} , 3)

