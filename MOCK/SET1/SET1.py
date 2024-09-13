
'''SET1 - OPPE1'''
'''Q1 - ''' # USE OF COPY()
def remove_keys_not_in_list(d: dict, l: list) -> None:
    '''
    Remove keys from a dictionary that are not present in a given list.
    The function modifies the dictionary in place and does not return anything.

    Note: 
        Modifying a dict while iterating over it will give an error in python. 
        So, make a copy of the dict keys and then iterate over it.

    Args:
        d (dict): The dictionary to modify.
        l (list): The list of keys to keep in the dictionary.

    Returns:
        None
    '''
    for key in d.copy():
        if(key not in l):
            del d[key]

remove_keys_not_in_list({1:'a', 2:'b', 3:'c', 4:'d' , 5:'e'},[7,6,5,4,3])



'''Q2'''  # IMPORTANT
'''
Given a list of strings, check if all strings follow the format where the same word is repeated exactly twice with a hyphen in-between them. The word repeated should not be empty.

Examples of correct format:

"fast-fast" - correct
"go-go" - correct
"yeah-yeah" - correct

Examples of incorrect format:  # IMPORTANT
"fast-slow" - incorrect (different words)
"fast-fast-fast" - incorrect (word repeated more than twice)
"fastfast" - incorrect (no hyphen)
"asfdadf" - incorrect (no hyphen, word not repeated)
"-" incorrect (empty word)'''

#Sol - 
def is_all_same_word_twice(strings: list) -> bool:
    '''
    Checks if all strings follow the format where 
    the same word is repeated exactly twice with a hyphen in-between them.

    Args:
        strings (list): A list of strings to be checked.

    Returns:
        bool: True if all strings are of the given format, otherwise False.
    '''
    for el in strings:
        mid = len(el) // 2
        data = el.split("-")
        
        if('-' not in el):
            return False
            
        if(el == '-'):
            return False
            
        if not((len(data) == 2) and (data[0] == data[1]) and (el[mid] == '-')):
            return False
    return True


'''Q3 - 
Given a multi-line passage where the words are separated by spaces, find the letter which occurs most frequently as the first letter of any word. Consider both uppercase and lowercase letters as the same and return the letter in lowercase.

Assume there will be only one letter that occurs the most number of times as the first letter of a word.

Example:

passage = 
word1 Word2 word3 word4 text1 text2
text3 Text4 word5 text5 word6
python1 python2 Python3
'''
#sol -
def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    first_letter_list = [el[0].lower() for el in passage.split(" ")]
    first_letter_dict = {el : first_letter_list.count(el)  for el in first_letter_list}
    
    return max(first_letter_dict , key = first_letter_dict.get)








