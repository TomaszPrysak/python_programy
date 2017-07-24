# -*- coding: utf-8 -*-
'''
###
### zmienne
###

zmienna1 = 5
zmienna2 = 5.3


poczatek komentarza wielowierszowego

# komentarz jednowierszowy

text = "tekst jako zmienna w cudzyslowiu"
text2 = 'tekst jako zmienna w apostrofach'
literka = "A"
literka = 'a'

koniec komentarza wielowierszowego
'''

'''
witaj = "I'm Pitek" # jezeli chcemy aby w tekscie byl apostrof ale nie bylo to interpretowane jako poczatek/koniec tekstu to umieszczamy go w cudzyslowiu (i odwrotnie, jezeli checy aby cudzyslow byl w tekscie to umieszczamy go w apostrofach)

zmienna3 = 2 + 5
Zmienna3 = 'liczba'

nowa_zmienna = zmienna3 + 5

###
### wypisywanie na ekranie
###

# print("wyrażenie", zmienna) wypisuje na ekranie zawartosc miedzy nawiasami
print(zmienna1)
print(zmienna1, zmienna2)
print(witaj)
print(zmienna3, Zmienna3)
print(nowa_zmienna)

print("Hi " + witaj)

print("Hi " + witaj + " and I want to be a programmer.")

# modyfikowanie wartosci zmiennej
Zmienna3 = 'liczba'
print("Przed zmiana:", Zmienna3)
Zmienna3 = 3.14
print("Po zmianie", Zmienna3)

# usuwanie zmiennej
del zmienna1 # możemy też zmienną ujać w nawiasy
#print(zmienna1) - żeby nie pojawiał się błąd


### ćwiczenie 1

a = 1
b = 2.4
c = "w1"

print(a,b,c)

### ćwiczenie 2

a = 2.1
b = "abc"
c = 0

print(a,b,c)

### ćwiczenie 3

imie = "Tomasz"
nazwisko = "Prysak"
data = "1987-02-20"
stanowisko = "bezrobotny"
placa = "null"

print(imie, nazwisko, data, stanowisko, placa)

### ćwiczenie 4
# int(wyrażenie) - zamienia wyrażenie na zmienną INTEGER
# input(wyrażenie) - pobiera wyrażenie wpisane z klawiatury i domyślnie przypiosuje zmienną STRING
pi = 3.14
promien = int(input("Podaj wartość promienia: "))
pole_kola = pi*(promien)*(promien)
# aby podnieść do kwadratu należy za wartością podnoszoną do kwadratu umieścić ** i do ktorej potęgi
print(pole_kola, pi*(promien**2))

### ćwiczenie 5

imie = input("Wprowadź imię: ")
nazwisko= input("Wprowadź nazwisko: ")
data_urodzenia = input("Wprowadź datę urodzenia: ")
stanowisko = input("Wprowadź stanowisko: ")
placa = input("Wprowadź placę: ")

print(imie, nazwisko, data_urodzenia, stanowisko, placa)

###
### typy zmiennych
###

# type(zmiena) - zwraca typ wartości zmiennej 
print(type(pole_kola))

print(type(21j))
# j - dodanie symbolu spowoduje indeksowanie tej liczy do której to j dodaliśmy jako części urojonej liczby zespolonej

# długa liczba całkowita

dluga = 31234569
print(type(dluga))
dluga2 = 32
print(type(dluga2))

# dzielenie z jednoczesnym odrzuceniem części ułamkowej zapisujemy z użyciem: //

print(3/2)
print(3//2) # pomija część ułamkową

# zaokrąglanie
# round(liczba, precyzja)

print(round(1.3), round(1.5), round(1.8)) # zaokrąglanie odbywa się matematycznie, tzn. że pomija piątkę i zaokrągla do całkowitej w górę

print(round(-1.8), round(-1.5), round(-1.3))

print(int(1.3), int(1.5), int(1.9))

### ćwiczenie 6

kwota_netto = float(input("Podaj kwotę do obliczenia podatku VAT: "))
vat = float(input("Podaj wielkość podatku VAT (3%, 7%, 23%: "))
kwota_brutto = kwota_netto + (kwota_netto*(vat/100))

print("Twoja kwota brutto przy stawce " + str(vat) + " vat wynosi: " + str(kwota_brutto) + " zł")

### ćwiczenie 7

nazwa_p1 = "chleb"
nazwa_p1 = "mleko"
nazwa_p1 = "cukierki"

cena_p1 = 1.99
cena_p2 = 2.50
cena_p3 = 6.59

zamowienie_p1 = int(input("Liczba chlebów: "))
zamowienie_p2 = float(input("Litry mleka: "))
zamowienie_p3 = float(input("Wagaq cukierków(g): "))
suma = (cena_p1 * zamowienie_p1) + (cena_p2 * zamowienie_p2) + ((cena_p3/1000) * zamowienie_p3)

print("Twoje zamówienie")
print("================")
print("Chleb: ", zamowienie_p1, " szt.")
print("Mleko: ", zamowienie_p2, " l.")
print("Cukierki: ", zamowienie_p3, " g.")
print("================")
print("Do zapłaty")
print("================")
print(round(suma), "zł")

# liczby zespolone

print((1+1j)+(12+20j))

# ćwiczenie 8

a = 12
b = 1+(-1j)

print(a*b)

# wartości typu True / False
# bool(wyrażenie) - zamienia wyrażenie na zmienną typu true/false
# jeżeli wyrażeniem będzie - "" [] () {} none - 

log1 = True
print(log1)

print(bool(""), bool(0), bool("Ala"))


# zmienne tekstowe
# znak przejścia do nowej lini
a = """
autor:
data:
wersja:
"""
print(a)

b = "autor:\ndata:\nversja:" # \n - znak przejścia do nowej lini 
print(a)

txt = "napis "

print(txt*3)

imie = str(input("Podaj imię: "))
n = int(input("Podaj krotność wypisania imienia: "))
imie1 = imie + ", "
imie2 = imie + "."

print(imie1*(n-1) + imie2)

# ćwiczenie 9

imie = input("Wprowadź imię: ")
nazwisko= input("Wprowadź nazwisko: ")
wiek = input("Wprowadź wiek: ")
stanowisko = input("Wprowadź stanowisko: ")
placa = input("Wprowadź placę: ")

txt = imie + " " + nazwisko + " " + "(wiek: " + wiek + ")" + " " + "pracuje na stanowisku:" + " " + stanowisko + " " + "(pensja: " + placa +")" + "\n"
    
print(txt*10)

# rozróżnienie płci
if imie[:-1].endswith('a'): 

    txt = "Pani" + " " + imie + " " + nazwisko + " " + "(wiek: " + wiek + ")" + " " + "pracuje na stanowisku:" + " " + stanowisko + " " + "(pensja: " + placa +")" + "\n"

    print(txt*10)

else:
    
    txt = "Pan" + " " + imie + " " + nazwisko + " " + "(wiek: " + wiek + ")" + " " + "pracuje na stanowisku:" + " " + stanowisko + " " + "(pensja: " + placa +")" + "\n"
    
    print(txt*10)

#zrzucanie tekstu do liczby

a = `1`
print(type(a))
napis = str(a)
# bool(), float(), int(), str()
print(type(napis))

### Operatory arytmetyczne
# normalnie takie jak w matematyce (dodawanie, odejmowanie itd.)

# ćwiczenie 10

netto = 5500

h = 168

kwota_netto = netto / h

print("Kwota netto za h: ", round(kwota_netto,2))
print("Kwota brutto za h: ", round((kwota_netto*1.23),2))

### Operatory logiczne
# and, or 

# ćwiczenie 11

p = True
q = True

dM1 = not(p and q)
dM2 = (not p) or (not q)

print(dM1, dM2)
print(dM1 == dM2) # dwa znaki równa się służą do porównywania

# ćwiczenie 12

a = False
b = False
c = True

bramka_1 = (not a) and (not b) and (not c)
bramka_2 = (not a) and (not b) and c
bramka_3 = (not a) and b and (not c)
bramka_4 = a and (not b) and (not c)

print(bramka_1, bramka_2, bramka_3, bramka_4)

wyjscie = bramka_1 or bramka_2 or bramka_3 or bramka_4

print(wyjscie)

### Operatory relacji
# mniejszy, większy, mniejszy bądź równy itd.

print("Ala" < "alan")

# ćwiczenie 13
# część urujona z liczby zespolonej Xj = pierwiastek z j = -1

liczba = round((17**(1/2)),2)
urojona = 1j

print(liczba*urojona)
print("Liczba zespolona: 0 + ", liczba)

# ćwiczenie 14

z = 17 % 7

print(z**2 + 3*z)

# ćwiczenie 15

w1 = 1.2e+3+34.5

print((str(w1)+";\n")*20)


# ćwiczenie 16

n1 = str(input("Podaj pierwszy napis: "))

n2 = str(input("Podaj drugi napis: "))

print("Czy napis pierwszy jest większy od drugiego: ", n1>n2)
print("Czy napis drugi jest większy od drugiego: ", n1<n2)
print("Czy napisy są sobie równe: ", n1==n2)

### znaki specjalne
#

print("imie\t"+"nazwiko\t"+"stanowisko")
'''
# ćwiczenie 17

spk = int(input("Podaj stank konta: "))
r = float(input("Podaj oprocentowanie: "))
n = int(input("Podaj liczbę lat: "))

res = spk*(1+(r/100))**n

print("Kwota po " + str(n) + " latach wynosi: " + str(res) + " zł.")