# LIST COMPREHENSION

'''Q1 - a) sum_of_squares - find the sum of squares of numbers in a list - (mapping and aggregation)'''
numbers = [1,3,5,2,3,6]

res = sum(list(map(lambda x : x**2 , numbers)))
res2 = sum([el**2 for el in numbers])

print(res , res2)


'''b) total_cost - given quantitiy and price of each item as a list of tuples find the total cost using list comprehensions'''
t = [(10,40),(5,20),(10,100)]

total_cost = sum(map(lambda x : x[0]*x[1] , t))
print(total_cost)


'''Q2 - a) abbreviation - 
given a string with multiple words seperated by space, form an abbrevation out of it by taking the first letter in caps. (mapping and aggregation)'''
s = 'hello world hello world'

res = list(map(lambda x : x[0].upper() , s.split(" ")))
print(".".join(res))


'''b) palindromes - given a list of strings, create a new list with only palindromes filtering'''
s = ['mom' , 'dad','moon','shiva','pop', 'poptop', 'madam']

res = list(filter(lambda x : x == x[::-1] , s))
print(res)


'''Q3 - all_chars_from_big_words - 
find the all unique characters (case insensitive, make all lowercase) from all words with size greater than 5 
in a given sentence with words seperated by spaces. (filtering)'''

sent = 'List comprehensions are a good start for functional programming'

words = list(filter(lambda x : len(x) > 5 , sent.split(" ")))
list_of_set_of_word = [set(word.lower()) for word in words]
res = set.union(*list_of_set_of_word)

print(sorted(res))



'''Q4 - a) flatten - flatten a nested list using comprehension'''
nested_l = [[1,2,3],[3],[6,1,2,1,4]]

def flatten(l):
    res = [x for el in l for x in el]
    print(res)

flatten(nested_l)


'''VERY IMP'''
'''b) unflatten - given a flat list and number of rows, create a matrix (2d list) with that number of rows. (nested-aggregation)'''
def unflatten(l , row):
    col = len(l) // row
    
    return [[l[col*i+j] for j in range(col)] for i in range(row)]

l = [1,2,3,4,1,2,3,4,1,2,3,4]
print(unflatten(l , 3))



'''VERY IMPORTANT'''
'''Q5 - a) make_identity_matrix - make an identity (with ones on the main diagonal and zeros elsewhere) given the size.'''
def make_identity_matrix(size):
    return [[1 if(i == j) else 0 for j in range(size)] for i in range(size)]

print(make_identity_matrix(4))

'''b) given number of rows m, create a lower triangular matrix like the pattern below. for m = 5''' 
'''
[
  [1,0,0,0,0],
  [1,2,0,0,0],
  [1,2,3,0,0],
  [1,2,3,4,0],
  [1,2,3,4,5]
]
'''
def lower_triangular_matrix(m):
    return [[j+1 if(i >= j) else 0 for j in range(m)] for i in range(m)]

print(lower_triangular_matrix(5))

