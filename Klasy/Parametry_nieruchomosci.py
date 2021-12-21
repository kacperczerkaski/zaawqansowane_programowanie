class ParametryNieruchomości:
    def __init__(self, powierzchnia: float, liczba_pokoi: int, dzielnica: str, cena_nieruchomości: float):
        self._powierzchnia = powierzchnia
        self._liczba_pokoi = liczba_pokoi
        self._dzielnica = dzielnica
        self._cena_nieruchomosci = cena_nieruchomości

    @property
    def powierzchnia(self) -> float:
        return self._powierzchnia

    @property
    def liczba_pokoi(self) -> int:
        return self._liczba_pokoi

    @property
    def dzielnica(self) -> str:
        return self._dzielnica

    @property
    def cena_nieruchomości(self) -> float:
        return self.cena_nieruchomości
