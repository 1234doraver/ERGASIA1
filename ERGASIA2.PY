#!/usr/bin/python
# -*- coding: utf-8 -*-
#Ανοιγουμε το αρχειο και αποθηκευουμε ολο το κειμενο σε μια μεταβλητη
import os
fin=open("text1.txt","r")
keimeno=fin.read()
fin.close()
#Αφαιρουμε τα κενα που υπαρχουν
text=os.linesep.join([s.strip() for s in keimeno.splitlines() if s])
keimeno=" ".join([s.strip() for s in keimeno.split(" ") if s])
#Και χωριζουμε το κειμενο σε λεξεις
lekseis=keimeno.split()
#Φτιαχνουμε λιστα με τα 'ειδικα' γραμματα
Grammata= ('f', 'c', 'k', 'r', 'F','C','K','R')
#Φτιαχνουμε λιστα με τα φωνηεντα
Vowels= ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
#Για καθε μια λεξη
for x in lekseis:
  b=0
  v=0
  #Για καθε γραμμα της λεξης ελεγχουμε αν ειναι 'ειδικο' γραμμα ή φωνηεν
  for i in x:
    if i in Grammata:
      b+=1
    elif i in Vowels:
      v+=1
   #Βρισκουμε το μηκος της καθε λεξης και ποσα 'καλα' και 'κακα' συμφωνα εχει
  m=(len(x))
  bad=b
  vowl=v
  good=m-(bad+vowl)
  if (bad>=good):
    print 'The word',x,'is a bad word!'
  else:
    print "The word",x,"is a good word!"
