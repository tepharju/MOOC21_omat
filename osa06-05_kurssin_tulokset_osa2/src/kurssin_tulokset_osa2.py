# tee ratkaisu tänne
if True:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
    koepisteet = input("Koepisteet:")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"
    koepisteet = "koepisteet1.csv"

nimet = {}

with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        nimet[osat[0]] = (osat[1] +" "+ osat[2]).strip() 

#print(nimet)



teht = {}
#lista = []

with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
       
        #teht[osat[0]] = [int(osat[1]), int(osat[2]),int(osat[3]), int(osat[4]), int(osat[5]), int(osat[6]),int(osat[7])]
        
        arvosana = 0

        summa = (int(osat[1]) + int(osat[2]) + int(osat[3]) + int(osat[4]) + int(osat[5]) + int(osat[6]) + int(osat[7]))
        
        pojot = summa / 4
        
        #print(summa)
        #teht[osat[0]] = int(osat[1]) + int(osat[2]) + int(osat[3]) + int(osat[4]) + int(osat[5]) + int(osat[6]) + int(osat[7])
        teht[osat[0]] = pojot

koe = {}

with open(koepisteet) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        koesumma = (int(osat[1]) + int(osat[2]) + int(osat[3]))
        
        koe[osat[0]] = koesumma

#lasketaan arvosana





for avain in nimet:
    if avain in teht.keys():
        summa = (teht[avain]+koe[avain])
        if summa > 28:
            arvosana = 5
        if summa >= 24 and summa < 28:
            arvosana = 4
        if summa >= 21 and summa < 24:
            arvosana = 3
        if summa >= 18 and summa <21:
            arvosana = 2
        if summa >= 15 and summa < 18:
            arvosana = 1
        if summa < 15:
            arvosana = 0
        print(nimet[avain], arvosana)
#print(teht)
#print(teht.values())