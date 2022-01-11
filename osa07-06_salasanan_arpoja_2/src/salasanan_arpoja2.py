# tee ratkaisu tänne
from random import choice
from random import randint

from string import ascii_lowercase
from string import digits
 
def luo_hyva_salasana(pituus: int, numerot: bool, erikoismerkit:bool):
    
    salasana = ""
    erikois = "!?=+()#"
    salasana += choice(ascii_lowercase)

    while len(salasana) < pituus:
        
        noppa = randint(1,3)

        if noppa == 1:
            salasana += choice(ascii_lowercase)
        
        if noppa == 2 and erikoismerkit == True:
            salasana += choice(erikois)
        
        if noppa == 3 and numerot == True:
            salasana += choice(digits) 

    for merkki in salasana:
        if not merkki.isdigit() and numerot == True:
            salasana[0] == 1
            
    #for merkki in salasana:
    if "!?=+()#" not in salasana and erikoismerkit == True:
        salasana[0] == 1
        salasana[2] == "!"
    
    #for i in range(pituus):
    #    ssana += choice(ascii_lowercase)
 
    return salasana

if __name__ == "__main__":
    #luo_salasana(5)
    for i in range(10):
        print(luo_hyva_salasana(12,True, True))