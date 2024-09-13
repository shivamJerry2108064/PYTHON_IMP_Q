
'''Q'''
'''The input is in multiple lines. The first line contains a positive integer n. This is followed by n lines, each containing sequences of words. Each line thus consists of multiple words, separated by commas, with no spaces in between words.

You have to output, for each line, the length of the longest subsequence of words following the antakshari property.

Assume all words are lowercase.

A sub-sequence is a subset of consecutive words in this sequence.

A sub-sequence is said to have the antakshari property if the last letter of every word is equal to the first letter in the next word in the sequence.

Input Format

The first line contains an integer n denoting the number of sequences.
The following n lines each contain a sequence of comma-separated words.
Output Format For each sequence, output the length of the largest sub-sequence that follows the antakshari property over multiple lines.

Example

Input:

2
one,two,order,real,long,tight,tree,cool,lot,trouble
ant,tree,ear,rat,tower,retail'''
#Sol-
n = int(input())

for j in range(n):
    l = input().split(",")
    
    count = 1   # first word itself in count
    max_seq_len = 1
    for i in range(len(l)-1):
        if(l[i][-1] == l[i+1][0]):
            count += 1
            if(count > max_seq_len):
                max_seq_len = count
        else:
            count = 1
    print(max_seq_len)



