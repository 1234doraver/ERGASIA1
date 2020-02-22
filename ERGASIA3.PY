#!/usr/bin/python
# -*- coding: utf-8 -*-
#Δημιουργία λεξικού
d = {
'milk' : 3.67 ,
'butter' : 1.95 ,
'bread' : 1.67 ,
'cheese' : 4.67 ,
'coca cola' : 1.34,
'coffee':2.69
}
cost=0
tax=0
taxes=[]
prices=[]
#Συνάρτηση για την εύρεση των φορων
def FindTheTax(cost):
  tax=cost*24/100
  taxes.append(tax)
  return taxes
#Συναρτηση για την εύρεση του ποσού πληρωμής
def FindTheTotalCost(prices,ShoppingList,taxes):
   i=0
   total=0
   for item in ShoppingList:
     total+=prices[i]+taxes[i]
     i+=1
   return total
 #Δημιουργία λίστας με αυτά που θέλει να αγοράσει ο χρήστης
ShoppingList=[]
#Πρόσθεσε μέχρι να μην υπάρχει input
while len(ShoppingList)!="":
  item=raw_input("Add an item to the list: ")
#Αν δε θες να προσθέσεις κατι αλλο πάτα το enter,οπότε θα σταματησει η επανάληψη
  if (item==""):
    break
 #Δείχνει τις επιλογες του χρήστη
  elif (item=='Help' or item=='help'):
    print(d)
  else:
  #Ελέγχει αν το input υπαρχει
    if item in d:
      ShoppingList.append(item)
      print (ShoppingList)
      cost=(d.get(item))
      prices.append(cost)
      FindTheTax(cost)
   #Ενώ αν δεν υπάρχει εμφανιζει μηνυμα
    else:
      print("Item does not exist!")
 #Τέλος εμφανιζει τη λιστα που δημιουργησε ο χρηστης με αυτα που θελει να αγορασει και το ποσο που θα πρεπει να πληρωσει 
print "Your list is:",ShoppingList
print "The total cost you have to pay is:",FindTheTotalCost(prices,ShoppingList,taxes)




