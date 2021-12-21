from Parametry_nieruchomosci import ParametryNieruchomości


class Dom(ParametryNieruchomości):
    def __init__(self, powierzchnia: float, liczba_pokoi: int, dzielnica: str, cena_nieruchomości: float,
                 rozmiar_ogrodu: int):
        super().__init__(powierzchnia, liczba_pokoi, dzielnica, cena_nieruchomości)
        self._rozmiar_ogrodu = rozmiar_ogrodu

    def __str__(self):
        return f"Powierzchnia mieszkania: {self._powierzchnia}, Liczba pokoi: {self._liczba_pokoi}, " \
               f"Dzielnica: {self._dzielnica},Cena domu: {self._cena_nieruchomosci}, " \
               f"Rozmiar ogrodu (w ha): {self._rozmiar_ogrodu}"

    @property
    def rozmiar_ogrodu(self) -> int:
        return self._rozmiar_ogrodu

