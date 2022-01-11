# Tee ratkaisusi tähän:
class Sarja:

    def __init__(self,nimi:str,kaudet:int,lista:list):
        self.nimi = nimi
        self.kaudet = kaudet
        self.lista = lista
        self.arvosanatLista = []

    def genret(self):
        genret = ""
        for i in range (len(self.lista)):
            genret = genret + self.lista[i] + ", "
        return genret[:-2]
    
    def arvostele(self, arvosana:int):
        
        self.arvosanatLista.append(arvosana)

    def ka(self):
        return sum(self.arvosanatLista)/len(self.arvosanatLista)
    
    def arvosanat(self):
        if len(self.arvosanatLista) == 0:
            return f"ei arvosteluja"
        else:
            return f"arvosteluja {len(self.arvosanatLista)}, keskiarvo {self.ka():.1f} pistettä"

    
    
    def __str__(self):
        return f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: {self.genret()}\n{self.arvosanat()} " 

def arvosana_vahintaan(arvosana:float, sarjat:list):
        tulos = []

        for alkio in sarjat:
            if alkio.ka() >= arvosana:
                tulos.append(alkio)
        return tulos

def sisaltaa_genren(genre:str, sarjat:list):
        elokuvat = []

        for alkio in sarjat:
            if genre in alkio.genret():
                elokuvat.append(alkio)
        return elokuvat

if __name__ == "__main__":
    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    sarjat = [s1, s2, s3]

    print("arvosana vähintään 4.5:")
    for sarja in arvosana_vahintaan(4.5, sarjat):
        print(sarja.nimi)

    print("genre Comedy:")
    for sarja in sisaltaa_genren("Comedy", sarjat):
        print(sarja.nimi)