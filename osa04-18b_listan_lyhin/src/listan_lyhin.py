# tee ratkaisu tänne
# tee ratkaisu tänne

def lyhin(lista):

    lyhin = min(lista, key=len)

    
    return lyhin


if __name__ == "__main__":
    lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti"]

    tulos = lyhin(lista)
    print(tulos)