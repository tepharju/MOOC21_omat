# tee ratkaisu tänne
from random import sample

def lottonumerot(maara:int, alaraja:int, ylaraja:int):

    #lottorivi = []

    #if maara == 1:
    #    rivi = []
    #    rivi.append(8)
    #    return rivi

    kaikki = list(range(alaraja,ylaraja))

    rivi = sample(kaikki, maara)

    lottorivi = rivi.sort()

    print(kaikki)
    print(lottorivi)

    return sorted(rivi)









if __name__ == "__main__":
    for numero in lottonumerot(2, 2, 10):
    
        print(numero)