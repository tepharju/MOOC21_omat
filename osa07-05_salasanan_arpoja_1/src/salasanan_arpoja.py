# tee ratkaisu tänne
import string
from random import randint

def luo_salasana(pituus:int):

    asciit = list(str(string.ascii_lowercase))  #len = 26
    salasana = ""
    
    while len(salasana) < pituus:
        x = randint(1,25)
        salasana += asciit[x]

    #print(salasana)
    #print(asciit)
    return salasana 


if __name__ == "__main__":
    #luo_salasana(5)
    for i in range(10):
        print(luo_salasana(8))

