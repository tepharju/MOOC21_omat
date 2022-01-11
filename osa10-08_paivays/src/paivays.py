# TEE RATKAISUSI TÄHÄN:
class Paivays:

    def __init__(self, d,m,y):
        self.__d = d
        self.__m = m
        self.__y = y

    def __str__(self) -> str:
        return f"{self.__d}.{self.__m}.{self.__y}"

    def __eq__(self,toinen):
        if self.__d == toinen.__d and self.__m == toinen.__m and self.__y == toinen.__y:
            return True
        else:
            return False 

    def __ne__(self,toinen):
        if self.__d != toinen.__d or self.__m != toinen.__m or self.__y != toinen.__y:
            return True
        else:
            return False

    def __gt__(self,toinen):
        if self == toinen:
            return False
        if self.__y > toinen.__y:
            return True
        elif self.__y == toinen.__y and self.__m > toinen.__m:
            return True
        elif self.__y == toinen.__y and self.__m == toinen.__m and self.__d > toinen.__d:
            return True
        else:
            return False

    def __lt__(self,toinen):
        if self == toinen:
            return False
        return not self > toinen
    
    def __add__(self,lisaa):
        uusi_d = self.__d + lisaa
        uusi_m = self.__m
        uusi_y = self.__y

        if uusi_d > 30:
            uusi_m = int (uusi_d /30)
            uusi_m = uusi_m + self.__m
            uusi_d = uusi_d % 30
        
        if uusi_m > 12:
            uusi_y = int(uusi_m / 12) + self.__y
            uusi_m = uusi_m % 12

        return Paivays(uusi_d,uusi_m,uusi_y) 

    def __sub__(self, toinen):
        if self > toinen:
            pvm1 = self
            pvm2 = toinen
        else:
            pvm1 = toinen
            pvm2 = self
        pv_erotus = pvm1.__d - pvm2.__d
        kk_erotus = (pvm1.__m - pvm2.__m)*30
        v_erotus = (pvm1.__y - pvm2.__y)*30*12
        
        return pv_erotus + kk_erotus + v_erotus 



if __name__ =="__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(28, 12, 1985)
    p3 = Paivays(28, 12, 1985)

    print(p1)
    print(p2)
    #print(p1 == p2)
    #print(p1 != p2)
    #print(p1 == p3)
    #print(p1 < p2)
    #print(p1 > p2)