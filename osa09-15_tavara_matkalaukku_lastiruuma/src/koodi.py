# Tee ratkaisusi tähän:
class Tavara:
    
    def __init__(self, nimi:str, paino:int):
        self.__n = nimi
        self.__p = paino
    
    def nimi(self):
        return self.__n

    def paino(self):
        return self.__p
        
        
    def __str__(self):
        return f"{self.__n} ({self.__p} kg)"

class Matkalaukku:

    def __init__(self, maksimipaino):
        self.maksimipaino = maksimipaino
        self.laukku = []
        self.laukunpaino = 0
        

    def lisaa_tavara(self,tavara:Tavara):
        if self.laukunpaino + tavara.paino() <= self.maksimipaino:
            self.laukku.append(tavara)
            self.laukunpaino += tavara.paino()
            
    def tulosta_tavarat(self):
        for alkio in self.laukku:
            print (alkio)

    def paino(self):
        kokonaispaino = 0

        for alkio in self.laukku:
            kokonaispaino += alkio.paino()
        return kokonaispaino
    
    def raskain_tavara(self):
        if self.laukku == []:
            return None
        s = sorted(self.laukku, key=lambda t: t.paino())
        return s[-1]


    def __str__(self) -> str:
        if len(self.laukku) == 1:
            return f"{len(self.laukku)} tavara ({self.laukunpaino} kg)"

        return f"{len(self.laukku)} tavaraa ({self.laukunpaino} kg)"

class Lastiruuma:

    def __init__(self, maksimipaino:int):
        self.maksimipaino = maksimipaino
        self.ruuma = []
        self.ruumanpaino = 0

    def paino(self):
        yhteispaino = 0

        for alkio in self.ruuma:
            yhteispaino += alkio.paino()
        return yhteispaino

    def lisaa_matkalaukku(self,laukku:Matkalaukku):
        if self.paino() + laukku.paino() <= self.maksimipaino:
            self.ruuma.append(laukku)
    
    def tulosta_tavarat(self):
        for alkio in self.ruuma:
            for i in alkio.laukku:
                print(i)

    def __str__(self) -> str:
        
        tilaa = self.maksimipaino - self.paino()
        if len(self.ruuma) == 1:
            return f"{len(self.ruuma)} matkalaukku, tilaa {tilaa} kg"

        return f"{len(self.ruuma)} matkalaukkua, tilaa {tilaa} kg"


if __name__ == "__main__":
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)

    lastiruuma = Lastiruuma(1000)
    lastiruuma.lisaa_matkalaukku(adan_laukku)
    lastiruuma.lisaa_matkalaukku(pekan_laukku)

    print("Ruuman matkalaukuissa on seuraavat tavarat:")
    lastiruuma.tulosta_tavarat()
