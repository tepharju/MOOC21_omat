# tee ratkaisu tänne
def tee_tuple(x: int, y:int, z:int):
    lista = []
    lista.append(x)
    lista.append(y)
    lista.append(z)
    suurin = max(lista)
    pienin = min(lista)
    summa = x+y+z

    tup = (pienin, suurin, summa)

    return tup

if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))