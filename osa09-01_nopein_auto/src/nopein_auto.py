# Tee ratkaisusi luokan Auto perään
# Älä muuta luokkaa!
class Auto:
    def __init__(self, merkki: str, huippunopeus: int):
        self.merkki = merkki
        self.huippunopeus = huippunopeus

    def __str__(self):
        return f"Auto (merkki: {self.merkki}, huippunopeus: {self.huippunopeus})"
    
    
def nopein_auto(autot:list):
    nopein = 0
    nopein_merkki = ""
    for alkio in autot:
        if alkio.huippunopeus > nopein:
            nopein = alkio.huippunopeus
            nopein_merkki = alkio.merkki
    return nopein_merkki


# TEE RATKAISUSI TÄHÄN:

if __name__ == "__main__":
    auto1 = Auto("Mersu", 195)
    auto2 = Auto("Lada", 110)
    auto3 = Auto("Ferrari", 280)
    auto4 = Auto("Trabant", 85)

    autot = [auto1, auto2, auto3, auto4]
    print(nopein_auto(autot))









