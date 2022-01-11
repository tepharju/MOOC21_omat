
# Tee ratkaisusi tähän:
class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
            self.__henkilot[nimi].lisaa_numero(numero)
        else:
            self.__henkilot[nimi].lisaa_numero(numero)

    def lisaa_osoite(self,nimi,osoite):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
            self.__henkilot[nimi].lisaa_osoite(osoite)
        else:
            self.__henkilot[nimi].lisaa_osoite(osoite)


    def hae_tiedot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]

    def hae_numero(self, numero:str):
        for alkio in self.__henkilot.items():
            if numero in alkio[1]:
                return alkio[0]
        return None

    def tiedot(self, nimi):
        if nimi not in self.__henkilot:
            return None
        return self.__henkilot[nimi]
    
    def hae_nimi(self,nimi:str):
        pass


class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 numeron lisäys")
        print("2 haku nimellä")
        print("3 haku numerolla")

    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def lisaa_osoite(self):
        nimi = input("nimi: ")
        osoite = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)

    def haku(self):
        nimi = input("nimi: ")
        
        tiedot = self.__luettelo.hae_tiedot(nimi)
        if tiedot == None:
            print("numero ei tiedossa")
            print("osoite ei tiedossa") 
            return 
        
        numerot = tiedot.numerot()
        
        if len(numerot) == 0:
            print("numero ei tiedossa")
        else:

            for numero in numerot:
                print(numero)

        osoitteet = tiedot.osoite()

        if osoitteet == None:
            print("osoite ei tiedossa")
        else:
            #for osoite in osoitteet:
            print(osoitteet)       

    # nimen haku numeron perusteella

    def hae_numerolla(self):
        numero = input("numero: ")
        nimi = self.__luettelo.hae_numero(numero)
        if nimi == None:
            print("numero ei tiedossa")
            return
        
        print(nimi)




    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.lisaa_osoite()

            else:
                self.ohje()

class Henkilo:

    def __init__(self, nimi):

        self.__nimi = nimi
        self.__numerot = []
        self.__osoite = None
    
    def nimi(self):
        return self.__nimi

    def numerot(self):
        return self.__numerot
    
    def osoite(self):
        return self.__osoite

    def lisaa_numero(self,numero):
        self.__numerot.append(numero)

    
    def lisaa_osoite(self,osoite:str):
        self.__osoite = osoite

    


        

# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit

sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
#luettelo = Puhelinluettelo()
#luettelo.lisaa_numero("Erkki", "02-123456")
#print(luettelo.tiedot("Erkki"))
#print(luettelo.tiedot("Emilia"))
