from Mieszkanie import Mieszkanie
from Dom import Dom

class Zamowienie:
    def __init__(self, data_zakupu: str, rodzaj_nieruchomosci: str, mieszkanie: Mieszkanie, dom: Dom):
        self._data_zakupu = data_zakupu
        self._rodzaj_nieruchomosci = rodzaj_nieruchomosci
        self._mieszkanie = mieszkanie
        self._dom = dom

    def __str__(self):
        return f"Data zakupu: {self._data_zakupu}, Rodzaj nieruchomosci: {self._rodzaj_nieruchomosci}, " \
               f"Cena zakupu: {self._mieszkanie}, Suma zakupionych metrow kwadratowych {self._dom}"

    def suma_zakupow(self) -> float:
        x = 0
        for cena in self._mieszkanie:
            x += cena.cena_nieruchomosci
            return round(x, 2)

    def suma_metrow_kw(self) -> float:
        y = 0
        for metry in self._dom:
            y += metry.powierzchnia
            return y

    @property
    def data_zakupu(self) -> str:
        return self._data_zakupu

    @data_zakupu.setter
    def data_zakupu(self, value: str) -> None:
        self._data_zakupu = value

    @property
    def rodzaj_nieruchomosci(self) -> str:
        return self._rodzaj_nieruchomosci

    @rodzaj_nieruchomosci.setter
    def rodzaj_nieruchomosci(self, value: str) -> None:
        self._rodzaj_nieruchomosci = value

    @property
    def mieszkanie(self) -> Mieszkanie:
        return self._mieszkanie

    @mieszkanie.setter
    def mieszkanie(self, value: Mieszkanie) -> None:
        self._mieszkanie = value

    @property
    def dom(self) -> Dom:
        return self._dom

    @dom.setter
    def dom(self, value: Dom) -> None:
        self._dom = value



