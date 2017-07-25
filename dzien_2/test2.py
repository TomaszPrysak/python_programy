# -*- coding: utf-8 -*-

zamowienie = input("Podaj towar: ")
zamowienie_ilosc = int(input("Podaj ilość sztuk zamawianego produktu: "))

sklep_produkty = {"komputer" : 1, "drukarka" : 2, "abc" : 3, "myszka" : 4, "klawiatura" : 5, "głośniki" : 6}
produkty_cena = {1: 2500, 2:350, 3:780, 4:45, 5:80, 6:150}
produkty_dostepnosc = {1: 8, 2:13, 3:7, 4:99, 5:9, 6:4}

for k in sklep_produkty:
    if (zamowienie == k and (produkty_dostepnosc[sklep_produkty[k]] >= zamowienie_ilosc)):
        print("Produkt dostępny: " + k)
        print("Zamawiasz: " + str(zamowienie_ilosc) + " szt.")
    elif (zamowienie == k and (produkty_dostepnosc[sklep_produkty[k]] < zamowienie_ilosc)):
        print("Produk jest dostępny: " + k)
        print("Jest dostepne tylko: " + str(produkty_dostepnosc[sklep_produkty[k]]) + " szt")
    else:
        print("Brak produktu który chcesz zamówić")
        break