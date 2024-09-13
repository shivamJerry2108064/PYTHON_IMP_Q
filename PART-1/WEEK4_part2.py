
''' Q1
# a) Increment all the odd numbers in a list by 1 and decrement all the even numbers by 1, without modifying the original list.'''
l = [1,2,3,4,-1]

l_copied = l.copy()
for i in range(len(l_copied)):
    if(l_copied[i] % 2 == 0):
        l_copied[i] -=1
    else:
        l_copied[i] += 1
print(l_copied,l)


'''b) Flatten a list of lists into a single list.
Input: A list of lists.
Output: A single flattened list.'''

l = [[1,2,3],[4,5]]

res = []

for el in l:
    res.extend(el)

print(res)



'''important'''
'''Q2 - 
more_than_two_unique_vowels: 
Given a string of comma-separated words, return a "set" containing words that have more than two unique vowels.'''

s = 'functions,are,not,complicated'

def unique_vowels(s):
    s_list = s.split(",")
    res = set()

    vowels = {'a','e','i','o','u'}

    for i in range(len(s_list)):
        unique_vowels_word = len(set(s_list[i]) & vowels)

        if(unique_vowels_word > 2):
            res.add(s_list[i])
    return res

print(unique_vowels(s))



'''IMPORTANT'''
'''Q3) all_common: Find the common characters that are present in all strings in a list of strings and return them as a string in ascending order.
Input: A list of strings.
Output: A string containing common characters in ascending order'''

l= ['abc','bcdef','zqopbcb']

list_of_set_of_char = [set(item) for item in l]
common_set_of_char = set.intersection(*list_of_set_of_char)
print("".join(sorted(common_set_of_char)))



'''Q4 - 
vocabulary: Given a list of sentences (with only alphabets and spaces), find the vocabulary (list of unique words) and return it as a set. 
Convert all words to lowercase before adding to the vocabulary.
Input: A list of sentences.
Output: A set of unique words in lowercase.'''

sentences = [
"This is a car",
"He is playing with a bat",
"He and she are playing",
]

vocab = set()
for el in sentences:
    word_list = el.split(" ")
    for word in word_list:
        vocab.add(word)

print(vocab)



'''Q5 a) swap_at_index: Break a tuple at a given index ( k ) (the element at the ( k )-th index is included in the first half before swapping) 
and swap the parts.
Input: A tuple and an integer ( k ).'''
def swap_at_index(t,k):
    return t[k+1:] + t[:k+1]

print(swap_at_index((1,2,3,4,5,6),1))


'''b) reverse_first_and_last_halves: Reverse the first and last halves of a list with even length in place.
Input: A list with an even length.
Output: None (the list should be modified in place).'''

l = [1,2,3,4,5,6]

def reverse_first_and_last_halves(l):
    mid = len(l) // 2
    rev_first_half = l[:mid][::-1]
    rev_last_half = l[mid:][::-1]

    return rev_first_half + rev_last_half

print(reverse_first_and_last_halves(l))



'''IMPORTANT'''
'''Q6) first_and_last_index: Get the indices of the first and last occurrence of a given item in a list. Assume the item is present in the list at least once.
Input: A list and an item.
Output: A tuple with the first and last indices of the given item in the list.'''

def first_and_last_index(l , item):
    idx_list = [idx for idx in range(len(l)) if l[idx] == item]
    return (idx_list[0] , idx_list[-1])

print(first_and_last_index([2,3,4,1,2,3,1],1))


'''IMPORTANT'''
'''Q7 - rotate_k: Create a new list with elements of the given list moved ( k ) positions towards the right. 
The elements at the end should come back to the beginning in a circular order.'''

def rotate_k(l , shift):
    l_copied = l.copy()  # return as new list 

    shift = shift % len(l)
    for i in range(len(l)):
        new_idx = i + shift

        rotated_idx = new_idx % len(l_copied)
        l_copied[rotated_idx] = l[i]

    return l_copied

l1 = [9,7,5,3,2,4]

print(rotate_k(l1 , 3))






















        
