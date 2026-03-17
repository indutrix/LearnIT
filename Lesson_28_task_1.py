class Ksiazka:
    def __init__(self, tytul, autor, isbn, rok, dostepna):
        self.tytul = tytul
        self.autor = autor
        self.isbn = isbn
        self.rok = rok
        self.dostepna = dostepna

    def info(self):
        print("Tytuł:", self.tytul)
        print("Autor:", self.autor)
        print("ISBN:", self.isbn)
        print("Rok:", self.rok)
        if self.dostepna == True:
            print("Status: dostępna")
        else:
            print("Status: wypożyczona")


class Czytelnik:
    def __init__(self, imie, nazwisko, numer_czytelnika):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_czytelnika = numer_czytelnika
        self.wypozyczone_ksiazki = []

    def info(self):
        print("Imię:", self.imie)
        print("Nazwisko:", self.nazwisko)
        print("Numer czytelnika:", self.numer_czytelnika)

    def pokaz_wypozyczone(self):
        if len(self.wypozyczone_ksiazki) == 0:
            print(self.imie, "nie wypożyczył/a żadnej książki")
        else:
            print(self.imie, "wypożyczył/a:")
            for ksiazka in self.wypozyczone_ksiazki:
                print("-", ksiazka.tytul)


class Biblioteka:
    def __init__(self, nazwa, adres):
        self.nazwa = nazwa
        self.adres = adres
        self.__ksiazki = []
        self.__czytelnicy = []

    def dodaj_ksiazke(self, ksiazka):
        self.__ksiazki.append(ksiazka)
        print("Dodano książkę:", ksiazka.tytul)

    def dodaj_czytelnika(self, czytelnik):
        self.__czytelnicy.append(czytelnik)
        print("Zarejestrowano czytelnika:", czytelnik.imie, czytelnik.nazwisko)

    def wypozycz_ksiazke(self, czytelnik, isbn):
        for ksiazka in self.__ksiazki:
            if ksiazka.isbn == isbn:
                if ksiazka.dostepna == True:
                    ksiazka.dostepna = False
                    czytelnik.wypozyczone_ksiazki.append(ksiazka)
                    print(czytelnik.imie, "wypożyczył/a:", ksiazka.tytul)
                else:
                    print("Książka jest już wypożyczona")
                return
        print("Nie znaleziono książki o ISBN:", isbn)

    def zwroc_ksiazke(self, czytelnik, isbn):
        for ksiazka in czytelnik.wypozyczone_ksiazki:
            if ksiazka.isbn == isbn:
                ksiazka.dostepna = True
                czytelnik.wypozyczone_ksiazki.remove(ksiazka)
                print(czytelnik.imie, "zwrócił/a:", ksiazka.tytul)
                return
        print("Ten czytelnik nie ma książki o ISBN:", isbn)

    def szukaj_po_tytule(self, szukany_tytul):
        print("Wyniki wyszukiwania dla:", szukany_tytul)
        znaleziono = False
        for ksiazka in self.__ksiazki:
            if szukany_tytul.lower() in ksiazka.tytul.lower():
                ksiazka.info()
                print("---")
                znaleziono = True
        if znaleziono == False:
            print("Brak wyników")

    def szukaj_po_autorze(self, szukany_autor):
        print("Wyniki wyszukiwania dla autora:", szukany_autor)
        znaleziono = False
        for ksiazka in self.__ksiazki:
            if szukany_autor.lower() in ksiazka.autor.lower():
                ksiazka.info()
                print("---")
                znaleziono = True
        if znaleziono == False:
            print("Brak wyników")

    def szukaj_po_isbn(self, isbn):
        for ksiazka in self.__ksiazki:
            if ksiazka.isbn == isbn:
                ksiazka.info()
                return
        print("Brak książki o ISBN:", isbn)