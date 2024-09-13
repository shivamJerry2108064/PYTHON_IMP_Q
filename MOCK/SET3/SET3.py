
'''IMPORTANT'''

'''Q1 - a)'''
def square_and_clip(x: int, threshold:int) -> int:
    '''
    Square the given integer and clip the result to threshold
    (clipping means if the value x goes greater than the threshold, keep it at threshold).

    Arguments:
    x: int - the input number
    threshold: int - the threshold value

    Return:
    int - squared and clipped result
    '''
    val = x**2
    if(val >= threshold):
        return threshold
    if(val < threshold):
        return val
    


'''b) '''
def lowercase_first_half_and_uppercase_second_half(s: str) -> str:
    '''
    Given an even-length string of any case, create a string with the first half 
    in lowercase and the second half in uppercase.

    Arguments:
    s: str - the input string

    Return:
    str - the modified string
    '''
    mid = len(s) // 2
    return s[:mid].lower() + s[mid:].upper()



'''Q2- '''
def add_the_middle_element_to_both_ends(l: list) -> None:
    '''
    Given an odd-length list, insert the middle element to both ends of the list.
    Modify the input list and do not return a new list.

    Arguments:
    l: list - the input list

    Return:
    None - the input list is modified inside the function.
    '''
    mid = len(l) // 2
    
    l.insert(0, l[mid])
    l.append(l[mid+1])

    return l


'''Q3 a) '''
def number_of_unique_common_digits(n1: int, n2: int) -> int:
    '''
    Given two integers, return the number of unique digits that are common in both numbers.
    Eg, 287498,295424 - 2, 4 and 9 are common to both nums so answer is 3
    Arguments:
    n1: int - the first number
    n2: int - the second number

    Return:
    int - the number of unique common digits.
    '''
    return len(set(str(n1)) & set(str(n2)))



'''b) '''
def manhattan_distance_via_b(a: tuple, b: tuple, c: tuple) -> int:
    '''
    Given three points a, b, and c on the Cartesian plane, 
    calculate the Manhattan distance to go from point a to point c via point b.

    Manhattan distance is the sum of the absolute differences of their Cartesian coordinates.

    Args:
        a (tuple): Coordinates of point a as (x1, y1).
        b (tuple): Coordinates of point b as (x2, y2).
        c (tuple): Coordinates of point c as (x3, y3).

    Returns:
        int: The Manhattan distance from point a to point c via point b.
    '''
    # return abs(c[0] - a[0]) + abs(c[1] - a[1])
    
    d_ab = abs(b[0] - a[0]) + abs(b[1] - a[1])
    d_bc = abs(c[0] - b[0]) + abs(c[1] - b[1])
    
    return d_ab + d_bc


#IMPORTANT
'''Q4 -'''
def num_to_word(num: int) -> str:
    '''
    Given an integer, generate a string with its digits as words separated by hyphens.

    Arguments:
    num: int - the input number

    Return:
    str - the string with digits as words separated by hyphens
    '''
    l = ['zero' , 'one' , 'two' ,'three' , 'four' , 'five' , 'six', 'seven' , 'eight','nine']
    d = {str(i) : l[i] for i in range(len(l))}
    
    res = []
    for k in range(len(str(num))):
        res.append(d[str(num)[k]])
    
    return "-".join(res)


# IMPORTANT
'''Q5 -'''
def courses_sorted_by_enrollment(student_courses: dict) -> list:
    '''
    Given a dictionary of student roll numbers 
    with the list of courses they chose, 
    find the courses sorted from the 
    most number of enrollments to the least.

    Assume no courses will have the same number of students enrolled.

    Arguments:
    student_courses: dict - a dictionary where keys are 
        student roll numbers and values are lists of courses they chose

    Return:
    list - a list of courses sorted by the 
        number of students enrolled in descending order
    '''
    values = [student_courses[key] for key in student_courses]
    
    flatten_values = []
    for i in range(len(values)):
        for j in range(len(values[i])):
            flatten_values.append(values[i][j])
    
    courses_count = {el : flatten_values.count(el) for el in flatten_values}
    courses_count_desc_sorted_val = sorted([courses_count[key] for key in courses_count] , reverse = True)
    
    result = []
    for el in courses_count_desc_sorted_val:
        for key in courses_count:
            if(el == courses_count[key]):
                result.append(key)
                
    return result



'''Q6 -'''
'''Given an initial balance and a series of daily transactions, 
find the minimum balance, maximum balance, and balance at the end of the day for each day. 
The input will consist of multiple lines where the first line gives the number of days, the second line gives the initial balance, 
and each subsequent line represents the transactions for one day. 
The final balance of the previous day will be the initial balance of the current day.

Input

The first line contains an integer n, the number of days.
The second line contains an integer initial_balance, the initial balance for the first day.
Each of the next n lines contains a space-separated list of integers representing transactions for that day.
Output

For each day, print the minimum balance, maximum balance, and current balance as a comma-separated string.

Sample Input

2
150
-10 10 -10 5
20 -20 30 -10
Sample Output

140,150,145
145,175,155
Explanation

Day 1:

Initial balance: 150
Transactions: -10, 10, -10, 5
Calculations:

Balance after -10: 140
Balance after +10: 150
Balance after -10: 140
Balance after +5: 145
Min balance: 140 Max balance: 150 Current Balance: 145

Output for Day 1: 140,150,145

Day 2:

Initial balance (end balance of Day 1): 145
Transactions: 20, -20, 30, -10
Calculations:

Balance after +20: 165
Balance after -20: 145
Balance after +30: 175
Balance after -10: 165
Min balance: 145 Max balance: 175 Current Balance: 165

Output for Day 2: 145,175,165'''

# Sol-
days = int(input())

initial_bal = int(input())

for i in range(days):
    t = input().split(" ")
    
    res = []
    for el in t:
        initial_bal += int(el)
        res.append(initial_bal)
    # print(res)
    print(f"{min(res)},{max(res)},{initial_bal}")