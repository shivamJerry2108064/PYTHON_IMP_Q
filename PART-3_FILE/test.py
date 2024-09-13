
# '''Q1 -'''
'''Write a function named read_file that accepts a text file named filename as argument. 
# Within the function, read the file and print each line of the file on a separate line in the console. 
# You shouldn't print any extra characters at the end of a line. There shouldn't be an empty line between any two consecutive lines.'''

# def read_file(filename):
#     f = open(filename , 'r')

#     lines = f.readlines()
#     for line in lines:
#         if(line.strip()):
#             print(line.strip())
#         else:
#             print(line)
#     f.close()

# filename = 'public.txt'
# read_file(filename)



#IMPORTANT
'''Q2 - '''
def get_dict(filename):
    """
    Convert the contents of the file into a dict

    Argument:
        filename: string, path of the file
    Return:
        result: dict; keys are strings, values are integers
    """
    f = open(filename , 'r')
    f.readline()  # skip the header

    lines = f.readlines()
    x = [line.split(",") for line in lines]   # nested_l

    temp_dict = {el[0] : int(el[1].strip()) for el in x}
    sorted_key_list = sorted([key for key in temp_dict])

    return {el : temp_dict[el] for el in sorted_key_list}


print(get_dict('dict.csv'))



'''Q3 - '''
'''input :  a matrix
  1,2,3
  4,5,6
  7,8,9
'''

'''output = [[1,2,3],[4,5,6],[7,8,9]]'''

def get_matrix(filename):
    """
    Convert the contents of the file into a matrix

    Argument:
        filename: string
    Return:
        matrix: list of lists
    """
    f = open(filename , 'r')
    lines = f.readlines()
    
    res = []
    for line in lines:
        l = (line.strip()).split(",")
        l_int = [int(x) for x in l]
        res.append(l_int)
    print(res)

get_matrix('matrix.txt')



'''Q4 -'''
'''Write a function named write_AP that accepts the following arguments:

a_1: first term of the AP, integer.
d: common difference of the AP, integer.
n: number of terms in the AP, positive integer.
Within the function, create a file named AP.txt and write the first n terms of the AP to it, one term on each line, 
starting from the first term.'''
#Sol-
def write_AP(a_1 , d , n):
    f = open('AP_FILE', 'w')
    for i in range(n):
        next_term = a_1 + (i+1)*d
        f.write(str(next_term)+'\n')
    
    f.close()

write_AP(2 , 3 , 20)


'''Q5'''
'''The scores of a class of students in the online degree program is represented as a CSV file with the following header:
    Name,Gender,CT,Python,PDSA
The name of the file is given by the variable filename. The first line will be the header.

Write a function named improvement which accepts the filename as argument. 
It should return the number of students whose scores have increased across the three courses. 
That is, the number of students whose scores are in this order: CT < Python < PDSA.'''
#Sol-
def improvement(filename):
    f = open(filename , 'r')
    f.readline()    # skip the header

    lines = f.readlines()
    
    count = 0
    for line in lines:
        l = (line.strip()).split(",")
        if((int(l[2]) < int(l[3])) and ((int(l[3]) < int(l[4])))):
            # print(l)
            count += 1
    return count

#approach2 
def improvement_2(filename):
    f = open(filename , 'r')
    lines = f.readlines()
    
    count = 0
    for i in range(1,len(lines)):    # from 1 to skip the header
        name , gender , CT , python , PDSA = (lines[i].strip()).split(",")
        if((int(CT) < int(python)) and (int(python) < int(PDSA))):
            count += 1
    return count

print(improvement('scores.csv'))
print(improvement_2('scores.csv'))



'''Q5 - '''
'''The scores of a class of students in the online degree program is represented as a CSV file with the following header:
        SeqNo,Name,Gender,CT,Python,PDSA

The name of the file is given by the variable filename. The first line will be the header. 
The contents of the file will be in increasing order of sequence numbers.

Write a function named extract_lines that accepts filename as argument. 
Within the function, read the file and look for all male students who have scored at least 70 marks in Python. 
Copy these lines into a new file named python.csv. The entries in this file should be in the increasing order of sequence numbers. 
Also, the first line of python.csv should be the header, which is same as the one in filename.
'''
#Sol = 
def extract_lines(filename):
    f = open(filename, 'r')
    g = open('scores2_copy.csv','w')

    g.write(f.readline())

    for line in f.readlines():
        seqNo , Name , Gender , CT , Python , PDSA = (line.strip()).split(",")
        if((Gender == 'M') and (int(Python) >= 70)):
            g.write(line)
    
    f.close()
    g.close()

extract_lines('scores2.csv')



'''Q6 -'''
'''Write a function named number_grid that accepts two positive integers m and n as arguments. 
Within the function, create a file named numgrid.csv. 
Write the first mn positive integers to the file in the following way:

Each line should be a sequence of n comma-separated integers.
There should be a total of m lines in the file.
For example, for the case of m=5,n=3, the file should be:

1,2,3
4,5,6
7,8,9
10,11,12
13,14,15'''
def number_grid(m,n):
    g = open('numgrid.csv' , 'w')
    k = m*n
    count = 0
    for i in range(m):
        line = ''
        for j in range(n):
            count += 1
            line += str(count) + ','
        g.write(line[:-1] + "\n")
    
number_grid(5,3)



'''Q7 -'''
'''filename is a text file that contains a collection of words in lower case, one word on each line. 
Write a function named get_freq that accepts filename as argument. 
It should return a dictionary where the keys are distinct words in the file, the values are the frequencies of these words in the file.

For example, given the following file:

good
great
good
work
work
The dictionary returned should be:

{'good': 2, 'great': 1, 'work': 2}'''
#Sol-

def get_freq(filename):
    f = open(filename, 'r')
    word_list = [line.strip() for line in f.readlines()]
    
    return {el : word_list.count(el) for el in word_list}

print(get_freq('words.txt'))


'''Q8 -'''
'''
You are given two non-empty text files file1 and file2 that have f1 and f2 lines respectively. 
Each file is a collection of ten-digit phone numbers, one number per line. It is also known that-

0 < f1 ≤ f2.

The following relations are defined on these two files:

Subset: file1 is a subset of file2 if the phone number in the ithline of file1 is equal to the number in the ith line of file2, 
for 
1 ≤ i ≤ f  and f1 < f2.

Equal: file1 is equal to file2 if the phone number in the ith line of file1 is equal to the number in the ith line of file2 
for 
1 ≤ i ≤ f and f1=f2.

Write a function named relation that accepts these two text files as arguments. 
It should return the string Subset if file1 is a subset of file2. 
It should return Equal if file1 is equal to file2. If both these conditions are not satisfied, it should return the string No Relation.'''
#Sol-

def relation(f1 , f2):
    f_1 = open(f1,'r')
    f_2 = open(f2,'r')

    f1_lines = f_1.readlines()
    f2_lines = f_2.readlines()
    print(f1_lines , f2_lines)

    for i in range(len(f1_lines)):
        for j in range(len(f2_lines)):
            if(f1_lines[i].strip() == f2_lines[j].strip()):
                if (len(f1_lines)) < (len(f2_lines)):
                    return 'Subset'
                elif(len(f1_lines) == len(f2_lines)):
                    return 'Equal'
                else:
                    return 'No Relation'


print(relation('file1.txt','file2.txt'))



'''Q9- '''
'''
filename is a CSV file that has the following header:

Name,Country,Goals
The first five lines of a sample file are given below:

Name,Country,Goals                                        
P1,Brazil,20  
P2,Argentina,30
P3,Brazil,50                                                   
P4,Germany,30
Write a function named get_goals that accepts filename and the name of a country as arguments. 
It should return a tuple having two elements: (num_players, num_goals). 

"num_players" is the number of players from this country that appear in this file, 
"num_goals" is the total number of goals scored by all the players, who belong to this country. 
If the country is not present in the file, then return the tuple (-1, -1).'''
#Sol-
def get_goals(filename, country):
    # dict with key(countries) and values as tuple([num_players[], [num_goals])
    f = open(filename , 'r')
    f.readline()
    l = [(line.strip()).split(",") for line in f.readlines()]
    d = {}
    for el in l:
        Name , Country , Goals = el
        d[Country] = ([],[])
    
    for el in l:
        for key in d:
            if(el[1] == key):
                (d[key][0]).append(el[0])
                (d[key][1]).append(int(el[2]))
    for key in d:
        if(key == country):
            t = d[key]

    return (-1,-1) if(t == tuple()) else (len(t[0]) , sum(t[1]))
    

print(get_goals('sport.csv', 'India'))


#approach 2 : Better
def get_goals2(filename , country):
    f = open(filename , 'r')
    f.readline()
    
    count_players = 0
    sum_goals = 0
    for line in f.readlines():
        l = (line.strip()).split(",")
        if(country in l):
            count_players += 1
            sum_goals += int(l[2])
    return (-1,-1) if count_players == 0 else (count_players , sum_goals)
print(get_goals2('sport.csv', 'India'))



'''Q10'''
'''Write a function named num_to_words that accepts a square matrix of single digit numbers as argument. 
Within the function, create a file named word_matrix.csv. 
Write the matrix to the file by replacing the digits with their corresponding words. 

For example, num_to_words([[1, 2], [3, 4]]) should create the file words.csv with the following contents:

one,two
three,four

Note that the matrix will only have integers from 
0 to 9, endpoints inclusive.'''
#Sol-
def num_to_words(matrix):
    f = open('word_matrix.csv','w')

    temp_d = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
    for i in range(len(matrix)):
        res = []
        for j in range(len(matrix[i])):
            for key in temp_d:
                if(matrix[i][j] == key):
                    res.append(temp_d[key])
        f.write(",".join(res) + "\n")
    
    f.close()
                    
num_to_words([[1,2],[3,4]])

