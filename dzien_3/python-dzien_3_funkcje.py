# -*- coding: utf-8 -*-

###
### Funkcje
###

# początki z funkcjami

# zdefiniowanie funkcji bez zwracania wartości
def powitanie():
    print("Witaj") 
# odwołanie się do funkcji bez zwracania wartości
powitanie()

# definicja funkcji z argumentem
def powitanie(imie): # imie - jest argumentem, w tym miejscu jeżeli będziemy się powoływali na tą funkcję to wprowadzamy np tekst "Tomek"
    witaj = "Witaj " + imie # zmienna witaj przy
    return witaj

print(powitanie("Tomek"))

# 
def powitanie(imie):
    witaj = "Witaj " + imie
    return witaj

l= []

for i in range(1,4):
    l.append(powitanie(input("Podaj imie: ")))
             
print(l)

# funkcja dodawanie

def dodawanie(a,b,imie="Anonim", nazwisko="Anonim"): #użycie "Anonim" pozwala przypisać wartość domyślną dla argumentu którego nie użyjemy odwołując się do funkcji
    wynik = a + b
    print(a,b)
    print(imie, nazwisko)
    return wynik

rezultat = dodawanie(2,2, nazwisko="Prysak")
print(rezultat)

def dodawanie(a,b,imie="Anonim", nazwisko="Anonim"):
    wynik = a + b
    print(a,b)
    print(imie, nazwisko)
    return wynik

rezultat = dodawanie(2,2, nazwisko=input("Podaj nazwisko: "))
print(rezultat)

# ćwiczenie 40
# ---
def silnia(n):
    wynik = 1
    i = 1
    while (i <= n):
        wynik = wynik*i
        i = i + 1
    return wynik
# ---
n = int(input("Podaj liczbę silni: "))

rezultat = silnia(n)
print(rezultat)

# ćwiczenie 41
# ---
def silnia(n):
    wynik = 1
    l = []
    i = 1
    while (i <= n):
        wynik = wynik*i
        l.append(wynik)
        i = i + 1
    return l
# ---
def wyswietl(lista):
    for i in lista:
        print(i, end=" ")
# ---

n = int(input("Podaj liczbę silni: "))

wyswietl(silnia(n))

# ćwiczenie 42
# ---
def fibonacci(n):
    wynik = 0
    suma = 0
    f = [0,1]
    i = 2
    while (i < n):
        wynik = (f[i-2]+f[i-1])
        f.append(wynik)
        i = i + 1
    for i in f: # pamiętaj o tym, że pod to i przypisywana jest napierw pierwsza wartość z naszej tablicy !!!!! może tam być 1 ale równie dobrze i 10 !!!!!
        suma = suma + i
    return f[len(f)-1], suma, f
# ---

n = int(input("Podaj długość ciągu fibonacciego: "))

fib = fibonacci(n)

print("Ostatni element, suma ciągu, cały ciąg: ", fib)

# ćwiczenie 43 v1

def zdania(a = 5):
    wyrazy = ["pierwsze", "dwadzieścia", "wyrazów", "ciągu", "fibonacciego", "to"]
    i = 0
    zdanie = []
    while (i < a):
        zdanie.append(wyrazy[random.randint(0,len(wyrazy)-1)]) # losuję sobie indeks z naszej listy 
        i = i + 1
    return zdanie
    
def formatowanie(zdanie):
    for i, v in enumerate(zdanie):
        if (i == 0):
            print(v.capitalize(), end=" ")
        elif (i == len(zdanie)-1):
            print(v, end=" .")
        else:
            print(v, end=" ")

formatowanie(zdania())

# ćwiczenie 43 v2

def zdania(a = 5):
    wyrazy = ["pierwsze", "dwadzieścia", "wyrazów", "ciągu", "fibonacciego", "to"]
    i = 0
    zdanie = random.sample(wyrazy,a)
    return zdanie
    
def formatowanie(zdanie):
    for i, v in enumerate(zdanie):
        if (i == 0):
            print(v.capitalize(), end=" ")
        elif (i == len(zdanie)-1):
            print(v, end=".")
        else:
            print(v, end=" ")

formatowanie(zdania(3))

# ćwiczenie 44

def odleglosc(x1,y1,x2,y2):
    d = sqrt(((x2-x1)**2)+((y2-y1)**2))
    return round(d, 2)

print(odleglosc(1,1,5,5))

# ćwiczenie 45

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