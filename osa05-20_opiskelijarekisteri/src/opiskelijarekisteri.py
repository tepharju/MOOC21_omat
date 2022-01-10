# tee ratkaisu tänne

def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    #nimet.append(nimi)
    suoritukset = []
    opiskelijat[nimi] = suoritukset


def keskiarvo(opiskelijat: dict, nimi:str):

    ka = 0
    summa = 0

    #return (len(opiskelijat[nimi]))

    if (len(opiskelijat[nimi])) != 0:

        for i in range(len(opiskelijat[nimi])):
            summa = summa + int(opiskelijat[nimi][i][1])
        
        ka = summa / (len(opiskelijat[nimi]))

    return (round(ka,1))


def tulosta(opiskelijat: dict, nimi: str):
    if nimi in opiskelijat:
        ka = keskiarvo(opiskelijat, nimi)
        print(nimi+":")

        if len(opiskelijat[nimi]) == 0:
            print(" ei suorituksia")
        else:
            print(f" suorituksia {len(opiskelijat[nimi])} kurssilta:")

            for k in range(len(opiskelijat[nimi])):
                print(f"  {opiskelijat[nimi][k][0]} {opiskelijat[nimi][k][1]}")
                #print(f"  {opiskelijat[nimi][1][0]} {opiskelijat[nimi][1][1]}")
            print(f" keskiarvo {ka}")
            #print(f" keskiarvo {(opiskelijat[nimi][0][1]) / len(opiskelijat[nimi])}")
        #print(" " + opiskelijat[nimi])
    else:
        print("ei löytynyt ketään nimellä", nimi)



def lisaa_suoritus(opiskelijat: dict, nimi: str, kurssi: tuple):
    kurssit.append(kurssi)

    #tämä toimii
    if kurssi[1] != 0:
        #opiskelijat[nimi].append(kurssi)

        for i in range(len(kurssit)):
            if kurssi > kurssit[i]:
                kurssit.remove(kurssit[i])
                kurssit.append(kurssi)

    opiskelijat[nimi] = kurssit
        #    opiskelijat[nimi].append(kurssi)

    #opiskelijat["Panu"].append(kurssi)
    
    
    
        #if kurssi[0] not in opiskelijat[nimi] and kurssi[1] != 0:
        #    opiskelijat[nimi].append(kurssi)

    #lista = opiskelijat[nimi]

    #if kurssi in lista:
    #    if kurssi[1] > opiskelijat[nimi][0][1]:
    #        print("On suurempi")
    #        opiskelijat[nimi].pop()

    #if kurssin_nimi in opiskelijat.values():
    #    print("löytyy")
    #    print(nimi)
    #print(kurssi)
    #print(opiskelijat.values())
    #if kurssi in opiskelijat.values():
    #    print("löytyy")
    #else:
    #    print(opiskelijat.values())

        #for i in range(len(opiskelijat[nimi])):

        #    if kurssi[0] == opiskelijat[nimi][i]:
        #        if kurssi[1] > opiskelijat[nimi][i][1]:
        #            opiskelijat[nimi][i][1] = kurssi[1]

    #puh.setdefault(nimi,[])
    #    puh[nimi].append(numero)
    #print("testit:")
    #print(kurssi[0])

    #if kurssi[0] == opiskelijat[nimi]:
        #print("Totta")
    #print(opiskelijat[nimi][0])





if __name__ == "__main__":
    
    opiskelijat = {}
    kurssit = []
    #opiskelijat = collections.defaultdict(list)
    lisaa_opiskelija(opiskelijat, "pekka")
    lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 4))
    lisaa_suoritus(opiskelijat, "pekka", ("pylly", 0))
    lisaa_suoritus(opiskelijat, "pekka", ("pylly", 2))
    tulosta(opiskelijat, "pekka")
    
    
    #lisaa_suoritus(opiskelijat, "pekka", ("Tira", 2))
    #print(opiskelijat["pekka"][1][1])
    #print(keskiarvo(opiskelijat, "pekka"))
    
    