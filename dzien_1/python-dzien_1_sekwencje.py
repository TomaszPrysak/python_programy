# -*- coding: utf-8 -*-

###
### typy sekwencyjne
###

## 1. typy napisów

napis = "To jest długi napis"
#napis[0] = "t"
print(napis[0])

napis = "zawartość"
print(napis.capitalize())
print(napis.count("a")) # liczy ilość wystąpień "a"
print(napis.count("aw"))
print(napis.islower())
print(napis.index("a")) # pokazuje pierwsze wystąpienie litery "a"
print(napis.replace("zawa", "otw")) # zastępuje wystąpienie "zawa" na "otw", każde takie wystapienie zastępuje

## 2. typy list = tablice UWAGA !!! nawiasy kwadratowe
# tworzenie pustej listy:
tab = [] 
# dodanie komórek do listy:
tab.append(1)
tab.append("abc")
tab.append("A")
# sprawdzenie zawartości danej komórki listy
print(tab[0], tab[1], tab[2])
# wprowadzenie do listy wartości z klawiatury
oceny = []
a = input("Podaj ocenę z polskiego: ")
oceny.append(a)
oceny.append(input("Podaj ocenę z języka angielskiego: "))
print(oceny[0], oceny[1])
# zmiana wartości w liście
oceny[0] = "5"
print(oceny[0], oceny[1])
# deklaracja wartości w listy wraz z jej tworzeniem
oceny2 = [1, 2, 3]
print(oceny2[0], oceny2[1], oceny2[2])

#tworznie listy w liście i odwoływanie się do konkretnych komórek
listalist = [ [1, 2, 3], ["Nocny", [0, 1, 2]]]
print(listalist[1][1][0])
#wyświetlanie kilku elementów
oceny2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(oceny2[3:4])
print(oceny2[3:])

# konwertowanie napisu do tabeli (listy)
napis = "napis"
tabela = list(napis)
print(tabela)
tabela[2] = "W"
print(tabela)
print(tabela.pop(2))
print(tabela)

# ćwiczenie 18
# stworzenie listy artykułów spożywczch wraz z ich cenami
art = [["mleko", "cukier", "maslo"],[5.95, 2.45, 7.99]]
print("nazwa" + "\t" + "cena")
print(art[0][0] + "\t" + str(art[1][0])) # tutaj str bo ceny musimy zamienić na string bo zlepiamy poprzez 
print(art[0][1] + "\t" + str(art[1][1]))
print(art[0][2] + "\t" + str(art[1][2]))

## 3. typy krotki
# krotki nie możemy modyfikować!!! ale możemy dodawać elementy
# zastosowanie krotki: jeżeli nie chcemy żeby ktoś nam ingerował w wartości wpisywane w krotki
# tworzenie krotki UWAGA !!!! nawiasy okrągłe
krotka = ("a", 2, 13.5)
krotka2 = "a", 2, 13.5
print(krotka)
print(krotka2)

# ćwiczenie 19

krotka_data = (("mleko", "cukier", "maslo"), ("20-02-2018", "01-02-2018", "11-05-2019"))
print("Data spożycia artykułów")
print(krotka_data[0][0] + "\t" + krotka_data[1][0])
print(krotka_data[0][1] + "\t" + krotka_data[1][1])
print(krotka_data[0][2] + "\t" + krotka_data[1][2])

# ćwiczenie 20

tabela = [("Nowak", "Kowalski", "Prysak"), ("1987-02-25", "1990-02-25", "1990-10-02"), ["murarz", "tynkarz", "mechooptyk"]]
print(tabela[0][0], tabela[1][0], tabela[2][0])
print(tabela[0][1], tabela[1][1], tabela[2][1])
print(tabela[0][2], tabela[1][2], tabela[2][2])
tabela[2][0] = "dekarz" # możemy zmienić bo ta pozycja znajduje się w tabeli
print(tabela[0][0], tabela[1][0], tabela[2][0])
print(tabela[0][1], tabela[1][1], tabela[2][1])
print(tabela[0][2], tabela[1][2], tabela[2][2])
tabela[0][1] = "Bogdan" # NIE możemy zmienić bo ta pozycja znajduje się w krotce