# tee ratkaisu tänne

def pisimman_pituus(lista):

    pisin = 0

    for alkio in lista:
        if (len(alkio)) > pisin:
            pisin = len(alkio)
    return  pisin


if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = pisimman_pituus(lista)
    print(tulos)
