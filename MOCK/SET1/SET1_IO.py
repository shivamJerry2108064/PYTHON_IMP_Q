'''VERY IMPORTANT'''
'''Q4 - '''
'''
Given n positive integers over multiple lines, where n is provided in the first line, print the run-length encoding sequence for each number on separate lines. Run-length encoding represents how many times a digit is repeated consecutively. For each number, every two values in the output represent the count of consecutive digits followed by the digit itself.

Input

The first line contains an integer n representing the number of integers.
The next n lines each contain one integer.
Output

For each of the n integers, print the run-length encoded sequence on a new line. Each line contains pairs of numbers where the first number in each pair is the count of consecutive digits, followed by the digit itself.
Example

For example, given the following input:

4
44455544445
666666
77778888877
234567
The output should be:

3 4 3 5 4 4 1 5
6 6
4 7 5 8 2 7
1 2 1 3 1 4 1 5 1 6 1 7
Explanation

44455544445 - 3 4 3 5 4 4 1 5 - 3 times 4, 3 times 5, 4 times 4 and 1 time 5
666666 - 6 6 - 6 times 6
77778888877 - 4 7 5 8 2 7 - 4 times 7, 5 times 8, 2 times 7
234567 - 1 2 1 3 1 4 1 5 1 6 1 7 - 1 time 2, 1 time 3'''
#Sol

n = int(input())

for i in range(n):
    s = input() + " "
    
    output = []
    
    counter = 1
    i = 0
    while True:
        val = s[0]
        
        if(s[i+1] == " "):
            output.append(str(counter))
            output.append(str(val))
            break
        
        if(s[i] == s[i+1]):
            counter += 1
            i += 1
        else:
            output.append(str(counter))
            output.append(str(val))
            counter = 1
            s = s[i+1:]
            i = 0
    print(" ".join(output))