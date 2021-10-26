# Zadanie 3 lab_3
def zad_3(x: bool):
    if x % 2 == 0:
        return "Liczba parzysta"
    else:
        return "Liczba nieparzysta"
if __name__ == '__main__':
    x = 6
    zad_3(x)
    print(zad_3(x))