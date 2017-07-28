# -*- coding: utf-8 -*-

import random

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
    