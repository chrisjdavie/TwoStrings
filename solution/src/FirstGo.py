'''
Solution of the hackerrank Two Strings hackerrank puzzle.

https://www.hackerrank.com/challenges/two-strings

---------------------

Problem Statement

You are given two strings, A and B. Find if there is a substring that appears in both A and B.

Input Format

Several test cases will be given to you in a single file. The first line of the input will contain a single integer T, the number of test cases.

Then there will be T descriptions of the test cases. Each description contains two lines. The first line contains the string A and the second line contains the string B.

Output Format

For each test case, display YES (in a newline), if there is a common substring. Otherwise, display NO.

Constraints

All the strings contain only lowercase Latin letters.
1<=T<=10
1<=|A|,|B|<=105

---------------------

Is there a common subset of characters between two strings?

Created on 1 Jan 2016

@author: chris
'''

for _ in range(input()):
    inputString0 = raw_input().strip()
    inputString1 = raw_input().strip()
    
    set0 = set(inputString0)
    set1 = set(inputString1)
    
    subset = set0.intersection(set1)
    
    if len(subset) > 0:
        print "YES"
    else:
        print "NO"
    