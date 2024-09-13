
'''QUESTION'''
'''You are given two CSV files:

shopping_file: Contains details of items purchased by the customer which includes names and quantity of the items purchased.
SNo,ProductName,Qty

prices_file: Contains details like product Id, name and price of all available items.
Id,ProductName,Price

The variable shopping_file represents the name of the file containing product purchase details, 
and prices_file represents the name of the file containing product prices.

Define a function calculate_total_price that takes shopping_file and prices_file as argument and returns the total amount of goods purchased 
by the customer.'''


def calculate_total_price(prices_file: str, shopping_file: str) -> int:
    '''Compute the total amount spent on the products.

    Args:
        prices_file (str): path of file containing product purchase details.
        shopping_file (str): path of file containing product prices.

    Returns:
        float: The total amount.
    '''
    f = open(prices_file , 'r')
    g = open(shopping_file , 'r')

    f.readline()
    g.readline()
    
    d1 = {}
    for line in f.readlines():
        l = (line.strip()).split(",")
        d1[l[1]] = int(l[2])
    # print(d1)

    d2 = {}
    for line in g.readlines():
        l = (line.strip()).split(",")
        d2[l[1]] = int(l[2])
    # print(d2)
    
    total = 0
    for key_d2 in d2:
        for key_d1 in d1:
            if(key_d2 == key_d1):
                total += d2[key_d2]*d1[key_d1]
                # print(key_d1 , total)
    print(total)
        

def calculate_total_price2(prices_file: str, shopping_file: str) -> int:
    #Approach 2:
    f = open(prices_file , 'r')
    f.readline()   
    
    d_prices = {}
    for line in f.readlines():
        Id , ProductName , Price = (line.strip()).split(",")
        print(Price)
        d_prices[ProductName] = int(Price)
    

    g = open(shopping_file , 'r')
    g.readline()
    
    total = 0
    for line in g.readlines():
        ProductName , Qty = (line.strip()).split(",")[1:]
        total += d_prices[ProductName]*int(Qty)
    
    print('approach 2',total)

calculate_total_price2('prices_file.csv','shopping_file.csv')

calculate_total_price('prices_file.csv','shopping_file.csv')