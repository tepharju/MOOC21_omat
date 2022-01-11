# TEE RATKAISUSI TÄHÄN:
class Lahja:
    def __init__(self, nimi, paino:int):
        self.nimi = nimi
        self.paino = paino

    def __repr__(self):
        return f"{self.nimi} ({self.paino} kg)"

class Pakkaus:
    
    def __init__(self):
        
        self.yhtpaino = 0

    #def __init__(self, lahja:Lahja):
    #    self.lahja = lahja
        
    
    def lisaa_lahja(self, lahja:Lahja):
        #self.lahjat.append(lahja)
        self.yhtpaino += lahja.paino

    def yhteispaino(self):
        return self.yhtpaino




if __name__ == "__main__":
    kirja = Lahja("Aapiskukko", 2)

    pakkaus = Pakkaus()
    pakkaus.lisaa_lahja(kirja)
    print(pakkaus.yhteispaino())

    cd_levy = Lahja("Pink Floyd: Dark side of the moon", 1)
    pakkaus.lisaa_lahja(cd_levy)
    print(pakkaus.yhteispaino())

        




