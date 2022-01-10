# tee ratkaisu tänne
def parilliset(lista):
    uusi = []
    for alkio in lista:
        if alkio % 2 == 0:
            uusi.append(alkio)
    
    return uusi


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)