# Kirjoita ratkaisu tähän
lista = []
sorted = []

while True:
    luku = int(input("Anna luku:"))

    if luku != 0:
        lista.append(luku)
        sorted.append(luku)
        print(f"Lista: {lista}")
        sorted.sort()
        print(f"Järjestettynä: {sorted}")
    else:
        print("Moi!")
        break