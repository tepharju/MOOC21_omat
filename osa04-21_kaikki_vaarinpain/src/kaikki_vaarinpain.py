# tee ratkaisu tänne
def kaikki_vaarinpain(list):
    uusi = []
    
    for alkio in list:
        sana = alkio[::-1]
        uusi.append(sana)
    uusi.reverse()
    return uusi





if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)