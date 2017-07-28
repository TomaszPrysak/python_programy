# -*- coding: utf-8 -*-

import random

###
### Programowanie obiekty
###

# Klasy nadają cechy obiektom, przez które obiekty działają w konkretny sposób

# Klasa to worek w którym znajdują się nasze obiekty które mogą korzystać z cech naszej klasy

# zawsze sobie wszystko rozpisywać na kartce co się będzie działo w naszych klasach i deinicjach naszego programu, np w momencie utworzenia naszego obiektu co się dzieje w klasie

# pierwsza klasa:

class PierwszaKlasa:
    a = 1 # przypisujemy zmienne wykorzysytwane w naszej klasie
    b = "Witaj"
    
    def __init__(self, x, y): # konstrkutkro - tworzenie zeminnych globalnie widocznych w ramach naszej klasy
        self.x = x # przypisujemy wartości do zmienny aby była dostępna do całej klasy, przypisanie wprwadzonej w momencie uruchamiania obiektu zmiennej x do wewnętrznej klasowe
        self.y = y
        self.dodaj() # i od razu wywołujemy, uruchamiamy funkcji dodaj
        self.odejmowanie() # oraz funkcję odejmowanie
    
    def powitanie(self): # słowo kluczowe self podajemy w momencie kiedy pozwalamy obiektom na wyzwalanie tej definicji przez jakiś obiekt
        print("Witaj w klasie")
        
    #def dodaj(self, x, y):
    def dodaj(self):
        #self.x = x # składnia, że wartość przypisana do x będzie zależna od obiektu który będzie ją wywoływać, wypisujemy jeżeli nie mamy konstruktorów
        #self.y = y
        print("Dodawanie")
        self.wynik_d = self.x + self.y
    
    def odejmowanie(self):
        print("Odejmowanie")
        self.wynik_o = self.x - self.y
    
    def __str__(self): # rzutowanie do printa, to znaczy, że jak uruchomię printa z naszego obiektu to wyświetli się to co zapisaliśmy w tej klasie
        return "Wynik dodawania wynosi: " + str(self.wynik_d) + ", a odejmowania: " + str(self.wynik_o)
    
    def __add__(self, other): # to służy do łączenia operacji na dwóch obiektach, dla przykładu naszego to jest dodawanie, ale może być coś innego
        return self.x + other.x, self.y + other.y # self pochodzi z obiektu1, other pochodzi z obiektu2
    
    def __ge__(self, other):
        return self.wynik_d > other.wynik_o

obiekt1 = PierwszaKlasa(5, 6) # tutaj tworzymy obiekt który może korzystać z cech klasy, dzięki czemu po wpisaniu jego nazwy po kropce będą się wyświetlać cechy tej klasy z których możemy korzystać
                              # ponieważ zdefiniowaliśmy konstruktor klasy w nawiasie podajemy wartości dla zmiennych utworzonych konstruktorze i w ramach całej tej klasy i każdej funkcji itd zmienne będą miały tą wartośc którą zaimplementowaliśmy w konstruktorze

print(obiekt1)

obiekt2 = PierwszaKlasa(1, 2)

# rzutowanie z __str__
print(obiekt2)
# rzutowanie z __add__
print(obiekt1 + obiekt2)
# rzutowanie z __ge__ (operację większy/równy)
print(obiekt1 >= obiekt2)
# powyższe wykonane BEZ korzystania z __ge__
print(obiekt1.wynik_d > obiekt2.wynik_d)



# ćwiczenie 51

class BMI:
    def __init__(self, imie, nazwisko, waga, wzrost): # tuaj tworzymy sobie od razu zmienne które są nam potrzebne do korzystanie przez nasz obiekt i do nich będziemy 
        self.imie = imie 
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost
        self.obliczenia()
    def obliczenia(self):
        self.bmi = round(self.waga / ((self.wzrost/100)**2), 2)
    
    def __str__(self):
        return "BMI zawodnika " + self.imie + " " + self.nazwisko + " wynosi: " + str(self.bmi)
    
zawodnik1 = BMI("Pitosław", "Mirosław", 60, 190) # tworzenie obiektu zawodnik1 z powiązaniem z klasą BMI i parametrami wynikającymi z def __init__

print(zawodnik1)

print(BMI("Tomasz", "Prysak", 70, 174))

# UCZYMY SIĘ OD POCZĄTKU OBIEKTÓW

#-----------Klasa--początek-------
class Sklep:
    def __init__(self, towar, cena, ilosc): # tutaj trafiają argumenty wprowadzone w momencie tworzenia obiektu zakupy1 i ich wartości są przypisywane do zmiennych SELF aby były dostępne w całej klasie
        self.towar_klasa = towar
        self.cena_klasa = cena
        self.ilosc_klasa = ilosc
        # self.zaplata_calkowita = self.do_zaplaty*1.23 # dzięki RETURNOWI ale jeżeli zmienna jest bez SELF
    def zaplata(self): # zawsze w każdej metodzie musimy podawać SELF
        self.do_zaplaty = self.cena_klasa * self.ilosc_klasa # użyliśmy zmiennej z przedrostkiem SELF dzięki czemu znowu mamy dostęp do tej zmeinnej w ramach całej klasy
        # return self.do_zaplaty # return jest potrzebne wtedy jeżeli nie nie tworzymy zmiennej SELF dostępnej dla całej klasy

#-----------Klasa--koniec-------

zakup1 = Sklep("Chleb", 4.99, 4) # Tworzymy obiekt zakup1 i odwołujemy się do klasy Sklep i w związku z tym, że klasa ta ma 3 argumenty to podajemy wartości dla tych argumentów, i te argumenty trafiają do konstruktora klasy i tam są podstawiane 

print(zakup1.cena_klasa) # obiekt ma dostęp do każdej zmiennej w obiekcie
print(zakup1.ilosc_klasa) # obiekt ma dostęp do każdej zmiennej w obiekcie
print(zakup1.towar_klasa) # obiekt ma dostęp do każdej zmiennej w obiekcie

zakup1.zaplata() # obiekt mam dostęp do każdej metody, funkcji w klasie

# ćwiczenie 52

class LOTTO:
    def __init__(self):
        print(random.sample(range(1,50),6))

for v in range(1,7):
    lotto1 = (LOTTO)    
    
# ćwiczenie 53

class LOTTO:
    def __init__(self):
        self.l = range(1,50)
        self.tab = random.sample(self.l,6)
        self.sort()
    def sort(self):
        self.tab_sort = sorted(self.tab)
    def __str__(self):
        self.res = ""
        for i, v in enumerate(self.tab_sort):
            if (i == len(self.tab_sort) - 1):
                self.res = self.res + str(v)
            else:
                self.res = self.res = str(v) + " "
        return "Wynik losowania: " + self.res
        
lotto1 = LOTTO()
print(lotto1)

## dziedziczenie klas
# aby przeciążyć metody muszą się one tak samo nazywać
# ćwiczenie 54

class szkolenia: # klasa bazowa
    def __init__(self, nazwa, termin, cena_n, il_os):
        self.nazwa = nazwa
        self.termin = termin
        self.cena_n = cena_n
        self.il_os = il_os
    def obliczCalk(self):
        self.suma_b = self.cena_n * self.il_os * 1.23
        return self.suma_b

class technologie(szkolenia):
    def __init__(self, nazwa, termin, cena_n, il_os, technologia, poziom): # podczas dziedziczenia klas w klasie podrzędnej "technologie" muszę podać argumenty które będe pobierać z klasy nadrzędnej "szkolenia" PLUS moje nowe argumenty
        super().__init__(nazwa, termin, cena_n, il_os) # pobieranie argumentów z klasy "szkolenia"
        self.technologia = technologia
        self.poziom = poziom
        
class trenerzy(technologie):
    def __init__(self, nazwa, termin, cena_n, il_os, technologia, poziom, imie, nazwisko, pensja):
        super().__init__(nazwa, termin, cena_n, il_os, technologia, poziom) # super oznacza żeby interpreter szukał w klasie wyżej
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
    def obliczCalkTrenerzy(self): # dziedziczenie metody z klasy "szkolenia"
        return self.obliczCalk() - (self.pensja * 1.23) 
        

s1 = technologie("Python dla dzieci", "2017-09-10", 2000, 10, "Python 3,6", "podstawowy")
print(s1.obliczCalk())

s2 = trenerzy("Python dla dzieci", "2017-09-10", 2000, 10, "Python 3,6", "podstawowy", "Tomasz", "Prysak", 10000)
print(s2.obliczCalkTrenerzy())

# ćwiczenie 55

class produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
    def __str__(self):
        return "Produkt: " + self.nazwa + " o cenie: " + str(self.cena)
class oprogramowanie(produkt):
    def __init__(self, nazwa, cena, jezyk, system): 
        super().__init__(nazwa, cena) 
        self.jezyk = jezyk
        self.system = system
    def __str__(self):
        return "Produkt: " + self.nazwa + " o cenie: " + str(self.cena) + " " + self.jezyk + " " + self.system
class szkolenie(oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin
    def __str__(self):
        return "Produkt: " + self.nazwa + " o cenie: " + str(self.cena) + " " + self.jezyk + " " + self.system + " " + self.termin

sk1 = szkolenie("Witaj Python", 1000, "Python2.8", "MacOS", "2017-09-10")

print(sk1)

# ćwiczenie 56

class pracownik:
    def __init__(self, imie, nazwisko, etat="staż", pensja=500):
        self.imie = imie
        self.nazwisko = nazwisko
        self.etat = etat
        self.pensja = pensja
    def przelicz(self):
        self.pensja_b = self.pensja * 1.23
        return self.pensja_b, self.pensja       
class kontrakt(pracownik):
    def __init__(self,  imie, nazwisko, etat="staż", pensja=500):
        super().__init__(imie, nazwisko, etat, pensja)
    def zmienKontrakt(self, etat, pensja):
        self.etat = etat
        self.pensja = pensja     
    def nadgodziny(self, h):
        self.h = h
        self.pensja = self.pensja + ((self.pensja/(20*8)) * self.h)
    def __str__(self):
        return "Pensja pracownika " + self.imie + " " + self.nazwisko + " wraz z nadgodzinami: " + str(self.pensja * 1.23) + " zł"
    
p1 = kontrakt("Adam", "Nieborak")
print(p1.przelicz())
p1.zmienKontrakt("murarz", 8500)
print(p1.przelicz())
p1.nadgodziny(20)
print(p1.przelicz())
print(p1)