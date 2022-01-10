# Kirjoita ratkaisu tähän

lista = []
luku = 1

while True:

    
    print(f"Lista on nyt {lista}")
    toim = input("(l)isää, (p)oista, vai e(x)it:")

    if toim == "x":
        print("Moi!")
        break

    if toim == "l":
        if len(lista) == 0:
            lista.append(luku)
        else:
            seuraava = lista[-1] + 1
            lista.append(seuraava)

    if toim == "p":
        del lista [-1]

        if len(lista) == 0:
            luku=1
    
