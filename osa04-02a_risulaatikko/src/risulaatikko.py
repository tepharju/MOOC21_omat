# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(merkki):
    print("##########")


def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    for i in range(korkeus):
        viiva(korkeus)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
