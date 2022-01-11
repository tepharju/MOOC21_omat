# TEE RATKAISUSI TÄHÄN:
class Taikajuoma:
    def __init__(self, nimi: str):
        self._nimi = nimi
        self._ainekset = []

    def lisaa_aines(self, ainesosa: str, maara: float):
        self._ainekset.append((ainesosa, maara))

    def tulosta_resepti(self):
        print(self._nimi + ":")
        for aines in self._ainekset:
            print(f"{aines[0]} {aines[1]} grammaa")


class SalainenTaikajuoma(Taikajuoma):

    def __init__(self,nimi, salasana):
        super().__init__(nimi) 
        self.salasana = salasana
    
    def lisaa_aines(self, ainesosa: str, maara: float, salasana:str):
        if self.salasana == salasana:
            super().lisaa_aines(ainesosa, maara)
        else:
            raise ValueError("# VÄÄRÄ SALASANA")

    def tulosta_resepti(self, salasana):
        if self.salasana == salasana:
            super().tulosta_resepti()
        else:
            raise ValueError("# VÄÄRÄ SALASANA")
        

