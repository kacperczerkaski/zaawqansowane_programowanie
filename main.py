from Klasy.Developer import Developer
from Klasy.Mieszkanie import Mieszkanie
from Klasy.Dom import Dom
from Klasy.Zamowienie import Zamowienie

if __name__ == '__main__':
    deweloper = Developer("Adam", 45, "Warszawa", "Domy jednorodzinne")

    mieszkanie_1 = Mieszkanie(45.5, 3, "Przedmiescia", 250000, 3)
    mieszkanie_2 = Mieszkanie(75, 3, "Centrum", 450000, 4)

    dom_1 = Dom(90.4, 5, "Wieś", 500000, 5)
    dom_2 = Dom(325, 7, "Przedmieścia", 1230000, 1)

    cena_zakupu = [mieszkanie_1, mieszkanie_2]
    suma_metrow_kw = [mieszkanie_1, mieszkanie_2]
    zamowienie_1 = Zamowienie("2020-12-01", "Inwestycja", mieszkanie_1, dom_1)

    print(zamowienie_1)
