
'''Question''' # VERY IMPORTANT
'''A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of square of its digits.
Repeat the process until the number equals 1(where it will stay), or it loops endlessly in a cycle that doesn't include 1.
Those numbers for which the process ends in 1 are happy.
Example1:

19 is a happy number.

Explanation:

$1^{2} + 9^{2} = 82$

$8^{2} + 2^{2} = 68$

$6^{2} + 8^{2} = 100$

$1^{2} + 0^{2} + 0^{2} = 1$

Example2:

4 is not a happy number.
The cycle for 4 is as follows:

# Important line
$4 \rightarrow 16 \rightarrow 37 \rightarrow 58 \rightarrow 89 \rightarrow 145 \rightarrow 42 \rightarrow 20 \rightarrow 4$ (and same seq repeats)
if any of above repeats then 4 is not a happy number , here 4 itself repeats and then from 4 onwards 16 , 37... again

Define a function n_happy_numbers that accepts a list of positive integers and returns the count of happy numbers in the given list.'''

def n_happy_numbers(l:list):

    def sum_square_digit(n):
        return sum(int(str(n)[i])**2 for i in range(len(str(n))))

    def check_happy_num(val):
        set_num = set()
        while(val != 1 and val not in set_num):     # if val == 1 then val is happy
            set_num.add(val)   
            val = sum_square_digit(val)      # if val is not 1 and present in set then it means that now sequence repeats
        return val == 1

    count = 0
    happy_list = []
    for el in l:
        res = check_happy_num(el)
        if res:
            count += 1
            happy_list.append(el)

    return count , happy_list

print(n_happy_numbers([1, 65, 28, 23, 60, 31]))


print('a'.isalpha())