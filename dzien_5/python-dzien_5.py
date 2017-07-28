# -*- coding: utf-8 -*-

import pymysql

import modul

###
### Połączenie z bazą danych
###

class MySQLConnector:
    def __init__(self, password):
        self.password = password
        self.conn = pymysql.connect("localhost", "root", self.password, "skoczkowie")
        self.c = self.conn.cursor()
        print("Połączono z bazą danych")
        nav = ""
        while(nav != "Q"):
            nav = input("Co chcesz zrobić? (S)elect, (I)nsert, (U)date, (Q) - wyjście, : ")
            if (nav == "S"):
                self.select()
            elif (nav == "I"):
                self.insert()
            elif (nav == "U"):
                self.update()
        print("Połączenie zakończone")
        self.conn.close()
    def select(self):
        self.c.execute("select id_skoczka, imie, nazwisko, kraj from zawodnicy order by id_skoczka;")
        result = self.c.fetchall()
        print("ID", "Imię", "Nazwisko", "Kraj")
        for v in result:
            id = v[0]
            imie = v[1]
            nazwisko = v[2]
            kraj = v[3]
            print("%-3s %-15s %-15s %-3s" % (id, imie, nazwisko, kraj))
    def insert(self):
        self.c.execute("insert into zawodnicy values (18, 'TEST', 'TEST', 'XXX', '1982-09-04', 166, 56);")
        self.conn.commit
        print("Dane wprowadzono")
    def update(self):
        self.c.execute("update zawodnicy set kraj = 'YYY' where id_skoczka = 18;")
        self.conn.commit
        print("Dane zaktualizowano")        

c1 = MySQLConnector("Pitek1962mySQLF700Gs")