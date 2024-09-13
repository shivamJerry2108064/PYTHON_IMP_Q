
'''IMPORTANT CONCEPTS'''
# min
# max
# sum
# len
# sorted


#1
# sort a iterable in desc order => list and tuples are iterables collections. ( string and range are also iterables but not collections).
l = [2,4,6,3,2,1,4,8]
print(sorted(l , reverse= True))

t = (2,4,6,3,2,1,4,8)
print(sorted(t , reverse= True))


#2
# some iterables are reversible such as list and tuples can be reverse using reversed()
l2 = [7,3,4,6,2]
print(list(reversed(l2)))     # [2,6,4,3,2]
print(l2[::-1])

# but in case of 'set collection' : first sort it and then use reversed()  => to get reversed of sorted set
s1 = {2,3,4,2,1,2,3}
print(list(reversed(sorted(s1))))



#3
# set collections are also not indexable, ordered and slicable , but list and tuples are indexable and slicable.

#4
# list and tuples are ordered collections. check is some_val is at even indices of a list name 'some_collection'
def check(some_val, some_collection):
    return True if some_val in some_collection[::2] else False

print(check(5 , [1,2,3,4,5]))


#4
# list , set and tuple are interconvertible

l3 = [1,2,3]
print(set(l3), tuple(l3))

s3 = {1,2,3,6,2,3,4}   # s3 is set and set is an unordered unique collection
print(list(s3) , tuple(s3))



'''Q1 - print the string elements of an iterable with '-' in between each string element and return a string'''

list1 = ['Akshay','rani','rakshit']  # tuple is also as it is 
print("-".join(list1))

set1 = {'apple' , 'pineapple' , 'mango'}   # since set are not ordered , so output => apple-pineapple-mango , pineapple-mango-apple and more combinations.
print("-".join(sorted(set1)))    # Use sort to fix the order first(asc order) and then join with hyphen



'''OPERATIONS ON LIST AND SET'''

# Q2 : VERY IMPORTANT
# list methods and operations that will modify the list inplace.

# def list_mutating_inplace(l , i, j):
#     # sort the `list l` inplace
#     l.sort()
#     print('sorted-',l)

#     # extend `list l` with the first three elements in `items`
#     l.extend(l[:3])
#     print('extend-',l)

#     # add item j at index 3
#     l.insert(3,j)
#     print('j inserted at index 3-',l)

#     # pop the fifth element and store it in variable `popped_item`
#     popped_item = l.pop(4)
#     print('popped-',l)

#     # remove first occurance of `item j` from the list
#     l.remove(j)
#     print('removed-',l)

#     # make the element at index 4 None
#     l[4] = 'None'
#     print(l)

#     # make the even indices None
#     l[::2] = ['None']*len(l[::2])
#     print(l)

#     # # delete the even indices
#     del l[::2]
#     print(l)


#     return l , popped_item

# print(list_mutating_inplace(['Apple','cherry' , 'banana' , 'grapes'] , 'blueberry' , 'Apple'))



# def list_non_mutating_inplace(l, i , j):    # easy way to do it using l.copy() in each part and use list_mutate_inplace methods.
#     # print the sorted version of items
#     l_sorted = sorted(l)
#     print('sorted',l_sorted)

#     # print a list with item i appended to the `items` at the end
#     l_append = l + [i]
#     print('append',l_append)

#     # print a list with `item j` added to items at index 3
#     l_inserted = l[:3] + [j] + l[3:]
#     print(l_inserted)

#     #  print a list with the fifth element from `list l` removed
#     l_removed = l[:4] + l[5:]
#     print(l_removed)

#     # print a list with first occurance of `item j` removed from `list l` 
#     idx_item_j = l.index(j)
#     l_removed = l[:idx_item_j] + l[idx_item_j+1:]
#     print(l_removed)    

#     # print a list with the fourth element of `list l` changed to None
#     l_None = l[:3] + ['None'] + l[4:]
#     print(l_None)

#     # print a list with the even indices changed to None  : IMPORTANT
#     l_copy = l.copy()
#     l_copy[::2] = ['None']*len(l_copy[::2])
#     print(l_copy)


#     # print a list with even indices removed
#     l_copy2 = l.copy()
#     del l_copy2[::2]
#     print(l_copy2)

#     return l

# print(list_non_mutating_inplace(["Apple","Cherry","Banana", "Grapes", 'Pineapple','Orange'], "Blueberry","Apple"))


def set_operation(set1 , set2 , set3 , i , j):
    # add item i to set1
    set1.add(i)
    print(sorted(set1))   # sorted convert it to list

    # # remove item2 from set1.
    set1.remove(j)
    print(sorted(set1))

    # add elements from set2 to set1
    set1.update(set2)
    print(sorted(set1))

    # remove all elements from set1 that are in set3
    res = set1 - set3
    # set1.difference_update(set3)   # updates the set1 inplace
    print(sorted(res))

    # print the common elements in both set2 and set3 as a sorted list.
    res = set2 & set3
    print(sorted(res))

    # # print all unique elements present in set1, set2 an set3 as a sorted list
    # res = (set1.union(set2)).union(set3)
    res = set1|set2|set3
    print(sorted(res))

    # # print all the non common elements from both set2 and set3
    var1 = set2 - set3
    var2 = set3 - set2

    print((var1|var2))
    
    return set1 , sorted(set1) , sorted(set2) , sorted(set3)

print(set_operation({1,2,3,4},{3,4,5,6},{1,2,5,6,7,8},5,3))





