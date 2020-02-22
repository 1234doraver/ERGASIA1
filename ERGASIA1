#!/usr/bin/python
# -*- coding: utf-8 -*-
#Ανοιγουμε το αρχειο και αποθηκευουμε ολο το κειμενο σε μια μεταβλητη
import os
fin=open("text.txt","r")
text=fin.read()
fin.close()
#Αφαιρουμε τα πολλαπλα κενα
text=os.linesep.join([s.strip() for s in text.splitlines() if s])
text=" ".join([s.strip() for s in text.split(" ") if s])
#Χωριζουμε το κειμενο σε λεξεις 
words=text.split()
#Φτιαχνουμε λιστα που περιεχει τις λεξεις και το μηκος τους και μετα τις ταξινομω με βαση αυτο
w=[(len(wrd),wrd) for wrd in words]
w.sort(reverse=True)
#Τοποθετω σε μεταβλητες τις 5 μεγαλυτερες μαζι με το μηκος τους
a=w[0]
b=w[1]
c=w[2]
d=w[3]
e=w[4]
#Υστερα διατηρω σε μεταβλητες μονο τις λεξεις
A= (a[1])
B= (b[1])
C= (c[1])
D= (d[1])
E= (e[1])
#Αναποδογυριζω τις λεξεις
A=A[::-1]
B=B[::-1]
C=C[::-1]
D=D[::-1]
E=E[::-1]
#Δημιουργω λιστα με τα φωνηεντα
Vowels= ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
#Για καθε μια απο τις 5 μεγαλυτερες λεξεις αφαιρω τα φωνηεντα που περιεχουν και τις εμφανιζω
for x in A:
  if x in Vowels:
    A = A.replace(x, '')
print (A)
for x in B:
  if x in Vowels:
    B=B.replace(x,'')
print (B)
for x in Vowels:
  C=C.replace(x,'')
print (C)
for x in Vowels:
  D=D.replace(x,'')
print(D)
for x in Vowels:
  E=E.replace(x,'')
print(E)
