# -*- coding: utf-8 -*-

import random

# ćwiczenie 50

def wprowadz():
   tab = []
   i = "t"
   print("Wprowadz elementy do listy | (enter) - koniec wprowadzania ")
   while (i != ""):
      i = input(" ")
      if (i != ""):
         while (True):
            try:
               i = float(i)
               break
            except ValueError:
               print("Wprowadzona wartość jest błędna. Podaj wartość poprawną: ")
               i = input(" ")
         tab.append(float(i))
      elif (i== ""):
         print("Nacisnąłeś ENTER. wpraowadzanie zostało zakończone")
         print("Twoja tablica wygląda następująco:")
         print(tab)
         return tab
   
def wypisz(limit, tab):
   print("Tablica przefiltrowana. Elementy większe od " + str(limit))
   suma = 0
   for v in tab:
      if (v > limit):
         print(v, end=" ")
         suma = suma + v
   print("Suma: ",suma)

wypisz(int(input("Podaj wartość graniczą: ")), wprowadz())