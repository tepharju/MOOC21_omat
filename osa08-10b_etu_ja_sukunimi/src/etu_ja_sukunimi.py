# Tee ratkaisusi tähän:
class Henkilo:
    def __init__(self, nimi:str):
        self.nimi = nimi
        
    
    def anna_etunimi(self):
        etu = self.nimi.split(" ")
        return etu[0]


    def anna_sukunimi(self):
        suku = self.nimi.split(" ")
        return suku[1]
    
if __name__ == "__main__":
    pekka = Henkilo("Pekka Python")
    print(pekka.anna_etunimi())
    print(pekka.anna_sukunimi())

    pauli = Henkilo("Pauli Pythonen")
    print(pauli.anna_etunimi())
    print(pauli.anna_sukunimi())












