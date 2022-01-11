# tee ratkaisu tänne
def suurin():

    tiedosto = open("luvut.txt", "r")

    suurin = 0

    for x in tiedosto:
        luku = int(x)
        if luku > suurin:
            suurin = luku
    
    return suurin
        
        #if int(x) > suurin:
        #    x = suurin
        #print(suurin)

    
    #return suurin
    # with open("luvut.txt") as tiedosto:
        
        

    #     for rivi in tiedosto:
            
    #         rivi = rivi.replace("\n", "")
            
    #         luku = int(rivi)
            
    #         if luku > suurin:
    #             luku = suurin
    # return suurin

if __name__ == "__main__":
    print(suurin())