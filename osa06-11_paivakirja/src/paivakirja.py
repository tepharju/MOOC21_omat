# tee ratkaisu tänne
with open("paivakirja.txt" ,"a") as tiedosto:

    while True:
        print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
        
        valinta = int(input("Valinta:"))

        if valinta == 1:
            merkinta = input("Anna merkintä:")
            tiedosto.write(merkinta)
            tiedosto.write("\n")
            print("Päiväkirja tallennettu")

        

        if valinta == 2:
            with open("paivakirja.txt") as tiedosto:
                print("Merkinnät:")
                sisalto = tiedosto.read()
                print(sisalto)


        
        if valinta == 0:
            print("Heippa!")
            break