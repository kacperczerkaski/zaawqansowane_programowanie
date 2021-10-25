# Lab_2 zadanie 2c
def zad_2c (liczby: list):
    for x in range(len(liczby)):
        if liczby[x] % 2 == 0:
            print(f"Liczby przyste:{liczby[x]}")

if __name__ == '__main__':
    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    zad_2c(liczby)