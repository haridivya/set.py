'''
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5
'''
set1=input().split(' ')
values=[int(i) for i in set1]
print(len(set(values)))
