# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi

class Huone:

    def __init__(self):
        
        self.tyypit = []
        self.maara = 0
    
    #def __str__(self):
    #    return f"{self.nimi} ({self.pituus} cm)"

    
    def lisaa(self, henkilo:Henkilo):
        self.tyypit.append(henkilo)
        self.maara += 1

    def on_tyhja(self):
        if self.maara == 0:
            return True
        else:
            return False
    
    def tulosta_tiedot(self):
        for alkio in self.tyypit:
            print(f"{alkio.nimi} ({alkio.pituus} cm)")


    def lyhin(self):
        if self.maara == 0:
            return None
        else:
            pituudet = sorted(self.tyypit)
            return self.pituudet[0][1]


if __name__ == "__main__":
    huone = Huone()

    print("Huone tyhjä?", huone.on_tyhja())
    print("Lyhin:", huone.lyhin())

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))

    print()

    print("Huone tyhjä?", huone.on_tyhja())
    print("Lyhin:", huone.lyhin())

    print()

    huone.tulosta_tiedot()

