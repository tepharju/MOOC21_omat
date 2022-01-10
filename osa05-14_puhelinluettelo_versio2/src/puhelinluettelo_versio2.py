# tee ratkaisu tänne
kom = 0
puh = {}

while kom != 3:

    kom = int(input("komento (1 hae, 2 lisää, 3 lopeta)"))
    

    if kom == 2:
        nimi = input("nimi:")
        numero = input("numero:")
        print("ok!")

        puh.setdefault(nimi,[])
        puh[nimi].append(numero)
        #puh[nimi] = [numero]

    #print(puh)
    
    if kom == 1:
        nimi = input("nimi:")
        
        if nimi in puh:
            lista = puh[nimi]
            for alkio in lista:

                print(alkio)
            #for avain in puh.keys():
            #    print(puh[avain])
            #print(puh[nimi])
        else:
            print("ei numeroa")





print("lopetetaan...")