lista = [1,2,3,4,5]

while True:
    i = int(input("Anna indeksi:"))

    if i == -1:
        break

    arvo = int(input("Anna arvo:"))

    lista[i] = arvo
    print(lista)

