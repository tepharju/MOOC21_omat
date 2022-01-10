# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(n,merkki):
    for i in range(n):
        print(n*merkki)



def risunelio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    viiva(koko, "#")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
