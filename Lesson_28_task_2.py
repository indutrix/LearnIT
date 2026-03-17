class Produkt:
    def __init__(self, nazwa, cena, kod_produktu):
        self.nazwa = nazwa
        self.cena = cena
        self.kod_produktu = kod_produktu

    def info(self):
        print("Nazwa:", self.nazwa)
        print("Cena:", self.cena, "zł")
        print("Kod:", self.kod_produktu)

    def oblicz_cene(self):
        return self.cena


class Elektronika(Produkt):
    def __init__(self, nazwa, cena, kod_produktu, marka, gwarancja_lat):
        Produkt.__init__(self, nazwa, cena, kod_produktu)
        self.marka = marka
        self.gwarancja_lat = gwarancja_lat

    def info(self):
        Produkt.info(self)
        print("Marka:", self.marka)
        print("Gwarancja:", self.gwarancja_lat, "lat")

    def oblicz_cene(self):
        podatek = self.cena * 0.23
        return self.cena + podatek


class Ubrania(Produkt):
    def __init__(self, nazwa, cena, kod_produktu, rozmiar, material):
        Produkt.__init__(self, nazwa, cena, kod_produktu)
        self.rozmiar = rozmiar
        self.material = material

    def info(self):
        Produkt.info(self)
        print("Rozmiar:", self.rozmiar)
        print("Materiał:", self.material)

    def oblicz_cene(self):
        rabat = self.cena * 0.10
        return self.cena - rabat


class Ksiazka(Produkt):
    def __init__(self, nazwa, cena, kod_produktu, autor, gatunek):
        Produkt.__init__(self, nazwa, cena, kod_produktu)
        self.autor = autor
        self.gatunek = gatunek

    def info(self):
        Produkt.info(self)
        print("Autor:", self.autor)
        print("Gatunek:", self.gatunek)

    def oblicz_cene(self):
        return self.cena


class KoszykZakupowy:
    def __init__(self):
        self.__produkty = []

    def dodaj_produkt(self, produkt):
        self.__produkty.append(produkt)
        print("Dodano do koszyka:", produkt.nazwa)

    def usun_produkt(self, kod_produktu):
        for produkt in self.__produkty:
            if produkt.kod_produktu == kod_produktu:
                self.__produkty.remove(produkt)
                print("Usunięto z koszyka:", produkt.nazwa)
                return
        print("Nie znaleziono produktu i kodzie:", kod_produktu)

    def oblicz_sume(self):
        suma = 0
        for produkt in self.__produkty:
            suma = suma + produkt.oblicz_cene()
        return suma

    def pokaz_zawartosc(self):
        if len(self.__produkty) == 0:
            print("Koszyk jest pusty")
        else:
            print("Zawartość koszyka:")
            for produkt in self.__produkty:
                print("-", produkt.nazwa, "Cena końcowa:", produkt.oblicz_cene(), "zł")
            print("SUMA:", self.oblicz_sume(), "zł")


class Zamowienie:
    def __init__(self, koszyk, dane_klienta):
        self.koszyk = koszyk
        self.dane_klienta = dane_klienta
        self.__status = "Nowe"

    def zmien_status(self, nowy_status):
        self.__status = nowy_status
        print("Status zmieniony na:", self.__status)

    def pokaz_status(self):
        print("Status zamówienia:", self.__status)

    def info(self):
        print("Zamówienie dla:", self.dane_klienta)
        self.koszyk.pokaz_zawartosc()
        self.pokaz_status()


class Uzytkownik:
    def __init__(self, imie, nazwisko, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.__email = email

    def pokaz_email(self):
        return self.__email

    def info(self):
        print("Użytkownik:", self.imie, self.nazwisko)
        print("Email:", self.__email)


class Klient(Uzytkownik):
    def __init__(self, imie, nazwisko, email, metoda_platnosci):
        Uzytkownik.__init__(self, imie, nazwisko, email)
        self.metoda_platnosci = metoda_platnosci
        self.historia_zamowien = []

    def dodaj_zamowienie(self, zamowienie):
        self.historia_zamowien.append(zamowienie)
        print("Dodano zamówienie do klienta:", self.imie)

    def pokaz_historie(self):
        if len(self.historia_zamowien) == 0:
            print(self.imie, "nie ma żadnych zamówień")
        else:
            print("Historia zamówień dla:", self.imie, self.nazwisko)
            for i in range(len(self.historia_zamowien)):
                print("Zamówienie", i + 1, ":")
                self.historia_zamowien[i].info()
                print("---")

    def info(self):
        Uzytkownik.info(self)
        print("Metoda płatności:", self.metoda_platnosci)