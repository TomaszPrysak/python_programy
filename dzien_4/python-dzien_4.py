# -*- coding: utf-8 -*-

# ćwiczenie 46
# rysowanie wykresu
def wykres(opcja, ilosc=10, znak="*"): # ilosc i znak to parametry funkcji
    i = 0
    wartosci = []
    if (opcja == "M" or opcja =="m"):
        while (i < ilosc):
            wartosc_user = int(input("Podaj wartość: "))
            while (wartosc_user < 0 or wartosc_user > 9):
                wartosc_user = int(input("Podana wartość nie mieści się w przedziale 0-9 podaj wartość ponownie: "))
            wartosci.append(wartosc_user)
            i = i + 1
    elif (opcja == "A" or opcja == "a"):
        while (i < ilosc):
            wartosci.append(random.randint(0, 9))
            i = i + 1        
    for i, v in enumerate(wartosci):
        print("Słupek", (i+1), ":", znak*v) 

def wybor():
    znak_user = input("Podaj znak rysujący wykres: ")
    ilosc_user = input("Podaj illość słupków: ")
    opcja_user = input("Generowanie wykresu (A)uto czy (M)anual ? ")
    while (opcja_user != "a" and opcja_user != "A" and opcja_user != "m" and opcja_user != "M"):
        opcja_user = input("BŁĄD! Generowanie wykresu (A)uto czy (M)anual ? ")
    if (znak_user == "" and ilosc_user != ""):
        wykres(opcja=opcja_user, ilosc=int(ilosc_user))
    elif (znak_user != "" and ilosc_user == ""):
        wykres(opcja=opcja_user, znak=znak_user)
    elif (ilosc_user != "" and ilosc_user != ""):
        wykres(opcja_user, int(ilosc_user), znak_user)
    else:
        wykres(opcja=opcja_user)
    
wybor()

# ćwiczenie 47

def html_export(napis, color="black", font_size="12px", font_weight="5px"):
    return '<span style="color: ' + color + '; font-size: ' + font_size + '; font-weight: ' + font_weight + '">' + napis + '</span>'

print(html_export("witaj"))

# ćwiczenie 48

kolor = "black" # zmienna globalna
licznik = 0
licznik_białego = 0
licznik_czarnego = 0

def naprzemian():
    global kolor # pobieramy zmienną globalną i następnie dynamicznie będziemy jej przypisywać nową wartość przez naszą funkcję. Funkcja ta będzie ingerować w 
    global licznik, licznik_białego, licznik_czarnego
    licznik = licznik + 1
    if (kolor == "white"):
        kolor = "black"
        licznik_czarnego = licznik_czarnego + 1
    elif (kolor == "black"):
        kolor = "white"
        licznik_białego = licznik_białego + 1
    return kolor

print(naprzemian())
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(naprzemian())
print()
print("Ilość wystąpień białego: ", licznik_białego)
print("Ilość wystąpień czarnego: ", licznik_czarnego)
print("Suma wystąpień: ", licznik)

# ćwiczenie 49 - moja szalona wersja tego programu :P

def obliczenia(a, b):
    dzialanie = input("Podaj operację działania na liczbach (Odej)mowanie lub (Dod)awanie: ")
    if (dzialanie == "Odej" or dzialanie == "odej"):
        print(a - b) 
    elif (dzialanie == "Dod" or dzialanie == "dod"):
        print(a + b)

obliczenia(2,2)

# ćwiczenie 49

def dodawanie(a,b):
    suma = a + b
    return suma

def odejmowanie(a,b):
    roznica = a - b
    return roznica

def menu2():
    print("Witaj w piekielnie skomplikowanym programie matematycznym")
    print()
    menu = input("Menu programu: (O)peracje na dwóch liczbach - (W)yjscie z programu ")
    if (menu != "O" and menu != "o" and menu != "W" and menu != "w"):
        print("ERROR! ERROR! nie rozpoznano znaku, wybierz ponownie ")
        print()
        menu = input("Menu preogramu: (O)peracje na dwóch liczbach - (W)yjscie z programu ")
    elif (menu == "O" or menu =="o"):
        wybor = input("Wykonaj: (Dod)awanie lub (Od)ejmowanie")
        if (wybor == "Od" or wybor == "od"):
            print("wynik:", odejmowanie(int(input("Podaj wartość a: ")) , int(input("Podaj wartosć b: "))))
        elif (wybor == "Dod" or wybor == "dod"):
            print("wynik:", dodawanie(int(input("Podaj wartość a: ")) , int(input("Podaj wartosć b: "))))
    elif (menu == "W" or menu == "w"):
        print()
        print("Do zobaczenia")

menu2()

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