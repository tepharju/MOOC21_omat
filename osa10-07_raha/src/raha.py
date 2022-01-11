# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    def __str__(self):
        if self.__sentit < 10:
            return f"{self.__eurot}.0{self.__sentit} eur"

        return f"{self.__eurot}.{self.__sentit} eur"

    def __eq__(self,toinen):
        if self.__eurot == toinen.__eurot and self.__sentit == toinen.__sentit:
            return True
        else:
            return False 

    def __lt__(self,toinen):
        if self.__eurot < toinen.__eurot:
            return True
        elif self.__eurot == toinen.__eurot and self.__sentit < toinen.__sentit:
            return True
        else:
            return False 

    def __gt__(self,toinen):
        if self.__eurot > toinen.__eurot:
            return True
        elif self.__eurot == toinen.__eurot and self.__sentit > toinen.__sentit:
            return True
        else:
            return False

    def __ne__(self,toinen):
        if self.__eurot != toinen.__eurot or self.__sentit != toinen.__sentit:
            return True
        else:
            return False

    def __add__(self,toinen):
        e = 0
        e = (self.__eurot + toinen.__eurot)
        s = (self.__sentit + toinen.__sentit)
        if s >= 100:
            s = s -100
            e += 1
        
        return Raha(e,s)

    def __sub__(self,toinen):
        
        if toinen > self:
            raise ValueError(f"negatiivinen tulos ei sallittu") 
        e = 0
        c = self.__sentit - toinen.__sentit
        if c < 0:
            c += 100
            e = -1
        e = e + self.__eurot - toinen.__eurot
        return Raha(e, c)


if __name__ =="__main__":
    e1 = Raha(4, 10)
    e2 = Raha(2, 5)  # kaksi euroa ja viisi senttiä

    print(e1)
    print(e2)