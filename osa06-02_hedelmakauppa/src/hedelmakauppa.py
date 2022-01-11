# tee ratkaisu tänne
def lue_hedelmat():
    with open("hedelmat.csv") as tiedosto:
        hedelmat = {}
        
        for rivi in tiedosto:
            rivi = rivi.replace("\n" ,"")
            osat = rivi.split(";")
            nimi = osat[0]
            hinta = osat[1]
            hedelmat[nimi] = float(hinta)


    return hedelmat




if __name__ == "__main__":
    print(lue_hedelmat())

