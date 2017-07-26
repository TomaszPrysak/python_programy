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

# ćwiczenie 34 ver1
#ciąg geometryczny
a1 = int(input("Podaj pierwszy wyraz ciągu geometrycznego: "))
n = int(input("Podaj ile chcesz mieć wyrażeń w ciągu: "))
q = int(input("Podaj q: "))

i = 0
s = 0

while (i <= n):
    s = s + (a1*(q**i))
    i = i + 1
    
print(s)

# ćwiczenie 34 ver2
#ciąg geometryczny - aby zrozumieć to zadanie 
a1 = float(input("Podaj a1: "))
n = float(input("Podaj n: "))
q = float(input("Podaj q: "))

i = 0
s = 0

l = []

while (i < n):
    s = s + (a1*(q**i))
    l.append(a1*(q**i))
    i = i + 1

print("Ostatni wyraz ciągu geometrycznego:", a1*(q**(n-1)))

print("%35s%15.2f" % ("Suma:", s))

print("%35s" % ("Składowe:"), end="")

for i, v in enumerate(l):
    if (i == 0):
        print("%5.2f" % (v), end=" ")
    else:
        print("%5.2f" % (v), end=" ")
        

# ćwiczenie 35
# szukanie w napisie podanej przez użytkownika literki
napis = input("Wprwadź napis: ")
szukane = input("Wprowadź czego szukamy: ")

i = 0
licznik = 0

while (i <= (len(napis)-1)):
    if (napis[i] == szukane):
        print("Znaleziono:", szukane, "na pozycji", i + 1)
        licznik = licznik +1
    i = i + 1
    
print("Znaleziono:", szukane, "znaleziono:", licznik, "razy")

# ćwiczenie 36 vr 1
# szukanie w napisie podnanej przez użytkownika frazy

napis = input("Wprwadź napis: ")
szukane = input("Wprowadź czego szukamy: ")

x = len(napis)
y = len(szukane)

i = 0
licznik = 0

while (i <= x):
    tab = napis[i:i+y] # zrzuca do tablicy 
    if (tab == szukane):
        print("Znaleziono:", szukane, "na pozycji", i + 1)
        licznik = licznik + 1
    i = i + 1
    
print("Znaleziono:", szukane, "znaleziono:", licznik, "razy")

# ćwiczenie 36 ver 2
# 
napis = input("Wprwadź napis: ")
szukane = input("Wprowadź czego szukamy: ")

x = len(napis)
y = len(szukane)

i = 0
licznik = 0

while (i <= x):
    tab = napis[i:i+y]
    if (tab == szukane):
        print("Znaleziono:", szukane, "na pozycji", i + 1)
        licznik = licznik + 1
        i = i + len(szukane)
    else:
        i = i + 1
    
print("Znaleziono:", szukane, "znaleziono:", licznik, "razy")

# ćwiczenie 37
# tabela przeliczen Celcjusza na Farenhajta z przedziału (-20) - (40)
c = range(-20, 45, 5)
i = len(c) - 1

print("%5s   |%5s" % ("C", "F"))

while (i >= 0):
    print("%+5i   |%5i" % (c[i], (c[i]*1.8)+32))
    i = i - 1

# ćwiczenie 38
# tabela przeliczen Celcjusza na Farenhajta z przedziału podawanego przez użytkownika oraz kroku też przez użytkownika

x = int(input("Podaj startową wartość tablicy: "))
y = int(input("Podaj końcową wartość tablicy: "))
z = int(input("Podaj krok tablicy: "))

while (abs(y - x) < z):
    print("Podany krok jest zbyt duży: ")
    z = int(input("Podaj krok tablicy: "))

if ((y-x) % z == 0):
    c = range(x, y-z , z)
else:
    c = range(x, y, z)

i = len(c) - 1

print("%5s   |%5s" % ("C", "F"))

while (i >= 0):
    if ( c[i] == 0): # warunek na wydzielenie zera oraz zapisanie go bez plusa
        print("------------------")
        print("%5i   |%5i" % (c[i], (c[i]*1.8)+32))
        print("------------------")
    else:
        print("%+5i   |%5i" % (c[i], (c[i]*1.8)+32))
    i = i - 1
    
# ćwiczenie 39
# elektroniczny dziennik, mamy zdefiniowaną listę ocen
# uczen podaje ocene i jest ona dopisywana do jego listy ocen i sprawdzana czy znajduje się w zdeifniowanej liście ocen
# jeżeli ocena znajduje się na liście to dodaje ją do listy ocen ucznia i uczeń ma możliwość wprowadzenia kolejnej oceny
# naciśnięcie ENTER powoduje zakonczenie wprowadzania ocen

oceny = ("1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5" "5.5", "6")

uczen = []

i = "a" # nadajemy i taką wartość zeby nie była pusta

while (i != ""): # sprawdza czy i jest puste, ale po to sprawdza bo na początku nie jest puste ale później 
    i = input("Podaj ocenę: ")
    if (i in oceny):
        uczen.append(float(i))
    elif (i == ""):
        print("Naciśnięcie ENTER spowodowało zakończenie wprowadzania ocen")
    else:
        print("Podana wartość nie jest jest oceną")

print(uczen)

sr = 0 
if (len(uczen) != 0):
    for i in uczen:
        sr = sr + i
        print("Średnia Twoich ocen: ", round(sr/len(uczen), 2))
else:
    print("Brak wprowadzonych ocen do wyliczenia średniej")