# -*- coding: utf-8 -*-

n = int(input('input n : '))
arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = int(input('please input #' + str(i) +' element: '))
    
    
min = arr[0]

for i in range(1, n):
    if min > arr[i]:
        min = arr[i]
        
print('minimum value: ' + str(min))



max = arr[0]

for i in range(1, n):
    if max < arr[i]:
        max = arr[i]
        
print('maximum value: ' + str(max))