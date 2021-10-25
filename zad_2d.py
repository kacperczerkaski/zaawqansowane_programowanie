# Lab_2 zadanie 2d
def zad_2d (liczby: list):
    for x in range(len(liczby)):
        if x%2 == 0:
            co_druga_liczba.append(liczby[x])
            print(co_druga_liczba)

if __name__ == '__main__':
    co_druga_liczba = []
    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    zad_2d(liczby)