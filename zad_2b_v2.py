# Lab_2 zadanie 2b_v2
def zad_2b2 (liczby: list):
    mnozenie = [x*2 for x in liczby]
    return mnozenie
if __name__ == '__main__':
    liczby = [1, 8, 3, 4, 6]
    print(zad_2b2(liczby))