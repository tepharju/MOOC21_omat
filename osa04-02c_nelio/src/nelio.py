# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(n,merkki):
    for i in range(n):
        print(n*merkki)
    

def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    viiva(koko, merkki)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "x")
    nelio(5, "o")
