def most_frequent_element(lst: list) -> int:
    '''
    Arguments:
    lst: list - a list of integers

    Return:
    int - the integer that occurs most frequently, or the largest one
          if there are multiple with the same frequency

    Example:
    >>> most_frequent_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    4
    '''
    d = {el : lst.count(el) for el in lst}
    max_val_l = max([d[key] for key in d])
    
    res = []
    for key_i in d:
        for key_j in d:
            if((key_i != key_j) and (d[key_i] == d[key_j]) and (d[key_i] == max_val_l)):
                res.append(max(key_i , key_j))
        
    return max(res) if res else max(d , key = d.get)




def most_frequent_alpha_character(filename: str) -> str:
    '''
    Arguments:
    filename: str - name of the file

    Return:
    list - the most frequent alphabetic characters (case-sensitive)
    '''
    f = open(filename , 'r')
    
    res = []
    for line in f.readlines():
        l = (line.strip()).split(" ")

        temp_l = []
        for i in range(len(l)):
            for j in range(len(l[i])):
                if((l[i][j]).isalpha()):
                    temp_l.append(l[i][j])
        
        d = {x : temp_l.count(x) for x in temp_l}
        val_l = [d[key] for key in d]
        
        for key in d:
            if(d[key] == max(val_l)):
                res.append(key)
                
    res_d = {k : res.count(k) for k in res}
    val_res_d = [res_d[key] for key in res_d]
    
    output = []
    for key in res_d:
        if(res_d[key] == max(val_res_d)):
            output.append(key)
    
    return output



