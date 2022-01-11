# Tee ratkaisusi tähän:
class Maksukortti:
    
    def __init__(self, alkusaldo:float):
        self.alkusaldo = alkusaldo

    def __str__(self):
        return f"Kortilla on rahaa {self.alkusaldo:.1f} euroa"
    
    def syo_edullisesti(self):
        if self.alkusaldo > 2.60:
            self.alkusaldo = self.alkusaldo - 2.60
    
    def syo_maukkaasti(self):
        if self.alkusaldo > 4.60:
            self.alkusaldo = self.alkusaldo - 4.60
        
    def lataa_rahaa(self, summa:float):
        if summa < 0:
            raise ValueError("Kortille ei voi ladata negatiivista summaa")
        else:
            self.alkusaldo = self.alkusaldo + summa

        
pekan_kortti = Maksukortti(20)
matin_kortti = Maksukortti(30)
pekan_kortti.syo_maukkaasti()
matin_kortti.syo_edullisesti()
print(f"Pekka: {pekan_kortti}") 
print(f"Matti: {matin_kortti}") 

pekan_kortti.lataa_rahaa(20)
matin_kortti.syo_maukkaasti()

print(f"Pekka: {pekan_kortti}") 
print(f"Matti: {matin_kortti}") 
pekan_kortti.syo_edullisesti()
pekan_kortti.syo_edullisesti()
matin_kortti.lataa_rahaa(50)
print(f"Pekka: {pekan_kortti}") 
print(f"Matti: {matin_kortti}") 
