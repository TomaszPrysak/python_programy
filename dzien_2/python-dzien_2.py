# -*- coding: utf-8 -*-
import random

'''
### typy sekwencyjne 
## 4. typy słowników
# w typach słowników stosujemy nawiasy klamrowe {}

literki = {"a" : "A", "b" : "B", "c" : "C",}
print(literki)
print(len(literki)) # funkca len zwraca długość sekwencji czy to w napisach czy to w listach 

#wypisanie pierwszy element słownika
print(literki["a"], literki["b"])

#odyfikacja wartości klucza
literki["c"] = "test"
print(literki)
print(literki["c"])

# wyświetla klucze tylko lucze
print(literki.keys())

# dodanie jednego klucza i usunięcie jednego klucza
literki["d"] = "D"
del literki["c"]
print(literki)

#klucze liczboe
literki[2] = "abc"
print(literki)

#konwertowanie słownika na napis
to_str = str(literki)
print(to_str[0], to_str[1])

# ćwiczenie 21
# przypisanie słowie liczbe dziesiętną
cyfra = input("Zapisz słownie cyfrę z przedziału od 1 do 5: ")
to_dec = {'jeden':1, 'dwa':2, 'trzy':3, 'cztery':4, 'pięć':5, 'piec':5}
print(cyfra + " w postaci dziętnej to: " + str(to_dec[cyfra]))

# ćwiczenie 22
# UWAGA!!! wartość klucza słownika pierwszego jest kluczem sownika drugiego
cyfra = input("Podaj słownie cyfrę z przedziału od 1 do 5: ")
dziesietny = {'jeden':1, 'dwa':2, 'trzy':3, 'cztery':4, 'pięć':5, 'piec':5}
rzymski = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V"}
print(cyfra + " w postaci liczby dziesiętnej to: " + str(dziesietny[cyfra]) + ", a w postaci rzymskiej: " + str(rzymski[dziesietny[cyfra]]))

# ćwiczenie 23
produkt = input("Podaj produkt który chcesz zamówić (chleb, bułki, bagietka): ")
art = {"chleb":"001", "bułki":"002", "bagietka":"003"}
cena = {"001": 1.29, "002":0.59, "003":0.89}
ilosc = int(input("Podaj ilość wybranego produktu: "))

print("Do zapłaty: " + str(cena[art[produkt]]*ilosc) + " zł (" + str(round((cena[art[produkt]]*ilosc)*1.23,2)) + " brutto)")

## 5. typy zbiorów
# 
figury = set(['kolo', 'kwadrat', 'trojkat'])

# dodawanie do zbioru
figury.discard('trojkat')
figury.add('elipsa')
print(figury)

# metody teoriomnogościowe
okragle = set (['kolo'])
print(len(figury), len(okragle))
print(figury.issubset(okragle))
print(figury.issuperset(okragle))

# operacje na zbiorach
print(figury | okragle) # połączenie dwóch zbiorów
print(figury & okragle) # część wspólna zbiorów
print(figury - okragle) # różnica zbiorów
print(figury ^ okragle) # różnica symetryczna


# ćwiczenie 24
# losowanie 6 z 49 liczba
lotto = set ()
lotto.add(random.randint(1, 49))
lotto.add(random.randint(1, 49))
lotto.add(random.randint(1, 49))
lotto.add(random.randint(1, 49))
lotto.add(random.randint(1, 49))
lotto.add(random.randint(1, 49))
lotto.add(random.randint(1, 49))
lotto.add(random.randint(1, 49))
lotto.add(random.randint(1, 49))
lotto.add(random.randint(1, 49))

wynik=list(lotto) # przekształcamy na krotke 
print(wynik[:6]) # z tej krotki wyświetlamy tylko 6 wyników zeby unikn

###
### Instrukcje warunkowa
###

### Instrukcja warunkowa if

a = int(input("Podaj liczbę: "))

# samo if bez else
if (a%2 == 0):
    print("Podana liczba " + str(a) + " jest parzysta")
    print("Jestem jeszcze w pęli")

print("Wyszedłem z pętli")

# z else z warunkiem jeżeli nie prawda
if (a%2 == 0):
    print("Podana liczba " + str(a) + " jest parzysta")
    print("Jestem jeszcze w pęli")
else:
    print("Podana liczba " + str(a) + " jest NIEparzysta")
    
print("Wyszedłem z pętli")

# if zagnieżdżone
a = int(input("Podaj liczbę: "))

if (a%2 == 0):
    print("Podana liczba " + str(a) + " jest parzysta")
    if (a >= 10):
        print("Podana liczba " + str(a) + " jest parzysta i większa równa od 10")
    else:
        print("Podana liczba " + str(a) + " jest parzysta i mniejsza równa od 10")
else:
    print("Podana liczba " + str(a) + " jest NIEparzysta")
    
print("Wyszedłem z pętli")


# z elif
a = int(input("Podaj liczbę: "))

if (a%2 == 0 and a >= 10):
    print("Podana liczba " + str(a) + " jest parzysta i większa równa od 10")
elif (a%2 == 0 and a<10):
    print("Podana liczba " + str(a) + " jest parzysta i mniejsz od 10")
else:
    print("Podana liczba " + str(a) + " jest NIEparzysta")
    
print("Wyszedłem z pętli")

# ćwiczenie 25

if (1):
    print("Wartość 1 jest: " + str(bool(1))
if (2):
    print("Wartość 2 jest: " + str(bool(2))
if (3):
    print("Wartość 3 jest: " + str(bool(3))
if (4):
    print("Wartość 4 jest: " + str(bool(4))

# ćwiczenie 26

a= int(input("Podaj liczbę: "))

if (a >= 0 and a <=10):
    print("Podana liczba: ", a, "zawiera się w przedziale 0-9")
else:
    print("Podana liczba: ", a, "znajduje się poza przedziałem 0-9")

# ćwiczenie 27

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a= int(input("Podaj liczbę: "))

if (a >= 0 and a <= (len(lista)-1)):
    print("Podana liczba: ", a, "jest OK")
    print(lista[a])
else:
    print("Podana liczba: ", a, "jest poza zakresem")

# ćwiczenie 27

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if (lista[0] > 0 and lista[1] > 0):
    print("Oba elementy są większe od zera")
elif (lista[0] > 0 and lista[1] < 0):
    print("Pierwszy element jest większy od zara, a drugi mniejszy")
elif (lista[0] < 0 and lista[1] > 0):
    print("Pierwszy element jest mniejszy od zara, a drugi mniejszy")
else:
    print("Oba elementy są mniejsze od zera")

# ćwiczenie 28

A = set([1, 2, 3, 4, 5])
B = set([8])


if (A==B): # najpierw sprawdzamy czy zbiory są równe
    print("Zbiory są równe")
elif (A.issuperset(B)): # następnie sprwdzamy czy zbiór A jest nadzbiorem zbioru B
    print("Zbiór A jest nadzbiorem zbioru B")
elif (B.issuperset(A)):
    print("Zbiór B jest nadzbiorem zbioru B")
else:
    print("Zbiory są różne")


###
### Pętle
###
    
## Pętla while

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0

while (i <= (len(lista)-1)):
    print("Index: " + str(i) + "\t Wartość: " + str(lista[i]))
    i = i + 1

print("Poza pętlą")

# ćwiczenie

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0

while (i <= (len(lista)-1)):
    if (lista[i]%2 == 0):
        print("Index: " + str(i) + "\t Wartość: " + str(lista[i]))
    i = i + 1
print("Poza pętlą")

# ćwiczenie

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = len(lista)-1

while (i >= 0):
    if (lista[i]%2 == 0):
        print("Index: " + str(i) + "\t Wartość: " + str(lista[i]))
    i = i - 1
else: # else wywołuje się w momencie kiedy wykonane zostaną wszystkie interacje i program przechodzi do instrukcji ELSE
    print("Jestem w ELSE")
print("Poza pętlą")

## Zagnieżdżęnie trójarguimentowe

a = 31

b = 30

print("a jest większe od b o: ", a-b) if (a>=b) else print("a jest mniejsze od b o:", b-a)

## pętla for-in stosowana do list

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for var in lista:
    print("Wartość: " + str(var))
    
for index, var in enumerate(lista):
    print("Index: " + str(index) + "\tWartość: " + str(var))

## petla for-in stosowana do słowników
    
slownik = {1: "Tomek", 2: "Prysak", 3: "Mistrz"}

for key in slownik:
    print(key, slownik[key])


    
# zagnieżdżenia

slownik = {"a": 1, "b": 2, "c": 3}

for key in slownik:
    if (slownik[key] >= 2):
        print(key, slownik[key])
      
## szybkie sekwencje bez konieczności wpisywania zawartości w tabeli

s1 = range(100)
# wypisywanie wszystkich wartość z listy
for i in s1:
    print(i)
# bezpośrednie umieszczenie funkcji tworzenia listy w funkcji for-in
for j in range(10,16):
    print(j)
# wypisywanie wartosci z listy co jakis skok
for x in range(10,21,2):
    print(x)
# wypisanie wartości z listy z jednoczesnym podniesieniem jej do kwadratu
for x in range(10,21,2):
    print(x, x**2)    
    

# formatowanie wypisywania zawartości z listy

for k in range(0, 100):
    print("Wynik: %4i%6i%8i" % (k, k**2, k**3)) # każdy procent odpowiada konkretnym miejscom k w nawiasie --- pierwszy % -> k, drugi % -> k**2, trzeci % -> k**3

for x in range(0,100): 
    print("Pierwiastkiem liczby %2i jest %-5.3f" % (x, x**0.5)) # zwrócić uwagę na znaki tuż po procentach w stringu....
    

# ćwiczenie 29

sklep_produkty = {"komputer" : 1, "drukarka" : 2, "monitor" : 3, "myszka" : 4, "klawiatura" : 5, "głośniki" : 6}
produkty_cena = {1: 2500, 2:350, 3:780, 4:45, 5:80, 6:150}
produkty_dostepnosc = {1: 8, 2:13, 3:7, 4:99, 5:9, 6:4}

suma = 0
tn = "t"

while (tn == "t"):
        zamowienie = input("Podaj towar: ")
        zamowienie_ilosc = int(input("Podaj ilość sztuk zamawianego produktu: "))
        if (zamowienie in sklep_produkty.keys()):
                if (produkty_dostepnosc[sklep_produkty[zamowienie]] >= zamowienie_ilosc):
                        print("Produkt " + "'" + zamowienie + "'" + " jest dostępny")
                        print("Zamawiasz: " + str(zamowienie_ilosc) + " szt.")
                        suma += zamowienie_ilosc*produkty_cena[sklep_produkty[zamowienie]]
                elif (produkty_dostepnosc[sklep_produkty[zamowienie]] < zamowienie_ilosc):
                        print("Produk jest dostępny: " + zamowienie)
                        print("Dostepne jest tylko: " + str(produkty_dostepnosc[sklep_produkty[zamowienie]]) + " szt")
                else:
                        print("Brak produktu w sklepie")
        tn = input("Czy chcesz zamawiać dalej (tak/nie) ? ")         
print("Do zapłaty: " + str(suma))


# ćwiczenie 30

# wersja 1
cyfry = {"0":"zero","1":"jeden","2":"dwa","3":"trzy","4":"cztery","5":"pięć","6":"sześć","7":"siedem","8":"osiem","9":"dziewięć"}

lista= []
i ="t"

while (i == "t"):
    liczba = input("Podaj wartosć (cyfrę z przedziału 0-9) do przekonwertowania na formę tekstową: ")
    if (liczba.isdigit()):
        lista.append(cyfry[liczba]) # tutaj dodaje do listy nie cyfrę wprowadzoną przez użytkownika, a cyfrę słownie którą pobiera ze słownika
    else:
        print("Wprowadzona wartość nie jest cyfrą")
    i = input("Czy chcesz podać nową wartość (cyfrę z przedziału 0-9) ? (tak/nie)")
    
for i in lista:
    print(i, end="")

# wersja 2
cyfry = {"0":"zero","1":"jeden","2":"dwa","3":"trzy","4":"cztery","5":"pięć","6":"sześć","7":"siedem","8":"osiem","9":"dziewięć"}
    
lista= []
i ="t"
    
while (i == "t"):
    liczba = input("Podaj wartosć (cyfrę z przedziału 0-9) do przekonwertowania na formę tekstową: ")
    if (liczba.isdigit()):
        lista.append(liczba) # tutaj dodaje do listy nie cyfrę wprowadzoną przez użytkownika, a cyfrę słownie którą pobiera ze słownika
    else:
        print("Wprowadzona wartość nie jest cyfrą")
    i = input("Czy chcesz podać nową wartość (cyfrę z przedziału 0-9) ? (tak/nie)")
    
print(lista)
print(cyfra[lista[0]])

# ćwiczenie 31

print("    %4i%4i%4i%4i%4i%4i%4i%4i%4i%4i" % (1,2,3,4,5,6,7,8,9,10))
print("============================================")

for i in range(1,11):
    print(str(i) + "|", end="")) # end="" - wymuszamy brak przejścia do nowej lini
    print("%4i%4i%4i%4i%4i%4i%4i%4i%4i%4i" % (i, i*2, i*3, i*4,i*5,i*6,i*7,i*8,i*9,i*10))
    '''

# ćwiczenie 32

lista = range(1,10,2)

i = len(lista) - 1
while (i>=0):
    print(lista[i]**2)
    i = i - 1
    
### moment zrzucenia do GITa
