# -*- coding: utf-8 -*-


print('==========================================')
print('          PI Calculation Program.. ')
print('==========================================\n')
print('[FYI] Pi is an infinite number')
print('[FYI] Infinite decimal numbers become more accurate the more you calculate them.')
print()
print()

loop_count = int(input('How many times do we repeat the loop? '))

numberator = 4.0
denominator = 1.0
sum = 0.0



while loop_count > 0:
    sum = sum + numberator / denominator
    numberator = -numberator
    denominator = denominator + 2.0
    loop_count = loop_count - 1
    
print("PI Value = " + str(sum))