# Zadanie 5 lab_3
def zad_5(lista: list, x: int) -> bool:
    return x in lista
if __name__ == '__main__':
    lista = [2, 4, 6, 8, 10]
    x = 7
    zad_5(lista, x)
    print(zad_5(lista, x))