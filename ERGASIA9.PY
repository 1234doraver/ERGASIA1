#!/usr/bin/python
# -*- coding: utf-8 -*-
#Ο χρήστης δινει εναν αριθμο
number=int(raw_input("Enter a number:"))
#Οσο ο αριθμος δεν ειναι μονοψηφιος συνεχιζεται η επαναληψη
while (number>9):
    num=0
    number=number * 3
    number=number+1
    digits = [int(x) for x in str(number)]
    for x in digits:
       num+=x
       number=num
print(number)
