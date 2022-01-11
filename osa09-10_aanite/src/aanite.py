# TEE RATKAISUSI TÄHÄN:
class Aanite:

    def __init__(self, pituus:int):
        if pituus < 0:
            raise ValueError("Pituus ei saa olla negatiivinen!")
        else:
            self.__pituus = pituus
    
    @property
    def pituus(self):
        return self.__pituus

    @pituus.setter
    def pituus(self, pituus:int):
        if pituus < 0:
            raise ValueError("Pituus ei saa olla negatiivinen!")
        else:
            self.__pituus = pituus


if __name__ == "__main__":
    the_wall = Aanite(1)
    print(the_wall.pituus)
    the_wall.pituus = 1
    print(the_wall.pituus)