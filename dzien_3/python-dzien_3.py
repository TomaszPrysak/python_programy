# -*- coding: utf-8 -*-

# ćwiczenie 33
# podnoszenie do potęgi
x = int(input("Podaj liczbę którą chcesz podnieść do potęgi: "))
y = int(input("Podaj wykładnik potęgi: "))

i = 1
wew = 1

while (i <= y):
    wew = wew*x
    i = i + 1

print(wew)