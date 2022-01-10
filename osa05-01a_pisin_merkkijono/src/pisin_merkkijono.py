# tee ratkaisu tänne
def pisin(merkkijonot: list):
    pis = merkkijonot[0]
    
    for sana in merkkijonot:
        if len(sana) > (len(pis)):
            pis = sana
    return pis



if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))