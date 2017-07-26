# -*- coding: utf-8 -*-

# ćwiczenie 39
# tabela przeliczen Celcjusza na Farenhajta z przedziału podawanego przez użytkownika oraz kroku też przez użytkownika

oceny = ("1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5" "5.5", "6")

uczen = []

i = "a"

while (i != ""): 
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
    print("Brak podanych ocen do wyliczenia średniej")