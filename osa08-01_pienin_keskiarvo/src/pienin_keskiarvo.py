# tee ratkaisu tänne
def laske_keskiarvo(henkilo:dict):

    return (henkilo["tulos1"] + henkilo["tulos2"] + henkilo["tulos3"]) / 3

def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):

    ka1 = laske_keskiarvo(henkilo1)
    ka2 = laske_keskiarvo(henkilo2)
    ka3 = laske_keskiarvo(henkilo3)

    if ka1 < ka2 and ka1 < ka3:
        return henkilo1
    
    if ka2 < ka1 and ka2 < ka3:
        return henkilo2
    
    if ka3 < ka1 and ka3 < ka2:
        return henkilo3

    

if __name__ == "__main__":
    
    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}
    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))


