# TEE RATKAISUSI TÄHÄN:
class Pankkitili:

    def __init__(self,nimi:str, numero:str, saldo:float):
        self.__nimi = nimi
        self.__numero = numero
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo

    
    def talleta(self,summa:float):
        self.__saldo += summa
        self.__palvelumaksu()
        
    def nosta(self,summa:float):
        if self.__saldo > 0 and summa <= self.__saldo:
            self.__saldo -= summa
            self.__palvelumaksu()

    def __palvelumaksu(self):
        self.__saldo = self.__saldo - (self.__saldo * 0.01)

    def __str__(self):
        return f"{self.__saldo}"

if __name__ == "__main__ ":
    tili = Pankkitili("Raimo Rahakas", "12345-6789", 1000)
    tili.nosta(100)
    print(tili.saldo)
    tili.talleta(100)
    print(tili.saldo)
