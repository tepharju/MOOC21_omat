# tee ratkaisu tänne
from random import randint

def heita(noppa:str):

    #nopat

    a = [3,3,3,3,3,6]
    b = [2,2,2,5,5,5]
    c = [1,4,4,4,4,4]

    if noppa == "A":
        return a[randint(0,5)]
    if noppa == "B":
        return b[randint(0,5)]
    if noppa == "C":
        return c[randint(0,5)]


def pelaa(noppa1:str, noppa2:str, kertaa:int):

    #nopat

    a = [3,3,3,3,3,6]
    b = [2,2,2,5,5,5]
    c = [1,4,4,4,4,4]

   

    voitot1 = 0
    voitot2 = 0
    tasurit = 0

    for i in range(kertaa):
        ekasumma = 0
        tokasumma= 0

        if noppa1 == "A":
            ekasumma += a[randint(0,5)]
        if noppa1 == "B":
            ekasumma += b[randint(0,5)]
        if noppa1 == "C":
            ekasumma += c[randint(0,5)]
        
        if noppa2 == "A":
            tokasumma += a[randint(0,5)]
        if noppa2 == "B":
            tokasumma += b[randint(0,5)]
        if noppa2 == "C":
            tokasumma += c[randint(0,5)]
        
        if ekasumma > tokasumma:
            voitot1 += 1
        if tokasumma > ekasumma:
            voitot2 += 1
        if ekasumma == tokasumma:
            tasurit += 1

    return(voitot1, voitot2, tasurit)



if __name__ == "__main__":
    #for i in range(20):
    #    print(heita("A"), " ", end="")
    tulos = pelaa("A", "B", 100)
    print(tulos)
    tulos = pelaa("A", "B", 100)
    print(tulos)