# tee ratkaisu tänne
def poista_isot(list):
    uusi = []
    for sana in list:
        
        if not sana.isupper():
            uusi.append(sana)
    return uusi






if __name__ == "__main__":
    lista = ['EKA', 'TOKA', 'kolmas', 'neljäs', 'viides']
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)