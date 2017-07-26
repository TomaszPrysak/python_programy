# -*- coding: utf-8 -*-

import random

from math import sqrt

# ćwiczenie 44

def odleglosc(x1,y1,x2,y2):
    d = sqrt(((x2-x1)**2)+((y2-y1)**2))
    return round(d, 2)

i = 0
x = []
y = []

while (i < 2):
    if (i == 1):
        print("Podaj położenie końcowe:")
    else:
        print("Podaj położenie początkowe:")
    u1 = int(input(" "))
    u2 = int(input(" "))
    x.append(u1)
    y.append(u2)
    i = i + 1

print("Przejdziesz dystans: ", odleglosc(x[0],y[0],x[1],y[1]))