# tee ratkaisu tänne
from itertools import chain
#from string import string

syote = input("Write text:")
lause = [syote.lower()]
#lause.lower()
sanat = lause[0].split()
#print(sanat)
res = []


with open("wordlist.txt") as tiedosto:
    kaikki = tiedosto.read()
    for sana in sanat:
        if sana not in kaikki:
            res = list(map(lambda st: str.replace(st, sana,("*"+sana+"*")),sanat))
            #sana.replace(sana,("*"+sana+"*") )
            #korvaa = "*"+sana+"*"
            #sanat = [("*"+sana+"*") for i in sanat]
    #print(" ".join(map(str, sanat)))
    if len(res) == 0:
        #sanat[0].upper()
        tulos = (" ".join(map(str, sanat)))
        if syote[0].isupper():
            print(tulos.capitalize())
        #print(tulos.capitalize())
        else:
            print(tulos)
    else: 
        tulos = (" ".join(map(str, res)))
        if syote[0].isupper():
            print(tulos.capitalize()) 
        else:
            print(tulos)
 