# -*- coding: utf-8 -*-

seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("==== Theater Reservation System ====")
print("====================================")



while(True):
    seat = input('Do you want to book seats? (yes or no) ')
    if seat == "yes":
        print()
        print("=============================")
        print("== Seat reservation status ==")
        print("(1: booked,  0: not booked)")
        print("1  2  3  4  5  6  7  8  9  10")
        print("=============================")
        for i in seats:
            print(i, end = "  ")
        print()
        print("=============================")
         
         
        ans = int(input('Which seat do you want to book? '))
         
        if ans > 10 or ans < 0:
            print("[Warning] The seat which you choose can't be booked..\n\n")
            continue
         
         
        if seats[ans - 1] == 0: # not booking
            seats[ans - 1] = 1
             
            print()
            print("=============================")
            print("== Seat reservation status ==")
            print("(1: booked,  0: not booked)")
            print("1  2  3  4  5  6  7  8  9  10")
            print("=============================")
            for i in seats:
                print(i, end = "  ")
            print()
            print("=============================")
             
     
     
        else:
            print("[Warning] That seat which you choose already booked..")
            print("[Warning] That seat can not booked ...\n\n")
             
    
    
    elif seat == "no":
        print("Okay.. You don't want to book seats.. Bye..")  
        break  
    
    
    if all(seats) == True:
            print("All seat is reversed... \n\n")
            break