# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(n,merkki):
    for i in range(1,n+1):
        print(i*merkki)



def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    viiva(koko, "#")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
