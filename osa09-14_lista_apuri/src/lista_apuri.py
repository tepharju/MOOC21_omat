# TEE RATKAISUSI TÄHÄN:
class ListaApuri:

    @classmethod
    def suurin_frekvenssi(cls,lista:list):
        if len(lista) == 0:
            print("Lista oli tyhjä")
        else:
            tulos = {}
            for alkio in lista:
                tulos[lista.count(alkio)] = alkio
            return tulos[max(tulos)]

    @classmethod
    def tuplia(cls, lista:list):
        tuplat = 0

        for alkio in set(lista):
            n = lista.count(alkio)
            if n >= 2:
                tuplat +=1
        return tuplat
