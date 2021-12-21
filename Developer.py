class Developer:
    def __init__(self, imie: str, wiek: int, miejsce_pracy: str, specjalizacja: str):
        self._imie = imie
        self._wiek = wiek
        self._miejsce_pracy = miejsce_pracy
        self._specjalizacja = specjalizacja

    def __str__(self):
        return f"Imię dewelopera: {self._imie}, wiek: {self._wiek}, Rejon zlecień: {self._miejsce_pracy}, " \
               f"specjalność dewelopera: {self._specjalizacja}"

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def wiek(self) -> int:
        return self._wiek

    @property
    def miejsce_pracy(self) -> str:
        return self._miejsce_pracy

    @property
    def specjalizacja(self) -> str:
        return self._specjalizacja

