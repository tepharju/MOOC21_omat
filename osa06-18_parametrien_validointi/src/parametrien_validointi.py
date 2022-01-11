# tee ratkaisu tänne
def uusi_henkilo(nimi:str, ika:int):
    if nimi == "":
        raise ValueError
    if " " not in nimi:
        raise ValueError
    
    if len(nimi) > 40:
        raise ValueError
    if ika < 0 or ika > 150:
        raise ValueError
    
    return (nimi,ika)

if __name__ == "__main__":
    print(uusi_henkilo("Teppo", 300))