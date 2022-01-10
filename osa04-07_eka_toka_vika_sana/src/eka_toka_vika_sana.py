# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def eka_sana(lause):
    eka = lause.split()
    return eka[0]

def toka_sana(lause):
    toka = lause.split()
    return toka[1]

def vika_sana(lause):
    vika = lause.split()
    return vika[-1]



if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause)) 
    print(vika_sana(lause))