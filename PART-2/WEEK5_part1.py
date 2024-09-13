
'''BASICS'''
'''Q1
increase_prices(fruit_prices: dict) -> None
Increase the prices of every fruit by 20% and round to two decimal places. Modify the dictionary in place.'''

# def increase_prices(d):
#     # d = {key:d[key]+20/100*d[key] for key in d}
#     # print(d)  # return a modified dictionary

#     for key in d:
#         d[key] = d[key] + 20/100*d[key]
#     print(d)   # modify d in place

# d1 = {
# "Orange": 4, "Grapes": 3,
# "Banana": 2, "Cherry": 5,
# }
# increase_prices(d1)
# print(d1)


'''IMPORTANT'''
'''Q2 a) dict_from_string(string: str, key_type(str), value_type(int))
Convert a string with comma-separated key-value pairs into a dictionary, converting the keys and values to the specified types.'''

s = """Apple,2
Banana,3
Orange,4
Grapes,3
Papaya,5"""
# #approach - 1
def dict_from_string(s: str, key_type , value_type):
    data = [el.split(',') for el in s.split('\n')]
    d = {key_type(data[i][j]) : value_type(data[i][j+1])  for i in range(len(data)) for j in range(len(data[i])-1)}
    print(d)


# #approach 2
def dict_from_string2(s:str, key_type, value_type):
    d = {}
    for line in s.split('\n'):
        key , val = line.split(',')
        d[key_type(key)] = value_type(val)
    
    print(d)

dict_from_string2(s , str , int)
dict_from_string(s , str , int)



'''IMPORTANT'''
'''Q3 - dict_to_string(D: dict) -> str
Convert a dictionary back into a string with each key-value pair on a new line, using comprehensions.'''

d1 = {
'Apple':2,
'Banana':3,
'Orange':4,
'Grapes':3,
'Papaya':5
}

def dict_to_string(d:dict):
    return "\n".join([",".join([key,str(val)]) for key,val in d.items()])
    

def dict_to_string2(d:dict):
    l = [[key,str(val)] for key,val in d.items()]
    res = [",".join(el) for el in l]
    return "\n".join(res)

print(dict_to_string2(d1))
print(dict_to_string(d1))



'''Q4 - a) def total_price_no_loops(fruit_prices: dict, purchases) -> float:
    Compute the total price without loops. '''

def total_price_without_sum_func(fruit_prices: dict, purchases:list):
    amt = 0
    for el in purchases:
        amt += fruit_prices[el[0]]*el[1]
    print(amt)

def total_price_no_loops(fruit_prices , purchases):
    amt = sum([fruit_prices[el[0]]*el[1] for el in purchases])   # we can't use loops but in this part can use sum function
    print(amt)


fruit_prices = {'Apple':2.0,'Banana':3.0,'Orange':4.0,
'Grapes':3.0,'Papaya':5.0}
purchases = [("Apple",3),("Orange",5),("Grapes",4)]

total_price_without_sum_func(fruit_prices , purchases)
total_price_no_loops(fruit_prices , purchases)



'''Q5 - a) Find the cheapest fruit from the fruit_prices dict, do not use min function'''
def cheapest_fruit_without_min(fruit_prices):
    cheap = 10000
    res = None
    for key in fruit_prices:
        if(fruit_prices[key] < cheap):
            cheap = fruit_prices[key]
            res = key
    
    print(cheap)
    print(res)

cheapest_fruit_without_min(fruit_prices)


'''b) Find the cheapest fruit using min function. Do not use loops'''
def cheapest_fruit_no_loops(fruit_prices):
    cheapest_price = min([fruit_prices[key] for key in fruit_prices.keys()])
    res = "".join([key for key in fruit_prices if(fruit_prices[key] == cheapest_price)])
    print(res)


#Best
def cheapest_fruit_no_loops2(fruit_prices):
    cheap_fruit = min(fruit_prices , key = fruit_prices.get)
    print('cheap-fruit',cheap_fruit)

cheapest_fruit_no_loops(fruit_prices)
cheapest_fruit_no_loops2(fruit_prices)



'''IMPORTANT'''
'''Q6 - grouping
def group_fruits(fruits:list):
    
    Group the fruits based on the first letter of the names. Assume first letters will be upper case.

    Arguments:
    fruits - list: list of fruit names

    Return:
    dict: dict with the first letters as keys and list of fruits sorted in ascending order as values.
    '''

l = ["Mango",
"Avocado", "Apple", "Banana", "Grape",
"Blackberry", "Cherry", "Cranberry"
]

def grouping(l):
    sorted_l = sorted(l)
    key_set = sorted(set(map(lambda x : x[0] , sorted_l)))
    d = {x : [] for x in key_set}

    for el in sorted_l:
        for key in d:
            if(key == el[0]):
                d[key].append(el)

    print(d)
grouping(l)



'''Q7 - binning 
def bin_fruits(fruit_prices):
    Classify the fruits as cheap, affordable and costly based on the fruit prices. Create a dictionary with the classification as keys and a set of fruits in that category.

    cheap - less than 3 (not inclusive)
    affordable - between 3 and 6 (both inclusive)
    costly - greater than 6 (not inclusive)

    Arguments:
    fruit_prices: dict - dictionary with fruits as keys and prices as values

    Return:
    binned_fruits: dict - dictionary with category as key and a set of fruits in that category as values.
    '''

def binned_fruits(fruit_prices):
    d = {'cheap' : [] , 'affordable' : [] , 'costly' : []}

    for key in fruit_prices:
        if(fruit_prices[key] < 3):
            d['cheap'].append(key)
        elif(3 <= fruit_prices[key] <= 6):
            d['affordable'].append(key)
        else:
            d['costly'].append(key)
    print(d)

fruit_prices2 =  {'Apple':2.0,'Banana':3.0,'Orange':4.0,
'Grapes':3.0,'Papaya':5.0 , 'watermelon' : 7.0}
binned_fruits(fruit_prices2)

