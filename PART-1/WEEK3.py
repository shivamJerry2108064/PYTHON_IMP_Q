
# Q1
'''IMP'''
'''reverse_sum_palindrome: Continuously read positive integers from standard input until you encounter a "-1"(not included in the output). 
Print only those integers for which the sum of the number and its reverse is a palindrome.
'''

# val = input('enter a +ve integer')

# while(val != '-1'):
#     num_original = val
#     rev = val[::-1]

#     res = str(int(num_original) + int(rev))

#     if(res == res[::-1]):
#         print(num_original)

#     val = input('enter a +ve integer')


'''IMPORTANT'''
'''Q2 - odd_char: Continuously read strings from standard input until you encounter a string ending with a "."(include that string with the "." in the output).
Extract characters at odd positions (starting from 1) of each line, and print the results in a single line separated by spaces.'''

# res = ''
# while True:
#     string = input()
#     if(string.endswith('.')):
#         res += " " + string[::2]
#         break
#     res += " " + string[::2]

# print(res[1:])


'''Q3 - only_odd_lines: Continuously read lines from standard input until "END"(not included in the output) is encountered. 
Create a string by prepending only the odd lines (starting from 1) with a newline character in between, 
and print the result which will be the odd lines in reverse order.'''

# line = input()
# count = 1

# res = []
# while(line != 'END'):
#     if(count % 2 != 0):
#         res.append(line)
    
#     count += 1
#     line = input()

# print("\n".join(res[::-1]))



'''VERY IMPORTANT'''
'''Q4 - Starting from 100 and going in the decreasing order, print the reverse(digits reversed) of first n numbers starting from k 
which do not have the digit 5 and 9 and is odd number in multiple lines'''

# def from_k(n ,k):
#     def check_5_9(val):
#         return '5' in str(val) or '9' in str(val)
    
#     count = 1
#     for i in range(k,0,-1):
#         if(count > n):
#             break
#         if((i % 2 != 0) and not(check_5_9(i))):
#             print(str(i)[::-1])
#             count += 1
        

# from_k(5, 99)



'''Q5 - a) Permutation (permutation): Given a string s, print all the possible two-letter permutations(without repitition) of the letters in the string.
input : abc
output : ab , ac , bc , cb , ca , ba'''

# string = input()

# def permutation(s):
#     for i in range(len(s)):
#         for j in range(len(s)):
#             if(i != j):
#                 print(f"{s[i]}{s[j]}")
    
# permutation(string)


'''b) Sorted Permutation (sorted_permutation): 
Given a string s, print all the possible two-letter permutations(without repetition) of the letters in the string. 
where the first character comes before the second one in alphabetical order. 
The order in which the permutations are printed is same as the previous one (Type: Filtering).'''

# s = input()

# def sorted_permutation(s):
#     for i in range(len(s)):
#         for j in range(len(s)):
#             if((i != j) and (s[i] < s[j])):
#                 print(f"{s[i]}{s[j]}")


# sorted_permutation(s)



'''Q6 - Repeat the Repeat (repeat_the_repeat): Given a number n, print the numbers from 1 to n in the same line and repeat this n times.'''

# def repeat_the_repeat(n):

#     res = ''
#     for i in range(1,n+1):
#         res += str(i)
    
#     for j in range(n):
#         print(res)

# repeat_the_repeat(3)


'''Q7 - a) Repeat Incrementally (repeat_incrementally): 
Given a number n, print a pattern where the k-th line contains the first k numbers and there are n lines in total. 
For example, if n is 4, the output should be: 
1
12
123
1234'''


def repeat_incrementlly(n):
    res = ''
    for i in range(1,n+1):
        res += str(i)
        print(res)

repeat_incrementlly(4)
    

            

'''most imp'''
'''Q7 - b) Increment and Decrement (increment_and_decrement): 
Given a number n, print a pattern where the k-th line should have the numbers from 1 to k and then back down to 1. 
For example, if n is 4, the output should be:
1
121
12321
1234321'''


# def increment_and_decrement(n):
#     for i in range(1, n+1):
#         res = ''
#         for j in range(1, i+1):
#             res += str(j)
        
#         print(res + res[:len(res)-1][::-1])

# increment_and_decrement(4)



'''Q8 - a) is_sorted - Check if all characters of the given string from input are in alphabetical order. Print the output as "True" or "False" accordingly.'''
# s = input()

# flag = False

# for i in range(len(s)-1):
#     if(s[i] < s[i+1]):
#         flag = True
#     else:
#         flag = False
#         break

# if(flag):
#     print('True')
# else:
#     print('False')


'''c) - Manhattan distance : Take inputs directions such as "UP", "DOWN", "LEFT" and "RIGHT" from the input until the input is "STOP". 
Assume you are starting from (0,0) in a cartesian coordinate. 
Find the Manhattan distance between the starting point and the ending point by following the steps in the cartesian plane.
Write a program to solve these tasks. Use loops where necessary.'''


# direction = input()

# x , y = 0 , 0
# while(direction != 'STOP'):
#     if(direction == 'UP'):
#         y += 1
#     elif(direction == 'DOWN'):
#         y -= 1
#     elif(direction == 'LEFT'):
#         x -= 1
#     elif(direction == 'RIGHT'):
#         x += 1
        
#     direction = input()

# print(abs(x) + abs(y))

    









    







