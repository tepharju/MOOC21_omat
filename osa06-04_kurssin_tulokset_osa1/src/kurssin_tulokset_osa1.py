# tee ratkaisu tänne
if True:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"

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
        

        teht[osat[0]] = int(osat[1]) + int(osat[2]) + int(osat[3]) + int(osat[4]) + int(osat[5]) + int(osat[6]) + int(osat[7])

for avain in nimet:
    if avain in teht.keys():
        print(nimet[avain], teht[avain])
#print(teht)
#print(teht.values())
