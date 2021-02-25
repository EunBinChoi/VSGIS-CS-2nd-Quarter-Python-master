# -*- coding: utf-8 -*-

import random

dice = [0 for i in range(6)]

i = 0
while i < 10000:
    dice[int(random.randrange(0, 6))] = dice[int(random.randrange(0, 6))] + 1
    i  = i + 1

print()
print()
print("==============================")
print(" #dice          rolling result")
for i in range(6):
    print("   ", end = ' ')
    print(i + 1, end = '\t\t    ')
    print(dice[i])
print("==============================")