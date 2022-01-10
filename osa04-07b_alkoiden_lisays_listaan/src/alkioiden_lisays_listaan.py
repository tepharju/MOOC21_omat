# Kirjoita ratkaisu tähän
n = int(input("Kuinka monta lukua:"))

lista = []

for i in range (1,n+1):
    luku = int(input(f"Anna luku {i}:"))
    lista.append(luku)
print(lista)