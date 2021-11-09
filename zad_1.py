class Pojazd:
    def __init__(self, marka: str, rok_produkcji: int, przebieg: int, kierowca: str, podchodzenie: str):
        self.marka = marka
        self.rok_pordukcji = rok_produkcji
        self.przebieg = przebieg
        self.kierowca = kierowca
        self.pochodzenie = podchodzenie
    def __str__(self):
        return f"Marka pojazdu {self.marka}, Rok produkcji {self.rok_pordukcji}, Przebeig {self.przebieg}, Kierowca {self.kierowca}, Pochodzenie {self.pochodzenie}"

class FirmaTransportowa:
    def __init__(self, nazwa_firmy_t: str, lokalizacja: str, cena_uslugi: float, adres_biura: str, telefon: str) -> object:
        self.nazwa_firmy_t = nazwa_firmy_t
        self.lokalizacja = lokalizacja
        self.cena_uslugi = cena_uslugi
        self.adres_biura = adres_biura
        self.telefon = telefon
    def __str__(self):
        return f"Nazwa firmy tran. {self.nazwa_firmy_t}, Lokalizacja: {self.lokalizacja}, Cena usługi {self.cena_uslugi}, " \
               f"adres biura {self.adres_biura}, Telefon {self.telefon}"

class FirmaSpozywcza:
    def __init__(self, nazwa_firmy: str, numer_zlecenia: str, tel_kontatkowy: str, godziny_otwarcia: str, przedstawiciel: str):
        self.nazwa_firmy = nazwa_firmy
        self.numer_zlecenia = numer_zlecenia
        self.tel_kontaktowy = tel_kontatkowy
        self.godziny_otwarcia = godziny_otwarcia
        self.przedstawiciel = przedstawiciel
    def __str__(self):
        return f"Nazwa firmy spoz {self.nazwa_firmy}, Numer zlecenia: {self.numer_zlecenia}, Tel kontaktowy {self.tel_kontaktowy}, " \
               f"Godziny otwarcia {self.godziny_otwarcia}, Przedstawiciel {self.przedstawiciel}"

class Odcinek:
    def __init__(self, miejsce_staru: str, cel: str, odcinek_1: float, odcinek_2: float, kierowca: str) -> object:
        self.miejsce_stratu = miejsce_staru
        self.cel = cel
        self.odcinek_1 = odcinek_1
        self.odcinek_2 = odcinek_2
        self.kierowca = kierowca

    def __str__(self):
        return f"Start podróży {self.miejsce_stratu}, Cel podróży {self.cel}, Długość pierwszego odcinka {self.odcinek_1}, Długość " \
                       f"drugeigo odcinka {self.odcinek_2}, Pojazd prowadził {self.kierowca}"

class Kurs:
    def __init__(self, Odcinek: str, pojazd: str, odcinek_1: float, odcinek_2: float, FirmaTransportowa: str, kierowca: str):
        self.Odcinek = Odcinek
        self.pojazd = pojazd
        self.odcinek_1 = odcinek_1
        self.odcinek_2 = odcinek_2
        self.FirmaTransportowa = FirmaTransportowa
        self.kierowca = kierowca
    def odcinek(self):
        return self.odcinek_1 + self.odcinek_2
    def kierowca(self):
        return self.kierowca()

    def __str__(self):
        return f"Cel podróży {self.cel}, Pojazd: {self.pojazd}, Długość pierwszego odcinka {self.odcinek_1}, Długość " \
                       f"drugeigo odcinka {self.odcinek_2}, Zlecenie wykonane przez {self.FirmaTransportowa}"
if __name__ == '__main__':

    pojazd_1 = Pojazd("Ford", 2020, 250000, "Adam", "Ukraina")
    firma_transportowa = FirmaTransportowa("PolTrans", "Warszawa", "10.000 zł", "Prosta 2", "900800600")
    firma_spozywcza = FirmaSpozywcza("Makro", "123435435", "500600700", "10:00- 19:00", "Kamil")
    odcinek_dl = Odcinek("Warszawa", "Katowice", 500, 243, "Adam")
    kurs = Kurs(odcinek_dl, pojazd_1, 250, 235, firma_transportowa, "Adam")
    print(kurs)







