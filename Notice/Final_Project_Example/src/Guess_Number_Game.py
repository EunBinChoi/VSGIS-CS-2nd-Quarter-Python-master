# -*- coding: utf-8 -*-

import random

answer = random.randrange(1, 101) 

print('==========================================')
print('Guess the answer hidden by the program.. ')
print('[Hint] This is the digit between 1 and 100! ')
print('==========================================\n')


cnt = 0
while True:
    guess = int(input('Guess number? '))
    
    if guess == answer:
        print('[Congrat!] Your guess number is correct')
        break
    
    elif guess > answer:
        print('Your guess number is larger than answer..')
        print('Guess the other number which is smaller than what you guess before ...\n')
        
    
    elif guess < answer:
        print('Your guess number is smaller than answer..')
        print('Guess the other number which is larger than what you guess before ... \n')
            
    cnt =  cnt + 1
   
print('==========================================') 
print("The number of times the game was attempted to get the correct answer : " + str(cnt))