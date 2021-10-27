# Zadanie 6 lab_3
def zad_6(lista_1: list, lista_2: list):
    return list(x ** 3 for x in set(lista_1+lista_2))
if __name__ == '__main__':
    lista_1 = [2, 4, 6, 8, 10]
    lista_2 = [2, 3, 5, 9, 11]
    zad_6(lista_1, lista_2)
    print(zad_6(lista_1, lista_2))