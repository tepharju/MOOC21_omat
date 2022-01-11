# TEE RATKAISUSI TÄHÄN:
class Auto:

    def __init__(self):
        self.__bensa = 0
        self.__matka = 0
    
    def tankkaa(self):
        self.__bensa = 60
    
    def aja(self, km:int):
        if km > self.__bensa:
            pass
        else:
            self.__bensa -= km
            self.__matka += km
        
    def __str__(self):
        return f"Auto: ajettu {self.__matka} km, bensaa {self.__bensa} litraa"
    

if __name__ == "__main__":
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)

        