# tee ratkaisu tänne
def histogrammi(sana: str):
    kirjaimet = {}
    for kirjain in (sana):
        kirjaimet[kirjain] = sana.count(kirjain)
    
    for i in sorted (kirjaimet) :
        print (i, kirjaimet[i]*"*")

    #return kirjaimet



if __name__ == "__main__":
    print(histogrammi("saappeli"))
    #print(d)
