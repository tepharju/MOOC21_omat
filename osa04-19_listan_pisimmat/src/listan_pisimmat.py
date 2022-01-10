# tee ratkaisu tänne

def pisimmat(lista):

    p = []
    lst2 = sorted(lista, key=len)

    pisin = lst2[-1]

    #p.append(pisin)

    for alkio in lista:
        if (len(alkio)) == len(pisin):
            p.append(alkio)

    return p




if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = pisimmat(lista)
    print(tulos) # ['emilia', 'juhani']