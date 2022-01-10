# Kirjoita ratkaisu tähän
lista = []

while True:
    sana = input("sana:")

    if sana not in lista:
        lista.append(sana)
    else:
        print(f"Annoit {len(lista)} eri sanaa")
        break

