# -*- coding: utf-8 -*-

n = int(input('How many candidates are there? '))
voting = [0 for i in range(n)]

while True:
    print('You have ' + str(1) + ' ~ ' + str(n) + ' candidates')
    candidate = int(input('Which candidate would you like to vote? (exit: -1) '))
    if candidate == -1:
        break
    else:
        voting[candidate-1] = voting[candidate-1] + 1
        
print()
print()
print("==============================")
print("#candidate       voting result")
for i in range(n):
    print("   ", end = ' ')
    print(i + 1, end = '\t\t    ')
    print(voting[i])
print("==============================")