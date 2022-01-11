# tee ratkaisu tänne
def summa():
    with open("matriisi.txt") as tiedosto:
        summa = 0

        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            osat = rivi.split(",")
            
            for i in range(len(osat)):
                summa = summa + int(osat[i])




    return summa

def maksimi():

    with open("matriisi.txt") as tiedosto:
        suurin = 0

        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            osat = rivi.split(",")
            osaset = list(map(int,osat))
            if max(osaset) > suurin:
                suurin = max(osaset)
            
            #print(osat)
            #print(osaset)
        #print(suurin)    
        
    
    return suurin

def rivisummat():

    rivisummat = []

    with open("matriisi.txt") as tiedosto:
        #lukija = csv.lukija(tiedosto)

        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            osat = rivi.split(",")
            osaset = map(int, osat)
            
            rivisummat.append(sum(osaset))
            #arvot = rivi.split(",")




    return rivisummat


if __name__ == "__main__":
    
    #print(summa())
    print(maksimi())
    #print(rivisummat())