from Parametry_nieruchomosci import ParametryNieruchomości


class Mieszkanie(ParametryNieruchomości):
    def __init__(self, powierzchnia: float, liczba_pokoi: int, dzielnica: str, cena_nieruchomości: float,
                 pietro: int):
        super().__init__(powierzchnia, liczba_pokoi, dzielnica, cena_nieruchomości)
        self._pietro = pietro

    def __str__(self):
        return f"Powierzchnia mieszkania: {self._powierzchnia}, Liczba pokoi: {self._liczba_pokoi}, " \
               f"Dzielnica: {self._dzielnica}, Cena mieszkania: {self._cena_nieruchomosci} Pietro: {self._pietro}"

    @property
    def pietro(self) -> int:
        return self._pietro
