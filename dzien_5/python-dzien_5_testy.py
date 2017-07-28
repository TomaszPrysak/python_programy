# -*- coding: utf-8 -*-

#from Pakiet.modul import *
import Pakiet.modul

###
### Operacje na plikach
###

print(Pakiet.modul.a)

Pakiet.modul.info()

F = open("plik.txt", "w") # plik jest w trybie zapisu
print(F.closed, F.mode, F.name)
F.write("Start")
F.write("Kolejny napis")
F.writelines(["\n2 linia", "\n3 linia", "\n4 linia", "\n5 linia"])
F.close()
print(F.closed, F.mode, F.name)

G = open("plik.txt", "r")
print(G.read(10)) # wyświetlamy w pythonie to co jest w pliku plik.txt w tym przypadku pierwsze 10 znaków
print(G.tell()) # wyświetlenie pozycji kursora w pliku
G.seek(0) # ustawienie kursora na początku pliku
print(G.tell())
G.seek(20) # ustawienie kursora na 20 pozycji w pliku
print(G.tell())
G.seek(0,2) # ustawienie kursora na pierwszej pozycji od końca
print(G.tell())

