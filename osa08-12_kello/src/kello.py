# Tee ratkaisusi tähän:
class Kello:

    def __init__(self, tunnit:int, minuutit:int,sekunnit:int ):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = sekunnit
    
    def tick(self):
        self.sekunnit +=1
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit +=1
        if self.minuutit == 60:
            self.minuutit = 0
            self.tunnit +=1
        if self.tunnit == 24:
            self.tunnit == 0

    def aseta(self, tunti:int, min:int):
        self.tunnit = tunti
        self.minuutit = min

    def lisaa_nolla(self, aika):
        if aika < 10:
            return "0"+str(aika)
        else:
            return str(aika)

    def __repr__(self):
        return(f"{self.lisaa_nolla(self.tunnit)}:{self.lisaa_nolla(self.minuutit)}:{self.lisaa_nolla(self.sekunnit)}")
