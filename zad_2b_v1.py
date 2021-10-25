# Lab_2 zadanie 2b_v1
def zad_2b1 (liczby: list):
    mnozenie = []
    for x in liczby:
        mnozenie.append(x*2)
    return mnozenie
if __name__ == '__main__':
    liczby = [1, 2, 3, 4, 5]
    print(zad_2b1(liczby))