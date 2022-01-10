# tee ratkaisu tänne
def summa(ekalista, tokalista):
    summalista = []
    for i in range (len(ekalista)):
        summa = (ekalista[i] + tokalista[i])
        summalista.append(summa)
        summa = 0
    return summalista



if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    #print(summa(a, b)) # [8, 10, 12]
    print(summa([1],[1]))