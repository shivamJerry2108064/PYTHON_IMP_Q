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